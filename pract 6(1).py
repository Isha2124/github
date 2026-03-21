# Take input from user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
spaces = 0
lowercase = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Loop through each character
for char in text:
    if char in vowel_set:
        vowels += 1
    elif char.isalpha():
        consonants += 1

    if char == " ":
        spaces += 1

    if char.islower():
        lowercase += 1

# Display results
print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)
