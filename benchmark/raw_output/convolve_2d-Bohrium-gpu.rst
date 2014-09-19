
Raw Benchmark Output
====================

Running Convolution 2D on Octuplets using Bohrium/GPU
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-19 11:39:09.272977.

    command: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_2d.py", line 60, in <module>
            main()
          File "benchmark/Python/convolve_2d.py", line 51, in main
            image, image_filter = convolve_2d_init(N)
          File "benchmark/Python/convolve_2d.py", line 30, in convolve_2d_init
            img     = Image.open(photo)
          File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 1996, in open
            fp = builtins.open(fp, "rb")
        IOError: [Errno 2] No such file or directory: '/tmp/Hell.jpg'
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_2d.py", line 60, in <module>
            main()
          File "benchmark/Python/convolve_2d.py", line 51, in main
            image, image_filter = convolve_2d_init(N)
          File "benchmark/Python/convolve_2d.py", line 30, in convolve_2d_init
            img     = Image.open(photo)
          File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 1996, in open
            fp = builtins.open(fp, "rb")
        IOError: [Errno 2] No such file or directory: '/tmp/Hell.jpg'
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_2d.py", line 60, in <module>
            main()
          File "benchmark/Python/convolve_2d.py", line 51, in main
            image, image_filter = convolve_2d_init(N)
          File "benchmark/Python/convolve_2d.py", line 30, in convolve_2d_init
            img     = Image.open(photo)
          File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 1996, in open
            fp = builtins.open(fp, "rb")
        IOError: [Errno 2] No such file or directory: '/tmp/Hell.jpg'
        



