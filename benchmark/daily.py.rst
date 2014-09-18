
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-18 16:56:04.324653.

Jacobi Stencil
--------------

Bohrium/CPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``

Bohrium/GPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

Bohrium/CPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``

Bohrium/GPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

Shallow Water
-------------

Bohrium/CPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``

Bohrium/GPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

