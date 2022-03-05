
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


#converts hex to decimal
def convertHexToDecimals(hex_text):
    
    lst = list()

    for i in range(0, len(hex_text), 2): 
        
        curElem = hex_text[i : i + 2] 
  
        curNum = int(curElem, 16) 
  
        lst.append(curNum) 
        
    return lst

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
        
    return txt

# dectypts given hex
def getDecryptedStr(hex_txt):

    hex_bytes = bytes(convertHexToDecimals(hex_txt))

    return decode_all_cases(hex_bytes)

# calculates the letter frequecy sum in this string 
# and returs tis sum
def getStringScore(str):

    cur_score = 0.0

    for k in range(len(str)):

        cur_ch = str[k].lower()

        if(cur_ch >= 'a' and cur_ch <= 'z' or cur_ch == ' '):   
            cur_score += table[cur_ch]

    return cur_score

if __name__ == "__main__":
    
    n = int(input())
    hex_strings = list()

    for i in range(int(n)):

        str = input()

        hex_strings.append(str)

    res = ""
    maxScore = 0.0

    for i in range(n):

        curHex = hex_strings[i]

        decryptedStr = getDecryptedStr(curHex)

        curScore = getStringScore(decryptedStr)

        if curScore > maxScore:
            maxScore = curScore
            res = decryptedStr
    
    print(res)
    