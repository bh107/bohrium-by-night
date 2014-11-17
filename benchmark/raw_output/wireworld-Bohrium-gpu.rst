
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#b4d8bfe38389d9c2667c5152e52c456d50977f0d <https://bitbucket.org/bohrium/bohrium/commits/b4d8bfe38389d9c2667c5152e52c456d50977f0d>`_,
    time: 2014-11-17 18:05:56.036748.

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
        



