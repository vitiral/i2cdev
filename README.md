# i2cdev

very simple i2c module for linux 

```
from devi2c import I2C
device, bus = 0x42, 0
i2c = I2C(device, bus)
value = i2c.read(1)         # read 1 byte
i2c.write(b’some raw data’)     # write bytes
i2c.close()                 # close connection
```

It is recommended to use the `struct` module to pack data into bytes

For a list of data that is all in range(256) you can also use `bytearray(data)`
