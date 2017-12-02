import os
from .terminalserver import TerminalServer
from IPython.core.display import display, HTML
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

JS_FILE_NAME = 'terminalclient.js'

@magics_class
class Xterm(Magics):

    @line_magic
    def xterm(self, line):
        jsPath = os.path.abspath(os.path.dirname(__file__)) + '/' + JS_FILE_NAME
        with open(jsPath) as f:
            terminalClient_js = f.read()

        markup = """
        <div id="notebook_xterm"></div>
        <script>{0}</script>
        """.format(terminalClient_js)
        display(HTML(markup))

    def getTerminalServer(self):
        try:
            ts = self.ts
        except AttributeError:
            self.ts = ts = TerminalServer()
        return ts

    def deleteTerminalServer(self):
        if self.ts:
            self.ts.close()
            del self.ts
