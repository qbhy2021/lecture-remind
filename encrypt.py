import random
from Crypto.Cipher import AES
import base64


def pkcs7padding(text):
    # 明文使用PKCS7填充
    bs = 16
    length = len(text)
    bytes_length = len(text.encode('utf-8'))
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    return text + padding_text


def encryptAES(data, key):
    iv = ''.join(random.choice('ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678') for _ in range(16))
    iv = iv.encode('utf-8')
    key = key.encode('utf-8')
    data = pkcs7padding(''.join(random.choice('ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678') for _ in range(64)) + data)
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv).encrypt(data.encode('utf-8'))
    result = str(base64.b64encode(aes), encoding='utf-8')
    return result


# print(encryptAES("asd271828",'SggdVGlaY0MFCKwL'))