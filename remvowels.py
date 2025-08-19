vowel=["a","e","i","o","u","A","E","I","O","U"]
letter="saivamsi"
result=""
for i in range(len(letter)):
    if letter[i] not in vowel:
        result = result +letter[i]
print(result)