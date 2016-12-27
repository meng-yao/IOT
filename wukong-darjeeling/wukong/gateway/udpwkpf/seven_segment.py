from udpwkpf import WuClass, Device
import sys
import time
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
            self.gpio_2 = pin_mode(digit_2, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_3 = pin_mode(digit_3, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_4 = pin_mode(digit_4, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_A = pin_mode(Pin_A, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_B = pin_mode(Pin_B, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_C = pin_mode(Pin_C, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_D = pin_mode(Pin_D, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_E = pin_mode(Pin_E, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_F = pin_mode(Pin_F, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.gpio_G = pin_mode(Pin_G, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.counter = 0
            self.value = 0 
        def update(self,obj,pID=None,val=None):
            try:
                self.counter += 1
                digital_write(self.gpio_A,1)
                digital_write(self.gpio_B,1)
                digital_write(self.gpio_C,1)
                digital_write(self.gpio_D,1)
                digital_write(self.gpio_E,1)
                digital_write(self.gpio_F,1)
                digital_write(self.gpio_G,1)
                if pID ==0:
                    val = obj.setProperty(pID,val) 
                elif pID ==1:
                    val = obj.setProperty(pID,val) 
                elif pID ==2:
                    val = obj.setProperty(pID,val) 
                elif pID ==3:
                    val = obj.setProperty(pID,val) 
                if self.counter % 4 == 1:
                    digital_write(self.gpio_1,1)
                    digital_write(self.gpio_2,0)
                    digital_write(self.gpio_3,0)
                    digital_write(self.gpio_4,0)
                    self.value = obj.getProperty(0);
                elif self.counter % 4 == 2:
                    digital_write(self.gpio_1,0)
                    digital_write(self.gpio_2,1)
                    digital_write(self.gpio_3,0)
                    digital_write(self.gpio_4,0)
                    self.value = obj.getProperty(1);
                elif self.counter % 4 == 3:
                    digital_write(self.gpio_1,0)
                    digital_write(self.gpio_2,0)
                    digital_write(self.gpio_3,1)
                    digital_write(self.gpio_4,0)
                    self.value = obj.getProperty(2);
                elif self.counter % 4 == 0:
                    digital_write(self.gpio_1,0)
                    digital_write(self.gpio_2,0)
                    digital_write(self.gpio_3,0)
                    digital_write(self.gpio_4,1)
                    self.value = obj.getProperty(3);
                
                print self.value
                if self.value == 0:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,0)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,1)

                elif self.value == 1:
                    digital_write(self.gpio_A,1)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,1)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,1)
                    digital_write(self.gpio_G,1)
                elif self.value == 2:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,1)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,0)
                    digital_write(self.gpio_F,1)
                    digital_write(self.gpio_G,0)
                elif self.value == 3:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,1)
                    digital_write(self.gpio_G,0)
                elif self.value == 4:
                    digital_write(self.gpio_A,1)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,1)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,0)
                elif self.value == 5:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,1)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,0)
                elif self.value == 6:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,1)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,0)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,0)
                elif self.value == 7:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,1)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,1)
                    digital_write(self.gpio_G,1)
                elif self.value == 9:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,1)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,0)
                else:
                    digital_write(self.gpio_A,0)
                    digital_write(self.gpio_B,0)
                    digital_write(self.gpio_C,0)
                    digital_write(self.gpio_D,0)
                    digital_write(self.gpio_E,0)
                    digital_write(self.gpio_F,0)
                    digital_write(self.gpio_G,0)
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
