from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
from twisted.internet import reactor

Light_Actuator_Pin_R = 11
Light_Actuator_Pin_G = 12
Light_Actuator_Pin_B = 13

if __name__ == "__main__":
    class Light_Actuator(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Light_Actuator')
            self.light_actuator_gpio_R = pin_mode(Light_Actuator_Pin_R, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.light_actuator_gpio_G = pin_mode(Light_Actuator_Pin_G, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.light_actuator_gpio_B = pin_mode(Light_Actuator_Pin_B, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.count = 0
        def update(self,obj,pID=None,val=None):
            try:
                if pID == 0:
                    if val == True:
                        self.count += 1
                        if self.count > 125:
                            self.count =0
                        print "Light Actuator On"
                    else:
                        print "Light Actuator Off"
                    if self.count % 8 == 0:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 0)
                        digital_write(self.light_actuator_gpio_G, 0)
                        digital_write(self.light_actuator_gpio_B, 0)
                    elif self.count % 8 == 1:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 0)
                        digital_write(self.light_actuator_gpio_G, 0)
                        digital_write(self.light_actuator_gpio_B, 1)
                    elif self.count % 8 == 2:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 0)
                        digital_write(self.light_actuator_gpio_G, 1)
                        digital_write(self.light_actuator_gpio_B, 0)
                    elif self.count % 8 == 3:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 0)
                        digital_write(self.light_actuator_gpio_G, 1)
                        digital_write(self.light_actuator_gpio_B, 1)
                    elif self.count % 8 == 4:
                        digital_write(self.light_actuator_gpio_R, 1)
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_G, 0)
                        digital_write(self.light_actuator_gpio_B, 0)
                    elif self.count % 8 == 5:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 1)
                        digital_write(self.light_actuator_gpio_G, 0)
                        digital_write(self.light_actuator_gpio_B, 1)
                    elif self.count % 8 == 6:
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_R, 1)
                        digital_write(self.light_actuator_gpio_G, 1)
                        digital_write(self.light_actuator_gpio_B, 0)
                    elif self.count % 8 == 7:
                        digital_write(self.light_actuator_gpio_R, 1)
                        print "self.count %d",self.count
                        digital_write(self.light_actuator_gpio_G, 1)
                        digital_write(self.light_actuator_gpio_B, 1)

            except IOError:
                print ("Error")

    class MyDevice(Device):
        def __init__(self,addr,localaddr):
            Device.__init__(self,addr,localaddr)

        def init(self):
            cls = Light_Actuator()
            self.addClass(cls,0)
            self.obj_light_actuator = self.addObject(cls.ID)

    if len(sys.argv) <= 2:
        print 'python %s <gip> <dip>:<port>' % sys.argv[0]
        print '      <gip>: IP addrees of gateway'
        print '      <dip>: IP address of Python device'
        print '      <port>: An unique port number'
        print ' ex. python %s 192.168.4.7 127.0.0.1:3000' % sys.argv[0]
        sys.exit(-1)

    d = MyDevice(sys.argv[1],sys.argv[2])
    reactor.run()
