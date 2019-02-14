
import binascii

# Open in binary mode (so you don't read two byte line endings on Windows as one byte)
# and use with statement (always do this to avoid leaked file descriptors, unflushed files)
with open('pico.bmp', 'rb') as f:
    # Slurp the whole file and efficiently convert it to hex all at once
    hexdata = f.read().hex()


lsb =''
for i in range(2000):
    if i%2 == 1:
        s= hexdata[i]
        lsb = lsb + bin(int(s,16))[-1]

lsbString = lsb[54:]
print(lsbString)
