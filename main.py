pip install pycryptodome
from Crypto.Cipher import DES
import base64
ciphertext = "輸入密文"
key = b'輸入密鑰'
iv = b'輸入初始向量'
#使用base64解碼密文
ciphertext = base64.b64decode(ciphertext)
#創建DES密碼对象
cipher = DES.new(key, DES.MODE_CBC, iv)
#解密密文
plaintext = cipher.decrypt(ciphertext)
#輸出解密後的明文
print("解密後的明文為：", plaintext.decode('utf-8'))
