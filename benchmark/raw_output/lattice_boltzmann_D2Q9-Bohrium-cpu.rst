
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/CPU
    commit: `#62cc53b60eae0a14bef165e853c7017ace4411e8 <https://bitbucket.org/bohrium/bohrium/commits/62cc53b60eae0a14bef165e853c7017ace4411e8>`_,
    time: 2014-12-17 04:08:14.835360.

    command: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=1000*1000*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



