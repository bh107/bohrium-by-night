
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: [#88335e0b0a721a97d5d4977fc8a3d842f4626957](https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957),
    time: 2014-09-18 13:20:04.736009.

The CPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_array_create.py/array_create/zeros
  ************************ Finish ************************
  
  [84302 refs]
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_array_create.py/array_create/zeros
  
  clGetPlatformIDs
  terminate called after throwing an instance of 'std::runtime_error'
    what():  Error in the initialization of the VEM.
  
  
