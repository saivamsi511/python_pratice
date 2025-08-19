def replace_char(input_str,ch1,ch2):
    return input_str.replace(ch1,'temp').replace(ch2,ch1).replace('temp',ch2)
str_value = "apples"
ch1 = 'a'
ch2 = 'p'
modified_str = replace_char(str_value,ch1,ch2)
print(modified_str)
