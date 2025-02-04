def is_palindrome(num):
  
    num_str = str(num)
    
 
    reversed_str = num_str[::-1]
    

    if num_str == reversed_str:
        return True
    else:
        return False

numbers = [121, 1331, 12321, 12345]
for num in numbers:
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
