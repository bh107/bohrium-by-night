
Raw Benchmark Output
====================

Running Convolution 2D on Octuplets using Bohrium/CPU
    commit: `#4063fbf9497b979ca4a59ed845f3f1b189c88fc5 <https://bitbucket.org/bohrium/bohrium/commits/4063fbf9497b979ca4a59ed845f3f1b189c88fc5>`_,
    time: 2014-11-16 04:02:54.522467.

    command: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/convolve_2d.py", line 61, in <module>
            main()
          File "benchmark/Python/convolve_2d.py", line 52, in main
            image, image_filter = convolve_2d_init(N)
          File "benchmark/Python/convolve_2d.py", line 31, in convolve_2d_init
            img     = Image.open(photo)
          File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 1996, in open
            fp = builtins.open(fp, "rb")
        IOError: [Errno 2] No such file or directory: '/tmp/Hell.jpg'
        



