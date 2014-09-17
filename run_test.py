#!/usr/bin/env python
import subprocess
import argparse
import json
import sys
import os


def parser_bohrium_src(parser, path):
    """Check that 'path' points to the Bohrium source dir"""
    if os.path.isdir(path):
        return os.path.abspath(path)
    else:
        parser.error("The path %s does not exist!"%path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run the test suite and generate a rst-file.')
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
    args = parser.parse_args()

    pub="git clone git@bitbucket.org:bohrium/bohrium-by-night.git "\
        "&& mv $OUT bohrium-by-night/test/python/numpytest.py.json "\
        "&& cd bohrium-by-night && git commit -am 'nightly-test' && git push"

    cmd = "./press.py ../bohrium suites/numpytest.py --publish-cmd='%s' --wait --runs 1"%pub
    print cmd
    p = subprocess.Popen(
        cmd,
        cwd = args.benchpress_src,
        stdout  = subprocess.PIPE,
        stderr  = subprocess.PIPE,
        shell = True
    )
    out, err = p.communicate()
    print out
    print err

    subprocess.check_call("git pull --no-edit", shell=True)

    rst = \
"""
Python Test Suite
=================

The result::

"""
    with open("test/python/numpytest.py.json", 'r') as f:
        res = json.load(f)
        for r in res['runs']:
            for o,e in zip(r['stdout'],r['stderr']):
                o = o.replace("\n", "\n  ")
                e = e.replace("\n", "\n  ")
                rst += "  %s\n  %s\n"%(o,e)
    print rst
    with open("test/python/numpytest.py.rst",'w') as f:
        f.write(rst)

    subprocess.call("git commit -am 'nightly-test-rst'", shell=True)
    subprocess.check_call("git push", shell=True)



