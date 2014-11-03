
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#7b9b43918fd9fcc017c043405c1482875b413793 <https://bitbucket.org/bohrium/bohrium/commits/7b9b43918fd9fcc017c043405c1482875b413793>`_,
    time: 2014-11-03 04:06:30.227792.

    command: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 229, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 195, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 41, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        pure virtual method called
        terminate called without an active exception
        



