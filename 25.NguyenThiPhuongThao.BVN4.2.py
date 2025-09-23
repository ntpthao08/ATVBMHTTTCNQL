def mahoa_caesar(plaintext, key):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = (ord(ch) - base + key) % 26 + base
            ciphertext += chr(c)
        else:
            ciphertext += ch
    return ciphertext

plaintext = "Nguyen Thi Phuong Thao"
key = 25
ciphertext = mahoa_caesar(plaintext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)

