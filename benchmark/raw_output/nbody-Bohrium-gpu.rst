
Raw Benchmark Output
====================

Running N-Body on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-11-30 04:05:43.343350.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/nbody.py", line 13, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "ndarray.pyx", line 28, in init ndarray (/home/bhbuilder/bohrium/build/bridge/npbackend/ndarray.c:4999)
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/nbody.py", line 13, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "ndarray.pyx", line 28, in init ndarray (/home/bhbuilder/bohrium/build/bridge/npbackend/ndarray.c:4999)
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/nbody.py", line 13, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "ndarray.pyx", line 28, in init ndarray (/home/bhbuilder/bohrium/build/bridge/npbackend/ndarray.c:4999)
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



