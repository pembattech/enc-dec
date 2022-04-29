CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1','2','3','4','5','6','7','8','9','0', "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "|", "/", ".", ">", ",", "<", "-", "_", "+", "="]

def encrypt(data):
    off = 3
    enc = ""
    for i in data:
        try:
            enc = enc + CHARACTERS[int((CHARACTERS.index(i)+off)) % len(CHARACTERS)]
        except ValueError:
            enc += i
    return enc

def decrypt(data):
    off = 3
    dec = ""
    for i in data:
        try:
            dec = dec + CHARACTERS[int((CHARACTERS.index(i)-off)) % len(CHARACTERS)]
        except ValueError:
            dec += i
    return dec
