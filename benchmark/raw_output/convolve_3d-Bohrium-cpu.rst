
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/CPU
    commit: `#84083907fa6c76d7ab7e01356cd1607b0dc4bcc2 <https://bitbucket.org/bohrium/bohrium/commits/84083907fa6c76d7ab7e01356cd1607b0dc4bcc2>`_,
    time: 2014-11-05 19:07:44.573576.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



