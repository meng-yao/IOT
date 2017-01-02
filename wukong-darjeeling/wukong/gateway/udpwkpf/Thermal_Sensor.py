from twisted.internet import reactor
from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *

if __name__ == "__main__":
        class Thermal_Sensor(WuClass):
            def __init__(self):
                WuClass.__init__(self)
                self.loadClass('Thermal_Sensor')
                self.i2c = mraa.I2c(0)
                self.i2c.address(0x0A)
                self.i2c.frequency(mraa.I2C_STD)
        
            def update(self,obj,pID=None,val=None):
                try:
                    self.i2c.writeByte(0x4C)
                    result=self.i2c.read(35)
                    print 'Enviroment Temp:',(result[1]<<8)|result[0]
                    temp = [
                    (result[3]<<8) | result[2],
                    (result[5]<<8) | result[4],
                    (result[7]<<8) | result[6],
                    (result[9]<<8) | result[8],
                    (result[11]<<8) | result[10],
                    (result[13]<<8) | result[12],
                    (result[15]<<8) | result[14],
                    (result[17]<<8) | result[16],
                    (result[19]<<8) | result[18],
                    (result[21]<<8) | result[20],
                    (result[23]<<8) | result[22],
                    (result[25]<<8) | result[24],
                    (result[27]<<8) | result[26],
                    (result[29]<<8) | result[28],
                    (result[31]<<8) | result[30],
                    (result[33]<<8) | result[32]]
                    #print temp
                    up_Num=0
                    down_Num=0
                    for x in range (0, 16):
                        if temp[x] > 230:
                            temp[x] = 1
                            if(x%4 == 2 || x%4 == 3):
                                down_Num+=1
                            else:
                                up_Num+=1
                        else:
                            temp[x] = 0
                    for y in range(0, 4):
                        print temp[y*4],temp[y*4+1],temp[y*4+2],temp[y*4+3]
                    obj.setProperty(0,up_Num)
                    obj.setProperty(1,down_Num)
                    obj.setProperty(2,500);

                except IOError:
                    print "Error"
        
        class MyDevice(Device):
            def  __init__(self,addr,localaddr):
                Device.__init__(self,addr,localaddr)
            
            def init(self):
                m1=Thermal_Sensor()
                self.addClass(m1,0)
                self.obj_thermal_sensor=self.addObject(m1.ID)
        
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
