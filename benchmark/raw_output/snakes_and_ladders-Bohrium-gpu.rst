
Raw Benchmark Output
====================

Running Snakes and Ladders on Octuplets using Bohrium/GPU
    commit: `#4063fbf9497b979ca4a59ed845f3f1b189c88fc5 <https://bitbucket.org/bohrium/bohrium/commits/4063fbf9497b979ca4a59ed845f3f1b189c88fc5>`_,
    time: 2014-11-15 04:03:02.245392.

    command: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/snakes_and_ladders.py", line 3, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 7, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "_util.pyx", line 22, in init _util (/home/bhbuilder/bohrium/build/bridge/npbackend/_util.c:2470)
        ImportError: cannot import name _info
        



