from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
from .terminalserver import TerminalServer
from IPython.core.display import display, HTML
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
import time
from base64 import b64encode

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
        <script id="notebook_script">{0}</script>
        """.format(terminalClient_js)
        display(HTML(markup))
        ts = self.getTerminalServer()
        ts.initial_command = bytes(line, encoding="utf-8") + b"\r"

        return self.getTerminalServer()
        #ts.transmit(b64encode(b"ls"))

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
