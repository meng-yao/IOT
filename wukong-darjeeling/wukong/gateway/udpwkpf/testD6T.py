import mraa as m
import time

i2c=m.I2c(0)
i2c.address(0x0A)
i2c.frequency(m.I2C_STD)
while(True):
    #i2c.writeReg(0x14,0x4C)
    #i2c.write(bytearray(b'0x140x4C'))
    i2c.writeByte(0x4C)
    #test=i2c.readByte()
    #i2c.writeByte(0x15)
    #result=bytearray(35)
    result=i2c.read(35)
    
    #print len(result)
    #print test
    print 'Enviroment Temp:',(result[1]<<8)|result[0]
    print 'P0:',(result[3]<<8)|result[2]
    print 'P1:',(result[5]<<8)|result[4]
    print 'P2:',(result[7]<<8)|result[6]
    print 'P3:',(result[9]<<8)|result[8]
    print 'P4:',(result[11]<<8)|result[10]
    print 'P5:',(result[13]<<8)|result[12]
    print 'P6:',(result[15]<<8)|result[14]
    print 'P7:',(result[17]<<8)|result[16]
    print 'P8:',(result[19]<<8)|result[18]
    print 'P9:',(result[21]<<8)|result[20]
    print 'P10:',(result[23]<<8)|result[22]
    print 'P11:',(result[25]<<8)|result[24]
    print 'P12:',(result[27]<<8)|result[26]
    print 'P13:',(result[29]<<8)|result[28]
    print 'P14:',(result[31]<<8)|result[30]
    print 'P15:',(result[33]<<8)|result[32]
    time.sleep(1)


