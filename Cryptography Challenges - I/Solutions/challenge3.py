
# Relative frequency in the English language
table = {'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':13, 'f':2.2, 'g':2, 'h':6.1, 'i':7,
         'j':0.15, 'k':0.77, 'l':4, 'm':2.4, 'n':6.7, 'o':7.5, 'p':1.9, 'q':0.095, 'r':6, 
         's':6.3, 't':9.1, 'u':2.8, 'v':0.98, 'w':2.4, 'x':0.15, 'y':2, 'z':0.074, ' ':5.0}

#converts hex to plian text
def convertHexToPlain(hex_text):
    
    plain_text = ""

    for i in range(0, len(hex_text), 2): 
        
        curElem = hex_text[i : i + 2] 
  
        curChar = chr(int(curElem, 16)) 
  
        plain_text += curChar 
        
    return plain_text

# since we have 1 byte encoding here -> 8 bit
# there is just 256 differrent cases for key
# here we are decoding by every 256 keys 
# and getting the one that has the biggest
# letters appearence frequaces sum
def decode_all_cases(hex_bytes):

    txt = ""
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
        
    print(txt)

if __name__ == "__main__":
    
    hex_txt = input()

    hex_bytes = bytes(convertHexToPlain(hex_txt), 'ascii')

    decode_all_cases(hex_bytes)