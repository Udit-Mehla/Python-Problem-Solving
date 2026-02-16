# we will get the palindrome 
# palindrome means if we read from the left to right or right to left it same in reading

# now we will use the 'Two Pointer Method'  because it save time and space 

# we take the example 'LEVEL'
def palindrome(text):
    # we have to get the clear text by keep only letter and number
    clear_text = ''.join(char.lower() for char in text if char.isalnum())

    left = 0
    right = len(clear_text) - 1

    while left < right :
        if clear_text[left] != clear_text[right]:
            return False
    
        left +=1
        right -=1

    return True
result = palindrome('level')
print(result)