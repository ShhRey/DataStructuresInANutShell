# Custom Inputs from Users
ransomNote = input("Enter string for ransomNote: ").lower()
magazine = input("Enter string for magazine: ").lower()

# Function for Comparing Characters from both Strings
def canConstruct(ransomNote, magazine) -> bool:
    # Creating a dict to store letter occurrence and count in magazine
    charCount = {}
    for char in magazine:        
        charCount[char] = charCount.get(char, 0) + 1
    for char in ransomNote:
        # Checking of char in ransomNote is there is charCount (until count > 0)
        if (char not in charCount) or (charCount == 0):
            return False
        charCount[char] -= 1
    return True

# Displaying Result
print(canConstruct(ransomNote, magazine))