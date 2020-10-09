==================
pytest-vscodedebug
==================

.. image:: https://img.shields.io/pypi/v/pytest-vscodedebug.svg
    :target: https://pypi.org/project/pytest-vscodedebug
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-vscodedebug.svg
    :target: https://pypi.org/project/pytest-vscodedebug
    :alt: Python versions

.. image:: https://travis-ci.com/tmuguet/pytest-vscodedebug.svg?branch=master
    :target: https://travis-ci.com/tmuguet/pytest-vscodedebug
    :alt: See Build Status on Travis CI

A `pytest`_ plugin to easily enable debugging tests within Visual Studio Code.

Features
--------

Enables debugging a test session within Visual Studio Code, via attaching the debugger.

Installation
------------

You can install "pytest-vscodedebug" via `pip`_ from `PyPI`_:

.. code-block:: bash

    $ pip install pytest-vscodedebug

You will need to configure the debugging in Visual Studio Code, via editing ``.vscode/launch.json``:

.. code-block:: json

    {
      "configurations": [
        {
          "name": "Python: Remote Attach",
          "type": "python",
          "request": "attach",
          "connect": {
            "host": "localhost",
            "port": 10001,
          },
          "pathMappings": [
            {
              "localRoot": "${workspaceFolder}",
              "remoteRoot": "."
            }
          ]
        }
      ]
    }

Usage
-----

You can enable pytest-vscodedebug when running tests with the ``--vscodedebug`` flag:

.. code-block:: bash

    $ py.test --vscodedebug test_testfile.py

By default, it will listen on port 10001, but you can change it via the ``--vscodedebug-port`` option:

.. code-block:: bash

    $ py.test --vscodedebug --vscodedebug-port=5001 test_testfile.py

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-vscodedebug" is free and open source software.

This code is largely based on `adriencaccia`_'s tutorial "`Flask Debugging in VS Code with Hot-Reload 🔥 <https://blog.theodo.com/2020/05/debug-flask-vscode/>`_".

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


.. _`adriencaccia`: https://github.com/adriencaccia
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/tmuguet/pytest-vscodedebug/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
