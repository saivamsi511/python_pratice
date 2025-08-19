sen="vamsi"
final = "saivm"
sen = sen.lower()
final = final.lower()
if(len(sen)==len(final)):
    sorted1=sorted(sen)
    sorted2 = sorted(final)
    if (sorted1 == sorted2):
        print("anagram")
    else:
        print("nat an anagram")
else:
    print("nat ananagram")