
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#580a7bbc9e806f1abf194c55424e08024db0babb <https://bitbucket.org/bohrium/bohrium/commits/580a7bbc9e806f1abf194c55424e08024db0babb>`_,
    time: 2014-12-16 04:08:51.280922.

    command: ``python benchmark/Python/wireworld.py --size=100*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 73, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 59, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 16, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        pure virtual method called
        terminate called without an active exception
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 73, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 59, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 16, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 73, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 59, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 16, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        pure virtual method called
        terminate called without an active exception
        



