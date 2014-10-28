
Raw Benchmark Output
====================

Running Convolution 2D on Octuplets using Bohrium/GPU
    commit: `#0422b812bb026bb213aace5bf9a9bfb8f978b58d <https://bitbucket.org/bohrium/bohrium/commits/0422b812bb026bb213aace5bf9a9bfb8f978b58d>`_,
    time: 2014-10-28 04:07:18.197477.

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
        



