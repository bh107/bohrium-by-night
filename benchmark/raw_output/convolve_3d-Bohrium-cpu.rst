
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/CPU
    commit: `#5658bbbd87d6fa5dc2935e0e14b2df428b928a42 <https://bitbucket.org/bohrium/bohrium/commits/5658bbbd87d6fa5dc2935e0e14b2df428b928a42>`_,
    time: 2015-01-21 04:08:08.480016.

    command: ``python benchmark/Python/convolve_3d.py --size=100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



