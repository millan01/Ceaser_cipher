#function to encrypt
def encrypt(textenc , shift1):
    result = " "
#iterate through each character
    for i in range(len(textenc)):
        char = textenc[i]       

        if char.isupper():
            result += chr((ord(char) +int(shift1) - 65) %26 + 65)
        elif(char.islower()):
            result+= chr((ord(char) + int(shift1) - 97) %26 + 97)
        else:
           result+=char #alphanumberic character remain same
    return result
    
#function to decrypt
def decrypt(textdec, shift2):
    decryptresult=" "
    for i in range(len(textdec)):
        char2 = textdec[i]

        if  char2.isupper():
            decryptresult += chr((ord(char2)- int(shift2) -65)%26 +65)
        elif char2.islower():
            decryptresult+= chr((ord(char2) - int(shift2)- 97)%26 + 97)
        else:
            decryptresult+=char2 #alphanumberic character remain same
    return decryptresult

# take input from user
choose = input("What you would like to do encrypt or decrypt! \t Enter 1 for encrypt and 2 for decrypt ")
if(choose == '1'):
    textenc = input("Enter the word to encrypt ")
    shift1 = input("Enter the number of shift ")
    print("Text: " + textenc )
    print("shift value: " + shift1)
    print("Encrypted text : " + encrypt(textenc, shift1))
elif(choose == '2'):
    textdec = input("Enter the word to decrypt ")
    shift2 = input("Enter the number of shift ")
    print("Text: " + textdec )
    print("shift value: " + shift2)
    print("Decryptped text : " + encrypt(textdec, shift2))
else:
    print("Unexpected entry")