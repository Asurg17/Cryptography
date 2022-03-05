from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

# Connect to server
Oracle_Connect()

curTag = bytearray()

# every 2 block - > 32 byte
for i in range(0, len(data), 32):
    f_block = data[i:i+16]

    if(i+32 > len(data)):
        s_block = data[i+16:i+len(data)]
    else:
        s_block = data[i+16:i+32]

    f_btar = bytearray(f_block)
    newBlock = ""

    if(len(curTag) != 0):
        
        #if we already have the tag xor tag and first block of current message
        for j in range(0, 16):
            newBlock += chr(f_btar[j] ^ curTag[j])

    else:

        #if not just assign first block
        newBlock = f_block

    curMsg = newBlock+s_block

    curTag = Mac(curMsg, len(curMsg))

# ret = Vrfy(data, len(data), curTag)

# if ret == 1:
#     print "Message verified successfully!"
# else:
#     print "Message verification failed."

Oracle_Disconnect()


print curTag


