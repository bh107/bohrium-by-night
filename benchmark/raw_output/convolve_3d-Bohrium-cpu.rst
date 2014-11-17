
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/CPU
    commit: `#b4d8bfe38389d9c2667c5152e52c456d50977f0d <https://bitbucket.org/bohrium/bohrium/commits/b4d8bfe38389d9c2667c5152e52c456d50977f0d>`_,
    time: 2014-11-17 18:05:56.036748.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



