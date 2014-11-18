
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#0e67b7b00f693b98b768cfc3d3c85c2370605c86 <https://bitbucket.org/bohrium/bohrium/commits/0e67b7b00f693b98b768cfc3d3c85c2370605c86>`_,
    time: 2014-11-18 14:15:52.338679.

    command: ``python benchmark/Python/wireworld.py --size=100*100 --bohrium=True``

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
        



