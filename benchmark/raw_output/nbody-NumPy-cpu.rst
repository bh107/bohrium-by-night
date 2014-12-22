
Raw Benchmark Output
====================

Running N-Body on Octuplets using NumPy/CPU
    commit: `#fa32761e3dc4132d8188145007c8189576f85446 <https://bitbucket.org/bohrium/bohrium/commits/fa32761e3dc4132d8188145007c8189576f85446>`_,
    time: 2014-12-22 04:06:54.728745.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=False``

Run 00
~~~~~~
    stdout::

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 59.045243
        

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

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 58.787881
        

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

        benchmark/Python/nbody.py - target: None, bohrium: False, size: 1000*100, elapsed-time: 59.238320
        

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
        



