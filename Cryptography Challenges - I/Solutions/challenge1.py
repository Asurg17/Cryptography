import base64

def HexTo64(text):
    return base64.b64encode(bytes.fromhex(text)).decode()

if __name__ == "__main__":
    hex_text = input()
    
    print(HexTo64(hex_text))