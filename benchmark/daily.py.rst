
Python Benchmark Suite
======================

Running suites/daily_benchmark.py on Octuplets
    commit: `#b11f24fd2c44c4d5a0979fc1ef3fd94e59ccd878 <https://bitbucket.org/bohrium/bohrium/commits/b11f24fd2c44c4d5a0979fc1ef3fd94e59ccd878>`_,
    time: 2015-03-26 04:06:12.417209.

Heat Equation
-------------

`NumPy/CPU <raw_output/heat_equation-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 b b e 6 4 d f - 5 0 2 f - 4 a 2 b - b b b 1 - 2 3 2 e 2 4 b 8 c 5 5 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/heat_equation-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 7 e 1 6 7 b 4 - 1 8 4 0 - 4 e a 6 - 8 6 f 0 - 8 1 c 3 9 a 5 0 3 2 a 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/heat_equation-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 2 1 e 5 5 7 5 - 7 6 2 2 - 4 8 3 a - b d 5 7 - 0 4 6 7 6 f 3 1 a b 6 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / h e a t _ e q u a t i o n . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/heat_equation_runtime.png

Black Scholes
-------------

`NumPy/CPU <raw_output/black_scholes-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 b 6 6 4 d 0 0 - 1 e 4 4 - 4 f 5 2 - b c f e - e 9 0 e 7 0 9 b b 8 0 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/black_scholes-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - c 2 0 9 7 6 b 0 - d 3 e f - 4 1 a 4 - 8 b 0 4 - 8 3 d 5 d a 2 8 1 f 0 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/black_scholes-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 d 6 f 9 c b b - 6 a a 8 - 4 1 2 0 - a 1 4 b - 6 3 6 a 2 d c 3 7 e a 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / b l a c k _ s c h o l e s . p y   - - s i z e = 1 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/black_scholes_runtime.png

Monte Carlo Pi
--------------

`NumPy/CPU <raw_output/mc-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f e 1 9 8 e b 5 - a e f 3 - 4 2 9 8 - a c 4 7 - c c 7 0 3 a 5 0 d c e 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mc-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 0 4 5 f b 8 7 - d b 7 3 - 4 8 8 f - b 7 c 6 - 0 a 6 0 d e 9 7 6 5 4 f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mc-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 9 c 2 a 9 6 0 - f 6 c a - 4 2 9 7 - 9 7 7 8 - c 0 6 7 2 f 8 2 8 a a e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m c . p y   - - s i z e = 1 0 0 0 0 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mc_runtime.png

Wire World
----------

`NumPy/CPU <raw_output/wireworld-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 1 9 f 4 b 6 0 - 5 5 3 a - 4 c 0 7 - 8 6 d a - 6 a 3 f 6 2 a 7 8 c 0 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/wireworld-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 8 7 6 5 e e 0 - 5 4 5 5 - 4 7 7 2 - 8 d a a - 1 a 7 6 4 7 7 b e a 6 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/wireworld-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 8 a 9 e a 3 4 - a 7 b 2 - 4 0 6 2 - 8 4 5 7 - 8 0 e b 2 a 6 2 6 3 3 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / w i r e w o r l d . p y   - - s i z e = 1 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/wireworld_runtime.png

Lattice Boltzmann D2Q9
----------------------

`NumPy/CPU <raw_output/lattice_boltzmann_D2Q9-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 8 8 b a 9 0 6 - 5 1 a e - 4 2 b c - b 7 8 6 - 2 8 0 a 0 6 f c 9 2 e b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 3 1 1 1 7 8 c - f 3 0 8 - 4 8 e 6 - a a 6 1 - d c 6 1 d 1 1 6 1 1 e 3 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lattice_boltzmann_D2Q9-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 3 f c 9 4 c d 8 - b 0 2 3 - 4 a 8 e - 8 a 1 5 - f b 1 3 4 2 a d 6 6 7 e . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l a t t i c e _ b o l t z m a n n _ D 2 Q 9 . p y   - - s i z e = 1 0 0 0 * 1 0 0 0 * 1 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lattice_boltzmann_D2Q9_runtime.png

Gauss Elimination
-----------------

`NumPy/CPU <raw_output/gauss-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 6 b 6 e 9 c b 3 - 6 e 9 5 - 4 9 1 6 - a 1 6 1 - 8 6 5 a 5 8 a 9 3 8 3 a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/gauss-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 a 3 a 9 f b c - 3 6 f 7 - 4 c 5 d - 8 5 f c - e 2 5 2 e 2 9 1 9 6 2 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/gauss-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 8 5 b 8 9 5 f f - 5 1 8 4 - 4 e e 3 - b 2 e b - d 7 1 1 5 e 7 2 a 6 e 7 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / g a u s s . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/gauss_runtime.png

Matrix Multiplication
---------------------

`NumPy/CPU <raw_output/mxmul-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a 3 5 3 4 6 7 4 - 4 1 a 2 - 4 1 0 2 - b 5 3 d - b c 0 3 d 9 5 0 9 3 c c . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/mxmul-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 6 f a c 7 7 f - 9 8 d d - 4 1 4 e - a 0 3 3 - a e 4 f d 6 3 9 b 1 2 b . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/mxmul-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 1 b d 1 5 a c - d d e 0 - 4 8 2 0 - a 3 8 6 - 4 b 2 5 3 8 8 0 8 9 8 8 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / m x m u l . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/mxmul_runtime.png

LU Factorization
----------------

`NumPy/CPU <raw_output/lu-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 8 f f 8 b 7 c - 7 2 2 a - 4 4 1 a - a 7 8 b - a 0 a 1 5 7 1 c 4 8 8 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/lu-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a c 3 c 8 a 5 3 - a 3 e e - 4 f 9 4 - 8 d 7 c - e 5 2 e 7 9 b 1 a 5 a a . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/lu-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b 0 6 c a 7 5 9 - 0 7 6 9 - 4 d 0 5 - b 0 1 8 - 3 6 c 5 8 7 5 9 7 d 8 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / l u . p y   - - s i z e = 1 0 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/lu_runtime.png

Convolution 3D
--------------

`NumPy/CPU <raw_output/convolve_3d-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 9 c 5 e 9 5 8 - 2 8 1 7 - 4 8 0 3 - 8 7 5 5 - 3 5 5 9 9 2 1 9 5 5 3 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/convolve_3d-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 e 2 4 a 2 3 0 - 3 d b 3 - 4 c 6 4 - 9 3 6 2 - 1 f 1 4 8 7 3 6 9 c 3 d . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/convolve_3d-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 9 d f 9 1 0 7 7 - f 9 c a - 4 4 a 9 - 9 f 4 0 - a 6 0 e 8 4 c 1 d 2 4 c . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / c o n v o l v e _ 3 d . p y   - - s i z e = 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/convolve_3d_runtime.png

Shallow Water
-------------

`NumPy/CPU <raw_output/shallow_water-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 5 f d b c c e 5 - 1 0 5 1 - 4 f 3 d - a 9 c d - 8 c c a 4 7 b 8 5 4 e f . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/shallow_water-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - b e 1 f 2 1 6 e - 2 6 d 9 - 4 a 9 1 - 8 1 6 0 - 6 1 c c 1 3 9 2 6 7 b 5 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/shallow_water-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 f 9 e 2 0 c a - f b 6 3 - 4 5 e f - b d 6 e - 4 b 2 6 0 9 6 7 3 e 5 4 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / s h a l l o w _ w a t e r . p y   - - s i z e = 2 0 0 0 * 2 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/shallow_water_runtime.png

Jacobi Stencil
--------------

`NumPy/CPU <raw_output/jacobi_stencil-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 1 5 4 2 8 8 7 8 - 5 4 1 3 - 4 5 5 c - 8 b 1 0 - e 0 3 8 d 6 0 c 2 b e 9 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/jacobi_stencil-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 2 d f 8 f b d 1 - d a a 7 - 4 a a 9 - 9 0 2 b - 2 b e b 6 0 d 8 9 1 f c . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/jacobi_stencil-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - 0 2 1 3 3 1 5 8 - d 4 2 8 - 4 0 1 a - b e 3 1 - 4 3 8 d 7 b 5 b 0 8 a 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / j a c o b i _ s t e n c i l . p y   - - s i z e = 3 0 0 0 * 3 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/jacobi_stencil_runtime.png

N-Body
------

`NumPy/CPU <raw_output/nbody-NumPy-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - e 9 6 4 d c d d - a 5 1 6 - 4 3 5 f - 8 0 e 2 - e e f 8 0 1 d 9 b 4 7 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = F a l s e``

`Bohrium/CPU <raw_output/nbody-Bohrium-cpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - a a d 4 6 b 6 3 - a 1 1 3 - 4 0 d 3 - a 1 8 3 - 3 b e e 2 0 7 e c 6 2 6 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``

`Bohrium/GPU <raw_output/nbody-Bohrium-gpu.rst>`_: ``  / u s r / b i n / t i m e   - v   - o   / h o m e / b h b u i l d e r / b e n c h p r e s s / b h - j o b - f 8 c 8 8 3 6 2 - b a 2 9 - 4 7 c 8 - a b 6 8 - 2 2 d 6 d 4 e 0 6 3 d 0 . s h - 2 . t i m e   p y t h o n   b e n c h m a r k / p y t h o n / n b o d y . p y   - - s i z e = 1 0 0 0 * 1 0 0   - - b o h r i u m = T r u e``



.. image:: https://bytebucket.org/bohrium/bohrium-by-night/raw/master/benchmark/gfx/nbody_runtime.png

