
Raw Benchmark Output
====================

Running Matrix Multiplication on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-11-29 04:05:06.256950.

    command: ``python benchmark/Python/mxmul.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 2, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 2, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 2, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
            from .array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            from . import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
        ImportError: No module named bhc
        



