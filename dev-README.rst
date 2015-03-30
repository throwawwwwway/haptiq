Documentation for helping other developers
==========================================

Requisites
----------

* Python 2.7 or 3.4
* Pip (should be installed automatically) `if not <https://pip.pypa.io/en/latest/installing.html>`_
* Nose	(install with pip: pip install nose)
* Pytest (install with pip: pip install pytest)
* Pytest cov (install with pip: pip install pytest-cov)

Testing
-------

The different layers of the API will be placed in the app folder. Each layer is tested in the test folder.

In order to launch test, in the root of the project:
> py.test .

In order to check the test coverage
> py.test --cov app test/


Development Design Rational
---------------------------

* This README uses rst notation for furture protability with `Sphinx <http://sphinx-doc.org>`_
* Trying the get the most out of TTD `Test Driven Development <http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137>`_
* Code styling is checked with `flake8 <https://github.com/dreadatour/Flake8Lint>`_
