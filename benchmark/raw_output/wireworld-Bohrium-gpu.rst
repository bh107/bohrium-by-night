
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#fbb4f51971191402fc71c34310eae44732ee978f <https://bitbucket.org/bohrium/bohrium/commits/fbb4f51971191402fc71c34310eae44732ee978f>`_,
    time: 2014-11-12 04:05:21.349433.

    command: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

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
        



