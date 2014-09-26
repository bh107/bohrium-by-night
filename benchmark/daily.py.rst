
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c <https://bitbucket.org/bohrium/bohrium/commits/bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c>`_,
    time: 2014-09-26 04:06:36.394576.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=False``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=True``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``python benchmark/Python/heat_equation.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Convolution 2D
--------------

`NumPy/CPU <raw_output/convolve_2d-NumPy-cpu.rst>`_: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=False``

`Bohrium/CPU <raw_output/convolve_2d-Bohrium-cpu.rst>`_: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=True``

`Bohrium/GPU <raw_output/convolve_2d-Bohrium-gpu.rst>`_: ``python benchmark/Python/convolve_2d.py --size=5 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_2d_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``python benchmark/Python/mc.py --size=100*10 --bohrium=False``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``python benchmark/Python/mc.py --size=100*10 --bohrium=True``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``python benchmark/Python/mc.py --size=100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=False``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=False``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``python benchmark/Python/wireworld.py --size=10*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=False``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=True``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``python benchmark/Python/gauss.py --size=100 --bohrium=False``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``python benchmark/Python/gauss.py --size=100 --bohrium=True``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``python benchmark/Python/gauss.py --size=100 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``python benchmark/Python/mxmul.py --size=100 --bohrium=False``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``python benchmark/Python/mxmul.py --size=100 --bohrium=True``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``python benchmark/Python/mxmul.py --size=100 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``python benchmark/Python/lu.py --size=100 --bohrium=False``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``python benchmark/Python/lu.py --size=100 --bohrium=True``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``python benchmark/Python/lu.py --size=100 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=False``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``python benchmark/Python/shallow_water.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Snakes and Ladders
------------------

`NumPy/CPU <raw_output/snakes_and_ladders-NumPy-cpu.rst>`_: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=False``

`Bohrium/CPU <raw_output/snakes_and_ladders-Bohrium-cpu.rst>`_: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=True``

`Bohrium/GPU <raw_output/snakes_and_ladders-Bohrium-gpu.rst>`_: ``python benchmark/Python/snakes_and_ladders.py --size=100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/snakes_and_ladders_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=False``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=False``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=True``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

