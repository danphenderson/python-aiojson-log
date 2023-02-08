========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |coveralls| |codecov|
        | |scrutinizer|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-aiojson-log/badge/?style=flat
    :target: https://python-aiojson-log.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/danphenderson/python-aiojson-log/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/danphenderson/python-aiojson-log/actions

.. |coveralls| image:: https://coveralls.io/repos/danphenderson/python-aiojson-log/badge.svg?branch=main&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/danphenderson/python-aiojson-log

.. |codecov| image:: https://codecov.io/gh/danphenderson/python-aiojson-log/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/danphenderson/python-aiojson-log

.. |version| image:: https://img.shields.io/pypi/v/aiojson-log.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/aiojson-log

.. |wheel| image:: https://img.shields.io/pypi/wheel/aiojson-log.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/aiojson-log

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/aiojson-log.svg
    :alt: Supported versions
    :target: https://pypi.org/project/aiojson-log

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/aiojson-log.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/aiojson-log

.. |commits-since| image:: https://img.shields.io/github/commits-since/danphenderson/python-aiojson-log/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/danphenderson/python-aiojson-log/compare/v0.0.0...main


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/danphenderson/python-aiojson-log/main.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/danphenderson/python-aiojson-log/


.. end-badges

 Asynchronous JSON Log Library

* Free software: MIT license

Installation
============

::

    pip install aiojson-log

You can also install the in-development version with::

    pip install https://github.com/danphenderson/python-aiojson-log/archive/main.zip


Documentation
=============


https://python-aiojson-log.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
