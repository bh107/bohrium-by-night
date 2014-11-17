
Raw Benchmark Output
====================

Running Snakes and Ladders on Octuplets using Bohrium/CPU
    commit: `#01b6230bfd1cac67164bc5a3590d03d7400588a0 <https://bitbucket.org/bohrium/bohrium/commits/01b6230bfd1cac67164bc5a3590d03d7400588a0>`_,
    time: 2014-11-17 04:03:04.515681.

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
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
        ImportError: No module named array_create
        



