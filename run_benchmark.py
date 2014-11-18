#!/usr/bin/env python
import subprocess
import argparse
import json
import sys
import os
import tempfile

def bash_cmd(cmd, cwd=None):
    print cmd
    p = subprocess.Popen(
        cmd,
        stdout  = subprocess.PIPE,
        stderr  = subprocess.PIPE,
        shell = True,
        cwd=cwd
    )
    out, err = p.communicate()
    print out,
    print err,

def parser_bohrium_src(parser, path):
    """Check that 'path' points to the Bohrium source dir"""
    path = os.path.expanduser(path)
    if os.path.isdir(path):
        return os.path.abspath(path)
    else:
        parser.error("The path %s does not exist!"%path)

def parser_is_file(parser, path):
    """Check that 'path' points to a file"""
    path = os.path.expanduser(path)
    if os.path.isfile(path):
        return os.path.abspath(path)
    else:
        parser.error("The path %s does not point to a file!"%path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run the benchmark suite and generate a rst-file.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'bohrium_src',
        help='Path to the Bohrium source-code.',
        type=lambda x: parser_bohrium_src(parser, x)
    )
    parser.add_argument(
        'benchpress_src',
        help='Path to the Benchpress source-code.',
        type=lambda x: parser_bohrium_src(parser, x)
    )
    parser.add_argument(
        '--ssh-key',
        default="~/.ssh/bhbuilder_rsa",
        help='The ssh key to use when accessing the git repos',
        type=lambda x: parser_is_file(parser, x)
    )
    parser.add_argument(
        '--no-slurm',
        action="store_true",
        help="Disable the use of SLURM -- the benchmark runs locally"
    )
    args = parser.parse_args()

    if args.no_slurm:
        slurm = ''
    else:
        slurm = '--slurm'

    tmpdir = tempfile.mkdtemp()
    tmpdir_root = tmpdir
    
    #Lets update the bohrium and benchpress repos
    bash_cmd("git pull", cwd=args.bohrium_src)
    bash_cmd("git pull", cwd=args.benchpress_src)

    #We build and install bohrium in ~/.local
    bash_cmd("mkdir -p build && cd build && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .."\
             " && make install", cwd=args.bohrium_src)

    #We run/submit the benchmark suite
    bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; "\
             "git clone git@bitbucket.org:bohrium/bohrium-by-night.git'", cwd=tmpdir)
    tmpdir += "/bohrium-by-night" #move to the git repos
    cmd = "./press.py %s suites/daily_benchmark.py --no-perf --wait --runs 3 %s --publish-cmd='mv $OUT "\
          "%s/benchmark/daily.py.json'"%(args.bohrium_src, slurm, tmpdir)
    print cmd
    bash_cmd(cmd, cwd=args.benchpress_src)

    #We commit the result
    bash_cmd("git add benchmark/daily.py.json", cwd=tmpdir)
    bash_cmd("git commit -m 'nightly-benchmark'", cwd=tmpdir)
    bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)

    #We generate and commit graphs
    bash_cmd("./gen.graphs.py --type=daily %s/benchmark/daily.py.json "\
             "--output %s/benchmark/gfx"%(tmpdir,tmpdir), cwd=args.benchpress_src)
    bash_cmd("git add benchmark/gfx", cwd=tmpdir)
    bash_cmd("git commit -m 'nightly-benchmark-gfx'", cwd=tmpdir)
    bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)

    #We generate the raw output reStructuredText files
    with open("%s/benchmark/daily.py.json"%tmpdir, 'r') as f:
        data = json.load(f)
        meta = data['meta']


        #We write one rst-file per command
        for script in set([d['script'] for d in data['runs']]):
            for r in data['runs']:
                if script == r['script']:
                    #Write header
                    rst = \
"""
Raw Benchmark Output
====================

Running %s on Octuplets using %s/%s
    commit: `#%s <https://bitbucket.org/bohrium/bohrium/commits/%s>`_,
    time: %s.

    command: ``%s``

"""%(r['script_alias'], r['bridge_alias'], r['engine_alias'], meta['rev'],\
        meta['rev'], meta['started'], ' '.join(r['cmd']))

                    #Write all outputs
                    i = 0
                    for o, e in zip(r['stdout'], r['stderr']):
                        if len(o) == 0:
                            o = "N/A"
                        if len(e) == 0:
                            e = "N/A"
                        rst += "Run %02d\n~~~~~~\n"%i
                        rst += "    stdout::\n\n        %s\n\n"%(o.replace("\n","\n        "))
                        rst += "    stderr::\n\n        %s\n\n"%(e.replace("\n","\n        "))
                        rst += "\n\n"
                        i += 1
                    filename = "%s/benchmark/raw_output/%s-%s-%s.rst"%(tmpdir,r['script'],\
                            r['bridge_alias'].replace(" ", "-"),r['engine'])

                    with open(filename,'w') as f:
                        f.write(rst)

                    bash_cmd("git add %s"%filename, cwd=tmpdir)
        bash_cmd("git commit -m 'nightly-benchmark-raw-output'", cwd=tmpdir)
        bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)

    #Finally we generate and commits the reStructuredText file
    with open("%s/benchmark/daily.py.json"%tmpdir, 'r') as f:
        data = json.load(f)
        meta = data['meta']

        #Write header
        rst = \
"""
Python Benchmark Suite
======================

Running %s on Octuplets
    commit: `#%s <https://bitbucket.org/bohrium/bohrium/commits/%s>`_,
    time: %s.

"""%(meta['suite'], meta['rev'], meta['rev'], meta['started'])

        #We handle one script at a time
        for script in set([d['script'] for d in data['runs']]):
            for r in data['runs']:
                if script == r['script']:
                    #Write title
                    rst += "%s\n"%r['script_alias']
                    rst += "-"*len(r['script_alias']) + "\n\n"
                    break

            #Write the executed commands
            for r in data['runs']:
                if script == r['script']:
                    rst += "`%s/%s <raw_output/%s-%s-%s.rst>`_:"%(r['bridge_alias'], \
                            r['engine_alias'], r['script'], \
                            r['bridge_alias'].replace(" ", "-"),r['engine'])
                    rst += " ``%s``\n\n"%(' '.join(r['cmd']))
            rst += "\n\n"

            #Write the graphs
            rst += ".. image:: https://bytebucket.org/bohrium/bohrium-by-night"\
                   "/raw/master/benchmark/gfx/%s_runtime.png\n\n"%script
        with open("%s/benchmark/daily.py.rst"%tmpdir,'w') as f:
            f.write(rst)

        bash_cmd("git add %s/benchmark/daily.py.rst"%tmpdir, cwd=tmpdir)
        bash_cmd("git commit -m 'nightly-benchmark-rst'", cwd=tmpdir)
        bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)
        bash_cmd("rm -Rf %s"%tmpdir_root)
