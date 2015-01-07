
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using NumPy/CPU
    commit: `#a673929a5dfba7f9ad45cc9e15a8b62865e88876 <https://bitbucket.org/bohrium/bohrium/commits/a673929a5dfba7f9ad45cc9e15a8b62865e88876>`_,
    time: 2015-01-07 04:08:41.054075.

    command: ``python benchmark/Python/convolve_3d.py --size=100 --bohrium=False``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/Python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N)
          File "benchmark/Python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/Python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance) 
        IndexError: index 100 is out of bounds for axis 2 with size 100
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/Python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N)
          File "benchmark/Python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/Python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance) 
        IndexError: index 100 is out of bounds for axis 2 with size 100
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/Python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N)
          File "benchmark/Python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/Python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance) 
        IndexError: index 100 is out of bounds for axis 2 with size 100
        



