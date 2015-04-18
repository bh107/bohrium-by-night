
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#369b33555f0b3b45fc0dde490cf2f7340b51843f <https://bitbucket.org/bohrium/bohrium/commits/369b33555f0b3b45fc0dde490cf2f7340b51843f>`_,
    time: 2015-04-18 05:42:02.134734.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 6 f 4 1 5 f a - c b 6 f - 4 2 e d - 8 1 5 5 - d c c c d 6 3 8 e 1 a 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 5 3 4 4 5 4 3 - d e b 8 - 4 3 7 1 - a 8 e e - 0 7 b e 3 d b a 7 5 3 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d a 2 8 3 e e b - 4 4 c d - 4 5 1 d - b 8 b 4 - 1 5 c 9 2 a 5 8 8 3 d 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Black Scholes
-------------

`NumPy/CPU <raw_output/black_scholes-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 2 4 b 1 5 d 3 - e 1 6 b - 4 f c e - a a c f - b 2 9 f d f 3 f 5 8 0 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/black_scholes-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 6 6 5 0 f 3 b - 7 9 d 8 - 4 c 8 7 - 8 f c 3 - 3 1 5 3 0 e f 4 5 f c 4 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/black_scholes-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 5 5 c f 4 2 0 - 6 e 6 4 - 4 7 0 f - 9 5 e 7 - 8 a 3 f 4 6 6 4 5 3 3 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/black_scholes_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 5 6 1 6 1 4 b - 2 e a 1 - 4 6 f e - 9 f d a - a 5 6 9 9 6 4 8 5 4 2 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 2 7 f d b e 5 - 8 5 a 9 - 4 6 b 0 - b 8 6 e - c 0 8 1 6 e 7 1 b 3 0 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 0 5 0 4 e 4 6 - d f f b - 4 f 3 4 - 8 0 6 1 - 6 b 5 b 7 a d a 8 b 7 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 3 7 a 6 1 b 8 - 8 5 7 7 - 4 9 9 1 - 9 e 1 8 - 9 e 4 4 f 2 9 f 7 1 6 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a e 7 0 b d 8 a - e 4 b 2 - 4 2 8 5 - 8 6 4 2 - 9 3 c c b 7 e e a e 8 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 d d 5 d f 1 b - a 8 5 0 - 4 a 6 5 - b b f 3 - e 2 6 7 a b 9 4 d 0 2 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 d e e 4 5 0 5 - 0 2 e 3 - 4 1 2 d - b b 2 8 - 1 4 1 a 5 a a d c 2 6 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b b d 8 c d e 7 - 8 3 0 5 - 4 8 e 9 - a c c 3 - 5 5 2 d 5 6 7 4 c 2 3 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 c 4 5 e 5 a 0 - 1 4 c a - 4 e 1 8 - 8 f 8 c - 1 f f 1 0 5 c 3 2 5 6 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 3 7 c 8 8 e 0 - b c e 1 - 4 6 9 c - b 3 6 e - a 6 7 d 1 9 1 d 0 5 4 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 8 e 3 9 f d c - d 3 b 7 - 4 1 d 6 - 8 6 9 2 - 0 f e 7 8 9 2 6 d 0 7 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 3 4 a a 9 c e - a e 6 2 - 4 6 1 6 - 8 9 0 5 - 0 d 0 e 9 8 9 1 0 d 2 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 9 3 7 5 d a c - 0 c 7 d - 4 a 4 d - 8 c 3 5 - 1 2 b 3 c 2 a b e 2 3 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 8 a e e c 5 9 - d 0 d 7 - 4 8 2 5 - b 8 6 4 - 1 1 0 0 7 1 d e 4 a 9 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 c 2 a 8 a b 8 - e b b a - 4 a a 8 - a 8 9 f - 4 5 4 1 f 2 e f a 2 7 4 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 3 d b b 8 1 0 - 6 8 5 8 - 4 c 8 8 - 9 c c e - 3 e c 8 7 8 a b 4 1 6 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 7 b 0 c e f e - b 9 9 9 - 4 1 f 1 - 8 4 4 c - 5 8 d 8 1 6 5 e 8 5 4 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 4 d 3 3 f b f - 2 4 d b - 4 9 d 0 - 9 a 3 d - 1 0 d 2 8 1 8 7 6 1 6 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 7 3 5 0 e 4 d - d 5 6 d - 4 7 9 5 - b c 4 f - 9 e b d 8 4 9 1 8 2 9 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c f 6 d f 4 b 5 - b f 1 2 - 4 2 f 2 - 9 8 0 e - 0 b 8 2 1 6 2 4 8 5 0 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 f e 6 1 9 3 e - 8 2 7 9 - 4 b e e - b d 0 e - 5 6 b 5 e 7 4 c 7 1 e f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f f 0 8 a 8 8 f - 9 b 9 2 - 4 2 6 0 - a 2 e f - c 6 c a b f b 1 0 b 6 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 4 a 3 9 8 a d - 3 b c 2 - 4 3 3 1 - a 0 5 a - e f 7 9 0 8 9 1 0 8 7 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 1 c c 8 5 c 0 - 1 c 1 1 - 4 3 0 7 - a d 8 7 - 0 d f 4 4 2 3 c 4 7 8 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 8 0 2 7 e 9 a - a 5 f 2 - 4 a 8 e - 8 8 2 9 - 4 b 6 9 0 0 a 0 c b 2 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 9 e a 3 4 4 6 - a 6 a 7 - 4 0 8 9 - a c d 6 - a 6 8 3 d 2 2 7 b 3 3 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 0 5 7 c 5 5 0 - a 1 b 8 - 4 4 b a - b f b a - f 6 7 1 b 7 9 5 8 4 c 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 a 0 b 6 6 2 6 - 7 4 6 3 - 4 3 1 0 - b 1 5 1 - 9 3 4 f 7 e 1 d 3 3 e e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 c c 1 c 0 8 e - d 1 a c - 4 2 1 7 - 8 b 7 5 - e e e 2 a f 0 a 0 6 b f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 a f e 4 f c 1 - e 0 0 4 - 4 c 0 a - a e c 3 - 4 8 2 c d e 4 c d 0 7 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

