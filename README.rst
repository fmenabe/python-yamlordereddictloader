This is a loader for PyYAML allowing to keep items order when loading a file. In
some rare cases, it may be desired to keep the order of items when loading the
YAML file. For example, this is the case of the ``clg`` module
(https://pypi.python.org/pypi/clg) that generate a command-line from a
dictionnary. When a YAML file is used, and in a purely esthetic purpose, it
could be nice to keep order of the items.

The loader is based on stackoverflow topic:
http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts

To install it
-------------

.. code-block:: bash

    $ pip install yamlordereddictload

To use it
---------

.. code-block:: python

    import yaml
    import yamlordereddictloader

    datas = yaml.load(open('myfile.yml'), Loader=yamlordereddictloader.Loader)
