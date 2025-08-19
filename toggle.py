def toggle(letter):
    char=letter
    if char.isupper():
        return char.lower()
    else:
        return char.upper()
s=input("enter any name:")
for i in range(len(s)):
    j=toggle(s[i])
    print(j)
        
