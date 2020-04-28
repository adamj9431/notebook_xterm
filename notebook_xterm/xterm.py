from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
from .terminalserver import TerminalServer
from IPython.core.display import display, HTML
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from base64 import b64encode
from uuid import uuid4

JS_FILE_NAME = 'terminalclient.js'

@magics_class
class Xterm(Magics):

    @line_magic
    def xterm(self, line):
        jsPath = os.path.abspath(os.path.dirname(__file__)) + '/' + JS_FILE_NAME
        with open(jsPath) as f:
            terminalClient_js = f.read()

        unique_id = str(uuid4())
        markup = f"""
        <div id="notebook_xterm_{unique_id}"></div>
        <script id="notebook_script">{terminalClient_js}

        window.terminalClient = new TerminalClient($('#notebook_xterm_{unique_id}'))
        </script>
        """
        display(HTML(markup))
        ts = self.getTerminalServer()

        return self.getTerminalServer()

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
