import base64
import sys

# Relative frequency in the English language
table = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':13, 'f':2.2, 'g':2, 'h':6.1, 'i':7,
         'j':0.15, 'k':0.77, 'l':4, 'm':2.4, 'n':6.7, 'o':7.5, 'p':1.9, 'q':0.095, 'r':6, 
         's':6.3, 't':9.1, 'u':2.8, 'v':0.98, 'w':2.4, 'x':0.15, 'y':2, 'z':0.074, ' ':5.0}

# converts hex to plian text
def convertHexToPlain(hex_text):
    
    plain_text = ""

    for i in range(0, len(hex_text), 2): 
        
        curElem = hex_text[i : i + 2] 
  
        curChar = chr(int(curElem, 16)) 
  
        plain_text += curChar 
        
    return plain_text

# converts hex to decimal
def convertHexToDecimal(hex_text):

    decimal = list()

    for i in range(0, len(hex_text), 2): 
        
        curElem = hex_text[i : i + 2] 

        if(len(curElem) == 2):
  
            num_dec = int(curElem, 16)
    
            decimal.append(num_dec) 
        
    return decimal

# since we have 1 byte encoding here -> 8 bit
# there is just 256 differrent cases for key
# here we are decoding by every 256 keys 
# and getting the key of one that has the biggest
# letters appearence frequaces sum
def decode_all_cases(hex_bytes):

    txt = ""
    res_key = ""
    max_score = 0.0

    for i in range(256):

        result = list()
        key    = i

        for curByte in hex_bytes:

            result.append(curByte ^ key)

        cur_txt = convertHexToPlain(bytes(result).hex())
        cur_score = 0.0

        for k in range(len(cur_txt)):

            cur_ch = cur_txt[k].lower()

            if(cur_ch >= 'a' and cur_ch <= 'z' or cur_ch == ' '):   
                cur_score += table[cur_ch]

        if cur_score > max_score:
            max_score = cur_score
            txt = cur_txt
            res_key = key
        
    return chr(res_key)

# Decrypts given ciphertext, under the given key, using repeating-key XOR.
def decryptCiphertext(key_bytes, text_bytes):

    result = ""

    key_len = len(key_bytes)
    j = 0

    for i in range(len(text_bytes)):

        if j == key_len:
            j = 0

        xored = text_bytes[i] ^ key_bytes[j]
        
        result += chr(xored)

        j = j+1

    return result

###########################################################################################################
###########################################################################################################
###########################################################################################################

# computes hammingtone distance 
# by xor-ing elems of the strings so we get the number of different bits
# 0111 ^ 1010 -> 1101 so we have 4 different bits here (sum of 1-s is the hamming distance)
def computeHammingDistance(str1, str2):

    sum = 0
    bin_str = ""

    #if string are different sizes get the smllest size(just in case)
    size = min(len(str1), len(str2))

    for i in range(size):

        bin_str += bin(str1[i] ^ str2[i])

    for i in range(len(bin_str)):
        if(bin_str[i] == '1'):
            sum += 1

    return sum

##########################################################################################################
###########################################################################################################

# breaks ciphertext into blocks of possibleKeySize
# and returs this blocks
def breakIntoBlocks(ciphertext, possibleKeySize):

    blocks = list()

    prevIndex = 0
    checker = 0

    while True:

        newIndex = prevIndex + possibleKeySize

        if newIndex < len(ciphertext):
            curBlock = ciphertext[prevIndex:newIndex]
        else:
            curBlock = ciphertext[prevIndex:(len(ciphertext))]
            checker  = 1

        blocks.append(curBlock)

        if checker == 1:
            break
        else:
            prevIndex = newIndex

    return blocks

# computes possible size of the key
def getPossibleKeySize(ciphertext):
    
    possibleKeySize = 0
    minVal = sys.maxsize
    
    for curSize in range(2, 41):
    
        #get current size blocks list
        curBlocks = breakIntoBlocks(ciphertext, curSize)

        maxLen = len(curBlocks)
        curSum = 0.0
        index = 1
        counter = 0

        while True:

            if index >= maxLen:
                break

            f_block = curBlocks[index-1]
            s_block = curBlocks[index]

            counter += 1
            index += 2

            curHammingDistance = computeHammingDistance(f_block, s_block)
            normalizedValue = curHammingDistance / curSize

            curSum += normalizedValue

        avg_value = curSum / counter
        
        if avg_value < minVal:
            minVal = avg_value
            possibleKeySize = curSize

    return possibleKeySize


# transposes blocks
# makes a block that is the first byte of every block, 
# and a block that is the second byte of every block, and so on...
def transposeBlocks(blocks, numOfTransBlocks):

    transposedBlocks = list()

    for i in range(numOfTransBlocks):

        curTransBlock = b''

        for j in range(len(blocks)): 

            if (i < len(blocks[j])):

                curTransBlock += bytes([blocks[j][i]])

        transposedBlocks.append(curTransBlock)

    return transposedBlocks

# finds out the actual key
# to decrypt the given ciphertext
def computeTheKey(transposedBlocks, possibleKeySize):

    key = ""

    for i in range(len(transposedBlocks)):
        
        key += decode_all_cases(transposedBlocks[i])

    return key 

if __name__ == "__main__":
    
    base64txt = input()

    ciphertext = base64.b64decode(base64txt)

    possibleKeySize = getPossibleKeySize(ciphertext)

    blocks = breakIntoBlocks(ciphertext, possibleKeySize)

    transposedBlocks = transposeBlocks(blocks, possibleKeySize)

    key = computeTheKey(transposedBlocks, possibleKeySize)

    dectyted = decryptCiphertext(bytes(key, 'ascii'), ciphertext)

    print(dectyted)



