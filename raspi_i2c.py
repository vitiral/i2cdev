#!/usr/bin/python
import io
import fcntl
from threading import Lock


class i2c(object):
    lock = Lock()

    def __init__(self, device, bus, address):
        self.fr = io.open("/dev/i2c-" + str(bus), "rb", buffering=0)
        self.fw = io.open("/dev/i2c-" + str(bus), "wb", buffering=0)

        # set device address
        fcntl.ioctl(self.fr, address, device)
        fcntl.ioctl(self.fw, address, device)

    def write(self, data: bytes):
        self.fw.write(data)

    def read(self, num: int):
        return self.fr.read(num)

    def close(self):
        self.fw.close()
        self.fr.close()
