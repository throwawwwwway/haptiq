Documentation for helping other developers
==========================================

Requisites
----------

* Python 2.7 or 3.4
* Pip (should be installed automatically) _if not: https://pip.pypa.io/en/latest/installing.html
* Nose	(install with pip: pip install nose)
* Pytest (install with pip: pip install pytest)
* Pytest cov (install with pip: pip install pytest-cov)

Testing
-------

The different layers of the API will be placed in the app folder. Each layer is tested in the test folder.

In order to launch test, in the root of the project:
>>> py.test .

In order to check the test coverage
>>> py.test --cov app test/


Development Design Rational
---------------------------

* This README uses rst notation for furture protability with _Sphinx: http://sphinx-doc.org/
* Trying the get the most out of TTD _Test Driven Development: http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137
* Code styling is checked with _flake8: https://github.com/dreadatour/Flake8Lint
