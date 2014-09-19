
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using NumPy/CPU
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-19 10:19:05.678551.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

    stdout-00::

        N/A

    stderr-00::

        benchmark/Python/convolve_3d.py:23: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        


|
