from Crypto.Hash import SHA3_256

def sha3(message):
    """Calculate the SHA-3 hash of the given message."""
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhap chuoi can bam: ").encode('utf-8')
    hash_text = sha3(text)
    print("Chuoi da nhap:", text.decode('utf-8'))
    print("SHA-3 Hash: ", hash_text.hex())
if __name__ == "__main__":
    main()