
Raw Benchmark Output
====================

Running Matrix Multiplication on Octuplets using NumPy/CPU
    commit: `#e2eb8cda5af33d49993cdc9c0473aa962908adf4 <https://bitbucket.org/bohrium/bohrium/commits/e2eb8cda5af33d49993cdc9c0473aa962908adf4>`_,
    time: 2014-09-20 04:04:04.944559.

    command: ``python benchmark/Python/mxmul.py --size=100 --bohrium=False``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 1, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 9, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
            from array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 28, in <module>
            _bhc = swig_import_helper()
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 20, in swig_import_helper
            import _bhc
        ImportError: No module named _bhc
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 1, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 9, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
            from array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 28, in <module>
            _bhc = swig_import_helper()
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 20, in swig_import_helper
            import _bhc
        ImportError: No module named _bhc
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/mxmul.py", line 1, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 9, in <module>
            import bohrium as bh
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
            from array_create import *
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
            import ndarray
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
            from _util import dtype_equal
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
            import bhc
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 28, in <module>
            _bhc = swig_import_helper()
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 20, in swig_import_helper
            import _bhc
        ImportError: No module named _bhc
        



