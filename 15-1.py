#1
class Cipher:
    def __init__(self, key):
        if (key < 0) or (key > 255):
            raise Exception("Key must be integer in range [0; 255]")
        self.key = key
    def encrypt_byte(self, data_byte):
        return data_byte ^ self.key
    def decrypt_byte(self, encrypted_data_byte):
        return encrypted_data_byte ^ self.key
#2
with open('secret.txt','w') as fh:
        fh.write('The quick brown fox jumps over the lazy dog')
#3,4    
with open('secret.txt', 'br') as fh:
    raw = fh.read()
    encrypted_content = bytearray(0)
    worker = Cipher(42)
    for i in raw:
        encrypted_content.append(worker.encrypt_byte(i))
    #5
    with open('encryptedSecret.txt','bw') as fh2:
        fh2.write(encrypted_content)
#6
with open('encryptedSecret.txt','br') as fh:
    raw = fh.read()
    decrypted_content = bytearray(0)
    worker = Cipher(42)
    for i in raw:
        decrypted_content.append(worker.decrypt_byte(i))
    with open('revealedSecret.txt','bw') as fh2:
        fh2.write(decrypted_content)
