letter=input("Enter text:-")
vowels="aeiouAEIOU"
count =sum(letter.count(vowel) for vowel in vowels)
print(count)


