'''
Determine number of common integers among two sets

Status: Accepted
'''

###############################################################################

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    """Kattis-ready text IO routines"""
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        """Fast replacement of IO read function"""
        while True:
            bytez = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not bytez:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(bytez)
            self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        """Fast replacement of IO readline function"""
        while self.newlines == 0:
            bytez = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = bytez.count(b"\n") + (not bytez)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(bytez)
            self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        """Fast replacement of write flush function"""
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0)
            self.buffer.seek(0)


class IOWrapper(IOBase):
    """Utility to allow wrapping of custom class for stdin and stdout"""
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

###############################################################################

def main():
    """Read input and print output of number in set intersection"""

    while True:
        jacks, jills = [int(i) for i in input().strip().split()]
        if jacks == 0 and jills == 0:
            break

        jack, jill = set(), set()
        for _ in range(jacks): jack.add(int(input()))
        for _ in range(jills): jill.add(int(input()))

        print(str(len(jack & jill)))

###############################################################################

if __name__ == '__main__':
    main()
