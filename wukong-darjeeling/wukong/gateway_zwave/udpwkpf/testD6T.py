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
    print temp
    for x in range (0, 16):
        if temp[x] > 230:
            temp[x] = 1
        else:
            temp[x] = 0
    for y in range(0, 4):
        print temp[y*4],temp[y*4+1],temp[y*4+2],temp[y*4+3]

    #print (result[3]<<8)|result[2],' ',(result[5]<<8)|result[4],' ',(result[7]<<8)|result[6],' ',(result[9]<<8)|result[8]
    #print (result[11]<<8)|result[10],' ',(result[13]<<8)|result[12],' ',(result[15]<<8)|result[14],' ',(result[17]<<8)|result[16]
    #print (result[19]<<8)|result[18],' ',(result[21]<<8)|result[20],' ',(result[23]<<8)|result[22],' ',(result[25]<<8)|result[24]
    #print (result[27]<<8)|result[26],' ',(result[29]<<8)|result[28],' ',(result[31]<<8)|result[30],' ',(result[33]<<8)|result[32]
    time.sleep(1)


