# jupyter-nb-terminal-emulator

A fully-functional terminal emulator in a Jupyter notebook. Uses xterm.js for a VT100-compliant Javascript terminal. Instead of an actual WebSocket, the notebook uses the Javascript Jupyter cell execute function Jupyter.notebook.kernel.execute() as a channel to communicate between the Python runtime (TerminalServer) and browser (TerminalClient). TermalServer forks a shell and attaches stdin and stdout to the aforementioned channel.
