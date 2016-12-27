from twisted.internet import reactor
from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
import time
import pyupm_lpd8806

if __name__ == "__main__":
    class Strip_LED(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Strip_LED')
            self.mystrip = pyupm_lpd8806.LPD8806(4,7)
            self.mystrip.show()
            self.mystrip.setPixelColor(0,0,0,0)
            self.mystrip.setPixelColor(1,0,0,0)
            self.mystrip.setPixelColor(2,0,0,0)
            self.mystrip.setPixelColor(3,0,0,0)
            self.mystrip.show()
            print "Light Actuator init success"

        def update(self,obj,pID=None,val=None):
            try:
                if val == 1:
                    
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,10,0,0)
                    self.mystrip.setPixelColor(1,10,0,0)
                    self.mystrip.setPixelColor(2,10,0,0)
                    self.mystrip.setPixelColor(3,10,0,0)
                    self.mystrip.show()
                    time.sleep(0.2)
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,0)
                    self.mystrip.setPixelColor(1,0,0,0)
                    self.mystrip.setPixelColor(2,0,0,0)
                    self.mystrip.setPixelColor(3,0,0,0)
                    self.mystrip.show()
                    time.sleep(0.2)
                    
                    
                    print "Value: %d " % val
                elif val == 2:
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,10,10)
                    self.mystrip.setPixelColor(1,0,0,0)
                    self.mystrip.setPixelColor(2,0,0,0)
                    self.mystrip.setPixelColor(3,0,0,0)
                    self.mystrip.show()
                    time.sleep(0.2)
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,0)
                    self.mystrip.setPixelColor(1,0,10,10)
                    self.mystrip.setPixelColor(2,0,0,0)
                    self.mystrip.setPixelColor(3,0,0,0)
                    self.mystrip.show()
                    time.sleep(0.2)
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,0)
                    self.mystrip.setPixelColor(1,0,0,0)
                    self.mystrip.setPixelColor(2,0,10,10)
                    self.mystrip.setPixelColor(3,0,0,0)
                    self.mystrip.show()
                    time.sleep(0.2)
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,0)
                    self.mystrip.setPixelColor(1,0,0,0)
                    self.mystrip.setPixelColor(2,0,0,0)
                    self.mystrip.setPixelColor(3,0,10,10)
                    self.mystrip.show()
                    time.sleep(0.2)
                    print "Value: %d " % val
                elif val == 3:
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,10)
                    self.mystrip.setPixelColor(1,0,0,10)
                    self.mystrip.setPixelColor(2,0,0,10)
                    self.mystrip.setPixelColor(3,0,0,10)
                    self.mystrip.show()
                    print "Value: %d " % val
                elif val == 4:
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,10,0,0)
                    self.mystrip.setPixelColor(1,0,10,0)
                    self.mystrip.setPixelColor(2,0,0,10)
                    self.mystrip.setPixelColor(3,10,10,10)
                    self.mystrip.show()
                    print "Value: %d " % val
                elif val ==0:
                    self.mystrip.show()
                    self.mystrip.setPixelColor(0,0,0,0)
                    self.mystrip.setPixelColor(1,0,0,0)
                    self.mystrip.setPixelColor(2,0,0,0)
                    self.mystrip.setPixelColor(3,0,0,0)
                    self.mystrip.show()
                    print "Value: %d " % val
                time.sleep(1)
            except IOError:
                print ("Error")

    class MyDevice(Device):
        def __init__(self,addr,localaddr):
            Device.__init__(self,addr,localaddr)

        def init(self):
            m1 = Strip_LED()
            self.addClass(m1,0)
            self.obj_strip_led = self.addObject(m1.ID)


    if len(sys.argv) <= 2:
        print 'python %s <gip> <dip>:<port>' % sys.argv[0]
        print '      <gip>: IP addrees of gateway'
        print '      <dip>: IP address of Python device'
        print '      <port>: An unique port number'
        print ' ex. python %s 192.168.4.7 127.0.0.1:3000' % sys.argv[0]
        sys.exit(-1)

    d = MyDevice(sys.argv[1],sys.argv[2])
    reactor.run()
    device_cleanup()

