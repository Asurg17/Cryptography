
#converts hex to plain text
def convertHexToPlain(hex_text):
    
    plain_text = ""

    for i in range(0, len(hex_text), 2): 
        
        curElem = hex_text[i : i + 2] 
  
        curChar = chr(int(curElem, 16)) 
  
        plain_text += curChar 
        
    return plain_text

# xores given elems byte by byte
# and returnes xored bytes
def xor(f_bytes, s_bytes):

    result = list()

    for i in range(len(f_bytes)):

        result.append(f_bytes[i] ^ s_bytes[i])

    return bytes(result)

if __name__ == "__main__":
    
    f_hex = input()
    s_hex = input()

    f_bytes = bytes(convertHexToPlain(f_hex), 'ascii')
    s_bytes = bytes(convertHexToPlain(s_hex), 'ascii')

    xored = xor(f_bytes, s_bytes)

    result = xored.hex()

    print(result)
    