import pty, os, tty, termios, time, sys, base64, struct, signal
from fcntl import fcntl, F_GETFL, F_SETFL, ioctl

class TerminalServer:
    def __init__(self):
        self.closed = False
        self.pid, self.fd = pty.fork()
        if self.pid == pty.CHILD:
            # we are in the forked process
            # blow it away and replace with a shell
            os.execvp('bash',['bash'])
        else:
            tty.setraw(self.fd, termios.TCSANOW)

            #open the shell process file descriptor as read-write
            self.file = os.fdopen(self.fd,'wb+', buffering=0)

            #set the file reads to be nonblocking
            flags = fcntl(self.file, F_GETFL)
            fcntl(self.file, F_SETFL, flags | os.O_NONBLOCK)

    def transmit(self,data):
        # data in the "channel" is b64 encoded so that control characters
        # don't get lost
        os.write(self.fd, base64.b64decode(data))
        self.receive()

    def receive(self):
        try:
            data = os.read(self.fd, 8192)
        except OSError:
            data = b''
        sys.stdout.write(base64.b64encode(data))

    def update_window_size(self, rows, cols):
        #notify that the pty size should change to match xterm.js
        TIOCSWINSZ = getattr(termios, 'TIOCSWINSZ', -2146929561)
        s = struct.pack('HHHH', rows, cols, 0, 0)
        ioctl(self.fd, TIOCSWINSZ, s)
        self.receive()
    def close(self):
        if not self.closed:
            #send hang up to bash since the xterm is closing
            os.kill(self.pid, signal.SIGHUP)

    def __del__(self):
        self.close()
