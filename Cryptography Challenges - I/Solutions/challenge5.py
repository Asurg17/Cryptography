
#Encrypt given string, under the given key, using repeating-key XOR.
def getResult(key_bytes, text_bytes):

    result = list()

    key_len = len(key_bytes)
    j = 0

    for i in range(len(text_bytes)):

        if j == key_len:
            j = 0

        xored = text_bytes[i] ^ key_bytes[j]
        
        result.append(xored)

        j = j+1

    return bytes(result).hex()

if __name__ == "__main__":
    
    key = input()
    key_bytes = bytes(key, 'ascii')

    plain_text = input()
    text_bytes = bytes(plain_text, 'ascii')

    result = getResult(key_bytes, text_bytes)

    print(result)