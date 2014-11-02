
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/GPU
    commit: `#7b9b43918fd9fcc017c043405c1482875b413793 <https://bitbucket.org/bohrium/bohrium/commits/7b9b43918fd9fcc017c043405c1482875b413793>`_,
    time: 2014-11-02 04:06:22.447819.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:23: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



