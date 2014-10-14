
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/CPU
    commit: `#0422b812bb026bb213aace5bf9a9bfb8f978b58d <https://bitbucket.org/bohrium/bohrium/commits/0422b812bb026bb213aace5bf9a9bfb8f978b58d>`_,
    time: 2014-10-14 04:07:24.758101.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:23: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



