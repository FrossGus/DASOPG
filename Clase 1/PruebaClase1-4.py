b = bytearray()
b.append(0x02)
b.append(0x10)
b.append(0x05)
b.append(0x3c)
b.append(0x03)

print(b)
print(hex(b[3]))
print(chr(b[3]))
print(b[3])
print (len(b))

s = int(input("Numero: "))
print(type(s))

s = input("Numero: ")
print(type(s))