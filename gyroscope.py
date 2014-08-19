import smbus
import math

GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

class mpu6050:
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c
    bus = None
    address = 0x68

    def __init__(self, address):
        self.address = address
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(self.address, power_mgmt_1, 1)

    def read_byte(self, adr):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)

    def get_gyro_out(self):
        gyro_xout = self.read_word_2c(GYRO_XOUT)
        gyro_yout = self.read_word_2c(GYRO_YOUT)
        gyro_zout = self.read_word_2c(GYRO_ZOUT)
        return (gyro_xout / 131, gyro_yout / 131, gyro_zout / 131)

    def get_accel_out(self):
        accel_xout = self.read_word_2c(ACCEL_XOUT)
        accel_yout = self.read_word_2c(ACCEL_YOUT)
        accel_zout = self.read_word_2c(ACCEL_ZOUT)
        return (accel_xout, accel_yout, accel_zout, accel_xout / 16384, accel_yout / 16384, accel_zout / 16384)

    def get_rotation_x_y(self):
        accel = self.get_accel_out()
        return (self.get_x_rotation(accel[3], accel[4], accel[5]), self.get_y_rotation(accel[3], accel[4], accel[5]))


"""37  bus = smbus.SMBus(0) # or bus = smbus.SMBus(1) for Revision 2 boards
38  address = 0x68       # This is the address value read via the i2cdetect command
39
40  # Now wake the 6050 up as it starts in sleep mode
41  bus.write_byte_data(address, power_mgmt_1, 0)
42
43  print "gyro data"
44  print "---------"
45
46  gyro_xout = read_word_2c(0x43)
47  gyro_yout = read_word_2c(0x45)
48  gyro_zout = read_word_2c(0x47)
49
50  print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
51  print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
52  print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
53
54  print
55  print "accelerometer data"
56  print "------------------"
57
58  accel_xout = read_word_2c(0x3b)
59  accel_yout = read_word_2c(0x3d)
60  accel_zout = read_word_2c(0x3f)
61
62  accel_xout_scaled = accel_xout / 16384.0
63  accel_yout_scaled = accel_yout / 16384.0
64  accel_zout_scaled = accel_zout / 16384.0
65
66  print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
67  print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
68  print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled
69
70  print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
71  print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)"""
