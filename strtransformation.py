def string_transformation(str):
    stri = ""
    for i in range(len(str)):
        if str[i]=="a":
            stri +='b'
        elif str[i]=="b":
            stri +='a'
        else:
            stri += str[i]
    return stri
str = "abaabbcc"
fuck = string_transformation(str)
print(fuck)