
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#369b33555f0b3b45fc0dde490cf2f7340b51843f <https://bitbucket.org/bohrium/bohrium/commits/369b33555f0b3b45fc0dde490cf2f7340b51843f>`_,
    time: 2015-04-11 04:06:35.469541.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d d a c e a 5 6 - 3 7 a 3 - 4 2 8 9 - 8 f 7 2 - 3 1 5 3 e 9 2 5 8 7 6 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 1 9 c e 6 3 6 - 2 f e f - 4 f e a - 8 e a 2 - 2 7 6 f f b 0 9 5 0 7 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 4 5 a e 1 3 5 - 2 d 2 3 - 4 2 a 0 - 9 3 d c - 7 3 6 0 4 0 6 5 9 c 8 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Black Scholes
-------------

`NumPy/CPU <raw_output/black_scholes-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 2 2 9 8 8 e a - 8 0 6 1 - 4 4 9 c - b a f d - d c e 8 6 e c 2 f b a 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/black_scholes-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 6 5 4 b 9 c a - 3 b 2 e - 4 7 4 f - b a d 2 - f 8 e 0 0 c 4 1 c 9 2 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/black_scholes-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f e 5 5 0 2 0 4 - e c 3 e - 4 b 5 3 - b 4 c f - e 9 4 7 d a c b 2 e c c . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/black_scholes_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 0 c 1 a e 8 c - c 3 1 8 - 4 2 2 3 - 9 9 2 e - 7 5 e 0 d 9 8 f 4 e 5 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 9 e 2 9 5 2 8 - 6 7 2 0 - 4 d b 8 - a 5 0 b - 4 7 7 f 1 a 4 7 d a d 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a d f 1 b 6 c f - 8 7 d d - 4 b d 7 - a 1 2 9 - f 4 d 8 2 3 2 1 b 0 3 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 9 f b a f 3 4 - 9 7 d 6 - 4 9 1 9 - b 1 a c - d a 8 4 8 1 e f 5 0 f 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 b 0 1 a 7 a 6 - b 8 9 6 - 4 d e 0 - b 1 a e - 3 d b e 9 6 3 c 4 4 3 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 9 c 7 5 2 5 9 - 0 a 7 1 - 4 7 a 4 - a 8 8 5 - b 9 f 8 8 5 5 6 a 1 2 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 b d 2 e c 3 b - b b e a - 4 f e 7 - b f 7 0 - 6 7 0 2 9 7 a 6 d 9 6 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 8 5 f 0 d 1 0 - 7 3 6 a - 4 e 0 6 - 9 4 7 3 - 6 9 2 5 6 b 6 c 5 d d 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 f 3 c 4 c 5 e - f 3 8 1 - 4 3 1 c - 8 b f 3 - 4 d 8 1 3 a 9 8 3 c 7 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - d 7 0 a 6 1 9 2 - 1 c a e - 4 2 b c - 8 e 2 6 - 0 3 5 0 1 6 1 9 8 2 c e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 5 0 b 5 a b 5 - 0 8 7 4 - 4 e 9 a - a d 2 3 - f d 5 e b b 4 7 c e b 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 2 1 d a 7 0 e - e 8 d b - 4 d 8 6 - a 5 5 7 - 1 1 2 7 4 8 9 a 6 c e 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 2 c 1 a b 5 8 - f 5 9 2 - 4 5 e 5 - a c b c - 8 9 d 1 2 a c b 1 9 7 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 c c 7 4 b f 1 - 5 7 1 3 - 4 c a c - a 8 1 3 - e 3 c d c 4 7 7 7 c e 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f d d 4 7 f 6 5 - 4 3 9 1 - 4 4 8 a - 9 1 6 a - 4 6 e 2 9 e 1 5 8 d 0 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 f f 3 e b c 8 - a e c b - 4 a 8 4 - 9 c 6 5 - e e 1 c 7 7 d d b 2 5 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 e 3 4 e 5 b 3 - d 4 c 3 - 4 0 8 5 - a 2 9 5 - 4 f e 8 f 8 4 2 b 0 8 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 7 9 2 a d a 8 e - b 6 8 c - 4 d 9 8 - 8 2 5 c - 4 9 4 d 3 8 b d 8 9 6 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 f e a 7 4 2 2 - 1 4 6 9 - 4 9 3 e - 9 4 5 f - 2 a 3 e d b 4 1 8 b e a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 3 4 0 b 2 c 4 - 9 3 6 d - 4 9 b 5 - 8 7 3 9 - 2 a a d 9 3 0 a 6 8 5 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 a d 3 6 a 1 c - 0 d f 1 - 4 b d b - a 5 b 3 - a 4 8 5 5 2 3 b 1 c 3 2 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 9 6 7 b b f b - 4 c 6 c - 4 1 e 6 - b 8 4 4 - 5 4 1 b 3 9 c 4 5 e 4 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f a e e 3 2 4 8 - b 1 5 2 - 4 1 a 8 - 9 b a 8 - 5 a 7 7 e 2 6 a a 4 2 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 8 c 7 c 1 3 8 - 1 8 d c - 4 3 1 5 - a 4 7 b - e 2 9 1 9 f 1 c 1 4 a b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 9 d 8 3 7 3 9 - 1 9 7 2 - 4 8 b 9 - b 0 e e - 4 7 9 e f c e 4 7 0 1 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 a a 7 c 1 6 4 - a 9 3 9 - 4 f f 7 - a 9 0 1 - b 7 e 6 a 2 6 8 0 d c d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 0 f 7 8 c e 9 - 9 7 1 3 - 4 f 1 0 - 8 5 0 0 - 6 2 4 5 7 4 3 3 6 b a 1 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 8 d 8 4 a e 3 - b 6 b 3 - 4 0 6 c - a 0 0 0 - 0 8 5 8 2 9 2 8 3 c 1 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 8 4 9 7 6 c e - 4 c 4 f - 4 3 9 0 - b 7 5 0 - 9 2 2 0 5 d 6 0 b 0 5 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 4 3 9 b 8 c a 5 - a c a 8 - 4 b 7 9 - 8 b 1 9 - c 7 b 1 8 1 d a 3 7 d 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

