import hashlib

def blake2(message):
    """Calculate the BLAKE2 hash of the given message."""
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()
def main():
    text = input("Nhap chuoi can bam: ").encode('utf-8')
    hash_text = blake2(text)
    print("Chuoi da nhap:", text.decode('utf-8'))
    print("BLAKE2 Hash: ", hash_text.hex())
if __name__ == "__main__":
    main()