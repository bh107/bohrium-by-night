
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#369b33555f0b3b45fc0dde490cf2f7340b51843f <https://bitbucket.org/bohrium/bohrium/commits/369b33555f0b3b45fc0dde490cf2f7340b51843f>`_,
    time: 2015-04-10 04:06:19.914508.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 8 7 8 2 9 0 a - 7 e 7 9 - 4 5 7 8 - a 2 2 6 - 1 0 0 2 c 5 a f 4 4 8 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 a 0 3 b 3 6 b - e 3 9 0 - 4 d 1 c - a 4 1 c - c b 4 d 8 2 6 d 5 7 1 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 9 0 7 a 9 f 4 - 7 d 0 8 - 4 a 5 2 - a 4 b 0 - 0 6 3 7 c a a b b e 1 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Black Scholes
-------------

`NumPy/CPU <raw_output/black_scholes-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a b e 3 d 2 9 5 - 7 1 b 7 - 4 5 6 d - b 3 f 9 - d 9 0 e a 9 f d 1 3 5 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/black_scholes-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c d 7 b 9 c 6 5 - 5 5 d 4 - 4 4 d e - b 1 4 c - c 9 3 f 6 3 f a 3 9 5 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/black_scholes-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 4 d b 1 5 e b - f 8 d e - 4 f 3 d - 8 2 6 5 - e c 6 0 4 7 b 0 0 1 d b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/black_scholes_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 b 4 d f c 0 6 - 6 b e d - 4 7 b 8 - a c 8 e - b 9 5 6 d 1 0 2 f a 8 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 c d 9 3 c 7 b - 1 2 4 d - 4 b c f - 8 d a a - 5 7 7 b 2 3 0 5 0 5 c 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 1 6 5 7 a 7 a - 7 9 6 e - 4 0 f e - b 3 2 7 - 6 d 3 7 3 e 4 0 e 2 e e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 8 5 e c e 1 1 - 5 4 e 7 - 4 9 1 9 - 9 0 e 0 - 0 6 e 7 9 d 9 1 9 6 f 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b d 0 3 c a d a - 1 1 1 9 - 4 c 7 0 - a 3 4 b - 6 0 9 8 5 5 5 a c 8 c 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 6 0 4 8 4 5 6 - 1 2 4 f - 4 f f 4 - a 8 d 5 - 8 9 c 0 0 9 9 7 b f 6 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d d 1 0 b 3 8 c - 0 6 e 7 - 4 9 f e - a c f f - 5 6 9 8 e 0 0 4 1 f 8 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 1 b b f f 8 b - 5 0 c 0 - 4 3 5 7 - 8 d 9 8 - a 3 a 5 4 a 3 5 a 3 4 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 3 4 f 6 f 5 8 - 7 9 0 b - 4 5 c 4 - 8 b 0 d - 5 d 2 5 b c e c d 5 e 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 4 3 a 0 4 5 7 - f 6 b 1 - 4 f 9 c - a 3 3 b - 2 6 6 3 a 1 e 4 2 5 8 d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a f 4 9 8 4 5 0 - f 2 d b - 4 7 2 d - a e e 4 - f 1 9 b 1 0 d 5 a c a 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 3 b 8 5 f 6 1 - 6 f 0 f - 4 3 6 6 - b d 2 0 - 4 5 8 d 7 b a 7 8 b d 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 5 5 3 f 3 0 9 - b 1 0 5 - 4 a 0 4 - b 7 d a - 8 8 3 3 e e e 8 2 7 6 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 7 5 8 6 b f a - b b 8 2 - 4 3 5 6 - b 1 e e - d 2 a 3 1 d c e 3 a e 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 5 c a 0 8 b 2 - 6 4 b e - 4 3 8 9 - 9 f 2 e - 2 f 4 4 3 b 2 8 3 a 7 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 a c c e c 5 b - b c b 7 - 4 0 9 4 - b 6 8 f - 5 4 b f c 2 3 8 7 3 7 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 7 b 8 a 4 0 3 - 5 1 0 f - 4 b 7 d - 8 8 7 3 - 7 1 2 2 0 8 3 4 5 6 a d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 1 6 2 c 7 2 8 - 8 5 4 f - 4 2 8 d - a 5 3 5 - e d 3 b a a 0 d 6 d f d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 4 8 f 9 7 c 1 - 7 a f a - 4 f 2 e - b 2 5 b - c a e 0 7 c 7 3 9 3 6 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 4 5 8 d 6 f 7 - 0 3 d 8 - 4 0 9 c - a d f 6 - b 3 e 8 2 9 2 b 3 3 9 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 3 b f 2 a 0 5 - 4 1 0 0 - 4 d 6 7 - a c b f - 0 b 2 d 0 9 1 8 c a 1 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 4 c e 8 f 6 1 - 0 9 4 d - 4 3 5 b - 9 d 4 0 - d d b 1 8 d 1 f 2 d 8 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 4 c b 9 a 4 2 - 1 8 8 e - 4 c 9 7 - a a d d - d b 1 1 7 2 9 8 b d 9 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 5 d 7 3 4 2 a - 3 2 4 a - 4 b 8 7 - a 3 e 2 - d 6 9 c 6 b 2 a 5 4 e b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 c 7 7 4 4 0 9 - 2 7 9 b - 4 a 5 9 - 9 1 7 e - 6 d 9 2 0 6 f f 1 1 1 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 1 d f 2 e 6 7 - c 8 1 2 - 4 6 8 6 - 8 1 f f - 7 f e c 2 3 6 b a 1 6 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 f 5 6 2 1 2 a - 2 8 a d - 4 c 0 a - 9 7 f b - a 7 5 4 a 2 6 4 7 e e a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 3 c 6 a f 9 3 - 3 f b e - 4 8 6 d - 9 c 7 2 - 8 d 8 2 1 6 0 9 9 e d 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 f 6 3 0 1 d 6 - 0 6 9 6 - 4 0 5 b - 9 9 b d - b 7 4 3 e 4 6 8 a f 8 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 0 a b 3 8 1 5 - 4 2 1 c - 4 4 2 6 - a a 8 a - a 7 1 7 e e 4 b b b 1 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

