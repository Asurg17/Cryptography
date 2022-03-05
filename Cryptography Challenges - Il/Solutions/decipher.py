from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
ctext_cop = ctext[:]

message = []

Oracle_Connect()

# ----------------------------------------------------
plain_text = list()
intermediate = []

#fill with 1
for i in range(len(ctext)):
    intermediate.append(1)

num = 1
counter = 0

size = len(ctext)

for i in range(size-1, 15, -1):

    counter += 1

    for k in range(size-16*(num+1), size-16*num):
        ctext[k] = counter ^ intermediate[k+16]


    for ind in range(256):
        ctext[(size-16*num)-counter] = ind

        if(Oracle_Send(ctext[0:size-(num-1)*16], 3-(num-1)) == 1):
            break


    intermediate[i] = counter ^ ind

    message.append(intermediate[i] ^ ctext_cop[i-16])

    # check which block
    if (counter == 16):
        ctext = ctext_cop[:]
        num += 1
        counter = 0


Oracle_Disconnect()

padding = message[0]

resultMessage = ""

for a in range(len(message)-1, padding-1, -1):
    resultMessage += chr(message[a])

print(resultMessage)

