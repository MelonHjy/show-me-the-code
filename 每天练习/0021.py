import os
from hashlib import sha256
from hmac import HMAC


def encrypt(password, salt=None):
    if salt is None:
        salt = os.urandom(8)
    password = password.encode('utf-8')
    encrypt_password = password
    for i in range(10):
        encrypt_password = HMAC(encrypt_password, salt, sha256).digest()
    return salt + encrypt_password


hashed = encrypt(input('输入密码:'))
print(hashed)


def validate(hashed, input_password):
    return hashed == encrypt(input_password, salt=hashed[:8])


input_password = input('输入登录密码：')
assert  validate(hashed, input_password)