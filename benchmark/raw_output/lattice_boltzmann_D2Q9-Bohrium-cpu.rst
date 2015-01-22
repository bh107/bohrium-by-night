
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/CPU
    commit: `#6103f1ec1b8914f895dfb1b8f89c1ddb92e660e6 <https://bitbucket.org/bohrium/bohrium/commits/6103f1ec1b8914f895dfb1b8f89c1ddb92e660e6>`_,
    time: 2015-01-22 04:07:38.186877.

    command: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=1000*1000*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 246, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 226, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 43, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 246, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 226, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 43, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 246, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 226, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 43, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        



