def encrypt(text):
    output = ""
    for i, char in enumerate(text):
        ascii = ord(char)
        mod_ascii = ascii - 17
        output += str(mod_ascii)
        if i < len(text) - 1:
            output += "."
    output
    return output
    
def decrypt(secret):
    numbers = secret.split(".")
    output = ""
    for number in numbers:
        temp = int(number) + 17
        temp = chr(temp)
        output += temp
    return output

def main():
    print("Would you like to encrypt or decrypt?")
    will_encrypt = input() 
    if will_encrypt == "encrypt":
        print("Enter a message to encrypt:")
        message_input = input()
        code = encrypt(message_input)
        print(code)
    if will_encrypt == "decrypt":
        print("Enter a code to decrypt:")
        message_input = input()
        code = decrypt(message_input)
        print(code)

    
if __name__ == "__main__":
    main()