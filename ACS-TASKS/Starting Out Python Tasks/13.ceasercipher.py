def caesar_cipher(text, offset):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  #checks if the character is a letter
            #converts to lowercase and calculates the new character
            shifted_char = chr(((ord(char.lower()) - ord('a') + offset) % 26) + ord('a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char  #keeps non-alphabetic characters unchanged
        
    return encrypted_text

#input text and offset from the user
text = input("Enter sentence: ")
offset = int(input("Enter the offset: "))

# Encrypt the text and print the result
encrypted_text = caesar_cipher(text, offset)
print("Encrypted text:", encrypted_text)
