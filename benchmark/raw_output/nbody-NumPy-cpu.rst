
Raw Benchmark Output
====================

Running N-Body on Octuplets using NumPy/CPU
    commit: `#0e67b7b00f693b98b768cfc3d3c85c2370605c86 <https://bitbucket.org/bohrium/bohrium/commits/0e67b7b00f693b98b768cfc3d3c85c2370605c86>`_,
    time: 2014-11-19 04:07:40.014932.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=False``

Run 00
~~~~~~
    stdout::

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 59.503334
        

    stderr::

        benchmark/Python/nbody.py:55: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(r)[:] = 1.0
        benchmark/Python/nbody.py:68: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fx)[:] = 0.0
        benchmark/Python/nbody.py:69: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fy)[:] = 0.0
        benchmark/Python/nbody.py:70: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fz)[:] = 0.0
        



Run 01
~~~~~~
    stdout::

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 59.627812
        

    stderr::

        benchmark/Python/nbody.py:55: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(r)[:] = 1.0
        benchmark/Python/nbody.py:68: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fx)[:] = 0.0
        benchmark/Python/nbody.py:69: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fy)[:] = 0.0
        benchmark/Python/nbody.py:70: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fz)[:] = 0.0
        



Run 02
~~~~~~
    stdout::

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 59.389035
        

    stderr::

        benchmark/Python/nbody.py:55: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(r)[:] = 1.0
        benchmark/Python/nbody.py:68: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fx)[:] = 0.0
        benchmark/Python/nbody.py:69: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fy)[:] = 0.0
        benchmark/Python/nbody.py:70: FutureWarning: Numpy has detected that you (may be) writing to an array returned
        by numpy.diagonal or by selecting multiple fields in a record
        array. This code will likely break in a future numpy release --
        see numpy.diagonal or arrays.indexing reference docs for details.
        The quick fix is to make an explicit copy (e.g., do
        arr.diagonal().copy() or arr[['f0','f1']].copy()).
          np.diagonal(Fz)[:] = 0.0
        



