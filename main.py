import wechat
from flight_information import *
from config import *

dateList = initDate()
infoList = []


class out:
    def __init__(self):
        self.date = ''
        self.message = ''
        self.number1 = ''
        self.dTime1 = ''
        self.aTime1 = ''
        self.price1 = 0
        self.number2 = ''
        self.dTime2 = ''
        self.aTime2 = ''
        self.price2 = 0
        self.time1 = ''
        self.time2 = ''

    def setDate(self, date):
        self.date = date

    def setMessage(self, data):
        self.message = data

    def setNumber1(self, number):
        self.number1 = number

    def set_dTime1(self, d):
        self.dTime1 = d

    def set_aTIme1(self, a):
        self.aTime1 = a

    def setPrice1(self, price):
        self.price1 = price

    def setNumber2(self, number):
        self.number2 = number

    def set_dTime2(self, d):
        self.dTime2 = d

    def set_aTIme2(self, a):
        self.aTime2 = a

    def setPrice2(self, price):
        self.price2 = price

    def setTime(self):
        self.time1 = self.dTime1 + ' -> ' + self.aTime1
        self.time2 = self.dTime2 + ' -> ' + self.aTime2


out1 = out()
out2 = out()
out3 = out()
flag = 0
for each in dateList:
    infoList.append(getFlightinformation(dCity, aCity, each))
    flag += 1
    if flag == 1:
        out1.setDate(each)
    if flag == 2:
        out2.setDate(each)
    if flag == 3:
        out3.setDate(each)
flag = 0
for info in infoList:
    flag += 1
    message = ''
    FlightNumberList = getInfo(info, 'FlightNumber')
    dTimeList = getInfo(info, 'DepartureDate')
    aTimeList = getInfo(info, 'ArrivalDate')
    price = getInfo(info, 'LowestPrice')
    temp = []
    for eachPrice in price:
        if eachPrice:
            temp.append(int(eachPrice))
    price = temp
    minPrice = min(price)
    index = price.index(minPrice)
    number = FlightNumberList[index]
    dt = dTimeList[index]
    at = aTimeList[index]
    price.pop(index)
    FlightNumberList.pop(index)
    dTimeList.pop(index)
    aTimeList.pop(index)
    if flag == 1:
        out1.setNumber1(number)
        out1.set_dTime1(dt)
        out1.set_aTIme1(at)
        out1.setPrice1(minPrice)
    if flag == 2:
        out2.setNumber1(number)
        out2.set_dTime1(dt)
        out2.set_aTIme1(at)
        out2.setPrice1(minPrice)
    if flag == 3:
        out3.setNumber1(number)
        out3.set_dTime1(dt)
        out3.set_aTIme1(at)
        out3.setPrice1(minPrice)
    message = message + ' 航班号-> ' + number + ' 起降时间 {}->{} '.format(dt, at) + ' 价格 ' + str(minPrice)
    minPrice = min(price)
    index = price.index(minPrice)
    number = FlightNumberList[index]
    dt = dTimeList[index]
    at = aTimeList[index]
    price.pop(index)
    FlightNumberList.pop(index)
    dTimeList.pop(index)
    aTimeList.pop(index)
    message = message + ' | 航班号-> ' + number + ' 起降时间 {}->{} '.format(dt, at) + ' 价格 ' + str(minPrice)
    if flag == 1:
        out1.setMessage(message)
        out1.setNumber2(number)
        out1.set_dTime2(dt)
        out1.set_aTIme2(at)
        out1.setPrice2(minPrice)
    if flag == 2:
        out2.setMessage(message)
        out2.setNumber2(number)
        out2.set_dTime2(dt)
        out2.set_aTIme2(at)
        out2.setPrice2(minPrice)
    if flag == 3:
        out3.setMessage(message)
        out3.setNumber2(number)
        out3.set_dTime2(dt)
        out3.set_aTIme2(at)
        out3.setPrice2(minPrice)
print(out1.date + ' ==> ' + out1.message)
print(out2.date + ' ==> ' + out2.message)
print(out3.date + ' ==> ' + out3.message)
out1.setTime()
out2.setTime()
out3.setTime()
wechat.send(out1.date, out1.number1, out1.time1, out1.price1, out1.number2, out1.time2, out1.price2, out2.date,
            out2.number1, out2.time1, out2.price1, out2.number2, out2.time2, out2.price2, out3.date, out3.number1,
            out3.time1, out3.price1, out3.number2, out3.time2, out3.price2)
