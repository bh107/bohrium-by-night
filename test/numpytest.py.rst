
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-11-27 04:01:43.974015.

The CPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  
  Error in [node:impl]: /home/bhbuilder/.local/lib/libbh_vem_node.so: undefined symbol: bh_component_config_lookup_bool
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  
  Error in [node:impl]: /home/bhbuilder/.local/lib/libbh_vem_node.so: undefined symbol: bh_component_config_lookup_bool
  
