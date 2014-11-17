
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#b4d8bfe38389d9c2667c5152e52c456d50977f0d <https://bitbucket.org/bohrium/bohrium/commits/b4d8bfe38389d9c2667c5152e52c456d50977f0d>`_,
    time: 2014-11-17 18:05:56.036748.

    command: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=True``

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
        



