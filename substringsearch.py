def substring_search(str1,str2):
    index = str1.find(str2)
    return index if index != -1 else -1
str1 = "hello, world"
str2="world"
print(substring_search(str1,str2))