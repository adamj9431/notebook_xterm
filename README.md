# notebook_xterm
A fully-functional terminal emulator in an IPython/Jupyter notebook. This is useful for notebook environments that don't provide shell access. Uses [xterm.js](https://xtermjs.org) for a VT100-compliant Javascript terminal. Instead of an actual WebSocket, the notebook uses the Javascript Jupyter cell execute function `Jupyter.notebook.kernel.execute()` as a channel to communicate between the Python runtime on the server (`TerminalServer`) and JavaScript runtime in the browser (`TerminalClient`).

![jupyter-nb-terminal-emulator-demo](https://user-images.githubusercontent.com/1238730/32994956-04cb26da-cd3c-11e7-9f7c-527de15f654c.gif)

## Getting Started
Check out [IBM Data Science Experience](https://datascience.ibm.com/) for a free, managed data science platform that includes a Jupyter notebook server.

Link to an [Example notebook](example.ipynb)

From within an IPython notebook (Python 3), install the package using pip:
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
+ Python 3
+ [IBM Data Science Experience](https://datascience.ibm.com/)
+ Jupyter 4.3.0

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contributing
Pull requests welcome!
