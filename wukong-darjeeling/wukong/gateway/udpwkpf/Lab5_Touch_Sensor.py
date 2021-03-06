from twisted.internet import reactor
from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
import time

Touch_Sensor_Pin = 7
if __name__ == "__main__":    
    class TouchSensor(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Touch_Sensor')
            self.IO = pin_mode(Touch_Sensor_Pin, PIN_TYPE_DIGITAL, PIN_MODE_INPUT)
            self.count = 0 
    
        def update(self,obj,pID=None,val=None):
            try:
                if digital_read(self.IO) == 1:
                    self.count += 1
                    if self.count > 4:
                        self.count = 0
                obj.setProperty(0, self.count)
                print "Touchsensor value: %d " % self.count
                time.sleep(1)
            except IOError:
                print "Error"

    class MyDevice(Device):
        def __init__(self,addr,localaddr):
            Device.__init__(self,addr,localaddr)

        def init(self):

            m2 = TouchSensor()
            self.addClass(m2,0)
            self.obj_button = self.addObject(m2.ID)

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
