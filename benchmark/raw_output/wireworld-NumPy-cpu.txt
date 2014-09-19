
Raw Benchmark Output
====================

Running Wire World on Octuplets using NumPy/CPU
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-19 10:19:05.678551.

    command: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``

    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 72, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 58, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 15, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        

    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 72, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 58, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 15, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        

    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/wireworld.py", line 72, in <module>
            main()
          File "benchmark/Python/wireworld.py", line 58, in main
            world = wireworld_init(N)
          File "benchmark/Python/wireworld.py", line 15, in wireworld_init
            data[1:-1,1:-1] = np.tile(np.array([
        AttributeError: 'module' object has no attribute 'tile'
        

