
Raw Benchmark Output
====================

Running Wire World on Octuplets using Bohrium/GPU
    commit: `#2aec49afccb3bef69bdf38a71b10201af595e038 <https://bitbucket.org/bohrium/bohrium/commits/2aec49afccb3bef69bdf38a71b10201af595e038>`_,
    time: 2014-10-29 04:07:26.433237.

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
        



