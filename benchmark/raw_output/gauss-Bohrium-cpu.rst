
Raw Benchmark Output
====================

Running Gauss Elimination on Octuplets using Bohrium/CPU
    commit: `#d028afdda2e07d67e9768d32b234cbea9a700054 <https://bitbucket.org/bohrium/bohrium/commits/d028afdda2e07d67e9768d32b234cbea9a700054>`_,
    time: 2014-11-14 04:03:13.708249.

    command: ``python benchmark/Python/gauss.py --size=100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/gauss.py", line 2, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 8, in <module>
            from .array_manipulation import *
        ImportError: No module named array_manipulation
        Error in atexit._run_exitfuncs:
        Traceback (most recent call last):
          File "/usr/lib/python2.7/atexit.py", line 24, in _run_exitfuncs
            func(*targs, **kargs)
          File "_util.pyx", line 98, in _util.shutdown (/home/bhbuilder/bohrium/build/bridge/npbackend/_util.c:2156)
          File "_util.pyx", line 29, in _util.flush (/home/bhbuilder/bohrium/build/bridge/npbackend/_util.c:924)
        SystemError: Parent module 'bohrium' not loaded, cannot perform relative import
        Error in sys.exitfunc:
        Traceback (most recent call last):
          File "/usr/lib/python2.7/atexit.py", line 24, in _run_exitfuncs
            func(*targs, **kargs)
          File "_util.pyx", line 98, in _util.shutdown (/home/bhbuilder/bohrium/build/bridge/npbackend/_util.c:2156)
          File "_util.pyx", line 29, in _util.flush (/home/bhbuilder/bohrium/build/bridge/npbackend/_util.c:924)
        SystemError: Parent module 'bohrium' not loaded, cannot perform relative import
        



