
Raw Benchmark Output
====================

Running N-Body on Octuplets using NumPy/CPU
    commit: `#0422b812bb026bb213aace5bf9a9bfb8f978b58d <https://bitbucket.org/bohrium/bohrium/commits/0422b812bb026bb213aace5bf9a9bfb8f978b58d>`_,
    time: 2014-10-15 04:07:16.097156.

    command: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=False``

Run 00
~~~~~~
    stdout::

        benchmark/Python/nbody.py - backend: None, bohrium: False, size: 100*10, elapsed-time: 0.059570
        

    stderr::

        benchmark/Python/nbody.py:54: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(r)[:] = 1.0
        benchmark/Python/nbody.py:67: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fx)[:] = 0.0
        benchmark/Python/nbody.py:68: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fy)[:] = 0.0
        benchmark/Python/nbody.py:69: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fz)[:] = 0.0
        



