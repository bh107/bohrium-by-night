
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/GPU
    commit: `#541610fc2ad8a811fc78975452c3d4d238a77b51 <https://bitbucket.org/bohrium/bohrium/commits/541610fc2ad8a811fc78975452c3d4d238a77b51>`_,
    time: 2014-11-18 04:04:56.090847.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



