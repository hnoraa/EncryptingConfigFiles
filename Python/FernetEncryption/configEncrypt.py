# encrypt a config file
from cryptography.fernet import Fernet
import json


def writeKey(keyFile):
    """
    Generates a key and saves to file
    """
    key = Fernet.generate_key()
    with open(keyFile, "wb") as kf:
        kf.write(key)


def loadKey(keyFile):
    """
    Loads the key file
    """
    return open(keyFile, "rb").read()


def encryptFile(fileName, fileNameEncrypted, key):
    """
    Encrypt a file with a key
    """
    f = Fernet(key)

    # open and encrypt the file
    with open(fileName, 'rb') as file:
        fileData = file.read()

    encryptedData = f.encrypt(fileData)

    # write the encryptedFile
    with open(fileNameEncrypted, 'wb') as file:
        file.write(encryptedData)


def decryptFile(fileNameEncrypted, key):
    """
    Decrypt a file with a key
    """
    f = Fernet(key)

    # read the encrypted data
    with open(fileNameEncrypted, 'rb') as file:
        encryptedData = file.read()

    # decrypt the data to return
    decryptedData = f.decrypt(encryptedData)

    return decryptedData


def testWithString(data, keyFile):
    # generate the key file
    writeKey(keyFile)
    key = loadKey(keyFile)

    # encode the data using utf-8 codec
    message = data.encode()

    # initialize Fernet class
    f = Fernet(key)

    # encrypt the data
    encryptedData = f.encrypt(message)

    print("Encrypted:")
    print(encryptedData)

    # decrypt
    decryptedData = f.decrypt(encryptedData)
    print("Decrypted:")
    print(decryptedData)


def testWithFile(fileName, fileNameEncrypted, keyFile):
    # get the key
    writeKey(keyFile)
    key = loadKey(keyFile)

    # initialize Fernet class
    f = Fernet(key)

    encryptFile(fileName, fileNameEncrypted, key)

    data = decryptFile(fileNameEncrypted, key)
    print(data)

    x = json.loads(data)
    print(x)
    print(x['width'])
    

if __name__ == '__main__':
    testWithString("This is a test message....", "testWithString.key")
    testWithFile("config.json", "configEn.json", "testWithFile.key")