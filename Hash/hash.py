def get_hash(key):
    h=0
    for char in key:
        h+=ord(char)
    return h%100

print(get_hash("Sathish"))
print(get_hash("Sarathy"))
print(get_hash("march 6"))