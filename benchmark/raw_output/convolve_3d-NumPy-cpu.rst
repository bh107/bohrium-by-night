
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using NumPy/CPU
    commit: `#369b33555f0b3b45fc0dde490cf2f7340b51843f <https://bitbucket.org/bohrium/bohrium/commits/369b33555f0b3b45fc0dde490cf2f7340b51843f>`_,
    time: 2015-04-09 04:07:15.356241.

    command: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 c 6 f f d 3 e - 9 c 9 5 - 4 a c d - b 1 8 4 - 1 3 a 6 d 1 5 d 0 d 4 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N, B)
          File "benchmark/python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance)
        IndexError: index 100 is out of bounds for axis 2 with size 100
        Error in [node:impl]: /home/bhbuilder/.local/lib/libbh_vem_node.so: cannot open shared object file: No such file or directory
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N, B)
          File "benchmark/python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance)
        IndexError: index 100 is out of bounds for axis 2 with size 100
        Error in [node:impl]: /home/bhbuilder/.local/lib/libbh_vem_node.so: cannot open shared object file: No such file or directory
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/python/convolve_3d.py", line 59, in <module>
            main()
          File "benchmark/python/convolve_3d.py", line 50, in main
            image, image_filter = convolve_3d_init(N, B)
          File "benchmark/python/convolve_3d.py", line 33, in convolve_3d_init
            kernel  = gen_3d_filter(fsize, 13.0)
          File "benchmark/python/convolve_3d.py", line 23, in gen_3d_filter
            kernel[filterZ + kernelrad, filterY + kernelrad,filterX + kernelrad] = caleuler * np.exp(-distance)
        IndexError: index 100 is out of bounds for axis 2 with size 100
        Error in [node:impl]: /home/bhbuilder/.local/lib/libbh_vem_node.so: cannot open shared object file: No such file or directory
        



