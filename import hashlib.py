import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = input("Enter data to hash :")
print("Hashed data : ", hash_data(data))