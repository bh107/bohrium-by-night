
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-18 16:34:59.336611.

Jacobi Stencil: ``dython benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=False``
Jacobi Stencil: ``dython benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``
Shallow Water: ``dython benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=False``
Shallow Water: ``dython benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``
N-Body: ``dython benchmark/Python/nbody.py --size=100*10 --bohrium=False``
N-Body: ``dython benchmark/Python/nbody.py --size=100*10 --bohrium=True``

Jacobi Stencil
--------------

.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

Shallow Water
-------------

.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

