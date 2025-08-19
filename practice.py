# stri = "saivamsi"
# res = stri[::-1]
# print(res)

# def maxarr(arr):
#     ele = arr[0]
#     for i in arr:
#         if i > ele:
#             ele = i
#     print(ele)
# maxarr([1,2,31,2,42,13])

# def missele(arr):
#     arr.sort()
#     ele = arr[0]
#     for i in range(ele,len(arr)+1):
#         if i not in arr:
#             arr.append(i)
#     print(arr)
# missele([1,2,3,4,5,9])


# def intersection(arr1,arr2):
#     for i in range(len(arr1)):
#         if arr1[i] == arr2[i]:
#             print(arr1[i],end=" ")
#         else:
#             break
# intersection([1,2,3,4,4],[1,2,3,4,9])

# def dupli(arr):
#     arr1=[]
#     for i in arr:
#         if i not in arr1:
#             arr1.append(i)
#     print(arr1)
# dupli([1,2,3,4,3,2,32,2,3])

# def occurofele(arr,ele):
#     count = 0
#     for i in arr:
#         if i == ele:
#             count+=1
#     print(count)
# occurofele([1,2,3,3,4,1,3,21,31],3)

# def secondlargele(arr):
#     arr.sort()
#     arr1 = []
#     for i in arr:
#         if i not in arr1:
#             arr1.append(i)
#     print(arr1[-2])
# secondlargele(list(map(int,input().split())))


# def merge(arr1,arr2):
#     arr3 = []
#     for i in arr1:
#         arr3.append(i)
#     for i in arr2:
#         arr3.append(i)
#     print(arr3)
# merge([1,2,3,4],[5,6,7,8])

# def klargeele(arr,k):
#     arr.sort()
#     print(arr[-k])
# klargeele([1,2,3,4,4,4,4,2,2,4],3)

# def maxelepos(arr):
#     ele = max(arr)
#     count = 1
#     for i in arr:
#         if i != ele:
#             count += 1
#         else:
#             break
#     print(ele,count)
# maxelepos([1,2,31,2,4,13])

# def maxele(arr):
#     arr.sort()
#     print(arr[-1],end="")
#     print(arr[-2],end="")
#     print(arr[-3],end= "")
# maxele([1,2,3,4,5,6])

# def password(stri):
#     if len(stri)<8:
#         print("Invalid password")
#     num = 0
#     spec = 0
#     space = 0
#     cap = 0
#     spec2 = ['!','@','#']
#     for i in stri:
#         if i.isdigit():
#             num += 1
#         elif i.isspace():
#             space+=1
#         elif i in spec2:
#             spec+= 1
#         elif i.isupper():
#             cap+=1
#     print(num,spec,space,cap)
#     if num<1 or spec<1 or space<1 or cap<1 :
#         print("Invalid password")
#     else:
#         print("Valid password")
# password("saiam@1 ")


# stri = "bbbbddddrrrrrtttttyyyyyy"

# myset = []
# for i in stri:
#     if i not in myset:
#         myset.append(i)
    
# for ele in myset:
#     count = 0
#     for char in stri:
#         if char == ele:
#             count += 1
#     print(ele,end="")
#     print(count,end="")


# n = 6
# list2 =[]
# for i in range(n):
#     str1 = input()
#     list2.append(str1)
# res = "Hdkjd"
# print(list2)
# for i in list2:
#     if i == res:
#         print("Yes")
#         break

# def fact(n):
#     if n == 0 or n==1:
#         return 1
#     if n>1:
#         return n * fact(n-1)
# print(fact(5))

# n = 2
# list1 = []
# for i in range(n):
#     n = int(input())
#     list1.append(n)
# print(list1)
# ans = pow(list1[0],list1[1])
# print(list1[0],"raised to the power",list1[1],"is:",ans)

# arr = [1,2,3,4,5,6]
# sum = 0
# for i in arr:
#     if i %2 == 0:
#         sum = sum + i
# print(sum)

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1 
#     if n >1 :
#         return fib(n-2) + fib(n-1)
# print(fib(9))

# num = 5
# n1 = 0
# n2 = 1
# print(n1,n2,end=" ")
# for i in range(num):
#     n3  = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")

# num = 5
# sum = 0 
# for i in range(1,num+1):
#     sum =sum + i * i
# print(sum)


# def numofcarry(num1,num2):
#     carry = 0
#     count = 0
#     if len(num1) <= len(num2):
#         l = len(num1) - 1
#     else:
#         l = len(num2)-1
#     for i in range(l+1):
#         temp = int(num1[l-i]) + int(num2[l-i]) + carry
#         if len(str(temp)) > 1:
#             count += 1
#             carry = 1
#         else:
#             carry = 0
#     return count + carry
# num1 = input()
# num2 = input()
# print(numofcarry(num1,num2))

# num = 27
# for i in range(10):
#     num = num / 3
#     if num == 1:
#         print("Yes",end=" ")
#         break
#     elif num < 1:
#         print("No",end=" ")
#         break


# def longestsubstr(s):
#     n = len(s)
#     res = 0
#     for i in range(n):
#         visited = [False] * 256
#         for j in range(i,n):
#             if visited[ord(s[j])] == True:
#                 break
#             else:
#                 res = max(res,j-i+1)
#                 visited[ord(s[j])] = True
#     return res
# print(longestsubstr("abbabcdaaa"))

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# def dividen(arr,div,quo,rem,lenofarr):
#     for i in arr:
#         if i == div * quo + rem:
#             return arr.index(i)
#     return -1
# arr = [2,3,9,5]
# div =  4
# quo = 2
# rem = 1
# lenofarr =  4
# print(dividen(arr,div,quo,rem,lenofarr))


# h = 10
# v = 20
# vn = 5
# ans = v/vn
# print(ans)
# ans1 = ans * ans * h 
# print(int(ans1))

# def operationchoice(i,n1,n2):
#     if i == 1:
#         add = n1 + n2
#         print(add)
#     elif i == 2:
#         sub = n1 - n2
#         print(sub)
#     elif i == 3:
#         mul = n1 * n2
#         print(mul)
#     elif i == 4:
#         div = n1/n2
#         print(div)
#     else:
#         print("Invalid option")
# n1 = int(input())
# n2 = int(input())
# i = int(input())
# operationchoice(n1,n2,i)


# str1 = "listen"
# str2 = "slient"
# str1 = sorted(str1)
# str2 = sorted(str2)
# if str1 == str2 :
#     print("Anagram")
# else:
#     print("Not a anagram")


# def replacechar(str1,ch1,ch2):
#     list1= []
#     for i in str1:
#         if i == ch1:
#             list1.append(ch2)
#         elif i == ch2:
#             list1.append(ch1)
#         else:
#             list1.append(i)
#     print(''.join(list1))
# replacechar('saivamsi','s','a')
            
# def strreverse(str1):
#     list1 = []
#     str1 = str1[::-1]
#     for i in str1:
#         list1.append(i)
#     print(''.join(list1))
# strreverse("saivamsi")


# def rotate(arr,n):
#     ans = arr[n:] + arr[:n]
#     print(ans)
# arr = [1,4,5,2,1,42,24]
# n= 3
# rotate(arr,n)

# def checkpre(arr,ele):
#     for i in arr:
#         if i == ele:
#             print("Element is present in the arr")
#             break
#         elif ele not in arr:
#             print("not found")
#             break
# arr = [1,2,3,4,54,5,56,6,6,6]
# ele = 56
# checkpre(arr,ele)

# def findocc(arr,ele):
#     count = 0
#     for i in arr:
#         if i == ele:
#             count += 1
#     print(count)
# arr = [12,2,2,2,2,3,4,4,5]
# ele = 2
# findocc(arr,ele)

# def calavgpos(arr):
#     avg = 0
#     sum = 0
#     count = 0
#     for i in arr:
#         if i > 0:
#             count  += 1
#             sum = sum + i 
#         avg = sum/count
#     print(avg)
# arr = [1,2,3,4,5,-5,-4,3,-5]
# calavgpos(arr)

# def findminval(arr):
#     num = arr[0]
#     for i in arr:
#         if i < num:
#             num = i
#     ans = arr.index(num)
#     print(num,ans)
# arr = [2,3,4,5,5,6,6,1,7,7,7,3]
# findminval(arr)

# def maxsubarrsum(arr,size):
#     max_so_far = arr[0]
#     curr_max = arr[0]
#     for i in range(1,size):
#         curr_max = max(arr[i],curr_max + arr[i])
#         max_so_far = max(max_so_far,curr_max)
#     return max_so_far
# print(maxsubarrsum([1,2,3,4,5],5))

# str1 = "saivamsi"
# str2 = "sai"
# if str2 in str1:
#     print("Yes")
# else:
#     print("No")

# str1 = "sasasasi"
# if str1 == str1[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# num = int(input())
# if num == 1:
#     print("Not a prime")
# elif num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# else:
#     print("not a prime")

# def larsubarrsum(arr):
#     res = arr[0]
#     for i in range(len(arr)):
#         curr_sum = 0
#         for j in range(i,len(arr)):
#             curr_sum = curr_sum + arr[j]
#             res = max(res,curr_sum)
#     return res
# print(larsubarrsum([-2,1,-3,4,-1,2,1,-5,4]))


# str = "madam"
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# stri = "Hello, world"
# print(stri[::-1])

# stri = "apples"
# ch1 = 'a'
# ch2 = 'p'
# res = []
# for i in stri:
#     if i == ch1:
#         res.append(ch2)
#     elif i == ch2:
#         res.append(ch1)
#     else:
#         res.append(i)
# print(''.join(res))

# arr = [12,3,14,56,77,13]
# num = 13
# diff = 2
# list1 = []
# count = 0
# for i in range(num-diff,num+diff+1):
#     list1.append(i)
# print(list1)
# for i in arr:
#     if i in list1:
#         count += 1
# print(count)

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end= " ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


# n = 4
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for i in range(1,i+1):
#         print(" ",end=" ")
#     for i in range(1,i+1):
#         print(" ",end=" ")
#     for i in range(i,n):
#         print("*",end=" ")
#     print()

# arr = [-1,1,2,-34,3,-4,4,5,-3,5,6,3]
# n = len(arr)
# list1 = []
# curr_max = arr[0]
# max_so_far = arr[0]
# for i in range(1,n):
#     curr_max = max(arr[i] , curr_max+arr[i])
#     max_so_far = max(curr_max,max_so_far)
# print(max_so_far)



# s = "129000"
# i = 0
# key_press = 0
# while i<len(s):
#     if i+1<len(s) and s[i] == '0' and s[i+1] == '0':
#         key_press +=1
#         i+=2
#     else:
#         key_press +=1
#         i+=1
# print(key_press)

# stri = "saivamsi is a good boy"
# list1 = stri.split(" ")
# print(list1)
# list1.reverse()
# print(*list1)
# lengtth = []
# for i in list1:
#     lengtth.append(len(i))
# print(lengtth)
# max_ele = max(lengtth)
# ele = lengtth.index(max_ele)
# print(list1[ele])

# arr1 = [3,1,4,1,5]
# arr2 = [2,7,1,8]
# arr1= set(arr1)
# arr2 = set(arr2)
# ans1= arr1.union(arr2)
# ans2 = arr1.intersection(arr2)
# print(ans1,ans2)

# text  = "saSIVamHLsiaDSKHBds"
# up = 0
# lp =0
# for i in text:
#     if i.isupper():
#         up += 1
#     elif i.islower():
#         lp += 1
# print(up,lp)
# if up>lp:
#     text = text.upper()
# else:
#     text = text.lower()
# print(text)

# num = 43
# if num < 1:
#     print("Not a prime")
# elif num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not a prime")
#             break
#     else:
#         print('Prime')
# else:
#     print("not a prime")


# stri = "saivamsi"
# k = 5
# print(stri[k:]+stri[:k])

# n = 5
# arr = [-2,1,-4,5,3]
# up = 0
# lo = max(arr)
# for i in arr:
#     if i > up :
#         up = i
#     elif i < lo:
#         lo = i
# print(lo+up)

# n = 6
# arr = [7,10,4,3,20,15]
# k = 3
# arr.sort()
# print(arr[2])

# n = 5
# arr = [0,2,1,2,0]
# zero = []
# one = []
# two = []
# for i in arr:
#     if i == 0:
#         zero.append(i)
#     elif i == 1:
#         one.append(i)
#     else:
#         two.append(i)
# print(zero+one+two)

# arr = [1,2,3,-2,3,-4,1,3,-4,24,2,-2]
# neg = []
# pos = []
# for i in arr:
#     if i < 0 :
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg+pos)

# n = 5
# arr = [1,2,3,4,5]
# k = 3
# print(arr[-k:] + arr[:-k])

# arr = [1,2,3,-2,5]
# curr_sum = arr[0]
# max_so_far = arr[0]
# for i in range(1,len(arr)):
#     curr_sum = max(arr[i],curr_sum + arr[i])
#     max_so_far = max(curr_sum,max_so_far)
# print(max_so_far)

# arr = [1,-2,-23,-2,2,13,-13,-11,-13,9]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_index = max(values)
#         index = values.index(max_index)

# print(*keys[index],max(values))
# print(keys,values)
# print(dict1)

# stri = "#####***"
# star = 0
# hash = 0
# for i in stri:
#     if i == "*":
#         star += 1
#     else:
#         hash += 1
# print(star,hash)
# if star > hash:
#     print("star is the winner")
# else:
#     print("hash is the winner")


# def leapyear(year):
#     if year%4 == 0 and year %100 != 0:
#         print("Leap year")
#     elif year%400 == 0:
#         print("Leap year")
#     else:
#         print("Not a leap year")
# year = 2020
# leapyear(year)

# num = 20
# n1 = 0
# n2 = 1
# print(n1,n2,end= " ")
# for i in range(2,num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")

# num = 24
# list1 = []
# for i in range(1,num):
#     if num % i == 0:
#         list1.append(i)
# print(max(list1))

# num = 6
# list1 =[]
# for i in range(1,num):
#     if num % i == 0:
#         list1.append(i)
# print(list1)
# sum_of = sum(list1)
# if sum_of == num :
#     print("It is A perfect number")
# else:
#     print("Not a perfect Number")

# def fact(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * fact(n-1)
# n = 5
# print(fact(n))

# num = 1534
# temp = str(num)
# length = len(temp)
# print(length)
# list1 = []
# for i in temp:
#     list1.append(int(i))
# sum = 0
# mul = 1
# for i in list1:
#     mul = pow(i,length)
#     sum = sum + mul
# if sum == num :
#     print("armstrong")
# else:
#     print("Not a Armstrong number")

# def natural_num_sum(num):
#     if num == 0:
#         return 0
#     if num >= 1:
#         sum  =0
#         for i in range(num):
#             sum = sum + i
#         print(sum)
# num = 10
# natural_num_sum(num)

# num = 20
# dec = format(num,'b')
# print(dec)
# num = "1010"
# bin = int(num,2)
# print(bin)

# num = 76
# sq = num * num
# sq = str(sq)
# res = sq[-2],sq[-1]
# dig = ''.join(res)
# if int(dig) == num :
#     print("Automorphic number")
# else:
#     print("Not a automorphic number")

# char = "/"
# print(ord(char))

# string = "saivamsi3113&(*)"
# list1 = []
# for i in string:
#     if i.isalpha():
#         list1.append(i)
# print(''.join(list1))

# stri = "c  saiV ajbdckaak abd   b  an "
# list1=[]
# for i in stri:
#     if i != " ":
#         list1.append(i)
# print(''.join(list1))

# num = 6564
# temp = str(num)
# sum = 0
# for i in temp:
#     sum = sum + int(i)
# print(sum)

# num = 87
# power = 9
# print(pow(num,power))

# a = 50
# b = 34
# bina = format(a,'b')
# binb = format(b,'b')
# list1= []
# print(bina)
# print(binb)
# for i in range(len(bina)):
#     if bina[i] == '0' and binb[i] =='0':
#         list1.append(str(0))
#     else:
#         list1.append(str(1))
# ans = ''.join(list1)
# print(ans)
# ans1 = int(ans,2)
# print(ans1)
# print(a | b)

# stri1 = "ABCBCABAB"
# stri = "AB"
# count = 0
# for i in range(len(stri1)):
#     if stri1[i] == 'A' and stri1[i+1] == "B":
#         count  += 1
# print(count)

# a = 453
# b = 242
# bina = format(a,'b')
# binb = format(b,'b')
# list1 = []
# list2 =[]
# for i in range(len(bina)):
#     if bina[i] == '0':
#         list1.append(2)
#     else:
#         list1.append(3)
# for i in range(len(binb)):
#     if binb[i] == '0':
#         list2.append(2)
#     else:
#         list2.append(3)
# list = list1 + list2
# print(sum(list))

# num1 = 3
# num2 = 9
# num3 = num1 * num2
# num4 = num3 % 12
# print(num4)

# r =7 
# unit = 3
# n = 8
# arr = [2,8,3,5,7,4,1,2]
# total_food = r * unit
# sum = 0
# count = 0
# for i  in arr:
#     sum = sum + i
#     count += 1
#     if sum >= total_food:
#         break
# print(count)

# n = 4
# m = 20
# list1 = []
# list2 = []
# for i in range(1,m+1):
#     if i % 4 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(sum(list2) - sum(list1))

# arr = [3,2,1,7,5,4]
# even = []
# odd = []
# for i in range(len(arr)):
#     if i %2 == 0:
#         even.append(arr[i])
#     else:
#         odd.append(arr[i])
# even.sort()
# odd.sort()
# print(even,odd)
# print(even[-2]+odd[1])

# def operationbinstr(str):
#     a = int(str[0])
#     i = 1
#     while i < len(str):
#         if str[i] == "A":
#             a &= int(str[i+1])
#         elif str[i] == "B":
#             a |= int(str[i+1])
#         else:
#             a ^= int(str[i+1])
#         i+=2
#     return a
# str = "1C0C1C1A1B0B1"
# print(operationbinstr(str))

# sum1 = 9
# arr = [5,2,4,3,9,7,1]
# arr.sort()
# list1 = arr[1],arr[0]
# print(list1)
# if sum(list1)>sum1:
#     print(0)
# else:
#     print(list1[0] * list1[1])

# n = 12
# num = 718
# print(num/n)
# list1 = []
# while num>0:
#     quo = int(num/n)
#     rem = num % n
#     list1.append(rem)
#     num = quo
# list1.reverse()
# print(list1)
# ans = ''
# for i in list1:
#     if i > 9:
#         a = i - 9
#         a = 64 + a
#         ans += chr(a)
#     else:
#         ans += str(i)
# print(ans)

# n = 5
# p = 0
# for i in range(n):
#     for j in range(i,n):
#         print(p,end=" ")
#         p += 1
#     print()

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# dict1= {}
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         dict1[tuple(arr[i:j])] = sum (arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_val = max(values)
#         max_indec = values.index(max_val)
# print(*keys[max_indec],max(values))
# # print(dict1)
# print(values)

# arr = [1,2,3,0,3,3,3,3]
# sum1 = 0
# for i in arr:
#     sum1 = sum1 + i
#     if sum1 == 0:
#         print(True)
#     elif sum1 > 0:
#         sum1 = 0

# def next_gre_ele(arr):
#     n = len(arr)
#     result = [-1] * n
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[j] > arr[i]:
#                 result[i] = arr[j]
#                 break
#     return result
# arr = [4,5,2,25]
# print(next_gre_ele(arr))

# arr = [1,2,0,4,3,0,5,0]
# list1 = []
# count = 0
# for i in arr:
#     if i != 0:
#         list1.append(i)
#     elif i == 0:
#         count += 1
# print(count)
# for i in range(count):
#     list1.append(0)
# print(list1)

# num = 26
# m = 3
# print(num // m)
# lower = (num // m) * m
# upper = lower + m
# if abs(num-lower) < abs(num-upper):
#     print(lower)
# elif abs(num-lower) > abs(num-upper):
#     print(upper)
# else:
#     print(upper)


# arr = [1,0,1,1,1,0,0,1,0,0,1]
# one = 0
# zero = 0
# for i in arr:
#     if i == 1:
#         one += 1
#     else:
#         zero += 1
# if one ==  zero :
#     print(one + zero)
# elif one > zero :
#     print(zero * 2)
# else:
#     print(one * 2)

# num = "987654"
# print(num[::-1])

# arr = [12,2,4,4,5,5,3,9]
# max_ele = 0
# for i in arr:
#     if i > max_ele :
#         max_ele = i
# print(max_ele)

# arr = [1,2,5,6,14,3]
# min_val = arr[0]
# list1 = []
# for i in arr:
#     if i < min_val:
#         list1.append(i)
#         min_val = i
#     else:
#         list1.append(min_val)
# print(list1)


# num = 47
# if num < 1:
#     print("Not a prime")
# elif num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not a prime")
#             break
#         else:
#             print("Prime")
#             break
# else:
#     print("Not a Prime")

# s = "anagram"
# t = "nagarm"
# s= sorted(s)
# t = sorted(t)
# if s == t:
#     print("Anagram")
# else:
#     print("Not a Anagrama")

# arr = [3,0,1]
# max_ele = max(arr)
# list1 = []
# for i in range(max_ele+1):
#     if i not in arr:
#         print(i)
#         list1.append(i)
#     else:
#         list1.append(i)
# print(list1)

# str = "Hello world!"
# print(str[::-1])
# ans = str.split(" ")
# ans.reverse()
# print(*ans)

# def count_occ_ele(arr,ele):
#     count = 0
#     for i in arr:
#         if i == ele:
#             count += 1
#     print(count)
# arr= [5,2,4,1,2]
# ele = 2
# count_occ_ele(arr,ele)


# m =  1
# n =  10
# even = []
# odd = []
# for i in range(m,n):
#     if i % 2 == 0:
#         even.append(i*i)
#     else:
#         odd.append(i*i)
# print(sum(odd) - sum(even))

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fib(n-2) + fib(n-1)
# print(fib(7))


# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

# arr = [10,5,10,15,10,5]
# list1 = []
# for i in arr:
#     if i not in list1:
#         list1.append(i)
# print(list1)
# count = 0
# for i in list1:
#     for j in arr:
#         if i == j :
#             count += 1
#     print(count)
#     count = 0
    
# arr = [3,1,-2,-5,2,-4]
# even = []
# odd = []
# for i in arr:
#     if i < 0:
#         odd.append(i)
#     else:
#         even.append(i)
# print(odd,even)
# list1 = []
# for i in range(len(odd)):
#     list1.append(even[i])
#     list1.append(odd[i])
# print(list1)

# n = "25"
# if len(n) == 1:
#     print(n)
# elif int(n) % 2==0:
#     print(int((int(n)-2)/2))
# else:
#     print(int(int(n)/2))

# m = 6
# n = 30
# list1 = []
# list2 = []
# for i in range(n+1):
#     if i % m == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(sum(list2) - sum(list1))

# num = 15
# bin = format(num,'b')
# print(bin)
# count = 0
# for i in bin:
#     if i == '1':
#         count += 1
# print(count)

# str = "yes no number"
# ans = str.split(" ")
# print(ans)
# max_len = 0
# for i in ans:
#     if len(i) > max_len:
#         max_len = len(i)
# print(max_len)
# for i in ans:
#     if len(i) == max_len:
#         print(i)

# wei = 42
# hei = 1.3
# bmi = wei / (hei * hei)
# print(bmi)
# if bmi < 18:
#     print(0)
# elif bmi>=18 or bmi < 25:
#     print(1)
# elif bmi>=25 or bmi < 30:
#     print(2)
# elif bmi>=30 or bmi < 40:
#     print(3)
# elif bmi >= 40 :
#     print(4)


# inp = 34
# inp = str(inp)
# list1= []
# for i in inp:
#     list1.append(str(int(i)*int(i)))
# print(list1)
# print(''.join(list1))

# n = 3
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         for k in range(i):
#             print(j,end=" ")
#     print()

# stri = "helloworld"
# leng = 10
# count = 0
# c= 'l'
# for i in stri:
#     if i == c:
#         count += 1
# print(count)

# arr = [1,2,1,3,4,4,1]
# res = ""
# for i in arr:
#     if i%2==0:
#         res += "Even"
#     else:
#         res += "Odd"
# print(res)

# arr = [10,5,6,3,7,2]
# even = 0
# odd = 0
# for i in range(len(arr)):
#     if i%2 == 0:
#         even =  even ^ arr[i]
#     else:
#         odd = odd + arr[i]
# print(odd - even)

# arr = [11,1,2,8,10,11,15,7]
# sum = 0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i] + arr[j] == 18:
#             temp = arr[i]*arr[j]
#             if temp >= sum:
#                 sum = temp
#                 res = arr[j],arr[i]
# print(res)

# num = 5
# ans = 3.14 * (num * num)
# print(int(ans))

# n= 4
# for i in range(n):
#     for j in range(i,n):    
#         print("*",end=" ")
#     print()

# def check_ne(arr):
#     n = len(arr)
#     res = [-1] * n
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[j] > arr[i]:
#                 res[i] = arr[j]
#                 break
#     return res
# arr = [1,6,7,3,5]
# print(check_ne(arr))

# n = 5
# if n >= 3 and n<5:
#     print("spring")
# elif n>=5 and n<7:
#     print("summer")
# elif n>=7 and n<9 :
#     print("Autumn")
# elif n>=9 and n<12 or n == 1 or n ==2:
#     print("winnter") 
# else:
#     print("Invalid month")

# n = 5
# char = 64
# for i in range(n):
#     char += 1
#     for j in range(i+1):
#         print(chr(char),end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1,n+1):
#         print(j-i,end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1,n+1):
#         print(" ",end= " ")
#     for j in range(i+1):
#         print(i+j+1,end=" ")
#     for i in range(i,0,-1):
#         print(i+j,end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for i in range(i,n-1):
#         print("*",end=" ")
#     print()

# n = 6
# for i in range(n):
#     for j in range(i,n):
#         print(" " ,end=" ")
#     value = 1
#     for j in range(i+1):
#         print(" ",value  ,end=" ")
#         value = value *(i-j)//(j+1)
#     print()

# n = 5
# ans = 1
# for i in range(n):
#     for j in range(i+1):
#         print(ans,end=" ")
#         ans += 1
#     print()

# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if j%2 == 0:
#             print("*",end=" ")
#         else:
#             print("A",end=" ")
#     for j in range(i):
#         if j%2 != 0:
#             print("A",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# n = 4
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# n1 = 1
# n2 = 1
# num = 6
# print(n1,n2,end=" ")
# for i in range(2,num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")

# num = "23GF"
# print(int(num,17))

# num = 10
# bin = format(num,'b')
# print(bin)
# res = ""
# for i in bin:
#     if i == '0':
#         res += '1'
#     else:
#         res += '0'
# print(res)
# val = int(res,2)
# print(val)

# arr = [1,0,2,0,1,0,2]
# num =[]
# count = []
# for i in arr:
#     if i != 0:
#         num.append(i)
#     else:
#         count.append(i)

# print(count + num)

# num = "5244"
# mul = 1
# for i in num:
#     mul = mul * int(i)
# print(mul)

# arr = [-1,1,-1,-1,1,1,1,1,1,-1,-1,1]
# right = 0
# left = 0
# start = 0
# sum = 0
# count = 0
# for i in arr:
#     if i == -1:
#         left += 1
#     elif i == 1:
#         right += 1
#     sum = sum + i
#     if sum == 0:
#         count += 1
# print(right,left,count)

# arr = [10,20,30]
# ans = 1000
# m = 3
# arr.sort()
# l = len(arr)
# for i in range(l - (m -1)):
#     if arr[i+m-1] - arr[i] < ans:
#         ans = arr[i+m - 1] - arr[i]
#     print(ans)
#     break

# num = 10
# list1 = []
# for i in range(1,num):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)
# dict1= {}
# for i in range(len(list1)):
#     for j in range(i,len(list1)):
#         dict1[tuple(list1[i:j])] = sum(list1[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
# print(values)
# for i in values:
#     if int(i) == 10:
#         ans = i
#         print(i)
#         break
# else:
#     print("Not Found")
# index = values.index(ans)
# print(keys[index])
# print(dict1)

# stri = "HTHTT"
# count = 0
# count1 = 0
# count2 = 0
# for i in stri:
#     if i == 'H':
#         count += 1
#         count1 += 1
#     elif count == 3:
#         break
#     elif i == 'T':
#         count = 0 
#         count2 += 1
# print(count1*2 + count2*-1)


# alp = []
# for i in range(65,91):
#     alp.append(chr(i))
# print(alp)
# stri = "WELCOME TO GEEKSFORGEEKS"
# list1 = []
# list2 = []
# for i in stri:
#     if i in alp and i not in list1:
#         list1.append(i)
# print(sorted(list1))
# stri1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in stri1:
#     if i not in stri:
#         list2.append(i)
# print(*list2)

# dog = 4
# human = 1
# ans = dog * 7
# print(ans)

# stri = "This is sai vamsijladljv  nj bj j bb j"
# count = 0
# for i in stri:
#     if i == " ":
#         count += 1
# print(count)


# list1 = [1,3,15,5]
# m = 15
# n = len(list1)
# count = 0
# for i in range(n):
#     for j in range(i,n):
#         for k in range(j,n):
#             if (list1[i] * list1[j] * list1[k] == m):
#                 count += 1
# print(count)


# num = 6
# list1 = []
# if num < 0:
#     print("Not a prime")
# elif num > 1:
#     for i in range(2,num+5):
#         if i % 2 == 0:
#             continue
#         elif i>num:
#             list1.append(i)
#     print(list1[0])
        
# else:
#     print("Not a prime")


# stri = "aaaaddddddddddd"
# list1 = []
# list2 = []
# list3 = []
# count = 0
# for i in stri:
#     if i not in list1:
#         list1.append(i)
# print(list1)
# for i in list1:
#     ans = stri.count(i)
#     list2.append(i)
#     list3.append(ans)
# if len(list1) == 1:
#     print(0)
# print(list2,list3)
# max_ele = list3.index(max(list3))
# ele = max(list3)
# print(list2[max_ele])
# sum = 0
# for i in list3:
#     if i !=  ele:
#         sum = sum + i
# print(sum)


# num = "167"
# ans = ""
# for i in num:
#     ans  += str(int(i) * int(i))
# print(ans)

# arr = [1,2,1,2]
# arr1 = arr[:2]
# arr2 = arr[3:]
# print(arr1,arr2)
# if sum(arr1) == sum(arr2):
#     print("Equilibiam",arr[2:3])
# else:
#     print("Not an Equlibrium")


# n1 = 12
# n2 = 18
# list1 = []
# for i in range(1,n2):
#     if n1 % i == 0 and n2 % i == 0:
#         list1.append(i)
# ans = max(list1)
# lcm = (n1 * n2) // ans
# print(ans)
# print(lcm)

# list1 = [1,3,3,4]
# ans = 4
# dict1= {}
# for i in range(len(list1)):
#     for j in range(i,len(list1)):
#         dict1[tuple(list1[i:j])] = sum(list1[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
# print(values)
# print(keys)
# ans = values.index(ans)
# ans2 = keys[ans]
# list3 = []
# for i in ans2:
#     list3.append(list1.index(i))
# print(list3)

# arr = [2,7,11,15]
# m = 9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == m:
#             print([i,j])


# n = str(100)
# count = 0
# i = 0
# while i < len(n):
#     if n[i]== '0' and n[i+1] == '0':
#         count += 1
#         i += 2
#     else:
#         count += 1
#         i+=1
# print(count)

# arr  =[1,2,2,3,4,4]
# even = []
# odd = []
# for i in arr:
#     if i %2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even,odd)
# even = set(even)
# odd = set(odd)
# odd = list(odd)
# even = list(even)
# count = 0
# list1 = []
# list2= []
# teama = 0
# teamb =0 
# for i in even:
#     list1.append(arr.count(i))
# for i in odd:
#     list2.append(arr.count(i))
    
# print(list1,list2)
# for i in list1:
#     if i %2 == 0:
#         teama += 1
#     else:
#         teamb +=  1
# for i in list2:
#     if i % 2 ==0:
#         teamb+=1
#     else:
#         teama+= 1
# if teama == teamb :
#     print("TO")
# elif teama > teamb :
#     print("TeamA")
# else:
#     print("TeamB")

# num = 10001
# num = str(num)
# length = len(num)
# ans =0 
# count = 0
# if length < 3:
#     ans = 0
# if length > 3:
#     for i in range(999,int(num)):
#         ans = i // 3
#         count += 1
# print(count)


# x = 56
# y = 98
# while y!=0:
#     if x<y:
#         x,y = y,x
#     else:
#         t = x - y
#         x = y
#         y = t
# print(x)

# num = 10
# bin = format(num,'b')
# print(bin)
# num = "1010"
# ans = int(num,2)
# print(ans)
# num = 8
# if num < 1:
#     print("Not a prime")
# elif num > 1:
#     for i in range(2,num):
#         if num % 2 == 0:
#             print("Not a prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not a prime")
# num = 122
# num = str(num)
# sum = 0
# for i in num:
#     sum = sum + int(i)
# print(sum)


# import math
# def task(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n > 1:
#         return ((n-1) + 7 * (n-2) + (n/4)) % (pow(10,9) + 7)
# print(task(20))

# import math
# def task(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n > 1:
#         return (((n-1) * (n-1)) + ((n-2) * (n-2))) % 47
# print(task(16))

# arr = [1,17,18,0,18]
# sum = 18
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] ==  18:
#             temp = arr[i],arr[j]
#             if arr[i] > arr[j]:
#                 print(temp)
            

# n = 3
# sum = 0
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(i-j+1,end=" ")
#         sum = sum + i-j+1
#     for j in range(i,0,-1):
#         print(i-j+2,end=" ")
#         sum = sum + i-j+2
#     print()
# print(sum)


# arr = [1,2,3,4]
# ans = 0
# n = len(arr)
# for i in range(n//2):
#     ans += (arr[n-i-1] - arr[i])
# print(ans) 

# stri = "abaadab"
# ans = []
# n = len(stri)
# for i in stri:
#     if ans and ans[-1] == i :
#         ans.pop()
#     else:
#         ans.append(i)
# print(''.join(ans))

# stri = "abcde"
# k = 2
# print(stri[k:] + stri[:k])

# n = 28
# while True:
#     if str(n) == str(n)[::-1]:
#         print(n)
#         break
#     else:
#         n += int(str(n)[::-1]) 

# n = 12
# list1 = []
# for i in range(1,n):
#     if n % i == 0:
#         list1.append(i)
# print(list1)
# if sum(list1) == n :
#     print(1)
# else:
#     print(list1)

# arr = [10,20,30,40,50]
# arr1 = [4,2,1,0,3]
# list1 = []
# for i in arr1:
#     list1.append(arr[i])
# print(list1)


# arr1 = [1,2,3,4,5]
# arr2 = [1,2,4,5]
# arr3 = [1,4,5]
# ele  =[]
# ele1 = []
# for i in range(len(arr1)):
#     if arr1[i] not in arr2:
#         ele.append(arr1[i])
# print(*ele)
# for i in range(len(arr2)):
#     if arr2[i] not in arr3:
#         ele1.append(arr2[i])
# print(*ele1)

# arr = [1,-2,-3,4,-5,6,7]
# list1 = []
# list2 =[]
# for i in arr:
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list1+list2)

# arr = [6,4,1,3,5]
# max_ele = max(arr)
# for i in range(1,max_ele):
#     if i not in arr:
#         print(i)

# num = 6
# bin = format(num,'b')
# print(bin)
# sum = 0
# for i in bin:
#     sum = sum + int(i)
# print(sum)

# arr = "0000000"
# list1 = []
# for i in range(len(arr)):
#     if arr[i] == "1":
#         list1.append(i)
# if len(list1) == 0:
#     print("-1")
# else:
#     print(list1[-1])

# num = 5
# list1 =['A','B','A','A','A']
# # for i in range(num):
# #     ans = input()
# #     list1.append(ans)
# print(list1)
# count_a = 0
# count_b = 0
# for i in list1:
#     if i == 'A':
#         count_a += 1
#     else:
#         count_b += 1
# if count_a > count_b :
#     print("Team A win")
# else:
#     print("Team B won")


# arr = [10,20,30]
# sum = 0
# for i in arr:
#     if i >= 5:
#         sum = sum + i
# print(sum)


# arr = [1,3,1,7,1,2,3,15]
# arr.sort()
# print(arr)
# num = max(arr)
# list1 = []
# if num < 1:
#     print("Not a prime")
# elif num > 1:
#     for i in range(2,num):
#         if i % 2 == 0:
#             continue
#         else:
#             list1.append(i)
# else:
#     print("Not a prime")
# print(list1)
# list3 =[]
# for i in list1:
#     if i in arr:
#         list3.append(i)
# print(max(list3))

# arr = [15,12,122]
# arr.sort()
# print("Smallest number is:",arr[0])
# print("Largest number is:",arr[-1])


# m = int(input().strip())
# n = int(input().strip())
# arr = []
# for i in range(m):
#     arr.extend(map(int,input().strip().split()))
# arr.sort()
# for i in range(m):
#     print(*arr[i * n:(i+1) * n])

# n1 = 25
# n2 = 30
# list1 = []
# for i in range(1,n2):
#     if n1%i == 0 and n2 %  i == 0:
#         list1.append(i)
# print(max(list1))

# arr = [1,2,1,3,5]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if len(arr[i:j]) == 3:
#             dict1[tuple(arr[i:j])] = sum(arr[i:j])
#             keys = list(dict1.keys())
#             values = list(dict1.values())
# print(values)
# print(keys)
# print(dict1)

# n = 3
# arr = [15,25,35]
# div = 7
# quo= 3
# rem = 2
# divd = div * quo + rem
# print(divd)
# for i in range(len(arr)):
#     if divd == arr[i]:
#         print(i)
#     else:
#         print("-1")
#         break

# arr = [11,21,32,45,1,23]
# k = 12
# list1 = []
# i = 2
# while k > 1:
#     if k % i == 0:
#         list1.append(i)
#         k //= i
#     else:
#         i += 1
# print(list1)
# list2 = []
# for i in list1:
#     list2.append(arr[i])
# print(sum(list2))

# arr = [1,0,1,4,1,5,6,3]
# list1 = []
# list2 = []
# for i in arr:
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list2 + list1)

# stri = "13a4v5c"
# list1 = []
# list2 = []
# for i in stri:
#     if i.isnumeric():
#         list1.append(int(i))
#     else:
#         list2.append(i)
# print(list1)
# for i in range(len(list1)):
#     ans = list1[i] * list2[i]
#     print(ans,end="")
# for i in stri:
#     if i.isalpha():
#         list1.append()


# stri = "aaaabbbccc"
# list1 = []
# count = 0
# for i in stri:
#     if i not in list1:
#         list1.append(i)
# print(list1)
# for i in list1:
#     ans = stri.count(i)
#     print(ans,end=" ")

# str1 = "ACB"
# str2 = "BDC"
# str3 = "CED"
# str4 = "DEF"
# l1,l2,l3,l4 = [],[],[],[]
# ind = int(ord(str1[0]))
# l1.append(ind)
# l1.append(ind+2)
# l1.append(ind+1)

# ind = int(ord(str2[0]))
# l2.append(ind)
# l2.append(ind+2)
# l2.append(ind+1)

# ind = int(ord(str3[0]))
# l3.append(ind)
# l3.append(ind+2)
# l3.append(ind+1)

# ind = int(ord(str4[0]))
# l4.append(ind)
# l4.append(ind+2)
# l4.append(ind+1)

# print(l1,l2,l3,l4)
# if l1[0] == l1[1] - 2 and l1[1] == l1[2] +1 and l1[1] == l1[2] :
#     print("There is no error")
# else:
#     print(*l1)
# if l2[0] == l2[1] - 2 and l2[1] == l2[2] +1:
#     print("There is no error")
# else:
#     print(*l2)
# if l3[0] == l3[1] - 2 and l3[1]== l3[2] +1:
#     print("There is no error")
# else:
#     print(*l3)
# if l4[0] == l4[1] - 2 and l4[1] == l4[2] +1:
#     print("There is no error")
# else:
#     print(*l4)

# n = 3
# list1 = []
# for i in range(n):
#     n = input()
#     list1.append(n)
# print(list1)
# list2 = []
# for i in list1:
#     list2.append(ord(i[0]))
# print(list2)
# for i in range(len(list2)):
#     if list2[i] == list1

# stri= "123321"
# l1 = []
# for i in  stri:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# list2 = []
# for i in l1:
#     ans = stri.count(i)
#     list2.append(ans)
# for i in list2:
#     if i < 2 and i > 2:
#         break
#     # else:

# s = "12344321"    
# max_len = 0 
# n = len(s)
# for i in range(n):
#     for j in range(i+2,n+1,2):
#         print(j,end=" ")
#         substri = s[i:j]
#         print(substri,end= " ")
#         mid = len(substri) // 2
#         left = sum(int(x) for x in substri[:mid])
#         right = sum(int(x) for x in substri[mid:])
#         if left == right:
#             max_len = max(max_len,len(substri))
# print(max_len)

# n = "123123"
# list1 = []
# max_len = 0
# dict1 ={}
# for i in n:
#     list1.append(int(i))
# for i in range(len(list1)):
#     for j in range(i,len(list1)):
#         dict1[tuple(list1[i:j])] = sum(list1[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         mid = len(keys) // 2
#         left = sum(int(x) for x in list1[:mid])
#         right = sum(int(x) for x in list1[mid:])
#         print(left,right)
#         if left == right:
#             max_len = max(max_len,len(list1))
# print(max_len)
# print(dict1)

# n = 6
# arr = [1,2,3,4,5,6]
# arr.sort()
# mid = len(arr) // 2
# ans = arr[:mid]
# ans1 = arr[mid:]
# ans1.reverse()
# print(ans,ans1)
# list1 = []
# for i in range(len(ans)):
#     list1.append(ans1[i])
#     list1.append(ans[i])
# print(list1)

# m = 3
# x = [2,1,6]
# y = [1,5]
# n = 2
# count = 0
# for i in range(m):
#     for j in range(n):
#         if x[i]**y[j] > y[j]**x[i]:
#             count += 1
# print(count)

# arr = [0,2,1,2,0]
# count = 0
# count1 = 0
# count2 = 0
# for i in arr:
#     if i == 0:
#         count += 1
#     elif i == 1:
#         count1 += 1
#     else:
#         count2 += 1
# list1 = []
# for i in range(count):
#     list1.append(0)
# for i in range(count):
#     list1.append(1)
# for i in range(count):
#     list1.append(2)
# print(list1)

# arr = [16,17,4,3,5,2]
# list1 = []
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] < arr[j]:
#             list1.append(arr[j])
# list1.append(arr[-1])
# print(list1)

# arr = [12,3,4,5,2,4,24]
# dict1= {}
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
# print(dict1)

# arr = [12,22,32]
# m = 3
# a = 0
# b = 0
# c = 0
# for i in arr:
#     ans = i % 3
#     if ans == 0:
#         a += i // 3
#         b += i // 3
#         c += i // 3
#     elif ans == 1:
#         a += i // 3
#         b += i // 3
#         c += (i // 3) + 1
#     elif ans == 2:
#         a += i // 3
#         b += (i // 3) + 1
#         c += (i // 3) + 1
#     elif ans == 3:
#         a += (i // 3) + 1
#         b += (i // 3) + 1
#         c += (i // 3) + 1
# print(a,b,c)

# num = 9
# if num % 2 == 0:
#     print("Yes")
# else:
#     print("No")

# sen = "saivamsi is a good boy and he has no bad habbits and eat good food and he is a helathy person"
# sen = sen.upper()
# list1 = []
# for i in sen:
#     if i not in list1:
#         list1.append(i)
# print(list1)
# list2 = []
# for i in range(65,91):
#     list2.append(chr(i))
# print(list2)
# for i in range(len(list2)):
#     if list2[i] not in list1:
#         print(list2[i],end=" ")


# def printlarnum(arr):
#     maxi = 0
#     list1 = []
#     for x in arr:
#         list1.append(str(x))
#     for x in list1:
#         maxi = max(maxi,len(x))
#     return "".join(sorted(list1,reverse=True,key = lambda _:_ *maxi ))
# arr = [3,30,34,5,9]
# print(printlarnum(arr))


# def spiraltra(r,c,mat):
#     a = mat 
#     k = 0
#     l = 0
#     res = []
#     while(k<r and l<c):
#         for i in range(l,c):
#             res.append(a[k][i])
#         k+=1
#         for i in range(k,r):
#             res.append(a[i][c-1])
#         c-=1
#         if (k<r):


# r = 4
# c = 4
# mat =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


# arr =[4,3,7,8,6,2,1]
# n = len(arr)
# for i in range(0,n-1):
#     if(i%2 ==0 and arr[i]>arr[i+1]):
#         arr[i],arr[i+1] = arr[i+1],arr[i]
#     elif (i%2 != 0 and arr[i]<arr[i+1]):
#         arr[i],arr[i+1] = arr[i+1],arr[i]
# print(arr)

# arr =[100,180,260,310,40,535,695]
# ans = min(arr)
# ans1 = max(arr)
# print(ans,ans1)
# for i in range(len(arr)):
#     if arr[i] == ans or arr[i] == ans1 :
#         print(i,end=" ")

# stri = "saivamsi"
# ans = ""
# for i in reversed(stri):
#     ans +=i 
# print(ans)

# arr =[12,3,3,4]
# print(max(arr))

# arr =[1,2,3]
# arr1 =[1,2,34,5]
# arr=set(arr)
# arr1  = set(arr1)
# print(arr.union(arr1))

# arr =[1,2,3,4,2]
# list1 =[]
# for i in arr:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# arr =[1,2,3,4]
# max_ele = 0
# list1=[]
# for i in arr:
#     if i > max_ele:
#         max_ele = i
#         list1.append(max_ele)
# print(list1[-2])

# stri = "babacda"
# arr = []
# count = 0
# for i in stri:
#     if i not in arr:
#         arr.append(i)
#         count+=1
#         print(count)
#     else:
#         count = 0


# arr =[1,2,3,4]
# arr.sort()
# k = 3
# print(arr[-k])
# j =0
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         arr[i],arr[i+1] = arr[i+1],arr[i]
#     else:
#         arr[i+1],arr[i] = arr[i],arr[i+1]
# print(arr)

# stri ="bB1_89"
# dig = 0
# cap =0
# space = 0
# slash = 0
# for i in stri:
#     if i.isdigit():
#         dig += 1
#     elif i.isupper():
#         cap += 1
#     elif i.isspace():
#         space += 1
#     elif i =="/":
#         slash  += 1
# if len(stri)<4:
#     print("length is in sufficient")
# elif stri[0].isnumeric():
#     print("0")
# elif space > 1 or slash >1:
#     print("0")
# elif dig >= 1 and cap >= 1:
#     print("1")
# else:
#     print("1")


# stri = "aaabbbc"
# ans = ""
# for i in stri:
#     if i == "a":
#         ans += "b"
#     elif i =="b":
#         ans += "a"
#     else:
#         ans += i
# print(ans)

# arr = [1,1,1,2,2,3,3,3,3,5]
# arr1 = arr
# list1 =[]
# for i in arr:
#     if i not in list1:
#         list1.append(i)
# print(list1)
# # list2 = []
# # for i in list1:
# #     list2.append(arr.count(i))
# # print(list2)
# # list2.sort()
# # list2.reverse()
# # print(list2)
# dict1 = {}
# for i in list1:
#     dict1[i] = arr.count(i)
#     keys = list(dict1.keys())
#     values = list(dict1.values())
# print(keys,values)
# print(dict1)


# arr = [1,2,1,1,2,3,3,3,3,5]
# arr1 = sorted(arr,reverse=True,key = lambda i:arr.count(i))
# print(arr1)

# Lambda function to multiply two numbers
# multiply = lambda x, y: x * y
# print(multiply(2,4)) # Output: 6

# List of tuples
# points = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# # Sort the list of tuples by the second element
# sorted_points = sorted(points, key=lambda point: point[1][1])
# print(sorted_points) # Output: [(4, 1), (1, 2), (2, 2), (5,3)]

# numbers = [1, 2, 3, 4, 5]
# list1 = [1,2,3]
# even_numbers = list(filter(lambda x: x not in list1, numbers))
# print(even_numbers) # Output: [2, 4]

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers) 

# print(abs(-12)) 

# a = 5.35353
# b = 5
# ans = a + b
# print(round(ans,2))

# stri = 3 * 'saivamsi' 
# print(stri)

# stri = "saivamsi"
# print(stri[1:-1:2])

# str1 = " dgcvgj"
# str1 = str1.strip()
# print(str1)

# n = int(input("Enter the no of semisters:-"))
# list1 = []
# for i in range(n):
#     m = 1
#     print("Enter the no of subjets in",m, "semister:-")
#     n = int(input())
#     m += 1
#     list1.append(n)
# print(list1)
# list2 = []
# for i in list1:
#     print("marks obtained:-")
#     for j in range(i):
#         n = int(input())
#     list2.append(n)
# print(list2)
        
# num = 54
# list1 = []
# for i in range(1,num+1):
#     if num % i == 0:
#         list1.append(i)
# print(list1)

# stro = "1358932424444444447287682865"
# ans = int(stro) % 11
# print(ans)

# str1 = "100101110110"
# list1 = [5,19,8,7,6,15,4,3,2,1,10,8]
# print(sum(list1))

# r = 7
# unit = 2
# n = 8
# arr = [2,8,3,5,7,4,1,2]
# if n == 0:
#     print("-1")
# tot = r * unit
# sum = 0
# count = 0
# for i in arr:
#     sum += i
#     count += 1
#     if sum > tot :
#         print(count)
#         break

# n = 5
# list1 = []
# for i in range(1,n+1):
#     bin = format(i,'b')
#     list1.append(bin)
# print(list1)
# for i in list1:
#     for j in i:
#         if j == '0' :
#             j = '1'
#         elif j == '1' :
#             j = '2'
#         print(j,end=" ")
        
# s = "ABCD"
# vow = ['A','E','I','O','U']
# count = 0
# for i in s:
#     if i not in vow:
#         count += 1
# mul = 1
# for i in range(1,count+1):
#     mul = mul * i
# print(mul)

# cad = 4
# arr = [5,5,2,9,105,8]
# money = 16
# count = 0
# for i in arr:
#     if i % 5 == 0:
#         count += 1
#     else:
#         money = money - i
#         count  += 1
#     if money <= 0:
#         break
# print(count)

# arr = [1,2,2,3,13,3]
# n = 2
# count = 0
# for i in arr:
#     if i == n:
#         count += 1
# print(count)
# print(arr.count(n))

# arr = [11,12,13,14]
# arr1 = [15,16,17,18]
# arr,arr1 = arr1,arr
# print(arr,arr1)

# stri = "prepbytes"
# print(''.join(sorted(stri)))

# stri = "saivamsi"
# ans = ""
# count = 0
# for i in stri:
#     if i not in ans:
#         ans += i
#         count += 1
# print(ans,count)

# num = 100
# list1 =[]
# if num < 1:
#     print("not a prime")
# elif num > 1:
#     for i in range(2,num):
#         if i % 2 == 0:
#             continue
#         else:
#             list1.append(i)
# else:
#     print("Not a prime")
# print(list1)


# arr = [1,34,3,98,9,76,45,4]
# maxi = 0
# list1 =[]
# for x in arr:
#     list1.append(str(x))
# for x in list1:
#     maxi = max(maxi,len(x))
# ans = "".join(sorted(list1,reverse=True,key=lambda _:_ *maxi))
# print(ans)


# def printlarnum(arr):
#     maxi = 0
#     list1 = []
#     for x in arr:
#         list1.append(str(x))
#     for x in list1:
#         maxi = max(maxi,len(x))
#     return "".join(sorted(list1,reverse=True,key = lambda _:_ *maxi ))
# arr = [3,30,34,5,9]
# print(printlarnum(arr))

# arr = [12,2,3,4,22]
# sum = 14
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == sum :
#             print(arr[i],arr[j])


# arr = [1,2,3,4,7]
# max_ele = max(arr)
# for i in range(1,max_ele):
#     if i not in arr:
#         print(i,end=" ")

# stri = "saivamsi"
# for i in stri:
#     ans = stri.count(i)
#     if ans == 1 :
#         print(i)
#         break

# vow = ['a','i','e','o','u']
# stri = "saivamsi"
# vow2 = 0
# cosnt = 0
# for i in stri :
#     if i in vow:
#         vow2 += 1
#     else:
#         cosnt += 1
# print("vowels in the arr is",vow2)
# print("constants in the string is",cosnt)

# arr = [4,5,2,25,2,88]
# list1 =[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         print(arr[j],end=" ")
#         if arr[j] > arr[i]:
#             list1.append(arr[j])
#             break
# list1.append(-1)
# print(list1)

# arr = [1,2,3,0,0,1,1,1]
# count = 0
# list1 = []
# for i in arr:
#     if i == 0:
#         count += 1
#     elif i not in list1:
#         list1.append(i)
# for i in range(count):
#     list1.append(0)
# print(list1)

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         dict1[tuple(arr[i:j])] = sum (arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_ele = max(values)
#         index = values.index(max_ele)
# print(keys[index])
# print(max_ele)

# num = 70
# m = 8
# list1 = []
# for i in range(num+m):
#     if i % m == 0:
#         list1.append(i)
# print(list1)
# maxele = list1[-1] - num
# max1 = num - list1[-2] 
# print(maxele,max1)
# if maxele > max1 :
#     print(list1[-2])
# else:
#     print(list1[-1])

# stri = "0C1A1B1C1C1B0A0"
# ans = 0
# for i in range(len(stri)):
#     if stri[i] == "A":
#         ans = int(stri[i-1]) & int(stri[i+1])
#     elif stri[i] == "B":
#         ans = int(stri[i-1])  | int(stri[i+1])
#     elif stri[i] == "C":
#         ans = int(stri[i-1]) ^ int(stri[i+1])
# print(ans)

# arr = [12,3,14,56,77,13]
# num = 13
# diff = 2
# count = 0
# for i in range(num-2,num+3):
#     if i in arr:
#         count += 1
# print(count)

# n = 4
# m = 20
# sum = 0
# sum1 = 0
# for i in range(1,m+1):
#     if i % n  == 0:
#         sum += i
#     else:
#         sum1 += i
# print(sum1 - sum)

# arr = [3,2,1,7,5,4]
# arr.sort()
# list1 = []
# list2 = []
# for i in range(len(arr)):
#     if i % 2 == 0:
#         list1.append(arr[i])
#     else:
#         list2.append(arr[i])
# print(list1,list2)
# print(list1[-2]+list2[1])


# n = 12
# num = 718
# quo = 0
# rem = 0
# list1 = []
# while num > 0:
#     rem = num % n
#     list1.append(rem)
#     quo = num // n
#     num = quo
# print(list1)
# for i in list1:
#     if i > 9:
#         a = i - 9
#         ans = a + 64
#         print(chr(ans),end="")
#     else:
#         print(str(i),end="")
        
        
# stri = "Move-Hypens-to-the-start"
# list1 = []
# count = 0
# list2 = []
# for i in stri:
#     if i != "-":
#         list1.append(i)
#     else:
#         list2.append(i)
#         count += 1
# print(list1)
# ans = stri.split("-")
# print(''.join(list2)+''.join(ans))

# stri = "apples"
# ch1 = "a"
# ch2 = "b"
# ans = stri.replace(ch1,ch2)
# print(ans)

# c = 1
# a = 12
# b = 16
# if c == 1:
#     print(a+b)
# elif c == 2:
#     print(a-b)
# elif c == 3:
#     print(a * b)
# elif c == 4:
#     print(a/b)

# m = 12
# n = 50
# sum = 0
# for i in range(m,n):
#     if i % 3 == 0 and i % 5 == 0:
#         sum = sum + i
# print(sum)

# n = 5
# sum = 0
# for i in range(1,10+1):
#     print(n*i,end=" ")
#     sum = sum + n * i
# print("\n",sum)

# n = 100
# m = 200
# for i in range(n,m+1):
#     if str(i) == str(i)[::-1]:
#         print(i,end=" ")

# import math
# x1 = 1
# y1 = 1
# x2 = 2
# y2 = 4
# x3 = 3
# y3 = 6
# print(math.sqrt((x2-x1)**2) + math.sqrt((y2-y1)**2))

# arr = [26,32,41,36]
# ip1 = 5
# ip2 = 5
# ip3 = 1
# ip4 = 4
# sum1 = ip1 * ip2 + ip3
# for i in range(ip4):
#     if sum1 == arr[i]:
#         print(i)


# ip = 7
# arr = [11,22,12,24,13,26,14]
# ip1 = 5
# for i in range(ip):
#     if i == 5:
#         ans = arr[i]
#         prev = arr[i-1]
#         fro = arr[i+1]
# print(abs(ans-prev) + abs(ans-fro))

# v,a,t = map(int,input().split())
# print(v,a,t)
# u = v - (a * t)
# print(u)

# n = 5
# str = "asdgufed"
# list1 = ['a','e','i','o','u']
# list2 = []
# for i in str:
#     if i not in list1:
#         list2.append(i)
# print(list2[-3])

# str = "vamsi"
# print(str[::-1])

# n = 5
# arr = [-2,1,-4,5,3]
# list1 = []
# max_ele = 0
# for i in range(len(arr)):
#     if arr[i] > max_ele:
#         max_ele = arr[i]
# min_ele = min(arr)
# print(max_ele+ min_ele)

# n = 6
# arr = [7,10,4,3,20,15]
# k = 3
# arr.sort()
# print(arr[k-1])

# n = 5
# arr = [0,2,1,2,0]
# count_0 = 0
# count_1 = 1
# count_2 = 2
# list1 = []
# for i in arr:
#     if i == 0:
#         list1.append(count_0)
# for i in arr:
#     if i == 1:
#         list1.append(count_1)
# for i in arr:
#     if i == 2:
#         list1.append(count_2)
# print(list1)

# arr = [2,-3,4,5,6,-7,8,9]
# list1 = []
# list2 = []
# for i in arr:
#     if i < 0 :
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list1+list2)

# arr1 = [1,2,3]
# arr2 = [2,3,4]
# arr1 = set(arr1)
# arr2 = set(arr2)
# print(arr1.union(arr2))
# print(arr1.intersection(arr2))

# n = 5
# arr = [1,2,3,4,5]
# k = 1
# print(arr[-k:] + arr[:-k])


# n = 5
# arr = [1,2,3,-2,5]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i,len(arr)+1):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_val = max(values)
#         ind = values.index(max_val)
# print(keys,values)
# print(max_val,"index of max value is:-",keys[ind])
# # print(dict1)


# arr = [3,9,12,16,20]
# arr.sort()
# k = 3
# n = 5
# smallest = arr[0] + k
# largest = arr[n-1] - k
# diff = arr[n-1] - arr[0]
# for i in range(1,n):
#     if arr[i]-k<0:
#         continue
#     mini = min(smallest,arr[i]-k)
#     maxi = max(largest,arr[i-1]+k)
#     diff = min(diff,maxi-mini)
# print(diff)

# arr = [1,3,4,2,2]
# count = 0
# list1 = []
# for i in arr:
#     ans = arr.count(i)
#     if ans > 1  and i not in list1:
#         list1.append(i)
# print(list1[0])

# n = 4
# arr = [1,3,5,7]
# m = 5
# arr1 = [0,2,6,8,9]
# arr2 = arr + arr1
# ans = sorted(arr2)
# print(ans)
# ans1 = ans[:n]
# ans2 = ans[n:]
# print(ans1,ans2)

# inter = [[1,3],[2,6],[8,10],[15,18]]
# list1 = []
# inter.sort()
# print(inter)
# for [x,y] in inter:
#     if not list1 or list1[-1][1] < x:
#         list1.append([x,y])
#     elif list1[-1][1] < y :
#         list1[-1][1] = y
# print(list1)


# arr = [2,3,4,5,6]
# count = 0
# for i in range(len(arr)-1):
#     if arr[i] < arr[i+1]:
#         count += 1
# print(count)

# arr = [7,6,4,3,1]
# min_val = min(arr)
# ind = arr.index(min_val)
# max_val = 0
# if min_val == arr[-1]:
#     print(0)
# else:
#     for i in arr[ind+1:]:
#         if i > max_val :
#             max_val = i
#     print(max_val-min_val)

# n = 4
# k = 6
# arr = [1,5,7,1]
# dict1 = {}
# count = 0
# for i in range(len(arr)):
#     diff = k - arr[i]
#     if diff in dict1:
#         count = count + dict1[diff]
#     if arr[i] in dict1:
#         dict1[arr[i]] += 1
#     else:
#         dict1[arr[i]] = 1
# print(count)


# n1 = 6
# arr = [1,5,10,20,40,80]
# arr1 = [6,7,20,80,100]
# n2 = 5
# n3 = 8
# arr2 = [3,4,15,20,30,70,80,120]
# arr = set(arr)
# arr1 = set(arr1)
# arr2 = set(arr2)
# ans = arr.intersection(arr1)
# ans1 = ans.intersection(arr2)
# print(ans,ans1)

# arr = [2,8,-5,6,-1,-3]
# pos = []
# ans = []
# neg = []
# for i in arr:
#     if i < 0:
#         neg.append(i)
#     else:
#         pos.append(i)
# for i in range(len(pos)):
#     ans.append(pos[i])
#     ans.append(neg[i])
# print(ans)

# arr = [4,2,-3,1,6]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i,len(arr)+1):
#         if sum(arr[i:j]) == 0:
#             dict1[tuple(arr[i:j])] = sum(arr[i:j])
# print(dict1)

# n = 10
# ans  = 1
# for i in range(1,n+1):
#     ans = ans * i
# print(ans)

# import math
# arr = [6,-3,-10,0,2]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i,len(arr)+1):
#         dict1[tuple(arr[i:j])] = math.prod(arr[i:j])
#         values = list(dict1.values())
#         keys = list(dict1.keys())
#         max_val = max(values)
#         ind = values.index(max_val)
# print(max_val,keys[ind])
# print(dict1)

# n = 7
# arr = [2,1,9,4,5,3]
# count = 0
# for i in range(1,len(arr)):
#     if i in arr:
#         count += 1
#     else:
#         break
# print(count)

# arr = [2,2,9,2,6,3,2,2,2]
# k = 2
# n = 8
# x = n // k
# for i in arr:
#     if arr.count(i) >= 4:
#         print(i)
#         break
#     else:
#         print(0)
#         break

# def fun(a1,a2):
#     for i in a2:
#         if i in a1:
#             return "yes"
#         else:
#             return "no"
#             break
# a1 = [11,1,13,21,3,7]
# a2 = [11,3,1]
# print(fun(a1,a2))


# def fun(n,x,arr):
#     arr.sort()
#     for i in range(n):
#         l = i + 1
#         k = n - 1
#         while(l<k):
#             sum = arr[i] + arr[l] + arr[k]
#             if sum == x :
#                 return True
#             elif sum < x :
#                 l += 1
#             else:
#                 k -= 1
#     return False
# n = 6
# x = 13
# arr = [1,4,45,6,10,8]
# print(fun(n,x,arr))

# arr1 = [9,5,4,9]
# arr2 = [2,1,4]
# stri = ""
# stri1 = ""
# for i in arr1:
#     stri += str(i)
# print(stri)
# for i in arr2:
#     stri1 += str(i)
# print(stri1)
# print(int(stri) + int(stri1))

# arr = [1]
# if len(arr) == 1:
#     print(arr[0]+1)
# max_ele = max(arr)
# list1 = []
# for i in range(1,max_ele):
#     if i in arr:
#         list1.append(i)
#     else:
#         list1.append(i)
# list1.append(max_ele)
# print(list1)
# for i in list1:
#     if i not in arr:
#         print(i)/

# r = 7
# unit = 2
# n = 8 
# arr = [2,8,3,5,7,4,1,2]
# if len(arr) == 0:
#     print(-1)
# tot = r * unit
# sum = 0
# count = 0
# for i in arr:
#     sum = sum + i
#     count += 1
#     if sum >= tot:
#         break
# print(count)


# stri = "1C0C1C1A0B1"
# ans  = int(stri[0])
# for i in range(len(stri)) :
#     if stri[i].isalpha() and stri[i] == 'A':
#         ans &= int(stri[i+1])
#     elif stri[i].isalpha() and stri[i] == 'B':
#         ans |= int(stri[i+1])
#     elif stri[i].isalpha() and stri[i] == 'C':
#         ans ^= int(stri[i+1])
# print(ans)


# stri = "1C0C1C1A0B1"
# a = int(stri[0])
# i = 1
# while i < len(stri):
#     if stri[i] == "A":
#         a &= int(stri[i+1])
#     elif stri[i] == "B":
#         a |= int(stri[i+1])
#     if stri[i] == "C":
#         a ^= int(stri[i+1])
#     i += 2
# print(a)

# m = 12 
# n = 50
# sum = 0
# for i in range(1,n):
#     if i % 3 == 0 and i % 5 == 0:
#         sum = sum + i
# print(sum)

# stri = "1210"
# list1 = []
# for i in stri:
#     if i not in list1:
#         list1.append(i)
# print(len(list1))

# gar = 4
# ele = 3
# bikes = [6,5,14,11]
# cars = [8,7,10,13]
# trucks = [2,8,11,5]
# list1 = []
# sum = 0
# for i in range(gar):
#     sum = sum + bikes[i] * 100 + cars[i] * 250 + trucks[i] * 500
#     list1.append(sum)
#     sum = 0
# print(max(list1))

# arr = [3,2,11,7,6,5,6,7]
# list1 = []
# a = arr[0]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i] > arr[j] :
#             list1.append(arr[j])
#             break
#         elif arr[i] < arr[j] :
#             list1.append(-1)
#             break
# list1.append(-1)
# print(list1)

# n = 67
# list1 = []
# k = 8
# for i in range(1,n+8):
#     if i % k == 0 :
#         list1.append(i)
# print(list1)
# if n - list1[-1] < list1[-2] - n:
#     print(list1[-2])
# else:
#     print(list1[-1])


# arr = [-1,0,1,2,-1,-4]
# dict1={}
# ans = 0
# for i in range(len(arr)):
#     for j in range(i,len(arr)+1):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
#     keys = list(dict1.keys())
#     values = list(dict1.values())
#     list1 = []
#     for i in range(len(values)):
#         if values[i] == 0:
#             list1.append(i)
# print(list1)
# for i in range(len(keys)):
#     if i in list1:
#         print(keys[i])


# import math
# arr = [1,2,3,4,5]
# list1 = []
# if len(arr) % 2 == 0:
#     mid = len(arr) // 2
#     list1.append(arr[mid-1])
#     list1.append(arr[mid])
#     ans = sum(list1) / 2
#     print(ans)
# else:
#     mid = len(arr) // 2
#     print(arr[mid])

# nums = [3,2,2,3]
# list1 = nums
# val = 3
# nums.clear()
# for i in list1:
#     print(i)
#     if i != val:
#         nums.append(i)
# print(nums)  

# n = 4
# for i in range(n-1,-1,-1):
#     print(i)

# arr = [1,2,2]
# print([1] + arr)

# digits = [1,2,3,4]
# n = len(digits)
# for i in range(n-1,-1,-1):
#     if digits[i] < 9:
#         digits[i] += 1
#         print (digits)
#     digits[i] = 0
# print( [1] + digits)


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# list1 = []
# list2 = nums1
# print(list2)
# for i in range(m):
#     list1.append(list2[i])
#     nums1.remove(nums1[i])
#     print(list1)
#     print(list2)
#     print(nums1)
# for j in range(n):
#     list1.append(nums2[j])
#     list1.sort()
# print(list1)
# print(nums1)
        

# nums = [2,14,18,22,22]
# for i in nums:
#     ans = nums.count(i)
#     if ans > 1:
#         print (True)
#     else:
#         print (False)


# nums1 = [3,1,2]
# nums2 = [1,1]
# dict1 = {}
# for i in nums1:
#     if i not in dict1:
#         dict1[i] = 1
#         print(dict1)
#     else:
#         dict1[i] += 1
#         print(dict1)
# ans = []
# for i in nums2:
#     if i in dict1 and dict1[i] > 0:
#         ans.append(i)
#         dict1[i] -= 1
# print(ans)

# dict1 = {}
# for i in range(len(nums)):
#     for j in range(i,len(nums)+1):
#         dict1[tuple(nums[i:j])] = sum (nums[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_val = max(values)
# if len(nums) == 1:
#     return nums[0]
# for i in nums:
#             if i == 0:
#                 for i in values:
#                     if i == 0:
#                         values.remove(0)
#                 return max(values)
#             else:
#                 return max(values)

# arr = "Abcd"
# n = len(arr)
# ans = ""
# for i in range(n-1,-1,-1):
#     ans += arr[i]
# print(ans)

# list1 = [1,2,3,4,5,6,6,7,7,4]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i],end=" ")

# s = "madam"
# ans = s[::-1]
# print(ans)
# if s == ans:
#     print("avunu ra lucha")
# else:
#     print("kadu ra babu")

# def king(n,s):
#     for i in range(n):
#         print(s)
# king(3,"sai")
# king(4,"vamsoi")

# def pora(nenu,ranu):
#     print("nenu raanu ra bot ga pora")
#     print(ranu * nenu)
# pora(2,"king")
# pora(2,"bot")

# def king():
#     print("prabbhs")
#     return "endi macha edi"
# macha = king()
# print(macha)

# def table(n):
#     for i in range(1,11):
#         print(n,'*',i,'=',i * n)
# table(98)

# stri = "hello"
# list1 = []
# for i in stri:
#     list1.append(ord(i))
# print(list1)
# ans = 0
# king = 0
# for i in range(len(list1)-1):
#     ans = abs(list1[i] - list1[i+1])
#     king = king + ans 
# print(king)

# address = "255.100.50.0"
# ans = ""
# for i in address:
#     if i == ".":
#         ans += "[.]"
#     else:
#         ans += i
# print(ans)

# jewels = "z"
# stones = "ZZzzzz"
# count = 0
# for i in jewels:
#     ans = stones.count(i)
#     count += ans
# print(count)
# for i in range(len(jewels)):
#     for j in range(len(stones)):
#         if jewels[i] == stones[j]:
#             count += 1
# print(count)

# list1 = [5,8,10,11,50,15,20,25]
# max_val = 0
# for i in list1:
#     if max_val < i:
#         max_val = i
# print(max_val)

# li = [[1,2,3],[2,0,8],[0,9,3],[1,1,1]]
# for i in li:
#     for j in i:
#         print(j,end=" ")
# for i in li[2]:
#     print(i,end=" ")
# for i in range(len(li)):
#     print(li[i][2])
# for i in range(len(li[0])):
#     print(li[0][i])

# n = 5
# for i in range(n):#0,1,2,
#     for j in range(n):#0,1,2  0,1,2  0,1,2
#         print("*",end="  ")
        # if j != n-1:
        #     print(" ",end="")
    # print()/


# r = 3
# c = 20
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j != c-1:
#             print("_",end=" ")
#     print()

# r = 20
# c = 3
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j != c-1:
#             print("_",end="")
#     print()

# r = 6
# c = 6
# for i in range(r):
#     for j in range(c):
#         if i == 0 or i == c-1:
#             print("*",end=" ")
#         if i > 0 and i < c - 1:
#             if j > 0 and j < c - 1:
#                 print(" ",end= " ")
#             else:
#                 print("*",end=" ")
#     print()

# r = 5
# c = 5
# for i in range(r):
#     for j in range(c):
#         if i == 0 or i == r - 1 or j == 0 or j == c - 1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# r = 4
# c = 20
# for i in range(r):
#     for j in range(c):
#         if i == 0 or i == r - 1 or j == 0 or j == c-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# r = 4
# c = 4
# for i in range(r):
#     for j in range(i,c):
#         print(" ",end=" ")
#     for k in range(c):
#         print("*",end=" ")
#     print()

# c = 4
# r  = 4
# for i in range(r):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(c):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end = " ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end = " ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i*2+1):
#         if j == 0  or i == n-1 or j == i *2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 6
# for i in range(n-1,-1,-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i*2+1):
#         if j == 0  or i == n-1 or j == i *2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 6
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i*2+1):
#         if j == 0  or i == n-1 or j == i *2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(n-1,-1,-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i*2+1):
#         if j == 0  or j == i *2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(i-j+1,"",end= "")
#     for j in range(i):
#         print(j+2,end=" ")
#     print()

# arr = [1,2,3,4,5,5]
# min_val = min(arr)
# ind = arr.index(min_val)
# max_val = 0
# for i in arr[ind+1:]:
#     if i > max_val:
#         max_val = i
# if max_val == 0:
#     print(0)
# else:
#     print(max_val - min_val)

# nums = [9,4,3,2]
# min_val = min(nums)
# ind = nums.index(min_val)
# ans = 0 
# for i in nums[ind+1:]:
#     ans = max(ans,i)
# if ans == 0:
#     print(-1)
# else:print(ans-min_val)

# nums = [9,4,3,2]
# ans = -1
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i] < nums[j]:
#             ans = max(ans,(nums[j]-nums[i]))
# print(ans)
    
# nums = [1,2,3,4]
# low = nums[0]
# ans = -1
# for i in range(1,len(nums)):
#     if low < nums[i]:
#         temp = nums[i] - low
#         ans = max(ans,temp)
#     low = min(low,nums[i])
# print(ans)

# n = 5
# li = [i for i in range(n)]
# print(li) 

# colour = [1,8,3,8,3]
# ans = 0
# for i in range(len(colour)):
#     for j in range(i+1,len(colour)):
#         if colour[i] != colour[j]:
#             temp = j - i
#             ans = max(ans,temp)
# print(ans)

# colour = [4,1,3,4,5,4]
# ans = 0
# for i in range(len(colour)-1,-1,-1):
#     if colour[i]!= colour[0]:
#         temp = i
#         ans = max(ans,temp)
# for i in range(len(colour)+1,0):
#     if colour[len(colour)-1] != colour[i]:
#         temp = len(colour) -1 - i
#         ans = max(ans,temp)
# print(ans)
        
# arr = [17,18,5,3,6,1]
# list1 = []
# for i in range(len(arr)-1):
#     ans = float("-inf")
#     for j in range(i+1,len(arr)):
#         ans = max(ans,arr[j])
#     list1.append(ans)
# list1.append(-1)
# print(list1)

# arr = [17,18,5,3,6,1]
# list1 = []
# ans = float('-inf')
# for i in range(1,len(arr)):
#     temp = max(arr[i:])
#     list1.append(temp)
# list1.append(-1)
# print(list1)

# arr = [17,18,5,3,6,1]
# rmax = -1
# for i in range(len(arr)-1,-1,-1):
#     temp = arr[i]
#     arr[i] = rmax
#     rmax = max(temp,arr[i])
# print(arr)

# arr = list(int,input().split())
# n = 3
# li = []
# for i in range(n):
#     i = input()
#     li.append(i)
# print(li)
    
# li = list(map(int,input().split()))
# print(li)

# a = 4
# print(a)
# ans = "hello this is great"
# ans = ans.split()
# print(ans)
# ans = list(map(int,input().split()))
# print(ans)
# stri = "thop"
# stri = stri.split()
# print(stri)

# arr = [9,2,3,4,5]
# arr.sort()
# print(arr)
# a = 3
# b = 5
# temp = a
# a = b
# b = temp
# a,b = b,a
# print(a,b)

# arr = [20,2,3,4,5,1,100,0]
# j = 0
# for i in range(len(arr)-1):
#     if arr[j] > arr[j+1]:
#         arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)


# arr = [12,3,13,45,24,1,34,2,3,3,3,3,4,99]
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         arr[i],arr[i+1] = arr[i+1],arr[i]
# print(arr)


#bubble sort
# li = [1,2,3,7,4]
# for i in range(len(li)-1):
#     swap = False
#     for j in range(len(li)-i-1):
#         if li[j] > li[j+1]:
#             li[j],li[j+1] = li[j+1],li[j]
#             swap = True
#     print(li)
#     if(swap == False):
#         break
# print(li)


# li = [1,2,3,7,4]
# for i in range(len(li)-1):
#     swap = False
#     for j in range(len(li)-i-1):
#         if li[j] < li[j+1]:
#             li[j],li[j+1] = li[j+1],li[j]
#             swap = True
#     # print(li)
#     if(swap == False):
#         break
# print(li)

# li = [1,22,4,5,6]
# li.sort()
# ans = li[::-1]
# print(ans)

# arr = [1,5,8,0,1,8,1,5,1]
# dict1 = {}
# for i in arr:
#     dict1[i] = arr.count(i)
# print(dict1)
# for i in dict1:
#     print(i)
# if 5 in dict1:#only check for keys not for values
#     print("Yes")

# arr = [1,5,8,0,1,8,1,5,1]
# dici = {}
# for i in arr:
#     if i not in dici:
#         dici[i] = 1
#     else:
#         dici[i] = dici[i] + 1
# print(dici)

# arr = ["hello","bolo","hello","tata"]
# dici = {}
# for i in arr:
#     if i not in dici:
#         dici[i] = 1
#     else:
#         dici[i] = dici[i] + 1
# print(dici)
# for i in dici:
#     print(i,"->",dici[i])

# arr = [2,2,1,1,1,2,2]
# dict1 = {}
# for i in arr:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] = dict1[i] + 1
# max_val = 0
# temp = len(arr) // 2
# for i in dict1:
#     if dict1[i] > temp:
#         max_val = i
#         break
# print(max_val)

# arr = [2,2,1,1,1,2,2]
# arr1 = arr
# arr1 = set(arr1)
# arr1 = list(arr1)
# temp = len(arr) // 2
# ans = []
# for i in arr1:
#     a = arr.count(i)
#     ans.append(a)
# print(ans)
# max_val = max(ans)
# ind = ans.index(max_val)
# print(arr1[ind])

# arr =  [2,2,1,1,1,2,2]
# temp = len(arr) // 2
# arr.sort()
# print(arr[temp])

# nums = [1,2,3,1,1,3]
# count = 0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i] == nums[j] and i < j:
#             count += 1
# print(count)

# nums = [1,2,3,1,1,3]
# dict1 = {}
# for i in nums:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] = dict1[i] + 1
# print(dict1)
# a = 0
# ans1 = 0
# for i in dict1:
#     ans = dict1[i]
#     a = (ans-1) * ans // 2
#     ans1 += a
# print(ans1)
    

# arr = [1,1,1,1,1,1,11]
# leng = len(arr)
# ans = 0
# for i in range(1,leng):
#     ans += i
# print(ans)

# arr = [1,1,1,1,1,1]
# leng = len(arr)
# ans = leng * (leng - 1) // 2
# print(ans)

# jewels = "a"
# stones = "aAAbbbbbb"
# dict1 = {}
# for i in jewels:
#     dict1[i] = stones.count(i)
# print(dict1)
# ans = 0
# for i in dict1:
#     ans += dict1[i]
# print(ans)

#time complexity:- O(n)+O(k),O(n)

# key = "the quick brown fox jumps over the lazy dog"
# msg = "vkbs bs t suepuv"
# alp = {}
# a = 97
# for i in key:
#     if i not in alp and i != " ":
#         alp[i] = chr(a)
#         a += 1
# print(alp)
# for i in msg:
#     if i in alp:
#         print(alp[i],end="")
#     else:
#         print(" ",end="")

# s = "egg"
# t = "add"
# dici = {}
# dici2 = {}
# for i in range(len(s)):
#     dici[s[i]] = t[i]
# for i in range(len(s)):
#     dici2[t[i]] = s[i]
# print(dici)
# print(dici2)
# ans = ""
# ans1 = ""
# for i in s:
#     if i  in dici:
#         ans += dici[i]
# print(ans)
# for i in t:
#     if i  in dici2:
#         ans1 += dici2[i]
# print(ans1)
# if ans == t and ans1 == s:
#     return True
# return False

# nums = [1,1]
# misiing = -1
# duplicate = -1
# s = set()
# for i in nums:
#     val = i
#     if val not in s:
#         s.add(val)
#     else:
#         duplicate = val
# for i in range(1,max(s)+2):
#     if i not in s:
#         misiing = i
#         break
# print([duplicate,misiing])

# arr = [1,2,3,4]
# ans = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         a = arr[i:j+1]
#         ans.append(a)
        # temp = []
        # for k in range(i,j+1):
        #     temp.append(arr[k])
        # ans.append(temp)
# print(ans)


# arr = "saivamsi"
# ans = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         a = arr[i:j+1]
#         ans.append(a)
# print(ans)

# arr = [5,9,1,8,7,8,7,4,5]
# li = []
# for i in range(len(arr)):
# 	for j in range(i,len(arr)):
# 		if len(arr[i:j]) == 3:
# 			ans = sum(arr[i:j])
# 			li.append(ans)
# print(max(li))

#sliding window or two pointer problems     
# arr = [5,9,1,8,7]
# n = len(arr)
# l = 0
# temp = 0
# ans = 0
# for i in range(n):
# 	temp += arr[i]
# 	if i - l == 3:
# 		temp -= arr[l]
# 		l += 1
# 	if i - l + 1 == 3:
# 		ans = max(ans,temp)
# print(ans)


# s = "aababcabc"
# li = []
# for i in range(len(s)):
# 	for j in range(i,len(s)+1):
# 		if len(s[i:j]) == 3:
# 			ans = s[i:j]
# 			if len(set(ans)) == 3:
# 				li.append(ans)
# print(len(li))

# s = "aababcabc"
# ans = 0
# for i in range(len(s)):
# 	for j in range(i,len(s)):
# 		li =[]
# 		for k in range(i,j+1):
# 			li.append(s[k])
# 		if len(li) == 3 and len(set(li)) == 3:
# 			ans += 1
# print(ans)

# s = "aababcabc"
# l = 0
# dict1 = {}
# ans = 0
# for i in range(len(s)):
# 	if s[i] not in dict1:
# 		dict1[s[i]] = 1
# 	else:
# 		dict1[s[i]] += 1
# 	if (i - l) == 3:
# 		dict1[s[l]] -= 1
# 		if dict1[s[l]] == 0:
# 			dict1.pop(s[l])
# 		l += 1
# 	if len(dict1)== 3:
# 		ans += 1
# print(ans)

# s = "aababcabc"
# l = 0
# temp = []
# ans = 0
# for i in range(len(s)):
#     temp.append(s[i])
#     if (i - l) == 3:
#         temp.remove(s[l])
#         l += 1
#     if len(temp) == 3 and len(set(temp)) == 3:
#         ans += 1
# print(ans)

# nums = [9,4,1,7]
# nums.sort()
# l = 0
# li = []
# ans = float("inf")
# k = 2
# for i in range(len(nums)):
# 	if i - l == k:
# 		l += 1
# 	if i - l + 1 == k:
# 		ans = min(ans,nums[i] - nums[l])
# print(ans)

# nums = [9,4,1,7]
# nums.sort()
# k = 2
# ans = float("inf")
# for i in range(len(nums)):
# 	for j in range(i,len(nums)):
# 		temp = []
# 		for k in range(i,j+1):
# 			temp.append(nums[k])
# 		if len(temp) == 2:
# 			last = temp[-1]
# 			first = temp[0]
# 			ans = min(ans,last - first)
# print(ans)

# nums = [1,2,3,4,9]
# nums.sort()
# ans = 0
# for i in range(0,len(nums),2):
# 	print(i)
# 	ans += nums[i]
# print(ans)

# cost = [3,3,3,1]
# cost.sort()
# print(cost)
# l = 0
# ans = 0
# for i in range(len(cost)-1,-1,-1):
# 	if l == 2:
# 		l = 0
# 	else:
# 		ans += cost[i]
# 		l += 1
# print(ans)
# 11,13,17,23,29,31,7,5,2,3
# arr = [2,2,2,2,5,5,5,8]
# k = 3
# thre = 4
# ans = []
# a = 0
# for i in range(len(arr)):
# 	for j in range(i,len(arr)):
# 		temp = []
# 		for m in range(i,j+1):
# 			temp.append(arr[m])
# 		if len(temp) == k and (sum(temp) / len(temp)) >= thre :
# 			print(temp)
# 			a += 1
# print(a)

# arr = [11,13,17,23,29,31,7,5,2,3]
# l = 0
# k = 3
# thre = 5
# li = []
# n = len(arr)
# a = 0
# for i in range(n):
# 	li.append(arr[i])
# 	if i - l == k:
# 		li.remove(arr[l])
# 		l += 1
# 	if len(li) == k and (sum(li)/len(li)) >= thre :
# 		print(li)
# 		a+= 1
# print(a)

# li = [9,3,4,8,1]
# l = 0 
# ans = 0
# k = 3
# temp = 0
# for i in range(len(li)):
# 	temp += li[i]
# 	if (i - l )== k :
# 		temp -= li[l]
# 		l += 1
# 	if i - l + 1 == k:
# 		print(temp)
# 		ans = max(ans,temp)
# print(ans)

# arr = [9,3,4,8,1,4,2,2,3,5,7,2,5,2,2,2]
# temp = 0
# l = 0
# ans = 0
# k = 13
# n = len(arr)
# for i in range(n):
# 	temp += arr[i]

# 	while temp > k: 
# 		temp -= arr[l]
# 		l += 1 

# 	print(arr[l:i+1],sum(arr[l:i+1]))

# 	ans = max(ans,i-l+1)
# print(ans)


# arr = [0,1,3,1,1,6,7,1,0,1]
# k = 2
# l = 0
# temp = 0
# ans = 0
# n = len(arr)
# for i in range(n):
# 	if arr[i] == 1:
# 		temp += 1

# 	while  temp > k:
# 		if arr[l] == 1: 
# 			temp -= 1
# 		l += 1

# 	print(arr[l:i+1])
# 	ans = max(ans,i-l+1)
# print(ans)

# arr = [12,1,3,1,1,6,7,1,8,1]
# k = 2
# l = 0
# temp =0
# ans = 0
# n = len(arr)
# for i in range(n):
# 	if arr[i] % 2 != 0:
# 		temp += 1

# 	while temp > k:
# 		if arr[l] % 2 != 0:
# 			temp -= 1
# 		l += 1
# 	print(arr[l:i+1])
# 	ans = max(ans,i - l + 1)
# print(ans)


# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# l = 0
# ans = 0
# temp = 0
# n = len(nums)
# k = 3
# for i in range(n):
# 	if nums[i] == 0:
# 		temp += 1
	
# 	while temp > k:
# 		if nums[l] == 0:
# 			temp -= 1
# 		l += 1

# 	print(nums[l:i+1])
# 	ans = max(ans,i-l+1)
# print(ans)


# nums = [0,1,1,1,0,1,1,0]
# l = 0
# ans = 0
# n = len(nums)
# k = 2
# ones = 0
# zero = 0
# for i in range(n):
# 	if nums[i] == 0:
# 		zero += 1
# 	else:
# 		ones += 1

# 	while min(ones,zero) > k:
# 		if nums[l] == 0:
# 			zero -= 1
# 		else:
# 			ones -= 1
# 		l += 1

# 	ans = max(ans,i-l+1)
# print(ans)

# answer = "TTFTTFTT"
# k = 1
# l = 0
# ans = 0
# cnt = 0
# cnt1 = 0
# n = len(answer)
# for i in range(n):
# 	if answer[i] == "T":
# 		cnt += 1
# 	else:
# 		cnt1 += 1
	
# 	while min(cnt,cnt1) > k:
# 		if answer[l] == "T":
# 			cnt -= 1
# 		else:
# 			cnt1 -= 1
# 		l += 1

# 	ans = max(ans,i - l + 1)
# print(ans)


# s = "pwwkew"
# l = 0
# n = len(s)
# li = set()
# ans = 0
# for i in range(n):
# 	if s[i] not in li:
# 		li.add(s[i])
# 	else:
# 		while s[i] in li:
# 			li.remove(s[l])
# 			l+= 1
# 		li.add(s[i])
# 	ans = max(ans,i-l+1)
# print(ans)

# s = "pwwkew"
# ans = 0
# temp = ""
# for i in range(len(s)):
# 	while s[i] in temp:
# 		temp = temp[1:]
# 	temp += s[i]
# 	print(temp)
# 	ans = max(ans,len(temp))
# print(ans)

# fruits = [1,2,3,2,2]
# temp = {}
# ans = 0
# l = 0
# count = 0
# n = len(fruits)
# for i in range(n):
# 	if fruits[i] not in temp:
# 		temp[fruits[i]] = 1
# 		count += 1
# 	else:
# 		temp[fruits[i]] += 1
# 	while len(temp) > 2:
# 		temp[fruits[l]] -= 1
# 		if temp[fruits[l]] == 0:
# 			temp.pop(fruits[l])
# 		l += 1
# 	ans = max(ans,i-l+1)
# print(ans)

# def fun(dici1,dici2):
# 	if len(dici1) != len(dici2):
# 		return False
# 	for i in dici1:
# 		if i not in dici2 or dici1[i] != dici2[i]:
# 			return False
# 	return True

# str1 = "sai"
# str2 = "sai"
# dici1 = {}
# dici2 = {}
# for i in range(len(str1)):
# 	if str1[i] not in dici1:
# 		dici1[str1[i]] = 1
# 	else:
# 		dici1[str1[i]] += 1
# for i in range(len(str2)):
# 	if str2[i] not in dici2:
# 		dici2[str2[i]] = 1
# 	else:
# 		dici2[str2[i]] += 1
# print(fun(dici1,dici2))


# def fun(dict1,dict2):
# 	if len(dict1) != len(dict2):
# 		return False
# 	for i in dict1:
# 		if i not in dict2 or dict1[i] != dict2[i]:
# 			return False
# 	return True

# s = "cbaebabacd"
# p = "abc"
# dict1={}
# dict2 ={}
# for k in p:
# 	if k not in dict2:
# 		dict2[k] = 1
# 	else:
# 		dict2[k] += 1
# l = 0
# ans = []
# n = len(p)	
# for i in range(len(s)):
# 	if s[i] not in dict1:
# 		dict1[s[i]] = 1
# 	else:
# 		dict1[s[i]] += 1
# 	if i - l == n:
# 		dict1[s[l]] -= 1
# 		if dict1[s[l]] == 0 :
# 			dict1.pop(s[l])
# 		l+= 1
# 	if i - l + 1 == n:
# 		if fun(dict1, dict2):
# 			ans.append(l)
# print(ans)



# s = "abab"
# p = "ab"
# ans = []
# count = 0
# for i in range(len(s)):
# 	for j in range(i,len(s)):
# 		temp = ""
# 		for k in range(i,j+1):
# 			temp += s[k]
# 		if sorted(p) == sorted(temp):
# 			ans.append(i)
# print(ans)

# nums = [2,3,1,2,4,3]
# target = 7
# if sum(nums) < target:
# 	print(0)
# l = 0
# ans = float("inf")
# temp = 0
# for i in range(len(nums)):
# 	temp += nums[i]
# 	while temp >= target:
# 		ans = min(ans,i-l+1)
# 		temp -= nums[l]
# 		l+= 1
# print(ans)
	
# arr = [1,3,4,5,7]
# temp = 0
# ans = 0
# l = 0
# k = 2
# ans1 = 0
# for i in range(len(arr)):
# 	if arr[i] % 2 == 1:
# 		temp += 1
# 	while temp > k:
# 		if arr[l] % 2 == 1:
# 			temp -= 1
# 		l += 1
# 	ans1 +=len(arr[l:i+1]) 
# 	ans = max(ans,i - l + 1)
# print(ans,ans1)

# def fun(nums,k):
# 	ans = 0
# 	temp= 0
# 	l = 0
# 	ans1 = 0
# 	n = len(nums)
# 	for i in range(len(nums)):
# 		if nums[i] % 2 != 0:
# 			temp += 1
# 		while temp > k :
# 			temp -= 1
# 			l+= 1
# 		print(nums[l:i+1])
# 		ans1 +=len(nums[l:i+1]) 
# 		ans = max(ans,i - l + 1)
# 	return ans1
# nums = [1,1,2,1,1]
# k = 3
# print(fun(nums,k) - fun(nums,k-1))

# def fun(nums,goal):
# 	if goal < 0:
# 		return 0
# 	l = 0
# 	ans = 0
# 	temp = 0
# 	for i in range(len(nums)):
# 		if nums[i] == 1:
# 			temp += 1
# 		while temp > goal:
# 			if nums[l] == 1:
# 				temp -= 1
# 			l += 1
# 		ans += i -l + 1
# 	return ans
# nums = [0,0,0,0,0]
# goal = 2
# if goal > 0:
# 	a = fun(nums,goal)
# 	b = fun(nums,goal-1)
# 	print(a- b)
# else:
# 	print(fun(nums,goal))


# def fun(nums,k):
# 	l = 0
# 	ans = 0
# 	temp = 0
# 	te = {}
# 	ans1 = 0
# 	for i in range(len(nums)):
# 		if nums[i] not in te:
# 			te[nums[i]] =  1
# 		else:
# 			te[nums[i]] +=  1

# 		while len(te) > k:
# 			te[nums[l]] -= 1
# 			if te[nums[l]] == 0:
# 				te.pop(nums[l])
# 			l += 1
# 		ans +=i-l+1
# 	return ans
# nums = [1,2,1,2,3]
# k = 2
# print(fun(nums,k) - fun(nums,k-1))

# p = "abab"
# s = "dog cat cat dog"
# s = s.split(" ")
# print(s)
# dict1 = {}
# dict2 = {}
# for i in p:
# 	if i not in dict1:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] += 1
# print(dict1)
# for i in s:
# 	if i not in dict2:
# 		dict2[i] = 1
# 	else:
# 		dict2[i] += 1
# print(dict2)
# if len(dict1) == len(dict2):
# 	list1 = list(dict1.values())
# 	list2 = list(dict2.values())
# 	if list1 == list2:
# 		print(True)
# 	else:
# 		print(False)
# else:
# 	print(False)


# p = "abba"
# s = "dog dog dog dog"
# pattern = p
# st = s
# s = s.split(" ")
# list1 = []
# for i in p:
# 	list1.append(i)
# l1,l2 = [],[]
# for i in list1:
# 	if i not in l1:
# 		l1.append(i)
# for i in s:
# 	if i not in l2:
# 		l2.append(i)
# i
# dict1= {}
# for i in range(len(l1)):
# 	dict1[l1[i]] = l2[i]
# list2 = []
# for i in list1:
# 	if i in dict1:
# 		list2.append(dict1[i])
# if list2 == s:
# 	print(True)
# else:
# 	print(False)

# s = "ab"
# t = "baab"
# list1 = []
# list2 = []
# for i in s:
# 	list1.append(i)
# for i in t:
# 	list2.append(i)
# print(list1,list2)
# list3 = []
# for i in list2:
# 	if i in list1 and i not in list3:
# 		list3.append(i)
# print(list3,list1)
# if len(list3) == len(list1) and list1 == list3:
# 	print(True)
# else:
# 	print(False)

# arr = [0,1,0,3,12]
# l = 0
# for i in range(len(arr)):
# 	if arr[i] != 0:
# 		arr[i],arr[l] = arr[l],arr[i]
# 		l += 1
# 	print(arr)

# s = ["h","e","l","l","o"]
# l = len(s)-1
# a = 0
# while a < l:
# 	temp = s[a]
# 	s[a] = s[l]
# 	s[l] = temp
# 	l -=1
# 	a += 1
# print(s)

# arr = [7,2,5,11,1]
# arr.sort()
# tar = 6
# l = len(arr)-1
# r = 0
# while True:
# 	if arr[r]+arr[l] > tar:
# 		l -= 1
# 	elif arr[r]+arr[l] < tar:
# 		r += 1
# 	print(arr[r],arr[l])
# 	break

# nums = [6,2,6,5,1,2]
# nums.sort()
# temp = 0
# for i in range(0,len(nums),2):
# 	temp += nums[i]
# print(temp)

# list1 = ["shogun","tapico express","burger king","paitai"]
# list2 = ["paitai","the girl","hungry hunter","shogun"]
# list3 = list1
# list4 = list2
# list1 = set(list1)
# list2 = set(list2)
# ans = list1.intersection(list2)
# if len(ans) > 1:
# 	l1 = []
# 	l2 = []
# 	for i in range(len(list3)):
# 		if list3[i] in ans:
# 			l1.append(i)
# 	for i in range(len(list4)):
# 		if list4[i] in ans:
# 			l2.append(i)
# 	print(l1,l2)
# 	for i in 
# else:
# 	print(ans)

# s = "cbbd"
# l = 0
# n = len(s)
# temp = []
# ans = []
# for i in range(n):
# 	for j in range(i,n):
# 		temp = ""
# 		for k in range(i,j+1):
# 			temp+=(s[k])
# 		if temp[::-1] == temp and len(temp)>1:
# 			ans.append(temp)
# print(ans[0])

# x = -15
# if x > 0:
# 	x = str(x)
# 	x = x[::-1]
# 	x = int(x)
# 	if x > (2**31) -1:
# 		print(0)
# 	else:
# 		print(x)
# else:
# 	x = str(x)
# 	y = x[1:]
# 	a = x[:1]
# 	y = y[::-1]
# 	ans = int(a+y)
# 	if ans > (2**31) -1:
# 		print(0)
# 	else:
# 		print(ans)

# nums=[1,2,4,5,3]
# tar = 4
# dict1 = {}
# for i,n in enumerate(nums):
# 	ans = tar - n
# 	if ans in dict1:
# 		print([dict1[ans],i])
# 	dict1[n] = i


# arr = [7,5,5,1,6,4]
# l = 0
# r = 1
# ans = 0
# while r < len(arr): #1,2,3,4,5
# 	if arr[l] < arr[r]: #7<1 no 1 < 5 yes 1 < 3 no 1 < 6 5 1< 4
# 		profit = arr[r] - arr[l] # 5 - 1 = 4
# 		ans = max(ans,profit) # 0,4 = 4
# 	else:
# 		l = r #l = 1
# 	r+=1 # r = 5,3
# print(ans)

# nums = [1,2,3,4,1]
# dict1 = {}
# for i in nums:
# 	if i not in dict1:
# 		dict1[i] = 1
# 	else:
# 		print(i)
# 		dict1[i] += 1
# print(dict1)

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# l = nums[0]
# temp = 0
# ans = 0
# for i in nums:
# 	if temp < 0:
# 		temp = 0
# 	temp += i
# 	ans = max(ans,temp)
# print(ans)

# nums = [-1,0,1,2,-1,-4]
# ans = 0
# temp = 0
# l = 0
# for i in range(len(nums)):
#     temp += nums[i]
#     while temp > 0:
#         temp -= nums[l]
#         l += 1
#     print(nums[l:i+1])
#     # print(temp)

# dict1 = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# dig = "23"
# list1 = []
# for i in dig:
#     i = int(i)
#     if i in dict1:
#         list1.append(dict1[i])
# print(list1)

# n = 1000000000001011101010100111
# ans = 0
# while n:
# 	ans += n % 2
# 	n = n >> 1
# print(ans)

# s = "abcabcbb"
# l = 0
# ans = 0
# temp = set()
# for r in range(len(s)):
# 	while s[r] in temp:
# 		temp.remove(s[l])
# 		l += 1
# 	temp.add(s[r])
# 	ans = max(ans,r-l+1)
# print(ans)

# from collections import defaultdict


# strs = ["eat","tea","tan","ate","nat","bat"]
# res = defaultdict(list)
# for i in strs:
# 	count = [0] * 26
# 	for j in i:
# 		count[ord(j)-ord("a")] += 1
	
# 	res[tuple(count)].append(i)
# print(res.values())

# s = "(){[]}"
# dict1 = {"}":"{","]":"[",")":"("}
# stack = []
# for i in s:
# 	if i in dict1:
# 		if stack and stack[-1] == dict1[i]:
# 			stack.pop()
# 			print(stack)
# 		else:
# 			print(False)
# 	else:
# 		stack.append(i)
# 		print(stack)
# print(True) if not stack else False


# nums = [2,7,15,35]
# tar = 9
# for i in range(len(nums)):
# 	for j in range(i,len(nums)):
# 		if nums[i] + nums[j] == tar:
# 			print([nums[i],nums[j]])

# s = "ant"
# t = "nat"
# if len(s) == len(t):
# 	print(False)
# dict1 = {}
# dict2 = {}
# for i in range(len(s)):
# 	dict1[s[i]] = 1 + dict1.get(s[i],0)
# 	dict2[t[i]] = 1 + dict2.get(t[i],0)
# for j in dict1:
# 	if dict1[j] != dict2.get(j,0):
# 		print(False)
# print(True)

# s = "sain"
# t = "ias"
# s= list(s)
# t = list(t)
# if len(s) != len(t):
# 	print(False)
# for i in range(len(s)):
# 	flag = 0
# 	for j in range(len(t)):
# 		if s[i] == t[j]:
# 			t.remove(t[j])
# 			s.remove(s[i])
# print(t)
# if len(t) == 0:
# 	print(True)
# else:
# 	print(False)

# s = "madam"
# t = "adamm"
# dict1 = {}
# for i in range(len(t)):
# 	if t[i] not in dict1:
# 		dict1[t[i]] = 1
# 	else:
# 		dict1[t[i]] += 1
# for i in range(len(s)):
# 	if s[i] not in dict1:
# 		print(False)
# 	else:
# 		dict1[s[i]] -= 1
# print(dict1)
# for i in dict1:
# 	if dict1[i] != 0:
# 		print(False)
# 	else:
# 		print(True)

# nums = [2,3,4,5]
# dict1 = {}
# for i in nums:
# 	if i not in dict1:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] += 1
# print(dict1)
# for i in dict1:
# 	if dict1[i] > 1:
# 		print(i)
# print(False)

# nums = [1,2,3,1]
# for i in range(len(nums)):
# 	for j in range(i+1,len(nums)):
# 		if nums[i] == nums[j]:
# 			print(nums[i])

# nums = [1,2,3,1]
# nums.sort()
# for i in range(len(nums)-1):
# 	if nums[i] == nums[i+1]:
# 		print(nums[i])

# nums= [1,2,3,1]
# s = set()
# for i in nums:
# 	if i not in s:
# 		s.add(i)
# 		print(s)
# 	else:
# 		print(i)

# nums= [7,12,2,9,5,6,23]
# tar = 15
# for i in range(len(nums)):
# 	for j in range(i,len(nums)):
# 		if nums[i] + nums[j] == tar:
# 			print([i,j])

# nums = [7,12,2,9,5,6,23]
# tar = 15
# l = 0 
# temp = 0
# ans = 0
# for i in range(len(nums)):
# 	temp += nums[i]
# 	while temp > tar:
# 		temp -= nums[l]
# 		l += 1
# 	print(temp)

# nums = [7,12,2,9,5,6,23]
# tar = 15
# nums.sort()
# l = 0
# r = len(nums) - 1
# while l < r:
# 	if nums[l] + nums[r] > tar:
# 		r -= 1
# 	elif nums[l] + nums[r] == tar:
# 		print([nums[l],nums[r]])
# 		break
# 	else:
# 		l += 1

# nums = [7,12,2,9,5,6,23]
# tar = 15
# dict1 = {}
# for i in range(len(nums)):
# 	ans = tar - nums[i]
# 	if ans in dict1:
# 		print([dict1[ans],dict1[i]])
# 	dict1[nums[i]] = i
# print(dict1)

# s = "sai"
# list1 = [0] * 26
# for i in s:
# 	ans = ord(i) - ord('a')
# 	list1.insert(ans,s.count(i))
# print(list1) 

# s = ["eat","tea","tan","ate","nat","bat"]
# list1 = []
# for i in range(len(s)):
# 	for j in range(i+1,len(s)):
# 		if sorted(s[i]) == sorted(s[j]):
# 			temp = s[i]
# 			list1.append([s[i],s[j]])
# print(list1)

# s = ["eat","tea","tan","ate","nat","bat"]
# dict1 = {}
# for i in s:
# 	ans = "".join(sorted(i))
# 	if ans in dict1:
# 		dict1[ans].append(ans)
# 		print(dict1)
# 	else:
# 		dict1[ans] = [i]
# val = list(dict1.values())
# print(val)

# nums = [2,1,3,3,2,5,7,2,7,3,5,3]
# k = 3
# dict1 = {}
# for i in nums:
# 	if i not in dict1:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] += 1
# print(dict1)
# list1 = []
# for i in dict1:
# 	if dict1[i] >= k:
# 		list1.append(i)
# print(list1)

# nums = [1,8,6,2,5,4,8,3,7]
# for i in range(len(nums)):
# 	for j in range(i,len(nums)):
# 		ans = min(nums[i],nums[j]) * (j-i)
# print(ans)


# def encode(ip):
# 	ans = ""
# 	list1 = []
# 	for i in ip:
# 		a = len(i)
# 		ans += str(a)
# 		ans += "#"
# 		ans += i
# 	return ans
# ip = ["neet","code","love","you"]
# encode(ip)
# def decode(ans):
# 	a = encode(ip)
# 	list1 = []
# 	ans = ""
# 	for i in range(len(a)):
# 		if a[i].isdigit() and a[i+1] =="#":
# 			ans += i
# 			list1.append(ans)
# 		ans = ""
# 	print(list1)
# a = encode(ip)
# decode(a)

# arr = [7,6,9,3,2,6,8,2,9]
# list1 = []
# ans = 0
# l = 1
# r = 3
# for i in range(len(arr)):
# 	ans += arr[i]
# 	list1.append(ans)
# print(list1)
# if l == 0:
# 	print(list1[r])
# else:
# 	print(list1[r] - list1[l-1])

# arr = [7,6,9,3,2,6,8,2,9]
# list1 = []
# ans = 1
# l = 1
# r = 3
# for i in range(len(arr)):
# 	ans *= arr[i]
# 	list1.append(ans)
# print(list1)
# if l == 0:
# 	print(list1[r])
# else:
# 	print(list1[r] // list1[l-1])

# arr = [1,2,-4,-1,3]
# ans = 1
# list1 = []
# for i in arr:
# 	ans *= i
# for i in arr:
# 	a = ans / i
# 	list1.append(int(a))
# print(list1)

# arr = [1,2,-4,-1,3]
# list1 = []
# ans = 1
# for i in range(len(arr)):
# 	l1 = arr[i+1:]
# 	l2 = arr[:i]
# 	for i in l1:
# 		ans *= i
# 	for k in l2:
# 		ans *= k
# 	list1.append(ans)
# 	ans = 1
# print(list1)

# arr = [1,2,-4,-1,3]
# pre,suf,out = [],[],[]
# pre[0] = arr[0]
# n = len(arr)
# for i in range(1,n):
# 	pre[i] = pre[i-1] * arr[i]
# suf[n-1] = arr[n-1]
# for i in range(n-2,0):
# 	suf[i] = suf[i+1] * arr[i]
# out[0] = suf[1]
# out[n-1] = pre[n-2]
# for i in range(1,n-1):
# 	out[i] = pre[i-1] * suf[i+1]
# print(out)


# s = "saivamsi"
# s = s[::-1]
# print(s)

# arr = [10,2,3,1,4,5]
# l1= []
# for i in range(len(arr)):
# 	list1 = arr[i+1:]
# 	list2 = arr[:i]
# 	for j in list1:
# 		if arr[i] % j == 0:
# 			l1.append(arr[i])
# 	for j in list2:
# 		if arr[i] % j == 0:
# 			l1.append(arr[i])
# l1 = set(l1)
# print(len(l1))

# arr = [-1,-2,-3,2]
# arr.sort()
# l1 = []
# print(arr)
# for i in range(len(arr)):
# 	if arr[i] > 0:
# 		l1.append(abs(arr[i-1]))
# 		l1.append(arr[i])
# 		break
# else:
# 	print(arr[-1])
# print(l1)
# if len(l1) > 1:
# 	print(l1)
# 	print(min(l1))

# arr = [1,2,3,5]
# l1 = []
# for i in range(len(arr)):
# 	a = arr[i+1:]
# 	b = arr[:i]
# 	ans = 1
# 	for i in a:
# 		ans *= i
# 	for j in b:
# 		ans *= j
# 	l1.append(ans)
# print(l1)

# arr = [100,5,102,76,3,4,99,2,101,1]
# dict1 = {}
# ans = 0
# for i in range(max(arr)):
# 	if i in arr:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] = 0
# count = 0
# for i in dict1:
# 	if dict1[i] == 1 :
# 		count += 1
# 	else:
# 		ans = max(ans,count)
# 		count = 0
# print(ans)

# arr = [100,5,102,76,3,4,99,2,101,1]
# arr.sort()
# count = 0
# ans = []
# for i in range(max(arr)):
# 	if i in arr:
# 		count += 1
# 	else:
# 		ans.append(count)
# 		count = 0
# print(max(ans))

# arr = [1,-1,1,-1,1,1,1,-1]
# ans = 0
# count = 0
# for i in arr:
# 	ans += i
# 	if ans == 0:
# 		count += 1
# print(count)

# arr = [10,20,30]
# a,b,c = 0,0,0
# for i in arr:
# 	ans = i % len(arr)
# 	if ans == 0:
# 		a += i / len(arr)
# 		b += i / len(arr)
# 		c += i / len(arr)
# 	elif ans == 1:
# 		a += (i / len(arr)) + 1
# 		b += i / len(arr)
# 		c += i / len(arr)
# 	elif ans == 2:
# 		a += (i / len(arr)) + 1
# 		b += (i / len(arr)) + 1
# 		c += i / len(arr)
# print(a,b,c)

# num = 10
# l1 = []
# for i in range(num):
# 	if i % 2 == 0:
# 		l1.append(i)
# for i in range(len(l1)):
# 	for j in range(i,len(l1)):
# 		if l1[i] + l1[j] == num:
# 			print("Yes")
# 			break
# else:
# 	print("No")

# s = "saivamsi"
# l1 = []
# for i in range(97,123):
# 	l1.append(chr(i))
# for i in l1:
# 	if i not in s:
# 		print(i,end="")

# i = 6
# while i > 5 and i < 10:
#     print(i)
#     i += 1


# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# for i in wordDict:
# 	if i in s:
# 		print(True)
# 	else:
# 		print(False)
# 		break

# arr = [-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]
# dict1  = set(arr)
# print(dict1)
# ans = 0
# for i in arr:
# 	if i - 1 in dict1:
# 		continue
# 	else:
# 		count = 1
# 		next = i+1
# 		while next in dict1:
# 			count += 1
# 			next += 1
# 		ans = max(ans,count)
# print(ans)


#contains duplicate
# {
# nums = [1,4,3,5,4]
# dict1 = set()
# for i in nums:
# 	if i not in dict1:
# 		dict1.add(i)
# 	else:
# 		print(True)
# 		break
# else:
# 	print(False)

# nums = [1,4,3,5,4]
# for i in range(len(nums)):
# 	for j in range(i+1,len(nums)):
# 		if nums[i] == nums[j]:
# 			print(nums[i])
# 			break
# else:
# 	print(False)

# nums = [1,2,3,3]
# nums.sort()
# for i in range(len(nums)):
# 	if nums[i] == nums[i+1]:
# 		print(True)
# 		break
# else:
# 	print(False)
# }


#valid anagrams
# {
# s = "cat"
# t = "tac"
# if sorted(s) == sorted(t):
# 	print(True)
# else:
# 	print(False)

# s = "cat"
# t = "tac"
# dict1 = {}
# for i in range(len(s)):
# 	if s[i] in dict1:
# 		dict1[s[i]] += 1
# 	else:
# 		dict1[s[i]] = 1
# for i in range(len(t)):
# 	if t[i] in dict1:
# 		dict1[t[i]] += 1
# 	else:
# 		dict1[t[i]] = 1
# print(dict1)
# for i in dict1:
# 	if dict1[i] != 2:
# 		print(False)
# 		break
# 	else:
# 		print(True)

# s = "s"
# t = "s"
# dict1 = {}
# dict2 = {}
# for i in s:
# 	if i not in dict1:
# 		dict1[i] = 1
# 	else:
# 		dict1[i] += 1
# for i in t:
# 	if i not in dict2:
# 		dict2[i] = 1
# 	else:
# 		dict2[i] += 1
# print(dict1,dict2)
# if dict1 == dict2:
# 	print(True)
# else:
# 	print(False)
# }

#Top k elements
# {

# arr = [1,3,4,3,4,2,3,4,2,5,4,5,5]
# k = 3
# dict1 = {}
# for i in range(len(arr)):
# 	if arr[i] not in dict1:
# 		dict1[arr[i]] = 1
# 	else:
# 		dict1[arr[i]] += 1
# print(dict1)
# list1 = list(dict1.values())
# list1.sort()
# print(list1)
# list2 = []
# list3= []
# for i in range(1,k+1):
# 	list2.append(list1[-i])
# for i in dict1:
# 	if dict1[i] in list2:
# 		list3.append(i)
# print(list3)


# nums = [1,2,3,4]
# ans = 1
# ans1 = 1
# list1 = []
# list2 = []
# for i in range(len(nums)):
# 	ans = nums[:i]
# 	for i in ans:
# 		ans1 *= i
# 	list1.append(ans1)
# 	ans1 = 1
# nums.reverse()
# for i in range(len(nums)):
# 	ans = nums[:i]
# 	for i in ans:
# 		ans1 *= i
# 	list2.append(ans1)
# 	ans1 = 1
# list2.reverse()
# l1 = []
# for i in range(len(list1)):
# 	ans = list1[i] * list2[i]
# 	l1.append(ans)
# print(l1)


# nums = [1,2,3,4]
# n = len(nums)
# res=[1]*n
# prefix=1
# for i in range(n):
# 	res[i] = prefix
# 	prefix *= nums[i]
# suffix=1
# for i in range(n-1,-1,-1):
# 	res[i] *= suffix
# 	print(res)
# 	suffix *= nums[i]
# print(res)

# }

#encode and decode string
# {
# s = ["ab","b","c","abc"]
# enc = ""
# for i in s:
# 	enc += i 
# 	enc += chr(257)
# print(enc)
# ans= ""
# li = []
# for i in enc:
# 	if i != chr(257):
# 		ans += i
# 	if i == chr(257):
# 		li.append(ans)
# 		ans = ""
# print(li)
# }

#Longest Consecutive sequence 
# {
# nums = [-1,-2,4]
# first = 0
# count = 0
# ans = 0
# nums = set(nums)
# nums = list(nums)
# nums.sort()
# print(nums)
# if len(nums) == 0:
# 	print(0)
# for i in range(len(nums)-1):
# 	if nums[i] + 1 == nums[i+1]:
# 		count += 1
# 		ans = max(ans,count)
# 	else:
# 		count = 0
# 		first += 1
# print(ans + 1)

# nums = [100,5,102,76,3,4,99,102,1,2]
# hash = set(nums)
# print(nums)
# count = 0
# ans = 0
# for i in range(len(nums)):
# 	if nums[i] - 1 in hash:
# 		continue
# 	else:
# 		count = 1
# 		next = nums[i] + 1
# 		while next in hash:
# 			count += 1
# 			next += 1
# 			ans = max(ans,count)
# print(ans)
# }

#valid palindrome
# {
# s = "A man, a plan,a canal: Panama"
# s = s.lower()
# ans = ""
# for i in s:
# 	if i.isalnum():
# 		ans += i
# print(ans)
# if ans[::-1] == ans:
# 	print(True)
# else:
# 	print(False)

# s = "A man, a plan,a canal: Panamla"
# l = 0 
# r = len(s) - 1
# while l < r:
# 	if not s[l].isalnum():
# 		l += 1
# 	elif not s[r].isalnum():
# 		r -= 1
# 	elif s[l].lower() == s[r].lower():
# 		l += 1
# 		r -= 1
# 	else:
# 		print(False)
# 		break
# print(True)

# }

#Two sum II - input array is sorted

# numbers = [-4,-2,-2,1,5,6,8,10]
# target = 7
# dict1 = {}
# for i in range(len(numbers)):
# 	ans = target - numbers[i]
# 	if ans not in dict1:
# 		dict1[numbers[i]] = 1
# 	else:
# 		print([numbers.index(ans)+1,i+1])
# 		break
# print(dict1)

#3sum
# nums = [-4,-2,0,-2,6,6,4,4,2]
# l1 = set()
# for i in range(len(nums)):
# 	for j in range(i+1,len(nums)-1):
# 		for k in range(j,len(nums)):
# 			if nums[i] + nums[j] + nums[k] == 0:
# 				ans = tuple(sorted([nums[i],nums[j],nums[k]]))
# 				l1.add(ans)
# print([list(i) for i in l1])

# nums = [-4,-2,-2,0,2,4,4,6,6]
# nums.sort()
# l1 = set()
# for i in range(len(nums)):#-4
# 	j = i+1 # - 2 ,-2,0,2
# 	k = len(nums) - 1 # 6 ,6,4,4,2
# 	if nums[i] > 0 : #-4 > 0 ,
# 		break
# 	rem = 0 - nums[i] # 0-(-4) = 4
# 	while j < k:
# 		sum = nums[j] + nums[k] # -2 + 6 = 4 , 0 + 4 = 4 2 + 4 = 6
# 		if sum == rem:
# 			ans = tuple(sorted([nums[i],nums[j],nums[k]])) # -4,-2,6, -4,0,4  -4,2,2
# 			l1.add(ans)
# 			j += 1
# 			k -=1
# 		elif sum > rem: #6 > 4 
# 			k -= 1
# 		else: 
# 			j+= 1
# print([list(i) for i in l1])

#contains most water

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# max_val = 0
# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         val = min(height[i],height[j])
#         ans = val * (j - i)
#         max_val = max(max_val,ans)
# print(max_val)

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# i = 0
# r = len(height) - 1
# max_val = 0
# while i < r:
# 	val = min(height[i],height[r])
# 	ans = val * (r - i)
# 	max_val = max(max_val,ans)
# 	if height[r] > height[i]:
# 		i += 1
# 	else:
# 		r -= 1
# print(max_val)

#tapping rain water
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# count = 0
# for i in range(len(height)):
#     if i > 0:
#     	l1 = max(height[:i])
#     	print(height[:i],l1)
#     else:
#         l1 = 0
#     if i < len(height) - 1:
#         l2 = max(height[i+1:])
#     else:
#         l2 = 0
#     le = min(l1,l2)
#     ans = le - height[i]
#     if ans > 0:
#         count += ans
# print(count)

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# lmax = []
# rmax = []
# count = 0
# for i in range(len(height)):
# 	l1 = height[:i+1]
# 	if len(l1)==0:
# 		ans = 0
# 	else:
# 		ans = max(l1)
# 		lmax.append(ans)
# 	l2 = height[i:]
# 	if len(l2) == 0:
# 		ans1 = 0
# 	else:
# 		ans1 = max(l2)
# 		rmax.append(ans1)
# print(lmax,rmax)
# for i in range(len(height)):
#     ans = min(lmax[i],rmax[i]) 
#     if ans > height[i]:
#         count += (ans - height[i])
# print(count)

# height = [5,5,1,7,1,1,5,2,7,6]
# lmax = height[0]
# tot = 0
# i = 0
# j = len(height) - 1
# rmax = height[len(height) - 1]
# while i < j:
# 	if height[i] <= height[j]:
# 		lmax = max(lmax,height[i])
# 		if (lmax - height[i]) > 0:
# 			tot += (lmax-height[i])
# 		i += 1
# 	else:
# 		rmax = max(rmax,height[j])
# 		if (rmax - height[j]) > 0:
# 			tot += (rmax - height[j])
# 		j -= 1
# print(tot)

#Best time to buy and sell stocks
# prices = [7,1,5,3,6,4]
# ans = 0
# for i in range(len(prices)):
# 	for j in range(i+1,len(prices)):
# 		if prices[i] < prices[j]:
# 			val = prices[j] - prices[i]
# 			ans = max(ans,val)
# print(ans)

# prices = [2,1,4]
# l = prices[0]
# val = 0
# for i in range(len(prices)):
# 	if prices[i] < l:
# 		l = prices[i]
# 	val = max(val,prices[i]-l)
# print(val)

#Longet substring without repeating character

# s = "abcabcbb"
# val = 0
# for i in range(0,len(s)):
# 	for j in range(i,len(s)):
# 		ans = set()
# 		flag = True
# 		for k in range(i,j+1):
# 			if s[k] in ans:
# 				flag = False
# 				break
# 			ans.add(s[k])
# 		if flag == True:
# 			val = max(val,j-i+1)
# print(val)

# s = "abcabcbb"
# l = 0
# ans = set()
# temp = 0
# for i in range(len(s)):
# 	while s[i] in ans:
# 		ans.remove(s[l])
# 		l += 1
# 	ans.add(s[i])
# 	temp = max(temp,len(ans))
# print(temp)

#Longet repeating character replacement

# s= "ABAACC"
# k = 1 
# ans = 0
# for i in range(0,len(s)):
# 	for j in range(i,len(s)):
# 		dict1 = {}
# 		for k in range(i,j+1):
# 			if s[k] not in dict1:
# 				dict1[s[k]] = 1
# 			else:
# 				dict1[s[k]] += 1
# 		max_ele = 0
# 		for m in dict1:
# 			if dict1[m] > max_ele:
# 				max_ele = dict1[m]
# 		if (j+1-i) - max_ele < k and (j+1-i) > max_ele:
# 			print(s[i:j+1])
# 			ans = j + 1 - i
# print(ans)

# s = "AABABBA"
# l = 0
# k = 1
# ans = 0
# dict1 = {}
# max_ele = 0
# for i in range(len(s)):

# 	dict1[s[i]] = 1 + dict1.get(s[i],0)
# 	max_ele = max(max_ele,dict1[s[i]])
	
# 	if (i - l + 1) - max_ele > k:
# 		dict1[s[l]] -= 1
# 		l += 1

# 	ans = max(ans,i - l + 1)
# print(ans)

#permutation in string
# from itertools import permutations
# s1 = "ab"
# s2 = "eidbaooo"
# l1 = []
# a = permutations(s1)
# for i in list(a):
#     l1.append(i)
# print(l1)
# for i in range(len(s2)):
#     for j in range(i+1,len(s2)):
#         print(list(s2[i:j]))
#         if s2[i:j] in l1:
#             print(True)
# print(False)

# s1 = "a"
# s2 = "ab"
# dict1 = {}
# for i in s1:
#     dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# for i in range(len(s2)):
#     for j in range(i,len(s2)):
#         dict2 = {}
#         for k in range(i,j+1):
#             dict2[s2[k]] = 1 + dict2.get(s2[k],0)
#         print(dict2)
#         if dict1 == dict2:
#             print(True)
# print(False)

# s1 = "ab"
# s2 = "eidbaooo"
# if len(s1) > len(s2):
#     print(False)
# l1 = [0] * 26
# l2 = [0] * 26
# for i in range(len(s1)):
#     l1[ord(s1[i]) - ord('a')] += 1
#     l2[ord(s1[i]) - ord('a')] += 1
# matches = 0
# for i in range(26):
#     matches += 1 if l1[i] == l2[i] else 0
# l = 0
# for r in range(len(s1),len(s2)):
#     if matches == 26: print(True)

#     index = ord(s2[r]) - ord('a')
#     l2[index] += 1
#     if l1[index] == l2[index]:
#         matches += 1
#     elif s1[index] + 1 == s

#minimum window substring
# s = "ADOBECODEBANC"
# t = "ABC"
# dict1 = {}
# for i in t:
# 	dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# for i in range(len(s)):
# 	for j in range(i,len(s)):
# 		l1 = ""
# 		dict2 = {}
# 		for k in range(i,j+1):
# 			l1 += s[k]
# 		for i in range(len(l1)):
# 			dict2[l1[i]] = 1 + dict2.get(l1[i],0)
# 		print(dict2)

#maximum sliding window
# nums = [1,3,-1,-3,5,3,6,7]
# l1 = []
# for i in range(len(nums)):
# 	for j in range(i,len(nums)):
# 		temp = []
# 		for k in range(i,j+1):
# 			temp.append(nums[k])
# 		l1.append(temp)
# k = 3
# l2 = []
# for i in l1:
# 	if len(i) == k:
# 		l2.append(max(i))
# print(l2)

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# l = 0
# l1 = []
# s = []
# for i in range(len(nums)):
# 	l1.append(nums[i])
# 	while len(l1) > k:
# 		l1.remove(nums[l])
# 		l += 1
# 	if len(nums[l:i+1]) == k:
# 		s.append(max(l1))
# print(s)

#valid parentheses

# s ="{([])}()"
# dict1 = {')':'(',']':'[','}':'{'}
# st = []
# for i in s:
# 	if i in dict1:
# 		if st and st[-1] == dict1[i]:
# 			st.pop()
# 		else:
# 			print(False)
# 	else:
# 		st.append(i)
# 		print(st)
# print(True) if not st else False		
	
# nums = [4,1,3,3]
# bad_pairs = 0
# dict1 = {}
# for i in range(len(nums)):
# 	diff = i - nums[i]
# 	good_pairs_count = dict1.get(diff, 0)
# 	bad_pairs += i - good_pairs_count
# 	dict1[diff] = good_pairs_count + 1
# print(bad_pairs)

# details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# ans = ""
# count = 0
# for i in details:
# 	ans += i[11]
# 	ans += i[12]
# 	if int(ans)> 60:
# 		count += 1
# 	ans = ""
# print(count)

# arr = [-1,1,-1,1,1,1,-1]
# ans = 0
# count = 0
# for i in arr:
# 	ans += i 
# 	if ans == 0:
# 		count += 1
# print(count)

# arr = [10,20,30]
# ch = 3
# a = 0
# for i in arr:
# 	for j in range(1,i+1,3):
# 		a += 1
# print(a)

# s = 9
# if s % 2 == 0:
# 	print("yes")
# else:
# 	print("No")

# s = "HHHTT"
# for i in range(len(s)):
# 	if s[i-1] == "H" and s[i] == "H" and s[i+1] == "H":
# 		print(6)
	
# s = "saivami"
# ans = ""
# for i in range(97,122):
# 	if chr(i) not in s:
# 		ans += chr(i)
# print(ans)

# s= "s  ss  ss "
# count = 0
# for i in s:
# 	if i ==" ":
# 		count += 1
# print(count)

# arr = [5,3,20,10,1,4,2]
# prod = 60
# k = 3
# count = 0
# for i in range(len(arr)):
# 	for j in range(i+1,len(arr)):
# 		for k in range(j+1,len(arr)):
# 			if (arr[i] * arr[j] * arr[k]) == prod:
# 				count += 1
# print(count)

# arr = [1,2,3,4,5]
# arr.sort()
# avg = (arr[-1] + arr[-2]) / 2
# for i in range(len(arr)):
# 	if arr[i] < avg:
# 		arr[i] = 0
# 	else:
# 		continue
# print(arr)

# s = "aaabbbcccc"
# dict1 = {}
# for i in s:
#     dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# maxi = max(dict1.values())
# ans = 0
# for i in dict1:
#     if dict1[i] != maxi:
#         ans += dict1[i]
# print(ans)

# s = 12389
# ans = ""
# for i in str(s):
#     a = int(i) * int(i)
#     ans += str(a)
# print(int(ans))
    
# arr = [2,4,7,3,3]
# ans = 0
# tot = sum(arr)
# for i in range(len(arr)):
#     if ans == tot - arr[i]:
#         print(i)
#         break
#     ans += arr[i]
#     tot -= arr[i]
# print(-1)

# a = 12
# b = 18
# ans = 0
# for i in range(1,12):
#     if a % i ==0 and b % i == 0:
#         ans = max(ans,i)
# sol = a / ans
# so2 = b / ans
# print(ans,int(ans * sol * so2))

# arr = [1,2,3,4]
# tor = 4
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == tor:
#             print(i,j)
            
# arr = [2,3,11,7]
# tor = 9
# temp = 0
# ans = 0
# l = 0
# for i in range(len(arr)):
#     temp += arr[i]
#     while temp > tor:
#         temp -= arr[l]
#         l += 1
#     if temp == tor:
#     	print(l,i)

# s = str(10000)
# count = 0
# i = 0
# while i < len(s):
#     if s[i] == "0" and s[i+1] == "0":
#         count += 1
#         i += 2
#     else:
#         count += 1
#         i += 1
# print(count)
        
# arr = [1,2,2,3,4,4]
# ta = 0
# tb = 0
# a = set(arr)
# for i in arr:
#     if i %2 == 0 and arr.count(i) % 2 == 0:
#         ta += i
#     else:
#         tb += i
# print(ta,tb)
    
# i = 5000
# ans = 0
# com = 0
# for s in range(i):
#     if s >= 0 and s <= 999:
#         com += 0
#     elif s >= 1000 and s <= 9999:
#         com += 1
#     elif s >= 10000 and s<= 99999:
#         com += 1
#     elif s >= 100000 and s<= 999999:
#         com += 1
#     elif s >= 100000 and s<= 999999:
#         com += 2
# print(com+1)

# x = 48
# y = 18
# if y == 0:
#     print(x)
# while y != 0:
#     if x < y:
#         x ,y = y,x
#     else:
#         t = x - y
#         x = y
#         y = t
# print(x)

# num = 9
# bin = format(num,'b')
# print(bin)

# num =  "1001"
# dec = int(num,2)
# print(dec)

# n = 1092
# ans = 0
# for i in str(n):
#     ans += int(i)
# print(ans)

# n = 11
# for i in range(2,n):
#     if n % i ==0:
#         print("no")
#         break
#     else:
#         print("yes")
#         break

# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fun(n-1) * fun(n-1) + (n- 2 )* (n-2)) % 47
# n = 16
# print(fun(n))

# arr = [1,17,18,0,18]
# su = 18
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j] and arr[i] + arr[j] == 18:
#             print(arr[i],arr[j])
    
# 1 = 1 
# 2 = 6 
# 3 = 17 
# 4 = 25
# 5 = 65

# s = "abbaba"
# dict1 = {}
# count = 0
# ans = ""
# i = 0
# while i < len(s)-1:
#     if s[i] == s[i+1]: 
#         i += 2
#         continue
#     else:
#         ans += s[i]
#     i += 1
# ans += s[-1] 
# print(ans)

# s = "helloworldpython"
# k = 5
# l1 = s[:k]
# l2 = s[k:]
# print(l2+l1)

# n = 999
# for i in range(n+1):
#     if len(str(i)) % 2 != 0:
#         print(i,end=" ")

# n =  28
# while str(n) != str(n)[::-1]:
#     n += int(str(n)[::-1])
# print(n)

# pattern = "IIIDIDDD"
# ans = ""
# a  = 1
# b = pattern.count("I") + 1
# for i in range(len(pattern)):
#     if pattern[i] == "I":
#         ans += str(a)
#         a += 1
#     else:
#         ans += str(b)
#         b += 1
# print(ans)

# arr = [10,20,30,40,50]
# arr1 = [4,2,0,3,1]
# ans = []
# for i in arr1:
#     ans.append(arr[i])
# print(ans)

# l1 = [1,2,3,4,5]
# l2 = [1,2,4,5]
# l3 = [1,4,5]
# for i in l1:
#     if i not in l2:
#         a = i
# for i in l2:
#     if i not in l3:
#         b = i
# print(a,b)

# arr = [1,-2,3,-4,5]
# even = []
# odd = []
# for i in arr:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even + odd)

# arr = [-1,6,4,1,3,5]
# for i in range(min(arr),max(arr)):
#     if i not in arr:
#         print(i)

# n = 17
# bin = format(n,'b')
# ans = 0
# for i in bin:
#     ans += int(i)
# print(ans)

# s = "10101001"
# ans = 0
# for i in range(len(s)):
#     if s[i] == "1":
#         ans = i
# print(ans)

# s = "Secret"
# th = 500
# ans  = 0
# temp = ""
# for i in range(len(s)):
#     ans += ord(s[i])
#     if ans < th:
#         temp += s[i]
# print(ans,temp)
    
# cake = [5,6,7,8,9,2,4,4]
# ans =0
# for i in cake:
#     if i >= 5:
#         ans +=i
# print(ans)

# arr = [5,2,10,8,1]
# ans = []
# for i in range(len(arr)-1):
#     a = arr[i+1] - arr[i]
#     ans.append(a)
# print(ans) 

# dict1 = {}
# arr = "aa"
# for i in arr:
#     dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# maxi = max(dict1.values())
# if len(arr) >= maxi + 2:
# 	print(maxi+2)
# else:
#     print(maxi + 1)

# ans = 0
# arr =[1,2,3,-2,5]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         ans = max(ans,sum(arr[i:j+1]))
# print(ans)

# arr = [[3,4,1,2],[8,7,6,5],[12,11,10,9]]
# ans = []
# for i in arr:
#     i.sort()
#     ans.append(i)
# print(ans)

# x = 8
# y = 10
# ans = 0
# for i in range(1,x):
#     if x % i == 0 and y % i==0:
#         ans = max(ans,i)
# print(ans)

# arr = [2,4,2,6,4]
# count = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if len(arr[i:j+1]) == 3:
#             if arr[i:j+1][0] + arr[i:j+1][-1] == arr[i:j+1][1]:
#                 count += 1
# print(count)

# arr = [2,4,6,8,10]
# c1 = 0
# c2 = 0
# for i in range(len(arr)):
#     if arr[i] %2 == 0:
#         c1 += 1
#         if c1 == 2:
#             print("no")
#             break 
#         else:
#             print("Yes")
#     c1 = 0
#     if arr[i] %2 != 0:
#         c2 += 1
#     if c2 == 2:
#         print("no")
#         break 
#     else:
#         print("Yes")
#         c2 = 0

# v = 200
# w = 540
# if w <= 2 and w%2 == 0 and v < w:
#     print("Invalid")
# for i in range(1,v+1):
#     if i * 4 + (v - i) * 2 == w:
#         print("FW =",i,"Tw =",v-i) 


# s = "###***##"
# c1 = 0
# c2 = 0
# for i in s:
#     if i == "#":
#         c1 += 1
#     else:
#         c2 += 1
# print(c1 - c2)

# arr = [3,4,5,6,7,8]
# f1 = arr[0]
# count = 1
# for i in arr:
#     if i > f1:
#         count += 1
# print(count)

# r = 3
# c = 3
# arr = [0,1,0,1,1,0,1,1,1]
# l = 0
# l1 = []
# for i in range(r):
#     ans = []
#     for j in range(c):
#         ans.append(arr[l])
#         l += 1
#     l1.append(ans)
# print(l1)
# maxi =0
# for i in l1:
#     maxi = max(maxi,i.count(1))
# print(maxi)
# for i in range(len(l1)):
#     if l1[i].count(1) == maxi:
#         print(i+1)

# e = [3,5,2,0]
# l = [0,2,4,4]
# n = 4
# ans = 0
# count = 0
# for i in range(n):
#     count += e[i] - l[i]
#     ans = max(ans,count)
# print(ans)

# arr = ['a','b','b','b','c','c','c','a','f','c']
# for i in range(len(arr)):
#     if arr[i].isupper():
#         arr[i] = arr[i].lower()
# dict1 = {}
# for i in arr:
#     dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# maxi = 0
# l1 = dict1.values()
# for i in l1:
#     if i%2 != 0:
#         maxi = max(maxi,i)
# for i in dict1:
#     if dict1[i] == maxi:
#         print(i)
#         break

# tot = 10
# can = 9
# if can in range(1,6):
#     print("Candles left:-",tot - can)
#     print(can)
# else:
#     print("Invalid")
#     print(tot)

# arr = [95,92,95,92,90,92,90,92,90]
# s1 = 0
# s2 = 0
# s3 = 0
# for i in range(0,len(arr),3):
#     s1 +=arr[i]
# for i in range(1,len(arr),3):
#     s2 +=arr[i]
# for i in range(2,len(arr),3):
#     s3 +=arr[i]
# l1 = [s1,s2,s3]
# maxi = max(l1)
# for i in range(len(l1)):
#     if l1[i] == maxi:
#         print("Traniee number:",i+1)

# val = 0
# if val >= 7000:
#     print("OVERLOAD")
# elif val ==0:
#     ans = 0
#     print("Time to complete:",ans)
# elif val > 0 and val <=2000:
#     ans = 25
#     print("Time to complete:",ans)
# elif val > 2000 and val <= 4000:
#     ans = 35
#     print("Time to complete:",ans)
# elif val > 4000 and val < 7000:
#     ans = 45
#     print("Time to complete:",ans)

# s = "All the best"
# k = 1
# ans = ""
# for i in s:
#     if i.isalpha():
#         a = ord(i) + 1
#         ans += chr(a)
#     else:
#         ans += " "
# print(ans)

# int = [12.3,15.2,12.3,15.2,12.3,15.2]
# ext = [10.10,10.10,10.00]
# ans = 1
# ans1 = 1
# co1 = 18
# co2 = 12
# for i in int:
#     ans += i * co1
# print(ans/4)  
# for i in ext:
#     ans1 += i * co1
# print(ans1 - ans/4)  

# nums = [1,10,3,5,1,7]
# min1 = float("inf")
# min2 = float("inf")
# for i in nums:
#     if i <= min1:
#         min1 = i
#     elif i <= min2:
#         min2 = i
#     else:
#         print(True)
#         break
# print(False)

# s = "il**autonrd**cl**nh*up*afpizp****d*a****lst"
# ans = []
# for i in range(len(s)):
#     if s[i] != "*":
#         ans.append(s[i])
#     else:
#         a = i - 1
#         ans.remove(ans[-1])
# print("".join(ans))

# def fact(a):
#     if a == 1:
#         return 1
#     elif a > 1:
#         return fact(a - 1) * a
# a = 4
# print(fact(a))

# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return fib(n-1) + fib(n-2)
# n = 5
# print(fib(n))

# def tower(n,f1,m1,s1):
#     if n == 0:
#         return
#     tower(n-1,f1,m1,s1)
#     tower(n-1,m1,s1,f1)
# n = 4
# print(tower(n,'a','b','c'))

# def prime(n):
#     if n < 2:
#         return "no"
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return "no"
#     return "prime"
# n = 6
# print(prime(n))

# def arm(n):
#     ans = 0
#     for i in str(n):
#         ans += (int(i)*int(i)*int(i))
#     if ans == n:
#         return True
#     return False
# print(arm(8766))

# arr = [[2,5,3],[4,7,0],[1,2,3],[13,4,4]]
# ans = []
# for i in range(len(arr[0])):
#     l1 = []
#     for j in range(len(arr)):
#         l1.append(arr[j][i])
#     ans.append(l1)
# print(ans)

#Reverse a digit
# num = 1234
# ans = int(str(num)[::-1])
# print(ans)

#  Binary to Decimal Conversion
# num = "1001"
# bin = int(num,2)
# print(bin)

#  Decimal to Binary Conversion
# num = 9
# dec = format(num,'b')
# print(dec)

# Prime Number in the given range
# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# def check(a,b):
#     ans = []
#     for i in range(a,b+1):
#         if isprime(i):
#             ans.append(i)
#     print(ans)   
# check(10,20)

# Find all palindrome numbers in the range of A to B
# def ispalindrome(a):
#     if str(a) == str(a)[::-1]:
#         return True
#     return False
# def check(a,b):
#     ans = []
#     for i in range(a,b+1):
#         if ispalindrome(i):
#             ans.append(i)
#     print(ans)
# check(100,150)

# : Sum of digits of a number
# num = 456
# ans = 0
# for i in str(num):
#     ans += int(i)
# print(ans)

# Armstrong number check
# num = 153
# ans = 0
# for i in str(num):
#     ans += int(i) * int(i) * int(i)
# if ans == num:
#     print(True)
# print(False)

# : Find Armstrong numbers in the range of A to B
# def arms(n):
#     ans = 0
#     for i in str(n):
#         ans += int(i) * int(i) * int(i)
#     if ans == n:
#         return True
#     return False
# def check(a,b):
#     ans = []
#     for i in range(a,b+1):
#         if arms(i):
#             ans.append(i)
#     print(ans)
# check(100,500)

# Greatest Common Divisor (GCD) of two numbers
# a = 36
# b = 60
# l1 = []
# for i in range(1,a):
#     if a % i == 0 and b % i == 0:
#         l1.append(i)
# print(max(l1))

#  Least Common Multiple (LCM) of two numbers
# a = 6
# b = 8
# l1 = []
# for i in range(1,a):
#     if a % i == 0 and b % i == 0:
#         l1.append(i)
# n = max(l1)
# ans = a * b // n
# print(ans)

# Factorial of a number
# n = 5
# ans = 1
# for i in range(1,n+1):
#     ans *= i
# print(ans)

# Find the number of digits in a number
# num = 1234
# print(len(str(num)))

# Check if a number is perfect
# num = 28
# l1 = 0
# for i in range(1,num):
#     if num % i == 0:
#         l1 += i
# if l1 == num:
#     print(True)

#  Check if a number is harshad (divisible by the sum of its digits)
# num = 18
# ans = 0
# for i in str(num):
#     ans  += int(i)
# if num % ans == 0:
#     print(True)

# : Generate a bill, find the costly item and its price
# ans = {"Item A":200,"Item B":450,"Item C":120}
# a = max(ans.values())
# for i in ans:
#     if ans[i] == a:
#         print(i,ans[i])

# Find the sum of the first N natural numbers
# n = 10
# ans = (n) * (n + 1) // 2
# print(ans)

# Find the sum of the squares of the first N natural numbers
# n = 3
# ans = 0
# for i in range(1,n+1):
#     ans += i * i 
# print(ans)

# n = 1234
# sum = 0
# while n > 0:
#     r = n % 10
#     sum = sum + r
#     n = n // 10
#     print(n,sum)

# fib = [0,1]
# for i in range(2,10):
#     ans = fib[-1] + fib[-2]
#     fib.append(ans)
# print(fib)

# leap year
# n = 2000
# if n % 400 == 0 :
#     print("leap")
# elif n % 4 ==0 and n % 100 != 0:
#     print("leap")
# else:
#     print("no")

#fizz buzz
# ans = []
# n = 10
# for i in range(1,10):
#     if i % 2==0:
#         ans.append("fizz")
#     elif i % 3 == 0:
#         ans.append("Buzz")
#     elif i % 3 == 0 and i% 2== 0:
#         ans.append("FizzBuzz")
#     else:
#         ans.append(str(i))
# print(ans)

#prime number
# num = 11
# count = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         count += 1
# if count > 2:
#     print("no")
# else:
#     print("prime")

#fibbonaci series
# n = 5
# ans = [0,1]
# for i in range(n):
#     a = ans[-1] + ans[-2]
#     ans.append(a)
# print(ans)

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end= " ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
    
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(" *",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(" ",i+1,end=" ")
#     print()
# m = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print(" ",m,end=" ")
#     m -= 1
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(i+j+1,end=" ")
#     for j in range(i,0,-1):
#         print(i+j,end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*",end=" ")
#         else:
#         	print(" ",end=" ")
#     print() 


# n = 5
# l1 =[]
# for i in range(n):
#     a = int(input())
#     l1.append(a)
# print(l1)

# arr = [1,2,3,4,5]
# k = 3
# ans = 0
# for i in arr:
#     if i < k:
#         ans += i
# print(ans)

# k = 10
# arr = [6,4,3,1,9,2,5]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == k:
#             print(arr[i],arr[j])

# arr = [1,2,3,4,5]
# k = 3
# print(arr[-k:] + arr[:-k])

# arr = [1,2,3,5]
# for i in range(min(arr),max(arr)+1):
#     if i not in arr:
#         print(i)

# arr  = [5,4,3,2,1]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# print(arr)

# arr= [1,2,3,4,4,5,5,-55]
# ans = 0
# print(sum(arr))
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         ans = max(ans,sum(arr[i:j+1]))
# print(ans)

# arr = []
# dict1 = {1:"monday",2:"tuesday",3:"wednes",4:"thrus",5:"frida",6:"sat",7:"sun"}
# for j in range(1,7):
#     a = int(input())
#     arr.append(a)
# b = 1
# for i in arr:
#     print("day",b,dict1[b],"workout",i)
#     b += 1
# print("Average of the week is",sum(arr)//len(arr))    

# arr = [2,8,4,6]
# for i in range(len(arr)):
#     l1 = arr[i:]
#     l2 = arr[:i]
#     if sum(l1) == sum(l2):
#         print(l1,l2)

# arr = [3, 4, -7, 1, 3, 3, 1, -4]
# TargetSum = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if sum(arr[i:j+1]) == TargetSum:
#             print(arr[i:j+1])
    
# Arr = [10, 20, 30, 40]
# K = 1
# l1 = Arr[:-K]
# l2 = Arr[-K:]
# print(l2+l1)

# n1 = 101
# n2 = 200
# count = set()
# ans = 0
# for i in range(n1,n2+1):
#     a = len(str(i))
#     for j in str(i):
#         count.add(j)
#     if len(count) == a:
#         ans += 1
#         count.clear()
#     count.clear()
# print(ans)

# Arr = [10, 12, 5, 40, 30, 7, 5, 9, 10]
# l1 = []
# l2 = []
# for i in Arr:
#     if i % 10 == 0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l2+l1)


# s = "ThisIsAnAutomationEra"
# l1 = []
# ans = ""
# ans += s[0]
# for i in s[1:]:
#     if i.islower():
#         ans += i
#     else:
#         l1.append(ans)
#         ans = ""
#         ans +=i
# print(l1)
# l2 = []
# for i in l1:
#     a = i.lower()
#     l2.append(a)
# print(" ".join(l2))


# arr = list(map(int,input().split()))
# for i in arr:
#     if arr.count(i) == 1:
#         print(i)
# print(arr)

# def fun(p,q,r):
#     arr = [p,q,r]
#     arr.sort()
#     ans = 0

#     if arr[0] == arr[1] ==arr[2]:
#             return ans
#     while True:
#         arr[0] += 1
#         arr[1] += 1
#         arr[2] -= 1
#         ans += 1
#         arr.sort()

#         if arr[0] == arr[1] ==arr[2]:
#             return ans
        
#         if (arr[0] == arr[1] and arr[1] + 1 == arr[2]) or(arr[1] == arr[2] and arr[0] + 1 == arr[1]):
#             return -1
# n = int(input()) 
# l1 = []
# for i in range(n):
#     p,q,r = map(int,input().split())
#     a = fun(p,q,r)
#     l1.append(a)
# for i in l1:
#      print(i)

# n = int(input())
# l1 = []
# for i in range(n):
# 	i,j = map(int,input().split())
# 	if j <= 9999 and i >= 0:
# 		ans = 0
# 		for i in range(i,j+1):
# 			ans += i
# 		l1.append(ans)
# 	else:
# 		l1.append("Invalid input i&j <= 10000")
# for i in l1:
# 	print(i)

# s = "saivamsi"
# s.lower()
# con = ""
# vow = ""
# l1 = "aeiou"
# for i in s:
#     if i in l1:
#         vow += i
#     else:
#         con += i
# print(vow,con)

# s = "Geek12@"
# n = 0
# up = 0
# lo = 0
# sp = 0
# sp1 = "!@#$%^&*()_-|\;:'/,."
# if len(s) < 6:
#     print("Invalid password")
# for i in s:
#     if i.isdigit():
#         n += 1
#     elif i.isupper():
#         up += 1
#     elif i.islower():
#         lo += 1
#     else:
#         sp += 1
# if up >= 1 and lo >= 1 and sp >= 1 and n >= 1:
#     print("valid passwords")
# else:
#     print("invalid passowrds")

# s = "sai"
# if s[::-1] == s:
#     print(True)
# else:
#     print(False)

# s = "aabbcbbbdy"
# dict1 = {}
# for i in s:
#     dict1[i] = 1 + dict1.get(i,0)
# for i in dict1:
#     if dict1[i] == 1:
#         print(i)
#         break
# print(dict1)

# s = "aabbcbbbdy"
# dict1 = {}
# for i in s:
#     dict1[i] = 1 + dict1.get(i,0)
# maxi = 0
# for i in dict1:
# 	if dict1[i] > maxi:
# 		maxi = dict1[i]
# print(maxi)
# print(dict1) 

# s = "saivamsi"
# ans = ""
# for i in s:
#     if i not in ans:
#         ans += i
# print(ans)

# s = "kingviamsi"
# dict1 = {}
# for i in s:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         break
# print(dict1)
# ans = ""
# for i in dict1:
#     ans += i
# print(ans)

# s = "ten"
# v = "net"
# s = sorted(s)
# v = sorted(s)
# if s == v:
#     print(True)
# else:
#     print(False)

# s = "saivamsi"
# s = sorted(s)
# print(s)

# n  = 1234
# ans = 0
# las = 0
# print(las,n)
# while n != 0:
#     las = n % 10
#     ans += las
#     n = n // 10
#     print(las,n)
# print(ans)

# def fibb(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibb(n-1) + fibb(n-2)
# print(fibb(0))
# print(fibb(1))
# print(fibb(2))
# print(fibb(3))
# print(fibb(4))
# print(fibb(5))

# n = 5
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
    
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end= " ")
#     for m in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end= " ")
#     for m in range(i,n-1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i == 4 or j == 0 or j == 4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# for i in range(n):
#     print(" " * (n-i) ,end =" ")
#     c = 1
#     for k in range(i+1):
#         print(c,end=" ")
#         c = c * (i - k) // (k+1);	
#     print()
    
# arr = [1,2,2,33,43]
# maxi = float("-inf")
# mini = float("inf")
# for i in arr:
#     if i > maxi:
#         maxi = i
#     elif i < mini:
#         mini = i
# print(mini,maxi)

# arr = [1,2,3,4,5]
# m1, m2 = 100, 100
# for x in arr:
#     if x <= m1:
#         m1, m2 = x, m1
#     elif x < m2:
#         m2 = x
# print(m1,m2)

# arr = [1,2,3,4,3]
# j = 0
# for i in range(len(arr)-1,0,-1):
#     arr[j] = arr[i]
#     print(arr[j])
#     j += 1
# print(arr) 

# arr = [1,33,4,55,2]
# ele = 5
# for i in arr:
#     if i == ele:
#         print("found")
#         break
# print("mot found")

# n = 5
# ans = 1
# for i in range(1,n+1):
#     ans *=i
# print(ans)
    
# n = 12
# y = 15
# ans = 0
# for i in range(1,n):
#     if(n % i == 0) and y % i == 0:
#         ans = i
# print(ans)
# print((n * y) // ans)

# n = 153
# ans = 1
# sum = 0
# for i in str(n):
#     ans = (int(i) *int(i)*int(i))
#     sum += ans
# print(sum)  

# arr = [1,2,3,4,5]
# k = 2
# l1 = arr[:-k]
# l2 = arr[-k:]
# print(l2+l1)

# arr = [1,2,1,2,3,4,3,6]
# for i in arr:
#     if arr.count(i) == 1:
#         print(i)
#         break

# arr = [1,2,3,5]
# for i in range(min(arr),max(arr)):
#     if i not in arr:
#         print(i)

# arr = [1,2,3,4,-3,4,3]
# maxi = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         ans = sum(arr[i:j+1])
#         maxi = max(maxi,ans)
# print(maxi)

# arr = [1,2,3,4,-3,4,3]
# res = arr[0]
# tot = 0
# for i in arr:
#     if tot < 0:
#         tot = 0
#     tot += i
#     res = max(res,tot)
# print(res)

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# ans = []
# for i in range(len(mat)):
#     l1 = []
#     for j in range(len(mat[0])):
#         l1.append(mat[j][i])
#     l1.reverse()
#     ans.append(l1)
# print(ans)

# def tof(n,sou,aux,des):
#     if n == 1:
#         print(f"move 1 disk from {sou} to {des}")
#         return 
#     tof(n-1,sou,des,aux)
#     print(f"move {n} from disk {sou} to {des}")
#     tof (n-1,aux,sou,des)
# n = int(input())
# tof(n,'a','b','c')
    
# n = int(input())
# list1 = list(map(int,input().split()))
# for i in list1:
#     print(i)


# list1 = list(map(int,input().split()))
# print(list1)

# l1 = input()
# l2 = []
# ans = ""
# for i in l1:
#     if i.isdigit():
#         l2.append(i)
#     elif i.isalpha():
#         ans += i
# print(l2,ans)
# length = l2[0]
# print(length)
# l2.remove(l2[0])
# print(l2)

# l1 = input()
# l2 = []
# ans = ""
# for i in l1:
#     if i.isdigit():
#         l2.append(i)
#     elif i.isalpha():
#         ans += i
# print(l2,ans)
# length = l2[-1]
# print(length)
# l2.remove(l2[-1])
# print(l2)

# n = 5
# for i in range(n):
#     print(" "  * (n-i),end= " ")
#     c = 1
#     for j in range(i+1):
#         print(c,end=" ")
#         c = c *  (i - j) // (j + 1)
#     print()

#  c = c * (i - k) // (k+1)

# st = input()
# n = 4
# s1 = input()
# s2 = input()
# s3 = input()
# s4 = input()
# print(st,s1,s2,s3,s4)

# def isPrime(n):
#     if n == 0 :
#         return False
#     if n == 1:
#         return False
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return False
#     return True
# l1 = []
# s = 10
# e = 20
# for i in range(s,e+1):
#     if isPrime(i):
#         l1.append(i)
# print(sum(l1))

# arr = [2,11,1,7]
# dict1 = {}
# target= 9
# for i in arr:
#     diff = target - i
#     if diff in dict1:
#         print(diff,i)
#     else:
#         dict1[i] = 1

# s = "Hello World from OpenAI"
# s = s.split(" ")
# ans = s[::-1]
# l1 = []
# for i in range(len(ans)):
#     if i % 2 == 0:
#         l1.append(ans[i].lower())
#     else:
#         l1.append(ans[i].upper())
# print(" ".join(l1))   

# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1,0,-1):
#         print(i - k+ 2,end= " ")
#     for l in range(i):
#         print(i-1 - l + 1,end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print(k-i+1,end= " ")
#     for l in range(i,n-1):
#         print(l - i + 1,end=" ")
#     print()


# s = input()
# l1 = []
# count = 0
# for i in s:
#     l1.append(int(i))
# for i in range(len(l1)):
#     for j in range(i,len(l1)):
#         if sum(l1[i:j+1]) != len(l1[i:j+1]):
#             print(l1[i:j+1])
#             count += 1
# print(count)

# s = input()
# s = s.upper()
# ans = ""
# print(s)
# l1 = []
# for i in range(65,91):
#     l1.append(chr(i))
# for i in l1:
#     if i not in s:
#         ans += i
# print(ans.lower())

# arr = [20,15,26,2,98,6]
# l1 = []
# for i in arr:
#     l1.append(i)
# l1.sort()
# print(l1,arr)
# for i in arr:
#     if i in l1:
#         print(l1.index(i) +1 )

# arr = [4,5,5,20,0,0,13,0,13]
# l1 = []
# count = 0
# for i in arr:
#     if i != 0:
#         l1.append(i)
#     else:
#         count += 1
# for i in range(count):
#     l1.append(0)
# print(l1)

# l1 = [1,0,2,0,1,0,2]
# ans = []
# count = 0
# l1.sort()
# for i in l1:
#     if i != 0:
#         ans.append(i)
#     else:
#         count += 1
# print(ans,count)
# for i in range(count):
#     ans.append(0)
# print(ans)

# arr = [7,4,8,2,9]
# count = 1
# for i in range(1,len(arr)):
#     if arr[i] == max(arr[:i+1]):
#         count += 1
# print(count)

# n = 5244
# n = str(n)
# ans = 1
# for i in n:
#     ans *= int(i)
# print(ans)

# s = "bbbaaababa"
# ans = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if len(s[i:j+1]) == 3:
#         	ans = max(ans,s[i:j+1].count('a'))
# print(ans)

# s = "ten"
# y = "net"
# if sorted(s) == sorted(y):
#     print(True)
# else:
#     print(False)


# s = "AAbbaaxy"
# if len(s) == 0:
#     print("No")
# s.lower()
# dict1 = {}
# for i in s:
#     dict1[i] = 1 + dict1.get(i,0)
# print(dict1)
# for i in dict1:
#     if dict1[i] == 1:
#         print(i)
#         break
#     else:
#         print("No")


# def isPrime(x):
#     if x < 2 :
#         return False
#     if x > 2:
#         for i in range(2,x):
#             if x % i == 0:
#                 return False
#     return True

# def check(x,y):
#     l1 = []
#     for i in range(1,max(x,y)+10):
#         if isPrime(i):
#             l1.append(i)
#     print(l1[x-1]*l1[y-1] - 1)
# x = 5
# y = 3
# check(x,y)

arr = [2, -3, 4, 1, 1, 7]
maxi = max(arr)
for i in range(maxi):
    if i not in arr:
        print(i)