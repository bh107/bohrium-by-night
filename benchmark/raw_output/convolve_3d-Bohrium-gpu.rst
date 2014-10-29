
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/GPU
    commit: `#2aec49afccb3bef69bdf38a71b10201af595e038 <https://bitbucket.org/bohrium/bohrium/commits/2aec49afccb3bef69bdf38a71b10201af595e038>`_,
    time: 2014-10-29 04:07:26.433237.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:23: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



