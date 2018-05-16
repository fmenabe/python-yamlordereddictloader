python-yamlordereddictloader
============================

**DEPRECATED: the** `Phynix/yamlloader <https://github.com/Phynix/yamlloader>`_ **project
provide an improved version of this library with unit tests, performance improvements
(by providing access to the C implementation of PyYAML) and is more actively developed.
You should use it!**

.. image:: https://img.shields.io/pypi/l/yamlordereddictloader.svg
           :target: https://opensource.org/licenses/MIT
           :alt: License

.. image:: https://img.shields.io/pypi/pyversions/yamlordereddictloader.svg
           :target: https://pypi.python.org/pypi/yamlordereddictloader
           :alt: Versions

.. image:: https://img.shields.io/pypi/v/yamlordereddictloader.svg
           :target: https://pypi.python.org/pypi/yamlordereddictloader
           :alt: PyPi

.. image:: https://img.shields.io/badge/github-repo-yellow.jpg
           :target: https://github.com/fmenabe/python-yamlordereddictloader
           :alt: Code repo

.. image:: https://landscape.io/github/fmenabe/python-yamlordereddictloader/master/landscape.svg?style=flat
           :target: https://landscape.io/github/fmenabe/python-yamlordereddictloader/master
           :alt: Code Health

This module provide a loader and a dumper for PyYAML allowing to keep items order
when loading a file (by putting them in ``OrderedDict`` objects) and to manage
``OrderedDict`` objects when dumping to a file.

The loader is based on stackoverflow topic (thanks to Eric Naeseth):
http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts#answer-5121963

Self promotion: I use it a lot with `clg <https://clg.readthedocs.io>`_, which
allows to generate command-line definition from a configuration file, for keeping
order of subcommands, options and arguments in the help message!


To install it
-------------

.. code-block:: bash

    $ pip install yamlordereddictloader

Loader usage
------------

.. code-block:: python

    import yaml
    import yamlordereddictloader

    data = yaml.load(open('myfile.yml'), Loader=yamlordereddictloader.Loader)

**Note:** For using the safe loader (which want standard YAML tags and does
not construct arbitrary Python objects), replace ``yamlorderdictloader.Loader`` by
``yamlorderedictloader.SafeLoader``.

Dumper usage
------------

.. code-block:: python

    import yaml
    import yamlordereddictloader
    from collections import OrderedDict

    data = OrderedDict([
        ('key1', 'val1'),
        ('key2', OrderedDict([('key21', 'val21'), ('key22', 'val22')]))
    ])
    yaml.dump(
        data,
        open('myfile.yml', 'w'),
        Dumper=yamlordereddictloader.Dumper,
        default_flow_style=False)

**Note:** For using the safe dumper (which produce standard YAML tags and does
not represent arbitrary Python objects), replace ``yamlorderdictloader.Dumper`` by
``yamlorderedictloader.SafeDumper``.
