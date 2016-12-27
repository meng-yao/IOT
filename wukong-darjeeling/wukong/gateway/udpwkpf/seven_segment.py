from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
from twisted.internet import reactor

digit_1 = 2
digit_2 = 3
digit_3 = 4
digit_4 = 5
Pin_A = 6
Pin_B = 7
Pin_C = 8
Pin_D = 9
Pin_E = 10
Pin_F = 11
Pin_G = 12

if __name__ == "__main__":
    class Seven_Segment(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Seven_Segment')
            self.gpio_1 = pin_mode(digit_1, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_A = pin_mode(Pin_A, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_B = pin_mode(Pin_B, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_C = pin_mode(Pin_C, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_D = pin_mode(Pin_D, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_E = pin_mode(Pin_E, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_F = pin_mode(Pin_F, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_G = pin_mode(Pin_G, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
        def update(self,obj,pID=None,val=None):
            try:
                if pID == 0:
                    if val == 0:
                        digital_write(self.gpio_G,1)
                    elif val == 1:
                        digital_write(self.gpio_C,1)
                        digital_write(self.gpio_D,1)
                        digital_write(self.gpio_E,1)
                        digital_write(self.gpio_F,1)
                        digital_write(self.gpio_G,1)
                        print "Light Actuator On"
                    elif val == 2:
                        digital_write(self.gpio_B,1)
                        digital_write(self.gpio_E,1)
                    elif val == 3:
                        digital_write(self.gpio_D,1)
                        digital_write(self.gpio_E,1)

                    else:
                        digital_write(self.gpio_A,1)
                        print "Light Actuator Off"

            except IOError:
                print ("Error")

    class MyDevice(Device):
        def __init__(self,addr,localaddr):
            Device.__init__(self,addr,localaddr)

        def init(self):
            cls = Seven_Segment()
            self.addClass(cls,0)
            self.obj_Seven_Segment = self.addObject(cls.ID)

    if len(sys.argv) <= 2:
        print 'python %s <gip> <dip>:<port>' % sys.argv[0]
        print '      <gip>: IP addrees of gateway'
        print '      <dip>: IP address of Python device'
        print '      <port>: An unique port number'
        print ' ex. python %s 192.168.4.7 127.0.0.1:3000' % sys.argv[0]
        sys.exit(-1)

    d = MyDevice(sys.argv[1],sys.argv[2])
    reactor.run()
