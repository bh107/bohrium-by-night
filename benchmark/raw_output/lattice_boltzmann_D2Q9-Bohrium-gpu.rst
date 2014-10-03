
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c <https://bitbucket.org/bohrium/bohrium/commits/bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c>`_,
    time: 2014-10-03 04:06:03.887396.

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
        



