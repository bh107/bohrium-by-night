
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/CPU
    commit: `#2aec49afccb3bef69bdf38a71b10201af595e038 <https://bitbucket.org/bohrium/bohrium/commits/2aec49afccb3bef69bdf38a71b10201af595e038>`_,
    time: 2014-10-29 04:07:26.433237.

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
        



