# notebook_xterm
[![PyPI version](https://badge.fury.io/py/notebook-xterm.svg)](https://badge.fury.io/py/notebook-xterm)

A fully-functional terminal emulator in an IPython/Jupyter notebook. This is useful for notebook environments that don't provide shell access. Uses [xterm.js](https://xtermjs.org) for a VT100-compliant Javascript terminal front-end component. Instead of an actual WebSocket, notebook_xterm uses the Javascript Jupyter cell execute function `Jupyter.notebook.kernel.execute()` as a channel to communicate between the Python runtime on the server (`TerminalServer`) and JavaScript runtime in the browser (`TerminalClient`).

![notebook_xterm_animation](https://user-images.githubusercontent.com/1238730/33512219-7d093170-d6f9-11e7-905f-480d62d17cd2.gif)

## Getting Started
Link to an [Example notebook](example.ipynb).

Check out [IBM Data Science Experience](https://datascience.ibm.com/) for a free, managed data science platform that includes a Jupyter notebook server.

----

From within an IPython notebook, install the package using pip:
```
!pip install notebook_xterm
```

Load the IPython extension. You'll need to reload the extension each time the notebook kernel starts. Alternatively, you can add notebook_xterm to the [configuration file](http://ipython.readthedocs.io/en/stable/config/extensions/index.html#using-extensions) to load it automatically.
```
%load_ext notebook_xterm
```

To display a terminal, type the [magic function](http://ipython.readthedocs.io/en/stable/interactive/magics.html) `%xterm` in a blank cell:
```
%xterm
```

## Tested Environments
+ [IBM Data Science Experience](https://datascience.ibm.com/)
+ Jupyter 4.3.0
+ Python 2 and 3

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contributing
Pull requests welcome!
