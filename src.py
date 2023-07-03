import hashlib

def calculate_md5_hash(string):
    # Create an instance of the MD5 hash object
    md5_hash = hashlib.md5(bytes(string, "utf-8"))

    # Convert the string to bytes and update the hash object
    # md5_hash.update(string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hash_code = md5_hash.hexdigest()

    return hash_code

# Example usage
code = 'a09272b53419ab95507cdf127329336d'
with open("leksiko.txt", "r") as file :
    s = file.readlines()
found = "NOT FOUND"
for line in s :
    if calculate_md5_hash(line.replace("\n", ''))==code :
        found = line
        break
print(f"The password is: {found}")


