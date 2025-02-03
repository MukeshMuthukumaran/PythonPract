def caesar_cipher(text, shift):
  
    encrypted_text = ''
    
    for char in text:
       
        if char.isalpha():
            
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
           
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            
            encrypted_text += char
    
    return encrypted_text


print(caesar_cipher("abc", 3))   
print(caesar_cipher("hello", 1))  
