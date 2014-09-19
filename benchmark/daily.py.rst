
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-19 10:19:05.678551.

Heat Equation
-------------

NumPy/CPU: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Convolution 2D
--------------

NumPy/CPU: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_2d_runtime.png

Monte Carlo Pi
--------------

NumPy/CPU: ``python benchmark/Python/mc.py --size=100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/mc.py --size=100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/mc.py --size=100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Convolution 3D
--------------

NumPy/CPU: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Wire World
----------

NumPy/CPU: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

NumPy/CPU: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

NumPy/CPU: ``python benchmark/Python/gauss.py --size=100 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/gauss.py --size=100 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/gauss.py --size=100 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

NumPy/CPU: ``python benchmark/Python/mxmul.py --size=100 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/mxmul.py --size=100 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/mxmul.py --size=100 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

NumPy/CPU: ``python benchmark/Python/lu.py --size=100 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/lu.py --size=100 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/lu.py --size=100 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Shallow Water
-------------

NumPy/CPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Snakes and Ladders
------------------

NumPy/CPU: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/snakes_and_ladders_runtime.png

Jacobi Stencil
--------------

NumPy/CPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

NumPy/CPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``

Bohrium/CPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=False``

Bohrium/GPU: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=False``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

