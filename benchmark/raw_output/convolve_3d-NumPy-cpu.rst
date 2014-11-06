
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using NumPy/CPU
    commit: `#fbb4f51971191402fc71c34310eae44732ee978f <https://bitbucket.org/bohrium/bohrium/commits/fbb4f51971191402fc71c34310eae44732ee978f>`_,
    time: 2014-11-06 05:15:31.766887.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=False``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_3d.py", line 3, in <module>
            import util
          File "/home/bhbuilder/bohrium/benchmark/Python/util.py", line 10, in <module>
          File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
            from .array_create import *
        ImportError: No module named array_create
        



