from Key import KeyGenerator

def main():
    private_key, public_key = KeyGenerator.generate_key_pair()

    serialized_private_key = KeyGenerator.serialize_private_key(private_key)
    serialized_public_key = KeyGenerator.serialize_public_key(public_key)

    print("Private key:")
    print(serialized_private_key.decode())

    print("Public key:")
    print(serialized_public_key.decode())

if __name__ == "__main__":
    main()