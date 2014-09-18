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

    parser = argparse.ArgumentParser(description='Run the test suite and generate a rst-file.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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
        help="Disable the use of SLURM -- the test runs locally"
    )
    args = parser.parse_args()

    if args.no_slurm:
        slurm = ''
    else:
        slurm = '--slurm'

    #First we run/submit the test suite
    tmpdir = tempfile.mkdtemp()
    bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; "\
             "git clone git@bitbucket.org:bohrium/bohrium-by-night.git'", cwd=tmpdir)
    tmpdir += "/bohrium-by-night" #move to the git repos
    cmd = "./press.py %s suites/numpytest.py --no-perf --wait --runs 1 %s --publish-cmd='mv $OUT "\
          "%s/test/numpytest.py.json'"%(args.bohrium_src, slurm, tmpdir)
    bash_cmd(cmd, cwd=args.benchpress_src)

    #Then we commit the result
    bash_cmd("git add test/numpytest.py.json", cwd=tmpdir)
    bash_cmd("git commit -m 'nightly-test'", cwd=tmpdir)
    bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)

    #Finally we generate and commits the reStructuredText file

    with open("%s/test/numpytest.py.json"%tmpdir, 'r') as f:
        data = json.load(f)
        meta = data['meta']

        #Write header
        rst = \
"""
Python Test Suite
=================

Running %s on Octuplets
    commit: `#%s <https://bitbucket.org/bohrium/bohrium/commits/%s>`_,
    time: %s.

"""%(meta['suite'], meta['rev'], meta['rev'], meta['started'])

        #Write the runs
        for r in data['runs']:
            rst += "The %s results::\n\n"%r['engine_alias']
            for o,e in zip(r['stdout'],r['stderr']):
                o = o.replace("\n", "\n  ")
                e = e.replace("\n", "\n  ")
                rst += "  %s\n  %s\n"%(o,e)
        print rst
        with open("%s/test/numpytest.py.rst"%tmpdir,'w') as f:
            f.write(rst)

        bash_cmd("git add %s/test/numpytest.py.rst"%tmpdir, cwd=tmpdir)
        bash_cmd("git commit -m 'nightly-test-rst'", cwd=tmpdir)
        bash_cmd("ssh-agent bash -c 'ssh-add ~/.ssh/bhbuilder_rsa; git push'", cwd=tmpdir)
