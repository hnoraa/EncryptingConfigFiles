import json
from cryptography.fernet import Fernet


f = Fernet(open("testWithFile.key", "rb").read())

with open("configEn.json", 'rb') as file:
        encryptedData = file.read()

# decrypt the data to return
decryptedData = f.decrypt(encryptedData)
x = json.loads(decryptedData)

print("{}, {}".format(x['width'], x['height']))