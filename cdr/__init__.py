import sys
from importlib import import_module

_module = import_module("python_cdr")
sys.modules[__name__] = _module
