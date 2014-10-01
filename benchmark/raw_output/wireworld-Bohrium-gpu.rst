
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c <https://bitbucket.org/bohrium/bohrium/commits/bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c>`_,
    time: 2014-10-01 04:06:27.475774.

    command: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``

Run 00
~~~~~~
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
        



