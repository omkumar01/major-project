from cryptography.fernet import Fernet


class Encryption:
    def __init__(self):
        '''generates a key for encryption and decryption try storing for further use rather than generating everytime'''
        self.key = Fernet.generate_key()

    def encrypt_msg(self, key, msg):
        '''takes two arguments key and msg and returns a token for later decryption of message'''
        f = Fernet(key)
        return (f.encrypt(bytes(msg, encoding='UTF-8'))).decode('UTF-8')

    def decrypt_msg(self, key, token):
        '''takes two args key and token and returns decrypted msg'''
        f = Fernet(key)
        return (f.decrypt(bytes(token, encoding='UTF-8'))).decode('UTF-8')


if __name__ == "__main__":
    obj = Encryption()
    print(obj.key.decode('UTF-8'))
    token = obj.encrypt_msg(obj.key, "Hello dude")
    print(token)
    print(obj.decrypt_msg(obj.key, token))
