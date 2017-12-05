"""A fully-functional terminal emulator in a Jupyter notebook."""
__version__ = '0.2.0'
from .xterm import Xterm

def load_ipython_extension(ipython):
    ipython.register_magics(Xterm)
