import random


def get_coupon(num, length):
    couponList = []
    for x in range(num):
        coupon = ''
        for i in range(length):
            str = chr(random.randint(33, 127))
            coupon += str
        print(coupon)
        couponList.append(coupon)


get_coupon(200, 15)
