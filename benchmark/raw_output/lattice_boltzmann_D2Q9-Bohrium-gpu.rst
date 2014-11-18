
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#541610fc2ad8a811fc78975452c3d4d238a77b51 <https://bitbucket.org/bohrium/bohrium/commits/541610fc2ad8a811fc78975452c3d4d238a77b51>`_,
    time: 2014-11-18 04:04:56.090847.

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
        pure virtual method called
        terminate called without an active exception
        



