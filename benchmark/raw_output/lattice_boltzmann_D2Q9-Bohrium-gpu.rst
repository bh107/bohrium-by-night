
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#0422b812bb026bb213aace5bf9a9bfb8f978b58d <https://bitbucket.org/bohrium/bohrium/commits/0422b812bb026bb213aace5bf9a9bfb8f978b58d>`_,
    time: 2014-10-28 04:07:18.197477.

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
        



