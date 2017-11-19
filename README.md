# jupyter-nb-terminal-emulator

A fully-functional terminal emulator in a Jupyter notebook. Uses [xterm.js](https://xtermjs.org) for a VT100-compliant Javascript terminal. Instead of an actual WebSocket, the notebook uses the Javascript Jupyter cell execute function `Jupyter.notebook.kernel.execute()` as a channel to communicate between the Python runtime (`TerminalServer`) and browser (`TerminalClient`). `TerminalServer` forks a shell and attaches stdin and stdout to the aforementioned channel.

![jupyter-nb-terminal-emulator-demo](https://user-images.githubusercontent.com/1238730/32994956-04cb26da-cd3c-11e7-9f7c-527de15f654c.gif)

## Tested Environments
+ [IBM Data Science Experience](https://datascience.ibm.com)
+ Jupyter 4.3.0

Pull requests welcome!
