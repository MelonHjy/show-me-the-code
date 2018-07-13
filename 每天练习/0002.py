import pymysql
import random


def get_coupon(num, length):
    couponList = []
    for x in range(num):
        coupon = ''
        for i in range(length):
            str = chr(random.randint(33, 127))
            coupon += str
        couponList.append(coupon)
    return couponList


cList = get_coupon(200, 15)
db = pymysql.connect('localhost', 'root', 'HjY133163', 'aab')
cursor = db.cursor()
cursor.execute('drop table if exists couponlist')
cursor.execute('create table couponlist(coupon varchar(20) primary key)')
for c in cList:
    try:
        cursor.execute('insert into couponlist values (%s)', c)
        db.commit()
    except:
        db.rollback()

cursor.close()
db.close()