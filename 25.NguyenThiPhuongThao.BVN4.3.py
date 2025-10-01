def mod (sogoc, somu, sodu):
    result = 1
    for _ in range(somu):
        result = (result * sogoc) % sodu
    return result

def mahoa_RSA (p, q, e, message):
    n = p * q
    z = (p - 1) * (q - 1)
    print ("n=",n)
    print("z=", z)

    ascii_codes = [ord(ch) for ch in message]
    print("Mã ASCII:", ascii_codes)
    
    cipher = [mod(m, e, n) for m in ascii_codes]
    return cipher

p = 17
q = 23
e = 5
message = "NguyenThiPhuongThao"
cipher = mahoa_RSA(p, q, e, message)
print("Mã hoá:", cipher)


