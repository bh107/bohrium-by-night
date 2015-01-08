
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/CPU
    commit: `#a7036bb012cf1d24764010f2ec1c4618ad4321d3 <https://bitbucket.org/bohrium/bohrium/commits/a7036bb012cf1d24764010f2ec1c4618ad4321d3>`_,
    time: 2015-01-08 04:11:08.542788.

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
        



