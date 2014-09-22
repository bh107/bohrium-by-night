
Raw Benchmark Output
====================

Running N-Body on Octuplets using NumPy/CPU
    commit: `#e2eb8cda5af33d49993cdc9c0473aa962908adf4 <https://bitbucket.org/bohrium/bohrium/commits/e2eb8cda5af33d49993cdc9c0473aa962908adf4>`_,
    time: 2014-09-22 13:38:42.446690.

    command: ``python benchmark/Python/nbody.py --size=100*10 --bohrium=False``

Run 00
~~~~~~
    stdout::

        benchmark/Python/nbody.py - backend: None, bohrium: False, size: 100*10, elapsed-time: 0.059385
        

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
        



