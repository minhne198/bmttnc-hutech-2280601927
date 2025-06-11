from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_client_key_pair(parameters):
    """
    Generate a Diffie-Hellman key pair for the client.
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    """
    Derive the shared secret using the client's private key and the server's public key.
    """
    shared_key = private_key.exchange(server_public_key)
    # Derive a symmetric key from the shared secret
    
    return shared_key

def main():
    # Load the server's public key
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())
    
    # Generate Diffie-Hellman parameters
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_key_pair(parameters)

    shared_secret = derive_shared_secret(private_key, server_public_key)
    print("Shared secret:", shared_secret.hex())

if __name__ == "__main__":
    main()