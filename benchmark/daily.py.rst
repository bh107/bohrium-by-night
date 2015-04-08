
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#369b33555f0b3b45fc0dde490cf2f7340b51843f <https://bitbucket.org/bohrium/bohrium/commits/369b33555f0b3b45fc0dde490cf2f7340b51843f>`_,
    time: 2015-04-08 04:06:25.488757.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 1 6 7 c b 9 8 - 0 d b 7 - 4 b 2 b - 8 c 4 0 - 1 7 a 9 c e f 4 3 b 0 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 f 0 5 7 9 2 9 - f 1 c 2 - 4 8 4 d - 9 a 6 a - c 5 3 6 c a d e 4 5 f 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 c a 0 0 b a 4 - b 6 9 3 - 4 b 7 8 - 9 5 b 8 - 5 2 0 a 2 9 6 5 4 6 7 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Black Scholes
-------------

`NumPy/CPU <raw_output/black_scholes-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d c 2 8 f 4 6 c - 3 0 f 9 - 4 7 1 e - 8 b 2 c - d 5 6 c 5 1 c 1 0 a 1 d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/black_scholes-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 c d 1 d 6 8 7 - 8 8 f 6 - 4 8 e b - 8 c 4 a - 8 3 7 3 6 3 2 6 1 5 e b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/black_scholes-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 3 6 c b d 4 4 - c f 1 3 - 4 d d e - 8 0 b c - e c a 7 8 9 d 2 3 7 3 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/black_scholes_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 7 3 1 1 c 3 4 - f 8 3 1 - 4 c d 7 - b 0 9 b - 3 d 3 e 7 8 9 a e b 2 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 c a e a 1 7 f - 8 a c 5 - 4 d 4 e - 9 9 7 f - e f 1 2 6 6 7 3 8 4 7 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 0 b b 9 6 7 7 - e 1 3 a - 4 8 e e - 9 4 1 0 - a f b 0 a c 4 d c 2 1 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 8 9 9 a 0 c 1 - 0 d f 0 - 4 a 2 3 - 9 2 3 3 - e 4 1 2 2 5 a 2 7 1 f 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 9 5 9 a e c d - 6 5 b 7 - 4 0 e 0 - 9 7 a 1 - 1 9 c 6 6 5 0 2 d 8 7 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 f 9 c f 1 e 8 - a 4 1 3 - 4 6 a 6 - b 3 5 5 - d 6 0 c 7 2 5 8 8 7 1 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 1 2 3 1 8 3 0 - 1 3 e 1 - 4 0 3 f - 9 e 1 5 - c b 1 7 1 1 5 d d c a a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 0 9 7 1 8 1 2 - 2 8 d 1 - 4 b a 2 - a 9 6 d - 9 8 8 d d b 8 d c 9 a 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 e 5 0 d b d a - 9 2 7 e - 4 7 9 4 - b f 5 9 - 2 7 c 8 3 8 d 2 6 2 f 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 1 9 b 6 c 7 e - a 1 e 9 - 4 4 4 b - 9 9 5 e - 0 9 4 9 1 1 0 a f 3 8 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 6 9 3 f 7 e 5 - 1 4 f 9 - 4 c 7 f - a e a 4 - 4 d e 4 7 c 4 1 9 3 d c . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 7 0 b 5 8 2 a - a 6 f 4 - 4 2 1 8 - 9 2 6 8 - 8 a 9 1 7 b c c e 9 c 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 5 f d a e f 4 - 7 3 4 e - 4 d 2 3 - a 9 2 8 - 6 d 4 6 0 5 0 7 2 c c 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 6 5 6 8 f 2 1 - 7 4 6 b - 4 5 f a - a 8 5 e - 8 c c 2 e 2 4 1 a e b 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 8 1 e 3 0 0 9 - 6 8 5 0 - 4 d 3 2 - a 8 0 a - 5 4 9 0 0 4 c 2 7 e 0 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 9 1 8 f 8 5 3 - 1 1 0 6 - 4 1 e 1 - b f 6 9 - a f f a 2 3 f b 9 b d e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 c 4 4 6 6 6 d - d d e 4 - 4 a a 6 - a 3 4 a - 2 3 7 2 7 2 2 1 1 0 c a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 4 8 1 8 3 5 7 - 6 2 1 c - 4 f 1 7 - a c d 6 - 7 8 a 5 e f 2 2 6 c 0 d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 1 e d a 6 5 c - 9 4 d f - 4 b 8 0 - b c 5 6 - 1 c 8 f 4 1 0 a 6 f d 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 d a d 8 6 8 2 - 1 2 9 c - 4 5 d 9 - 8 2 f 0 - 4 9 e 0 7 8 b 6 9 8 f 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d e 6 f e e 1 a - 0 a b b - 4 7 2 f - a a d b - 3 0 0 8 4 2 5 0 a 6 3 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 6 9 7 a 8 3 d - 9 2 1 8 - 4 4 b 4 - a e 4 7 - 2 8 2 8 5 f 5 b f 6 c 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 8 1 7 f 2 1 1 - c a 3 1 - 4 a 1 0 - b 1 3 c - 6 e e d 3 2 5 7 6 9 8 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 6 6 8 8 b e 4 - 8 4 3 0 - 4 5 2 9 - 8 6 1 8 - d 3 2 4 c 5 1 1 d 4 e b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 6 a 2 0 5 1 9 - 5 e 6 d - 4 1 e 3 - 9 3 3 7 - 2 a f 8 f 6 9 a c a 1 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f d 2 4 7 3 b 2 - a e c c - 4 c 4 d - 8 6 9 4 - c 1 7 5 c b 9 4 d 5 a f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 5 f b 6 5 0 d - 8 5 7 5 - 4 3 0 b - 9 b 1 1 - 0 9 1 b 4 a 2 d b 4 9 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 4 7 8 6 6 5 b - 3 c 8 4 - 4 5 e d - 9 e 8 2 - 1 b f c a 8 7 3 b 5 8 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 a 2 8 f b 3 9 - f c 4 5 - 4 6 6 b - 9 7 0 1 - 3 f 1 c 0 7 f 6 6 9 a 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a c 6 d 8 2 5 b - d f a 9 - 4 6 0 8 - 8 1 f b - 3 f 2 b 0 4 3 0 6 f f a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

