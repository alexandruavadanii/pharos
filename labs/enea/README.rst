.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) 2018 OPNFV.

.. ENEA lab temporary PDF/IDF definitions

=========
TEST PODS
=========

enea-virtual1
=============

- x86 virtual POD (classic layout), noha (or ha without VCP);
- 1 x FN (x86_64);
- 4 x FN VM nodes (x86_64);

enea-hybrid1
============

- multiarch (x86_64 + aarch64) hybrid (virtual + baremetal) POD, ha without VCP;
- 1 x FN (x86_64);
- 3 x FN VM nodes (x86_64);
- 3 x baremetal nodes (aarch64);
