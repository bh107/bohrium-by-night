
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/CPU
    commit: `#7b9b43918fd9fcc017c043405c1482875b413793 <https://bitbucket.org/bohrium/bohrium/commits/7b9b43918fd9fcc017c043405c1482875b413793>`_,
    time: 2014-11-03 04:06:30.227792.

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
        



