# reverse string
# string = "hello"
# res=""
# # print(string[::-1])
# for i in string:
#     res= i +res
# print(res)

#max in array
# arr=[1,2,3,1,4,3]
# max=0
# for i in arr:
#     if i>max:
#         max = i
# print(max)

# find missing element in the array
# arr = [1,2,4,5,6]
# n=len(arr) +1
# total_sum = n*(n+1)/2
# sum = 0
# for i in arr:
#     sum=sum+i
# print(int(total_sum-sum))

#find the interstion of two arrays
# arr1 = [1,2,3]
# arr2 =[1,2]
# i,j=0,0
# ans=[]
# while i<len(arr1) and j<len(arr2):
#     if arr1[i]<arr2[j]:
#         i+=1
#     elif arr1[i]>arr2[j]:
#         j+=1
#     else:
#         ans.append(arr1[i])
#         i+=1
#         j+=1
# print(ans)

#remove duplicate element from the array
# arr=[1,2,3,3,1,3,4]
# uni = []
# for i in arr:
#     if i not in uni:
#         uni.append(i)
# print(uni)

#find occurance of the element in array
# def count_elements(arr):
#     count_dict = {}
#     for ele in arr:
#         if ele in count_dict:
#             count_dict[ele] +=1
#         else :
#             count_dict[ele] =1
#     return count_dict
# arr =[1,1,1,3,4,4,1,3,4,2,2]
# result = count_elements(arr)
# print(result)

#find second largest array in list
# def find_second_largest_number(arr):
#     first =second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first
#             first = num 
#         elif num>second and num!= first:
#             second  = num
#     return second
# print(find_second_largest_number([1,2,3,4,13,4,2,5]))

#merge two arrays
# arr1 = [1,2,3,4]
# arr2 = [1,2,3,4]
# arr3 = arr1 + arr2
# arr3.sort()
# print(arr3)

#kth largest method
# arr=[1,2,3,4,5,1,4,4]
# k=3
# arr.sort()
# print(arr[-k])\
# def kth_largest(arr,k):
#     for i in range(k):
#         max_index = i
#         for j in range(i+1,len(arr)):
#             if arr[j] >arr[max_index]:
#                 max_index = j
#         arr[i],arr[max_index] = arr[max_index],arr[i]
#     return arr[k-1]
# print(kth_largest([1,3,3,2,4,4,4,54,532,4],4))

#find maximum element and its position
# arr= [1,2,3,4,4,3,67]
# sum=0
# for i in arr:
#     if i>sum:
#         sum=i
#     print)

#divisior sum
# num=6
# sum=0
# for i in range(1,9):
#     if num%i == 0:
#         sum=sum+i
# print(sum)

# find the largest number that can be formed from an array

# arr=[1,2,3,4,5]
# arr.sort()
# res =arr[::-1]
# print(res)
# for i in res:
#     print(i,end="")

# bin1 = 110101
# bin2 = 111101
# print(bin1 and bin2)
# print(bin1 or bin2)

# num1 = 12
# num2 = 13
# print(num1+num2)
# print(num1*num2)
# print(num1-num2)
# print(num1//num2)

# def smalllargesum(arr):
#     temp = arr
#     uni = []
#     for i in arr:
#         if i not in uni:
#             uni.append(i)
#     print(uni)
#     if len(arr)<=3:
#         return 0
#     if len(arr) == 0:
#         return 0
# def find_second_largest_number(arr):
#     first =second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first
#             first = num 
#         elif num>second and num!= first:
#             second  = num
#     return second
# print(find_second_largest_number([1,2,3,4,3,4,24,5,6]))
# smalllargesum([1,2,3,4,3,4,24,5,6])

#password validator
# def checkpassword(str):
#     if len(str)<4:
#         return 0
#     has_lower = False
#     has_digit = False
#     has_upper = False
#     has_symbol = False
#     symbols="!\"#$%@^&*()%:;><.?"
#     for i in str:
#         if i.islower():
#             has_lower=True
#         if i.isupper():
#             has_upper = True
#         if i.isdigit():
#             has_digit=True
#         if i in symbols:
#             has_symbol=True
#     return has_lower and has_upper and has_digit and has_symbol
# print(checkpassword("ryMe2!"))

#find max element and return its index
# def findmaxinarr(arr):
#     max1=[]
#     for i in arr:
#         if i not in max1:
#             max1.append(i)
#     maxele = max(max1)
#     print(maxele)
#     print(max1.index(maxele))
# findmaxinarr([1,2,3,4,5,1,2,1])

#function for operationchoices
# def operationchoices(c,a,b):
#     if c==1:
#         print(a+b)
#     elif c==2:
#         print(a-b)
#     elif c==3:
#         print(a*b)
#     elif c==4:
#         print(a/b)
# operationchoices(2,15,20)

#anagrams-the word is formed by rearranging it
# str1="listen"
# str2 = "slient"
# str1.lower()
# str2.lower()
# if len(str1) == len(str2):
#     str1=sorted(str1)
#     str2=sorted(str2)
#     if str1 == str2:
#         print("anagram")
#     else:
#         print("not a anagram")
# else:
#     print("not a anagram")

#replace character
# def replace_character(str1 ,ch1,ch2):
#     if ch1 == ch2: 
#         return str1
#     str_list=[]
#     for i in str1:
#         if i == ch1:
#             str_list.append(ch2)
#         elif i == ch2:
#             str_list.append(ch1)
#         else:
#             str_list.append(i)
#     return ''.join(str_list)
# print(replace_character("saivamsi","s","a"))

#quadratic equaction
# def quabratic_equaction(a,b,c):
#     print(a*a + b + c)
# quabratic_equaction(2,3,4)

# string reverse
# string = "saivamsi"
# print(string[::-1])

#count swaps to arrange in ascending order
# def minimumswaps(arr):
#     sorted_array = sorted(arr)
#     sorted_idx = 0
#     for i in range(len(arr)):
#         if arr[i] == sorted_array[sorted_idx]:
#             sorted_idx +=1
#     min_moves = len(arr) - sorted_idx
#     return min_moves
# print(minimumswaps([1,2,3,1,1,1]))

#rotate array with element

#check element present in the array are not
# def check(arr,n):
#     if n in arr:
#         return True
#     else:
#         return False
# print(check([1,2,3,4,5,1],2))

#count the occurance of the element in the array 
# def count_occurance(arr,n):
#     count = 0
#     for i in arr:
#         if  i == n:
#             count = count+1
#     print(count)
# count_occurance([1,2,3,4,1,1,3],1)

#calculate the average of the array of positive numbers
# def calculate_average_of_positive_numbers(arr):
#     pos_arr=[]
#     for i in arr:
#         if i<0:
#             continue
#         elif i>0:
#             pos_arr.append(i)
#     sum=0
#     for i in pos_arr:
#         sum = sum +i
#     length = len(pos_arr)
#     print(sum/length)
# calculate_average_of_positive_numbers([1,2,3,4,-1,-1,-4,-1])

# finidng minimum value and its index
# def find_minimum(arr):
#     max1 = 1
#     for i in arr:
#         if i<max1:
#             max1 = i
#     ind = arr.index(max1)
#     print(max1)
#     print(ind)
# find_minimum([1,2,33,1,1,0])

#finding maximum sub array sum
# def maxsubbarraysum(arr,size):
#     max_so_far = arr[0]
#     curr_max = arr[0]
#     for i in range(1,size):
#         curr_max = max(arr[i],curr_max + arr[i])
#         max_so_far = max(max_so_far,curr_max)
#     return max_so_far
# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(maxsubbarraysum(arr,8))

# finding whether the sub string 1 present in the substring 2 are not
# str1="vamsisai"
# str2="sai"
# if str2 in str1:
#     ind = str1.index(str2)
#     print(ind)
# else:
#     print(False)

#reverse the string

# def reversestring(str):
#     li=[]
#     for i in str:
#         li.append(i)
#     li = (li[::-1])
#     print(''.join(li))
# reversestring("saivamsi")

#check palindrome 
# def check_palindrome(str):
#     if str[::-1] == str:
#         print("palindrome")
#     else:
#         print("not a palindrome")
# check_palindrome("racecar")

#binary operations
# def binary_and(s1,s2):
#     result = ""
#     for i in range(len(s1)):
#         if s1[i] == '1' and s2[i]  == '1':
#             result += '1'
#         else:
#             result += '0'
    
# def binary_or(s1,s2):
#     result = ""
#     for i in range(len(s1)):
#         if s1[i] == '0' and s2[i]  == '0':
#             result += '0'
#         else:
#             result += '1'

# def binary_xor(s1,s2):
#     result = ""
#     for i in range(len(s1)):
#         if s1[i] == '0' and s2[i]  == '0':
#             result += '0'
#         else:
#             result += '1'
#         if s1[i] == '1' and s2[i]  == '1':
#             result += '0'
#         else:
#             result += '1'

# s1 = input()
# s2 = input()
# operator = input()
# if operator =="AND":
#     print(binary_and(s1,s2))
# elif operator =="OR":
#     print(binary_or(s1,s2))
# else :
#     print(binary_xor(s1,s2))

#count no.of digits in the number and if it contains 00 it would return only one count
# s= input()
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

#replace character and vice versa
# def replace_character(str1,ch1,ch2):
#     res=[]
#     for i in str1:
#         if i == ch1:
#             res.append(ch2)
#         elif i == ch2:
#             res.append(ch1)
#         else:
#             res.append(i)
#     print(''.join(res))
# replace_character("saivamsi","s","a")

#anagram or not
# def anagram(str1,str2):
#     str1=sorted(str1)
#     str2=sorted(str2)
#     print(str1)
#     print(str2)
#     if str1 == str2:
#         print("yes")
#     else:
#         print("no")
# anagram("listen","slient")/

#program for reversing a string wordwise and reversing only the last word
# def reverse_string_wordwise(str1):
#     res=""
#     arr=[]
#     for i in range(len(str1)):
#         if str1[i] == ' ':
#             arr.append(res)
#             arr.append(' ') 
#             res = ""
#         else:
#             res += str1[i]
#     arr.append(res)
#     print(arr)
#     for i in range(len(arr)-1,-1,-1):
#         print(arr[i],end="")
# reverse_string_wordwise("saivamsi is a good")


#program to reverse the words in the string
# def str_word_reverse(str):
#     s = str.split()[::-1]
#     l=[]
#     for i in s:
#         l.append(i)
#     print(' '.join(l))
# str_word_reverse("saivamsi is a good boy")

# longest palindrome substring
# def longestPalindrome(s):
#     if len(s)>2:
#         return s
#     result = ""
#     maxlen = 0
#     for i in range(len(s)):
#         l,r = i,i
#         while l>=0 and r<len(s) and s[l] == s[r]:
#             if (r-l+1) >maxlen:
#                 maxlen = r-l+1
#                 result = s[l:r+1]
#             l-=1
#             r+=1
#     for i in range(len(s)):
#         l,r = i,i+1
#         while l>=0 and r<len(s) and s[l] == s[r]:
#             if (r-l+1) >maxlen:
#                 maxlen = r-l+1
#                 result = s[l:r+1]
#             l-=1
#             r+=1
#     return result
# print(longestPalindrome("bababaaaababa"))

# str1 = "you hello obtain"
# word = str1.split(' ')
# length = 0
# for i in word:
#     if len(i)>length:
#         length = len(i)
# print(i)

# n=5
# num=1
# for i in range(1,n):
#     for j in range(i):
#         print(num,end=" ")
#         num +=1
#     print()

# i = int(input())
# j = int(input())
# print(i+j)

# arr = [1,2,3,4,5,6,7,8,9]
# even = []
# odd = []
# for i in arr:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# n=5
# arr1 = [3,1,4,1,5]
# arr2 = [2,7,1,8]
# arr1w=[]
# arr2w = []
# for i in arr1:
#     if i not in arr1w:
#         arr1w.append(i)
# z=set(arr1w)
# for i in arr2:
#     if i not in arr2w:
#         arr2w.append(i)
# w=set(arr2w)
# print(z.union(w))
# print(z.intersection(w))

# arr1 =[2,4,6,8]
# arr2 =[1,3,5,7]
# arr1=set(arr1)
# arr2=set(arr2)
# if arr1.intersection(arr2) != set():
#     print(arr1.intersection(arr2))
# else:
#     print("-1")
# arr3=list(arr1.union(arr2))
# print(arr3)

# num = 98922
# num=str(num)
# print(num[::-1])

# n=int(input())
# temp= str(n)

# if len(temp) == 0:
#     print(n)
# elif n%2==0:
#     print((n-2)/2)
# elif n%2 != 0 :
#     print(n/2)

# text = "xYz"
# countup = 0
# countlow =0 
# for i in text :
#     if i.isupper():
#         countup +=1
#     else:
#         countlow +=1
# if countup >countlow :
#     text = text.upper()
#     print(text)
# else:
#     text = text.lower()
#     print(text)

# k=3
# arr = [1,2,3,4,8,5]
# arr.sort()
# print(arr)
# print(arr[k-1])
    
# arr=[0,2,1,2,0]
# list1=[]
# for i in arr:
#     if i == 0:
#         list1.append(i)
#     elif i == 1:
#         list1.append(i)
#     else :
#         list1.append(i)
# print(list1)


    
# n= int(input())
# k = int(input())
# arr = list(map(int,input().split()))
# max_score = 0
# for i in range(n-k+1):  
#     temp = arr[i:i+k]   
#     score = 0
#     for j in range(len(temp)):
#         score +=(j+1) * temp[j]
#     max_score = max(max_score,score)
# print(max_score)

# x=48
# y=18
# while (y!=0):
#     if x<y:
#         x,y=y,x
#     else:
#         t=x-y
#         x=y
#         y=t
# print(x)

# x=12
# y=3
# while True:
#     if x%y == 0:
#         break
#     y+=1
# sum_digits = 0
# while(y>0):
#     sum_digits+=y%10
#     print(sum_digits)
#     y=y//10
# print(sum_digits)

# n =str(1111)
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(sum)

# num=18
# if num>1:
#     for i in range(2,(num//2)+1):
#         if num%i ==0:
#             print("not a prime")
#         else:
#             print("prime")
# else:
#     print("not a prime")

# num = 10
# list1=[]
# while num!=0:
#     r=num%2
#     list1.append(r)
#     num =num//2
# list1.reverse()
# for i in list1:
#     print(i,end="")

# num = "1010"
# num=num[::-1]
# sum=0
# print(num)
# for i in range(len(num)):
#     sum=sum+num[i]*2**i
# print(sum)


#to find superior element in the array
# n=int(input())
# arr=list(map(int,input().split()))
# sup =0
# count = 0
# arr =arr[::-1]
# for i in arr:
#     if i>sup:
#         sup = i
#         count +=1

# print(count)
# n = 3
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(str(j)*i,end="")
#     print()


#sum b/w the differnce of the array elements 
# n=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# score =0
# for i in range(n//2):
#     score +=(arr[n-i-1]-arr[i])
# print(score)

# remove consective pairs of the string
# string = "baabc"
# list=[]
# for i in string:
#     if len(list)!=0 and list[-1] == i:
#         list.pop()
#     else:
#         list.append(i)
# if len(list) == 0:
#     print("Empty string")
# else:
#     print(''.join(list))

#reverse the string using given value
# n=6
# str1 = "helloworldpython"
# k = 5
# if n==0:
#     print("NULL")
# else:
#     k=k%n
#     print(str1[k:]+str1[:k])

# cut = 3
# pieces = (cut *(cut+1))/2
# print(pieces+1)

# n= 25
# length = list(len(n))
# if length == 0:
#     print(n)
# elif n%2 !=0:
#     print(n/2)
# else:
#     print((n-2)/2)

# k = 2
# m = 100
# a=0
# for i in range(k):
#     arr = list(map(int,input().split()))
#     arr1 = arr[1:]
#     for j in arr1:
#         a =a + j**2
#     print(a)


# string = "#####****"
# count_star = 0
# count_hash = 0
# for i in string:
#     if i == "#":
#         count_hash += 1
#     else:
#         count_star +=1
# j = count_star - count_hash
# if j <= -1:
#     j = j-j+j
# for k in range(j):
#     if count_star > count_hash:
#         print("*")
#     else:
#         print("#")

# d= 7
# unit = 2
# n =8
# arr = [2,8,3,5,7,4,1,2]
# food = d * unit
# sum=0
# count =0
# for i in arr:
#     food = food - i 
#     count +=1
#     if food<=0:
#         break
# print(count)5


# def check_leap_year(year):
#     if year%400 == 0:
#         print("leaap year")
#     elif year%4 == 0 and year %100 !=0:
#         print("leap")
#     else:
#         print(" not a leap")
# check_leap_year(2004)

#reverse the string
# string = "saivamsi"
# print(string[::-1])

# fiboonaci series


# num = 123
# while(str(num)!=str(num) [::-1]):
#     num = num+int(str(num)[::-1])
# print(num)

# num =12
# sum =0
# for i in range(1,num):
#     if num%i ==0:
#         sum = sum + i
# if sum == num :
#     print('1')
# else:
#     print(sum)

# n=int(input())
# arr = list(map(int,input().split()))
# arr1 = list(map(int,input().split()))
# res=[]
# for i in arr:
#     for j in arr1:
#         if arr[j] not in res:
#             res.append(arr[j])
# print(res)

# n=int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = list(map(int,input().split()))
# for i in a:
#     if i not in b:
#         print(i)
# for j in b:
#     if j not in c:
#         print(j)


# num = 6
# arr = [1,-2,3,-4,5,6,4]
# for i in arr:
#     if i < 0:
#         arr.remove(i)
# if len(arr)%2 != 0:
#     mid = len(arr)//2
#     print(arr[mid])
# else:
#     mid = len(arr)//2
#     print(arr[mid - 1])
    
#fiboonaci series in python
# num = 10
# n1,n2 =0,1
# print(n1,n2,end=" ")
# for i in range(2,num):
#     n3 =n1 + n2
#     n1 = n2
#     n2 =n3
#     print(n3,end=" ")
# print()


#gcd of a number
# num = 10
# list = []
# for i in range(1,num):
#     if num % i == 0:
#         list.append(i)
# print(max(list))


#perfect number in python
# num = 6
# list=[]
# for i in range(1,num):
#     if num%i== 0:
#         list.append(i)
# sum = 0
# for i in list:
#     sum = sum+i
# if sum == num:
#     print("perfect number")
# else:
#     print("mot perfect number")
# print(sum)

#anagram in python
# word1 = "listen"
# word2 = "slient"
# i=sorted(word1)
# j=sorted(word2)
# if i == j :
#     print("anagram")
# else:
#     print("not a anagram")

#string palindrome or not
# string = "madam"
# if string[::-1] == string:
#     print("palindrome")
# else:
#     print("not a palindrome")

#frequency of a characther in python
# string = "saivamsi"
# print(string.count("a"))

#non repeating character in python
# string = "saivamsi"
# res=[]
# for i in string:
#     if i not in res:
#         res.append(i)
# print(''.join(res))

#replace the substring in the main string
# string = "i is saivamsi"
# str2 = "is"
# str1 ="am"
# string = string.replace(str2,str1)
# print(string)

#factoraial of the number
# num = 5 
# fact =1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

#armstrong number in python
# num = 153
# temp = num
# sum=0
# digit = 0
# length = len(str(temp))
# for i in range(length):
#     digit = int(temp%10)
#     temp = temp/10
#     sum += pow(digit,length)
# if sum == num:
#     print("armstrong")
# else:
#     print("not a armstomng")

#sum of first n natural numbers
# def sum_of_nat(num):
#     if num == 0:
#         return 0
#     else:
#         return num+sum_of_nat(num-1)
# num = 10
# print(sum_of_nat(num))

#program to check whether letter is lower or not
# string ="saivamsi"
# vowels =['a','e','i','o','u']
# for i in string:
#     for j in vowels:
#         if i ==j:
#             print("vowel",end="")
#         else:
#             print("consonant",end="")

# nooflists = int(input())
# list1 = []
# for i in range(nooflists):
#     list1.append(map(int,input().split()))
# noofQueries = int(input())
# list =[]
# for i in range(noofQueries):
#     position = list.append(map(int,input().split()))
#     linenumber = list.append(map(int,input().split()))
# print(linenumber)
# print(position)

# n = int(input())
# list2=[]
# for i in range(n):
#     list1 = list((map(int,input().split())))
#     max_sum = 0
#     for i in list1:
#         max_sum = max_sum + i 
#     list2.append(max_sum)
# print(max(list2))

#binary to decimal 
# 1010 = 10
# binary_number = "0011"
# decimal_number = int(binary_number,2)
# print(decimal_number)

#decimal to binary
# def dec_to_bin(num):
#     if num>1:
#         dec_to_bin(num//2)
#     print(num%2,end='')
# num = 100
# dec_to_bin(num)

#to check vowel or consonant
# list=["a","e","i","o","u"]
# letter = "z"
# for i in list:
#     if letter in list:
#         print("vowel")
#         break
#     else:
#         print("consonant")
#         break

#automorphic number = an integer whose square ends with the given integer
# num = 76
# sq = num**2
# sq = str(sq)
# list = []
# for i in sq:
#     list.append(i)
# list1=[]
# list1.append(list[-2])
# list1.append(list[-1])
# dig = ''.join(list1)
# if int(num) == int(dig) :
#     print("automorphic num")
# else:
#     print("not automorphic")

#to print ascii value of a string
# char = "a"
# print(ord(char))

#remove  symbols
# list =[]
# str = "abacd#"
# res=""
# for i in range(97,123):
#     list.append(chr(i))
# for i in str:
#     if i in list:
#         res = i
#     print(res,end=" ")

#remove spaces
# string = "sai  v a m s i  "
# print(''.join(string.split()))

#ccount sum of digits of the number
# dig =625
# temp = str(dig)
# sum =0
# for i in temp:
#     sum = sum + int(i)
# print(sum)

#power of a number 
# num = 45
# pow1 = 3
# print(pow(num,pow1))

# def supermarket(num):
#     price = 1
#     for i in num:
#         price = price*int(i)
#     print(price)
# supermarket("5244")

# n = 5
# arr = [1,2,1,0,5]
# list1 =arr[:2]
# list2 =arr[2:5]
# max1 = max(list1)
# mini1 = min(list1)
# sum1 = max1 - mini1
# max2 = max(list2)
# mini2 = min(list2)
# sum2 = max2 - mini2
# print(sum1+sum2)

# n = 5
# sum = 0
# arr1 = [7,0,5,1,3]
# arr2 = [1,2,1,3,4]
# for i in arr1:
#     sum = sum + i
# for j in arr2:
#     sum = sum -j 
# print(sum)

# arr = [1,2,3,4,5,6,7]
# d=2
# arr1 = arr[:d]
# arr2 = arr[d:]
# print(arr2+arr1)

# arr = [1,-2,3,-4,5]
# list1=[]
# list2 =[]
# for i in arr:
#     if i<0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list1+list2)

#missing element on the array
# arr = [1,2,3,5,6]
# missing = []
# for i in range(arr[0],arr[-1]+1):
#     if i not in arr:
#         missing.append(i)
# print(missing)

# n=5
# arr = [1,2,3,5,6]
# sum_num = (n+1) * (n+2)//2
# print(sum_num-sum(arr))

# num = 15
# sum_digits = 0
# while num>0:
#     sum_digits += num%2
#     num = num //2
# print(sum_digits)

#moving an array with kth number
# n = 5
# arr = [1,2,3,4,5]
# d = 19
# f = d%n
# if d > n:
#     temp =arr[:f]
#     arr = arr[f:]
# else:
#     temp =arr[:d]
#     arr = arr[d:]
# print(arr+temp)

#move all zeros to the end
# arr = [1,2,3,0,1,0,1,0,2,0]
# list1=[]
# for i in arr:
#     if i == 0:
#         list1.append(i)
#         arr.remove(i)
# print(arr+list1)
        
#linear search
# arr = [1,2,3,4,5,6]
# search = 5
# for i in arr:
#     if i == search:
#         print(arr[i])
#         break
#     else:
#         print("-1")
#         break

#union of 2 sorted arrays
# arr1 = [1,2,3,4,4]
# arr2 =[5,5,6,7,8,9]
# arr1 =set(arr1)
# arr2 = set(arr2)
# print(arr1.intersection(arr2))

# n =5
# arr = [1,2,3,5,6]
# sum_dig = (n * n +1)//2
# print(sum(arr)-sum_dig)

#maximum consective ones
# arr = [1,2,2,3,1,1,1,1,0,0,3,4,5]
# count = 0
# maxi = 0
# for i in arr:
#     if i == 1:
#         count+=1
#         maxi = max(maxi,count)
#     else:
#         count =0
# print(maxi)

#find the number that appear once 
# arr = [1,1,2,2,3,4,4]
# for i in arr:
#     if arr.count(i) < 2:
#         print(i)

#find the longest sub array with sum k only postives
# subarray is the contiguous array
# n =13
# arr = [1,1,2,3,3,4,4,5,5,4,23,3,1] 
# k=3
# d = {}
# maxi , current_sum = 0,0
# for i in range(n):
#     current_sum += arr[i]
#     if current_sum  == k:
#         maxi =max(maxi,i+1)
#     rem = current_sum - k
#     if rem in d:
#         maxi = max(maxi,i-d[rem])
#     if current_sum not in d:
#         d[current_sum] = i 
# print(maxi)

#output all the unique pairs that sum up to a specific value k
# def sum_pair(arr,k):
#     if len(arr)<2:
#         return
#     seen = set()
#     output = set()
#     for i in arr:
#         target_var = k - i
#         if target_var not in seen:
#             seen.add(i)
#         else:
#             output.add((min(i,target_var),max(i,target_var)))
#     return output,len(output)
# print(sum_pair([1,2,3,2],4))


#find largest contiguous sum
# n=4
# arr  = [1,2,3,-2]
# max_so_far = arr[0]
# curr_max = arr[0]
# for i in range(1,n):
#     curr_max = max(arr[i] ,curr_max+arr[i])
#     max_so_far = max(max_so_far,curr_max)
# print(max_so_far)

#arr sum = k in array
# n=4
# arr = [1,5,7,1]
# k= 8
# count = 0
# dic = {}
# for i in range(n):
#     diff = k - arr[i]
#     if diff in dic:
#         count += dic[diff]
#     if arr[i] in dic:
#         dic[arr[i]]+=1
#     else:
#         dic[arr[i]] = 1
# print(count)


#alternative positive and negative number
# arr = [1,2,-2,-3,1,-1,4,-1]
# pos = []
# neg = []
# for i in arr:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(pos+neg)
# print(neg)

# num = str(input())
# print(int(num,17))

# list = ['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'type', 'var']
# keyword = 'reak'
# for i in list:
#     if keyword == i :
#         print(i,"it is a keywoard")
#         break
#     else:
#         print("it is not a keywoard")
#         break


#move 0 to the end of the array
# n = 8
# arr = [1,2,3,40,0,0,3,0]
# list1 =[]
# for i in arr:
#     if i == 0:
#         list1.append(i)
#         arr.remove(i)
# print(arr+list1)

# s = 'mon'
# a = 13
# m = {
# "mon": 6, "tue": 5, "wed": 4,
# "thu": 3, "fri": 2, "sat": 1,
# "sun": 0
# }
# ans = 0
# if a - m[s[:3]] >= 1:
#     ans = 1 + (a - m[s[:3]]) // 7
# print(ans)

# n = 7
# arr = [1,0,2,0,1,0,2]
# arr.sort()
# print(arr)

#elements greather than arr[0]
# n = 5
# arr =[7,4,8,2,9]
# first = arr[0]
# count = 1
# for i in arr:
#     if i > first:
#         count+=1
# print(count)

# n = "5244"
# mul = 1
# for i in n:
#     mul = mul * int(i)
# print(mul)


# n = 16
# arr = "XXXSXXSXXSSXXSXX"
# count=0
# for i in arr:
#     if i == "S":
#         count+=1
# print(count)

# str1 ="abaabbcc"
# res=""
# for i in str1:
#     if i == "a":
#         res +="b"
#     elif i =="b":
#         res +="a"
#     else:
#         res +=i   
# print(res)

# n = 5
# arr = [1,2,3,4,5]
# d = 16
# f = d%n
# if d<n:
#     arr1 = arr[:d]
#     arr2 = arr[d:]
# else:
#     arr1 = arr[:f]
#     arr2 = arr[f:]
# print(arr2+arr1)

# str1 = "Hello, world"
# str2 = "world"
# n= len(str1)
# m = len(str2)
# for i in range(n-m+1):
#     if str1[i:i+m] == str2:
#         print(i)

# str1 = "madam"
# if str1 == str1[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

# str1 = "saivamsi"
# print(str1[::-1])

# arr = [5,2,4,1,3,7]
# su = 9
# seen= set()
# for i in arr:
#     target = su - i
#     if target in seen:
#         print([target,i])
#     seen.add(i)

# n=4
# arr  = [-2,1,-3,4,2,1,-5,4]
# max_so_far = arr[0]
# curr_max = arr[0]
# for i in range(1,n):
#     curr_max = max(arr[i] ,curr_max+arr[i])
#     max_so_far = max(max_so_far,curr_max)
# print(max_so_far)

# string = "saivamsi is a good boy and good coder"
# n=10
# word = string.split(" ")
# length = len(word)
# if n<=len(word):
#     print(word[:n])
# else:
#     n = length%n
#     print(word[::-n])

# str1 = "saivamsi"
# print(str1[::-1])

# string = "1234"
# sum =0
# for i in string:
#     sum = sum + int(i)
# print(sum)

# str1 = "010010000"
# imp_sec = 0
# for i in range(len(str1)):
#     if str1[i] == '1':
#         imp_sec = i
# print(imp_sec)
        
# string = "Secret"
# ascii1 = 500
# sum =0
# msg = ""
# for i in string:
#     sum+= ord(i)
#     if sum>ascii1:
#         break
#     msg+=i
# print(msg)

# n = 5
# arr = [5,5,5,5,5,]
# sum = 0
# for i in arr:
#     if i>=5:
#         sum+=i
# print(sum)

#converting the 3x3 matrix into 2x2 matrix
# arr = [[1,2,3],[4,5,6]]
# res = [[0,0],[0,0],[0,0]]
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         res[j][i] = arr[i][j]
# print(res)

#prime number checking
# num = 978
# if num==1:
#     print("not a prime")
# elif num>1:
#     for i in range(2,num):
#         if num%i == 0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# else:
#     print("not a prime")

#move zeroes to the end of the array
# arr = [5,2,0,8,0,2,1]
# list2=[]
# list1 = []
# for i in arr:
#     if i == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list2+list1)
        
#fiboonacci series in python
# num = 3
# n1 = 0
# n2 = 1
# print(n1,n2,end=" ")
# for i in range(num):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")

# arr = [7,1,8]
# one = arr[0]
# list1=[]
# list1.append(one)
# if len(arr)<=2:
#     print(0)
# else:
#     for i in arr:
#         if i>one:
#             list1.append(i)
#     print(sum(list1))

# n = 5
# arr = [5,2,10,8,1]
# length = len(arr)
# res =[]
# for i in range(1,n):
#     res.append(arr[i]-arr[i-1])
# print(*res)

#palindrome check
# string = "racecar"
# if string[::-1] == string:
#     print("palindrome")
# else:
#     print("not a palindrome")

# Anagram checking
# str1 = "listen"
# str2 = "slient"
# if sorted(str1) == sorted(str2):
#     print("anagram")
# else:
#     print("not a anagram")

# binary = "1111"
# conversion = int(binary,2)
# print(conversion)

# r = 7
# unit = 2
# food = r*unit
# arr = [2,8,2,5,7,4,1,2]
# sum = 0
# list1 = []
# for i in arr:
#     if sum<=food:
#         sum += i
#         list1.append(i)
# print(len(list1))

# n = 2323
# res =0
# while(n != 0):
#     last_digit = n%10 #sstore last digit
#     res = res + last_digit #operations
#     n =n//10 #reduce the num by 1 digit(remove the last digit)
# print(res)

# num = 3434
# res = []
# while(num!=0):
#     last_dig = num % 10
#     res.append(last_dig)
#     num = num // 10
# print(*res)

# num = 76767
# temp = num
# res = 0
# while num!= 0:
#     last_digit =num % 10
#     res = 10 * res + last_digit
#     num =  num // 10
# if res == temp:
#     print("palindrome")
# else:
#     print("not a palindrome")

#armstrong number
# num = 370
# temp = num
# res = []
# while num!=0:
#     last_dig = num%10
#     res.append (last_dig**3)
#     num = num//10
# if temp == sum(res):
#     print("Armstrong number")
# else:
#     print("not a armstrong number")

#strong number
# num = 145
# temp = num
# fact = 1
# list1 = []
# while num!=0:
#     last_dig = num % 10
#     for i in range(1,last_dig+1):
#         fact =fact * i
#     list1.append(fact)
#     fact = 1
#     num = num // 10
# if temp == sum(list1):
#     print("strong number")
# else:
#     print("not a strong number")

# mat = [[1,2,3],[1,2,3]]
# res = [[0,0],[0,0],[0,0]]
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         res[j][i] = mat[i][j]
# print(res)

# str1  = "1C0C1C1A0B1"
# print("enter your choice:-")
# choice = int(input())
# if choice == 1:

# def prime(num):
#     if num <=1 :
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i ==0:
#             return False
#         return True
# num = int(input())
# max_hugeness = -1
# for i in range(1,num+1):
#     res = i^(i-1)
#     if prime(res):
#         max_hugeness = max(max_hugeness,res)
# print(max_hugeness)


# n = 8
# arr = [-5,1,2,3,-4,5,6,-2]
# max_sum = -float("inf")
# for i in range(n):
#     for j in range(i+1,n+1):
#         sub_array = arr[i:j+1]
#         if sum(sub_array) > max_sum:
#             max_sum = sum(sub_array)
# print(max_sum)

# str1 = "1C0C1C1A0B1"
# resc = []
# resa = []
# resb = []
# for i in range(len(str1)):
#     if str1[i] == "C":
#         resc.append(str1[i-1])
#         resc.append(str1[i+1])
#     elif str1[i] == "A":
#         resa.append(str1[i-1])
#         resa.append(str1[i+1])
#     elif str1[i] == "B":
#         resb.append(str1[i-1])
#         resb.append(str1[i+1])
# print(resa)
# print(resb)
# print(resc)
# for i in range(len(resa)-1):
#     print(int(resa[i]) & int(resa[i+1]))
# for i in range(len(resb)-1):
#     print(int(resb[i]) | int(resb[i+1]))
# for i in range(len(resc)-1):
#     print(int(resc[i]) ^ int(resc[i+1]))

# r = 7
# unit = 2
# n = 8 
# arr = [2,8,3,5,7,4,1,2]
# food = r * unit
# count =0
# sum1 = 0
# if len(arr)<=0:
#     print("-1")
# elif sum(arr) < food:
#     print("0")
#     exit()
# for i in arr:
#     if sum1<=food:
#         sum1 +=i
#         count +=1
# print(count)

# arr = [12,3,14,56,77,13]
# num = 13
# diff = 3
# res =[]
# arr.sort()
# num1 = num +diff
# num2 = num - diff
# for i in arr:
#     if i<=num1 and i>=num2:
#         res.append(i)
# print(len(res))

# num1 = "451"
# length1 = len(num1)
# print(length1)
# num2 = "349"
# count = 0
# # if num1[len(num1)-1:]

# def odd_even(num):
#     if num %2 == 0:
#         print("even")
#     else:
#         print("odd")
# num = 2
# odd_even(num)

#palindrome check
# num = "3232"
# if num[::-1] == num:
#     print("palindrome")
# else:
#     print("not a palindrome")

# num = 5
# letter = 76
# for i in range(num):
#     for j in range(i+1):
#         print(chr(letter),end=" ")
#         letter += 1
#     print()

# num1 = "451"
# num2 = "349"
# count = 0
# carry = 0
# if len(num1) <= len(num2):
#     l = len(num1) - 1
# else:
#     l = len(num2) - 1
# for i in range(l+1):
#     temp = int(num1[l-i]) + int(num2[l-i]) + carry
#     if len(str(temp)) > 1:
#         count +=1
#         carry = 1
#     else:
#         carry = 0
# print(carry + count)

# str = input("")
# a = int(str[0])
# i = 1
# while i<len(str):
#     if(str[i] == "A"):
#         a = a & int(str[i+1])
#     elif str[i] == "B":
#         a = a | int(str[i+1])
#     else:
#         a = a ^ int(str[i+1])
#     i+=2
# print(a)

# str1 = "2024"
# print(str1.replace("0","5"))

# n = 3
# arr = [608,601,609]
# sum = 0
# for i in arr:
#     sum +=i
# print(sum//5)

# str1 = "apples"
# res=''
# for i in str1 :
#     if i == "a":
#         res += "p"
#     elif i == "p":
#         res += "a"
#     else:
#         res += i
# print(res)

# n1 = 7
# n2 = 12
# a =[]
# for i in range(n1,n2):
#     a.append(pow(i,2))
# print(max(a))

# n1 = 12
# n2 = 50
# sum = 0
# for i in range(n1,n2):
#     if i%3 == 0 and i%5 == 0:
#         sum += i
# print(sum)

# str1 = "abcabdebabadcb"
# list1 =[]
# for i in str1:
#     if i not in list1:
#         list1.append(i)
#     elif i in list1:
#         break
# print(len(list1))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# list1 = []
# for i in matrix[0]:
#     list1.append(i)
# for i in matrix[1]:
#     list1.append(i)
# for i in matrix[2]:
#     list1.append(i)
# print(list1)

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for i in range(i,n):
#         print(" *",end="")
#     print()

# arr = [1,2,3,4,5,6]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         print(arr[i],end="")

# str1 = "sai"
# print('"'+ str1 + '"')

# arr = [5,3]
# list1 = []
# for i in arr:
#     if i not in list1:
#         list1.append(i)
# if len(arr) <=2:
#     print(arr[0])
# # print(len(list1))

# n = 3
# str1 = "abc"
# for i in range(len(str1)):
#     print(str1,end="")

# str1 = "ABC"
# str2 = "AABCCAD"
# for i in str2:
#     if str2 not in str1:
#         str1 += str2
# print(str1)

# arr = [1,2,3,4,5]
# list1 = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             list1.append(arr[k])
#         print()
# print(list1)

# num = 67
# m = 8
# list1 = []
# for i in range(0,68):
#     if i%m == 0:
#         list1.append(i)
# print(max(list1))

# n = 10
# m = 3
# sum = 10
# count = 0 
# for i in range(n+1):
#     if sum>0:
#         sum -= m
#         count += 1
# print(count)

# nums = [2,-4,5,-1,2,-3]
# new_dict = {}
# length = len(nums)
# for i in range(length):
#     for j in range(i+1,length+1):
#         new_dict[tuple(nums[i:j])] = sum(nums[i:j])
#         keys = list(new_dict.keys())
#         values = list(new_dict.values())
#         max_index = values.index(max(values))
# # print(keys)
# # print(max(values))
# print(*keys[max_index])


# arr = [-2,1,-3,4,-1,2,1,-5,4]
# length = len(arr)
# dict1 = {}
# for i in range(length):
#     for j in range(i+1,length+1):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_index = values.index(max(values))
# print(max(values))
# print(*keys[max_index])

# arr = [5,7,1,7,6,0]
# length = len(arr)
# list1 = []
# for i in range(length-1):
#     for j in range(i,length):
#         if arr[i] < arr[j]:
#             print(arr[j],end=" ")
#             break
#         elif arr[i] > arr[j]:
#             print(-1,end=" ") 
#             break
# print(-1)

# arr = [0,0,1,1,0]
# sum_index = {0:-1}
# length = len(arr)
# max_legth = 0
# cm_sum = 0
# for i in range(length):
#     if arr[i] == 0 :
#         cm_sum -= 1
#     else:
#         cm_sum +=1
#     if cm_sum in sum_index:
#         max_legth = max(max_legth,i - sum_index[cm_sum])
#     else:
#         sum_index[cm_sum] = 1
# print(max_legth)

# n = 4
# m = 20
# sumeve = 0
# sumodd = 0
# for i in range(m+1):
#     if i%n == 0:
#         sumeve += i
#     else:
#         sumodd += i
# print(sumodd - sumeve)

# arr = [1,8,0,2,3,5,6]
# arr.sort()
# sum_eve = []
# sum_odd = []
# for i in range(len(arr)):
#     if i % 2 == 0:
#         sum_eve.append(arr[i])
#     else:
#         sum_odd.append(arr[i])
# print(sum_eve[-2] + sum_odd[-2])

# arr = [9,8,3,-7,3,9]
# sum = 4
# n = 6
# arr.sort()
# arr1 = arr[0:2]
# sum1 = 0
# div1 = 1
# for i in arr1:
#     sum1 += i
#     if sum > sum1:
#         div1 *= i
#     else:
#         print(0)
#         break
# print(div1)

# seat = input()
# arrangement =input().split()
# index = arrangement.index(seat)
# z = float('inf')
# for i in range(index+1,len(arrangement)):
#     if arrangement[i] == '-':
#         z = min(z,i-1-index)
#         break
# for i in range(index,-1,-1):
#     if arrangement[i] == '-':
#         z = min(z,index-i-1)
#         break
# print(z)

# num = [50,66,23]
# num1 = num[0]
# final_num = 0
# for i in num:
#     if num1 > i :
#         final_num = i
# print("smallest number is",final_num)

# n = 3
# count = 0
# m = 4
# arr = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# print(arr)
# for i in range(len(arr)):
#     print(*sorted(arr[i]))
    
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for i in range(1,i+1):
#         print(" ",end=" ")
#     for i in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 12
# num = 718
# remainder = 0
# divisior = 0
# list = []
# alp = {10:'A',11:'B',12:'C'}
# while num>0:
#     remainder = num % n
#     list.append(remainder)
#     divisior = num // n
#     num = divisior
# print(list)
# for i in list:
#     if i in alp:
#         print(alp[i],end="")
#     else:
#         print(i)

# str1 = "sai-vams-i-"
# count = 0
# res = ""
# for i in range(len(str1)):
#     if str1[i] == '-':
#         count+=1
#     else:
#         res += str1[i]
# print("-" * count+res)

# n1 = "23"
# n2 = "563"
# carry = 0
# count = 0
# if len(n1)<=len(n2):
#     l = len(n1)-1
# else:
#     l = len(n2)-1
# for i in range(l+1):
#     temp = int(n1[l-i]) + int(n2[l-i])+carry
#     if len(str(temp))>1:
#         count+=1
#         carry = 1
#     else:
#         carry = 0
# print(count+carry)

# str1 = "apples"
# res = ""
# for i in str1:
#     if i == "a":
#         res += "p"
#     elif i == "p":
#         res +="a"
#     else:
#         res += i
# print(res)

# print("Enter your choice 1/2/3/4")
# c = int(input())
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
# else:
#     print("Inavalid input")

# m = 100
# n = 160
# list1 = []
# for i in range(m,n+1):
#     if i%3 ==0 and i%5 ==0:
#         list1.append(i)
# print(sum(list1))

# num = 5
# sum = 0
# for i in range(1,10+1):
#     n1 = i*num
#     sum += n1
# print(sum)

# n = int(input())
# a = list(map(int,input().split()))
# t = int(input())
# length = len(a)
# print(t-length)


# n1 = 10
# n2 = 80
# for i in range(n1,n2):
#     reverse = 0
#     temp = i
# while temp != 0:
#     remainder  = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp//10
# if i == reverse:
#     print(reverse,end="")


# n = 5
# arr = [0,1,2,3,4,5]
# count = 0
# for i in range(len(arr) - 2):
#     if arr[i] + arr[i+2] == arr[i+1]:
#         count+=1
# print(count)

# arr = [5,8,3,4,5,8]
# good = True
# for i in range(len(arr)-1):
#     if (arr[i] + arr[i+1])%2 == 0:
#         good = False
#         break
# if good == True:
#     print("Yes")
# else:
#     print("No")
        
# str1 ="saivamsi"
# vowels = 0
# cons = 0
# list1 = ['a','e','i','o','u']
# for i in str1:
#     if i in list1:
#         vowels +=1
#     else:
#         cons +=1
# print("vowels are:-",vowels)
# print("cons are:-",cons)

# x1 ,x2 = 1,1
# y1,y2 = 2,4
# print(pow((x1-x2),2) +pow((y1-y2),2))

# arr = [23,45,82,27,66,12,78,13]
# i = max(arr)
# print(i)
# print(arr.index(i))

# str1 = "1210"
# str1 = str1[::-1]
# list1 = []
# for i in str1:
#     if i not in list1:
#         list1.append(i)
#     else:
#         break
# print(len(list1))

# arr = [5,4,3,2,1]
# count =0 
# for i in range(len(arr)-1):
#     if arr[i]>arr[i+1]:
#         count+=1
# print(count)

# n = 4
# arr = [1,2]
# count =0 
# for i in arr:
#     if i%3 == 0:
#         count+=1
# print(count)

# n = 4 
# list1 = []
# for i in range(1,n+1):
#     list1.append(format(i,'b'))
# print(list1)
# for i in list1:
#     for j in i:
#         if j == '1':
#             i = '2'
#         elif j == '0':
#             i = '1'
#         print(i,end =" ")

# size = 5
# k = 3
# arr = [1,2,3,4,5]
# ans = 0
# for i in range(size- k+1):
#     sub_arr = arr[i:i+k]
#     temp_score = 0
#     for index in range(0,k):
#         temp_score += (index+1) * sub_arr[index]
#     if temp_score>ans:
#         ans = temp_score
# print(ans)

# arr =[1,1,-1,-1]
# count = 0
# sum =0
# for i in arr:
#     sum += i
#     if sum == 0:
#         count+=1
# print(count)


# n = 3
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(f"{j}" * i,end="")
#     print()


# n = 4
# arr = [12,24,36,48,24]
# div = 8
# quoi = 3
# rema = 0
# dividend = div * quoi + rema 
# res = -1
# for i in range(len(arr)):
#     if arr[i] == dividend:
#         res = i
#         break
# print(res)


# first_name = "JOhn"
# last_name = "doE"
# first_name = first_name.lower()
# last_name = last_name.upper()
# print(first_name +" " + last_name)

# n = 12
# temp = n
# e = 3
# d = 30
# count = 1
# days = ['mon','tue','wed','thu','fri','sat','sun']
# for i in range(len(days)):
#     if days[i] !='sun':
#         food = n - e
#         n = food
#         while n <= 0:
#             n = temp
#             count+= 1
# print(count)

# arr = [-1,-2,-3,-4]
# dict1 = {}
# length = len(arr)
# for i in range(len(arr)):
#     for j in range(i+1,length + 1):
#         dict1[tuple(arr[i:j])] = sum(arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
#         max_value = values.index(max(values))
# print(sum(keys[max_value]))

# n = 39
# str1 = "33 milestone is either 12 or 75 km away"
# res = [int(s) for s in str1.split() if s.isdigit()]
# if len(str1) == 0:
#     print(-2)
# elif len(res) == 0:
#     print(-1)
# else:
#     print(max(res))

# arr  = [10,20,30,40,50,60,70,80,90,100]
# positions = [2,3,5,7,11,13,17,19,23,29]
# list = []
# if len(arr) == len(positions):
#     for i in range(len(positions)):
#         j = positions[i] 
#         if j <len(arr):
#             list.append(arr[positions[i]])
# print(sum(list))


# n = 5
# mii = 3.14 * n * n
# print(int(mii))

# str1 = "ABCD"
# vowels = ['A','E','I','O','U']
# list = []
# for i in str1:
#     if i not in vowels:
#         list.append(i)
# print(list)
# dict1={}
# list1 = []
# for i in range(len(list)):
#     for j in range(i+1,len(list)+1):
#         if list[i:j] not in list1:
#             list1.append(list[i:j])
# list1.append(list[::-1])
# print(list1)
# count = 0
# for j in list1:
#     if len(j) >= 2:
#         print(j)
#         count +=1
# print(count)

# list1 = [2,3,4]
# for i in list1:
#     if i % 2 ==0:
#         print("Even",end="")
#     else:
#         print("Odd",end="")

# string = "mercermetti"
# n = input()
# print(string.count(n))

# first = "batta"
# last = "saivamsi"
# print(first.upper(),last.lower())

# res = "11101111011111"
# count  = 0
# ans = ""
# for i in res:
#     if i == "1":
#         count += 1
#     else:
#         if count > 0:
#             ans += chr(64 + count)
#             count = 0
# if count > 0:
#     ans += chr(64 + count)            
# print(ans)

# num = "54"
# sum = 0
# for i in num:
#     sum += int(i)
# if sum ==1 or sum == 2:
#     print("not a prime")
# elif sum>1:
#     for i in range(2,sum):
#         if sum % i == 0:
#             print("No")
#             break
#         else:
#             print("Yes")
# else:
#     print("No")

# sum = 10
# list = []
# for i in range(sum):
#     if i>1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             list.append(i)
# print(list)


# mat = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(mat[0])):
#     print(mat[0][i])
# for i in range(len(mat[0])):
#     print(mat[1][len(mat[1])-1])
#     print(mat[2][len(mat[1])-1])
#     break
# for i in range(len(mat[0])):
#     print(mat[2][i-1])

# n = 6
# arr = [6]
# count = 0
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         count += 1
# print(count)

# arr  = [6]
# count = 0
# for i in arr:
#     if i%3  == 0:
#         count += 1
# print(count)

# arr = [5,3]
# max = 0
# for i in arr:
#     if i>max:
#         max = i
# print(max)

# str1 = "ABC"
# n = 3
# print(str1 * n)

# str1 = "abcd"
# str1 = list(str1)
# list = []
# count = 0
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)+1):
#         list.append(str1[i:j])
#         list.append(str1[::-1])
# for i in list:
#     if i[::-1] == i:
#         count += 1
# print(count)

# str = "my name is saivamsi i am a good boy"
# k = 3
# str = str.split(" ")
# print(str)
# for i in range(k):
#     print(str[i],end=" ")

# string = "  fly me to the moon "
# st = string.split(" ")
# list1 = []
# for i in st:
#     if len(i) == 0:
#         continue
#     else:
#         list1.append(i)
# print(len(list1[-1]))

# arr = [1,2,2,1]
# if arr[::-1] == arr:
#     print("true")
# else:
#     print("false")

# arr = [3,6,9,19]
# diff = 0
# arr.sort()
# for i in range(len(arr)-1):
#     dif = arr[i+1] - arr[i]
#     if dif > diff :
#         diff = dif
# print(diff)

# arr = [1,2,3,4,3,3,5,6,7,8]
# k = 3
# print(arr[-k:] + arr[:-k])

# str = "abcabcbbf"
# list1 = []
# for i in str:
#     if i not in list1:
#         list1.append(i)
#     else:
#         break
# print(len(list1))

# arr = [1,12,-5,-6,50,3]
# k = 4
# list= []
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if len(arr[i:j]) == k: 
#             list.append(arr[i:j])
# print(list)
# max2 = []
# for j in list:
#     max2.append(sum(j)/k)
# print(max(max2))

# arr = [2,3,1,2,4,3]
# k = 7
# list= []
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         list.append(arr[i:j])
# count = 0
# for i in list:
#     if sum(i) >= k and len(i) <= 4:
#         count += 1
# print(count-1)

# arr = [100,4,200,1,3,2]
# arr.sort()
# list1 = []
# for i in range(1,200):
#     if i in arr:
#         list1.append(i) 
#     else:
#         break
# print(list1)

# arr  = [10,20,30,40,50,60,70,80,90,100]
# positions = [2,3,5,7]
# sum1 = 0
# for i in positions:
#     sum1 += arr[i]
# print(sum1)

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# s = "ABC"
# vowels = "aeiouAEIOU"
# count = 0
# for i in range(len(s)):
#     if s[i] not in vowels:
#         count += 1
# ans = factorial(count)
# print(ans)

# num =9
# n1 = 0
# n2 = 1
# for i in range(2,num+1):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
# print(n3,end=" ")

# num = 54
# bin = format(num,'b')
# print(bin)

# arr = "11101011110"
# count  = 0
# for i in arr:
#     if i == '1':
#         count +=1
#     else:
#         print(chr(64 + count),end="")
#         count = 0
# if count > 0:
#     print(chr(64 + count),end="")

# n = "43"
# sum = 0
# for i in n:
#     sum += int(i)
# if sum == 0 or sum == 1:
#     print("No")
# elif sum >1 :
#     for i in range(2,sum):
#         if i % sum == 0:
#             print("No")
#             break
#         else:
#             print("Yes")
#             break
# else:
#     print("No")


# s1 = "abcd"
# s2 = "xyz"
# res = ""
# if s1 not in s2:
#     res += s1
# print(res)

# a = ['a','b','c','d']
# s = ['x','y','z']
# cost = 0
# for char in a:
#     cost1 = float('inf')
#     for let in s:
#         distance = abs(ord(let) - ord(char))
#         if distance<cost1:
#             cost1 = distance
#     cost+= cost1
# print(cost)


# n = "100"
# re = n.replace("00","7")
# re = list(re)
# print(len(re))


# arr = [-1,2,3,10,-4,7,2,-5]
# list = []
# n = []
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)+1):
#         list.append(arr[i:j])
# for i in list:
#     n.append(sum(i))
# print(max(n))

# arr = list(map(int,input().split()))
# sum = 0
# for i in arr:
#     if i%2 == 0:
#         sum += i
# print(sum)

# arr = [18,19,20]
# a ,b , c = 0,0,0
# for i in arr:
#     print(i)
#     if i %3 == 0:
#         a += i//3
#         b += i//3
#         c += i//3
#     elif i % 3 == 1:
#         a += i//3 + 1
#         b += i//3
#         c += i//3
#     elif i % 3 == 2 :
#         a += i//3 + 1
#         b += i//3 + 1
#         c += i//3
# print(a)
# print(b)
# print(c)

# n = 4
# sum = 1
# for i in range(n):
#     for j in range(i+1):
#         print(sum,end=" ")
#         sum += 1
#     print()

# arr = [52,66,64,36,45,24,32]
# list1 = []
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         list1.append(arr[i])
# list1.append(arr[-1])
# print(sum(list1))

# str1 = "yes no number"
# st = str1.split(" ")
# len1 = 0
# for i in st:
#     if len(i) > len1:
#         len1 = len(i)
# ans = ""
# for i in st:
#     if len(i) == len1:
#         print("largest number is:-",i)

# h = 10
# v = 20
# v1 = 5
# e = v/v1
# ans = h * e ** 2
# print(int(ans))

# s1 = "adventure"
# s2  =  "future"
# list1 = []
# list2 = []
# list3 = []
# asci_sum = 0
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)+1):
#         list1.append(s1[i:j])
# for i in range(len(s2)):
#     for j in range(i+1,len(s2)+1):
#         list2.append(s2[i:j])
# for i in list1:
#     for j in list2:
#         if i == j and i not in list3:
#             list3.append(i)
# for i in list3:
#     if len(i) > asci_sum:
#         asci_sum = len(i)
# print(asci_sum)
# for i in list3:
#     if len(i) == asci_sum:
#         j = i
# sum = 0
# for i in j :
#     sum += ord(i)
# print(sum)

# n = 6
# arr = [10,5,6,3,7,2]
# sum_odd = 0
# odd = []
# for i in range(n):
#     if i % 2 != 0 :
#         sum_odd += arr[i]
#     else:
#         odd.append(arr[i])
# print(odd)
# out = odd[0]
# for i in range(1,len(odd)):
#     out = out ^ odd[i]
# sum_even = out
# print(sum_odd -sum_even)


# n = 8
# arr = [1,2,3,4,4,6,5,5,5]
# temp = arr
# arr.sort()
# arr = set(arr)
# arr = list(arr)
# second_last = arr[-2]
# length = temp.count(second_last)
# print(length)

# def choclate_dis(n):
#     ways = 0
#     for b in range(1, n//2+1):
#         for a in range(n//2,n+1):
#             if a+b == n:
#                 if a>b:
#                     ways += 1
#                 else:
#                     continue
#     return ways
# n = 12
# print(choclate_dis(n))

# def palindrome_check(str1):
#     if str1 == str1[::-1]:
#         print("true")
#     else:
#         print("false")
# str1 = "hello"
# palindrome_check(str1)

# str = "saivamsi"
# k = 5
# print(str[:k])

# import math 
# n = 7
# if n<=1:
#     print(0)
# else:
#     print(int(math.sqrt(n)))

# def square_sum(n):
#     total = 0
#     while n > 0:
#         dig = n%10
#         total += dig ** 2
#         n //= 10
#     return total
# def is_happy(num):
#     seen = set()
#     while num!= 1 and num not in seen:
#         seen.add(num)
#         num = square_sum(num)
#     return num == 1
# num = 19
# if is_happy(num):
#     print("True")
# else:
#     print("False")


# str1 = "apples"
# res = ""
# for i in str1:
#     if i == "a":
#         res += "p"
#     elif i == "p":
#         res += "a"
#     else:
#         res += i
# print(res)\\


# x = 3
# y = 6
# arr = [10,3,2,4,5,6,9,7,3]
# length = len(arr)
# list = []
# list1 = []
# final = []
# for i in range(length):
#     for j in range(i+1,length+1):
#         list.append(arr[i:j])
# for i in range(len(list)):
#     if list[i][0] == 3 and list[i][-1] == 6 or list[i][0] == 6 and list[i][-1] == 3 :
#         list1.append(list[i])
# print(list1)
# max_len = 1000000
# for i in list1:
#     if len(i) < max_len:
#         max_len = len(i)
# print(max_len)
# for i in list1:
#     if len(i) == max_len:
#         final.append(i)
# print(final)
# list2 = []
# for i in final:
#     for j in i:
#         if j == 6 or j == 3:
#             continue
#         else:
#             list2.append(j)
# print(len(list2))

# m = 12
# n = 50
# sum = 0
# for i in range(n+1):
#     if i%3 == 0 and i%5 == 0:
#         sum += i
# print(sum)

# n = "1210"
# list =[]
# for i in n:
#     if i not in list:
#         list.append(i)
# print(len(list))

# no_of_garage = int(input())
# m = int(input())
# garage = []
# small_garage = []
# for i in range(no_of_garage):
#     for j in range(m):
#         small_garage.append(int(input()))
#     garage.append(small_garage)
# print(garage)

# n = 7
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for i in range(i,n):
#         print("*",end=" ")
#     print()


# def pyramid(n):
#     if n == 0:
#         return 0
#     if n == 1 :
#         return 2
#     if n >= 2:
#         return 2*n + n - 1 + pyramid(n-1)
# n = 4
# print(pyramid(n) )

# arr = [1,2,3,4,5,6,7]
# max_num =0
# for i in range(len(arr)):
#     if arr[i] > max_num:
#         max_num = arr[i]
#         index = i
# print(max_num)
# print(index)          /


# num = 67
# m = 8
# list = []
# for i in range(1,num+1):
#     if i % m == 0:
#         list.append(i)
# print(max(list))

# arr = [12,34,45,9,8,90,3]
# even = []
# odd =[]
# for i in arr:
#     if i %2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even + odd)

# arr = [1,2,0,0,0,3,6]
# list = []
# list1 = []
# for i in arr:
#     if i == 0:
#         list.append(i)
#     else:
#         list1.append(i)
# print(list1 + list)

# def fact(n):
#     if n == 0:
#         return 1 
#     if n ==1 :
#         return 1
#     else:
#         return n * fact(n-1)
# n = 5
# print(fact(n))

# str = "babdc"
# str = sorted(str)
# dict1 = {}
# list1 =[]
# for i in str:
#     dict1[i] = str.count(i)
# keys = list(dict1.keys())
# values = list(dict1.values())
# print(dict1)
# for i in range(4):
#     list1.append(keys[i])
#     list1.append(values[i])
# for i in list1:
#     print(i,end="")

# str = "a2b2c2d1"
# ip = 5
# num = []
# list =[]
# res = ""
# for i in str:
#     if i.isdigit():
#         num.append(int(i))
#     else:
#         list.append(i)
# for i in range(len(num)):
#     res +=num[i] * list[i]
# print(res[ip])

# num = 350
# list = []
# for i in range(2,num):
#     if num % i == 0:
#         list.append(i)
# print(num - min(list))

# num = 1345
# print(num % 11)

# list1 = [1,2,3,4,5]
# list1.sort()
# max_num =  max(list1)
# min_num = min(list1)
# print(max_num+min_num)

# str ="ABCD"
# length = len(str)
# mul =1
# for i in range(1,length+1):
#     mul *= i
# print(mul)
 

# str = "{{{}}}"
# count1 = 0
# count2 =0
# for i in str:
#     if i == '{':
#         count1 +=1
#     else:
#         count2 += 1
# if count1 == count2 :
#     print("successful")
# else:
#     print("Compliation error")

# n = int(input())
# coins = 0
# list=[]
# for i in range(1,n+1):
#     coins = i ** 2
#     list.append(coins)
# print(sum(list))

# num = [4,3,5,4]
# charge = ['p','n','p','n']
# n = 4
# pos =[]
# neg = []
# for i in range(n):
#     if charge[i] == 'p':
#         pos.append(num[i])
#     else:
#         neg.append(num[i])
# pos_sum = sum(pos)
# neg_sum = sum(neg)
# mun = pos_sum - neg_sum
# print(mun * 100)

# str = "AbCdEfg"
# count1 = 0
# count2 = 0
# for i in str:
#     if i.isupper():
#         count1+=1
#     else:
#         count2 +=1
# if count1 > count2 :
#     print(str.upper())
# else:
#     print(str.lower())

# arr = [1,2,3,4,5,7]
# max_ele = max(arr)
# for i in range(1,max_ele+1):
#     if i not in arr:
#         print(i)

# str = "bB1_p"
# length = 0
# count_dig = 0
# count_upp = 0
# count_slash = 0
# count_space = 0
# dig = [0,1,2,3,4,5,6,7,8,9,10]
# for i in str:
#     length += 1
#     if i.isdigit() :
#         count_dig += 1
#     elif i.isupper():
#         count_upp += 1
#     elif i == '/':
#         count_slash +=1
#     elif i == ' ':
#         count_space +=1
# if length > 4 and count_slash < 1  and count_space <1 and str[0] not in dig and count_upp >= 1 and count_dig >= 1:
#     print("valid")
# else:
#     print("not a valid password")


# str = "saivamsi is a good boy"
# str1 = str.split(" ")
# print(*str1[::-1])

# s = "HTHHTTHTHHHT"
# sum = 0
# count = 0
# for i in s:
#     if i == "H" :
#         sum += 2
#         count += 1
#     elif count == 3:
#         break
#     else:
#         sum -= 1
#         count = 0
# print(sum)

# ip1 = [12,24,35,9]
# ip2 = 8
# ip3 = 3
# ip4 = 0
# ip5 = 4
# max1 = ip2 * ip3
# for i in ip1:
#     if i == max1:
#         j = i
# print(ip1.index(j))

# def dividend(arr,divisor,quotient,remainder):
#     divid = quotient * divisor + remainder
#     if divid in arr:
#         return arr.index(divid)
#     else:
#         return -1
# arr = [4,4,6,8]
# divsior = 1
# quoit = 2
# rem = 0
# print(dividend(arr,divsior,quoit,rem))

# length = 6
# arr = [1,-2,3,-4,6,-4,5,6,9]
# list1 = []
# for i in arr:
#     if i < 0:
#         continue
#     else:
#         list1.append(i)
# n = len(list1) - 1
# print(list1)
# mid = 0 + n 
# mid_val = mid //2
# print(list1[mid_val])

# arr = [2,-3,-14,5]
# sum = 0
# for i in arr:
#     if i < 0:
#         sum += i
# print(sum)


# n = 7
# arr = [5,2,3,4,6,5,-2]
# arr.sort()
# print(arr)
# mid = int(7/2)
# print(mid)
# large = arr[mid+1:]
# final = arr[:mid+1]
# print(large)
# print(final)
# for i in range(len(final) - 1):
#     final.append(large[i])
# print(final)

# arr = [3,2,11,7,6,5,6,1]
# list1 = []
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             list1.append(arr[j])
#             break
# list1.append(-1)
# print(list1)

# n = 5
# m = 6
# a=[6,7,8,11]
# b =[3,1,2]
# min_val = min(a)
# max_val = max(b)
# if max(b) > min(a):
#     print(max_val - min_val)
# else:
#     min_val = max(a)
#     max_val = min(b)
#     print(min_val - max_val)

# n = 3
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         if i == j or i+j ==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(i,n-1):
#         if i == j or i+j ==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i,n):
#         if i == j or i+j ==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(i,n-1):
#         if i == j or i+j ==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# arr = [9,8,3,-7,3,9]
# dict1 = {}
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)+1):
#         if len(arr[i:j]) <= 2 and  len(arr[i:j]) > 1: 
#             dict1[tuple(arr[i:j])] = sum(arr[i:j])
#         keys = list(dict1.keys())
#         values = list(dict1.values())
# print(dict1)
# min_val = min(values)
# index1 = values.index(min_val)
# ans = keys[index1]
# mul = 1
# for i in ans:
#     mul  *= i
# print(mul)

# arr.sort()
# min1 = arr[0]
# min2 = arr[1]
# print(min1 * min2)

# n1 = 100
# n2 = 200
# list = []
# list1 = []
# for i in range(n1,n2+1):
#     list.append(str(i))
# for i in list:
#     if i == i[::-1]:
#         list1.append(i)
# print(list1)


# import math
# x1, y1 = 1, 1
# x2, y2 = 2, 4
# x3, y3 = 3, 6
# first_diff = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
# second_diff = math.sqrt(math.pow(x3-x2, 2) + math.pow(y3-y2, 2))
# third_diff = math.sqrt(math.pow(x3-x1, 2) + math.pow(y3-y1, 2))
# print(round(first_diff,2), round(second_diff,2), round(third_diff,2))

# str1 = "abc,b,cc"
# str2 = str1.split(",")
# length  = 0
# for i in str2:
#     if len(i) > length:
#         length = len(i)
# print(length)

# a = 5
# b = 4
# c = 4
# d = 9
# list1 = []
# list1.append(a)
# list1.append(b)
# list1.append(c)
# list1.append(d)
# list2 = []
# list3 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         j = i
# for i in list1:
#     if i != j:
#         list3.append(i)
# print(sum(list3) - j)

# tot_tic = 5
# prem = 2
# cost = 2
# pre_cost = 3
# norm = tot_tic * cost
# prem_tic_ans = tot_tic / prem
# ans = prem_tic_ans * pre_cost
# if norm == ans:
#     print(norm)
# elif norm > ans:
#     print(round(ans))
# else:
#     print(norm)

# arr = [16,24,32,48,55,64,72]
# sum = 0
# count = 0
# for i in arr:
#     if i%3 == 0 and i%2 == 0:
#         sum += i
#         count+=1
# print(sum//count)


# def is_fair(n,mi,ma,w):
#     total_wei = n * w
#     if mi * n <= total_wei and ma * n >= total_wei:
#         if total_wei % 2 == 0:
#             print("Yes")
#         else:
#             print("No")
# n = 3
# mi = 100
# ma = 200
# weight = 100
# is_fair(n,mi,ma,weight)

# n1 = 675
# n2 = 835
# list1 = []
# for i in range(1,n2+1):
#     if n1 % i == 0 and n2 % i ==0:
#         list1.append(i)
# print(max(list1))


# arr =[16,18,20]
# f2 = sum(arr)
# f1 = 0
# digi = 0
# for i in arr:
#     while i>0:
#         digi = i%10
#         f1+= digi
#         i=i//10
# f1 = f1%10
# f2 = f2%10
# new = f1 - f2
# print(new)

# arr = [-6,10,8,-5,-14,-17,23,-20,-18,-19]
# even = []
# odd = []
# if len(arr) == 0:
#     print("NOne")
# for i in arr:
#     if i > 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd+even)

# arr = [-6,10,8,-5,-14,-17,23,-20,-18,-19]
# neg = 0
# for i in range(len(arr)):
#     if arr[i] < 0:
#         arr.insert(neg,arr.pop(i))
#         neg += 1
# print(*arr)

# str1 = "abciijklma"
# str1 = list(str1)
# print(str1)
# list2 = ""
# for i in range(len(str1)-1):
#     if str1[i] == str1[i+1]:
#         rem = str1[i]
# print(rem)
# for i in str1:
#     if i != rem:
#         list2 +=i
# print(list2)


# arr = [1,2,7,13]
# list=[]
# sum = 0
# for i in range(len(arr)):
#     i = (i+1) ** 2
#     list.append(i) 
# for i in range(len(arr)):
#     sub = list[i]- arr[i]
#     sum+=sub
# print(sum)

# import math
# arr = [3,8,4,2,5,6,7]
# n = 7
# sum1 = sum(arr)/n
# sum2 = 0
# print(sum1)
# for i in range(len(arr)):
#     ans = math.sqrt((i-sum1)**2)/n
#     sum2 += ans
# print(round(sum2))

# arr = [1,2,3,4,5,6,7,8]
# res_rooms = 8
# total_rooms = 10
# print(total_rooms - res_rooms

# a = -3
# b = 7
# c = -1
# d = 4
# list1 = []
# list1.append(a)
# list1.append(b)
# list1.append(c)
# list1.append(d)
# sum = 0
# for i in list1:
#     if i < 0:
#         sum += i
# print(sum)

# arr = [7,-3,8,2,-5,10,12]
# for i in arr:
#     if i<0:
#         arr.remove(i)
# print(arr)
# if len(arr) % 2 == 0:
#     mid = len(arr) //2
#     print(arr[mid-1])
# else:
#     mid = len(arr) //2
#     print(arr[mid])

# str = "sai*vam*s*i"
# ans = ""
# for i in str:
#     if i != "*":
#         ans += i
# print(ans)

# import math
# a1 = 2
# a2 = 12
# b1 =3
# b2 = 5
# hypo1 = math.sqrt(a1**2 + b1 ** 2)
# hypo2= math.sqrt(a2**2 + b2 ** 2)
# print(round(hypo1))
# print(round(hypo2))

# n = 16
# mul = 1
# sum = 0
# if n %2 == 0:
#     dig = 0
#     while n>0:
#         dig = n % 10
#         mul *= dig
#         n = n//10
#     print(mul)
# else:
#     dig = 0
#     while n>0:
#         dig = n % 10
#         sum += dig
#         n = n//10
#     print(sum)

# str1 ="100067"
# ans = ""
# for i in str1:
#     if i == "0":
#         ans += "5"
#     else:
#         ans += i
# print(ans)

# n = 3
# arr = [5,4,15,6]
# m = 5
# count = 0
# for i in arr:
#     if i%5 == 0:
#         count+=1
#     else:
#         m -= i
#         count+=1
# print(count)

# def spiral(arr):
#     ans = []
#     while arr:
#         ans+= arr.pop(0)
#         arr = (list(zip(*arr)))[::-1]
#     return ans
# arr = []
# n,m = (map(int,input().split()))
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# print(*spiral(arr))

# str1 = "abc bcd cda"
# str2 = "abc bc"
# count1 =0
# count2 = 0
# for i in str1:
#     if i ==" ":
#         count1+=1
# for i in str2:
#     if i ==" ":
#         count2+=1
# count = count1-count2
# if count%2==0:
#     print("Even:",count)
# else:
#     print("'Odd:'",count)

# str1 = "reply"
# alp = []
# list1=[]
# for i in range(97,123):
#     alp.append(chr(i))
# print(alp)
# for i in str1:
#     if i in alp:
#         list1.append(alp.index(i)+5)
# print(list1)
# for i in list1:
#     if i > 25:
#         i=(i%25)-1
#         print(alp[i],end="")
#     else:
#         print(alp[i],end="")

# inte = 6
# ext = 3
# list1=['12.3', '15.2', '12.3', '15.2', '12.3', '15.2']
# list2=['10.10', '10.10', '10.00']
# mul1 = 1
# mul2 = 1
# # for i in range(inte):
# #     list1.append(input())
# # print(list1)
# # for i in range(ext):
# #     list2.append(input())
# # print(list2)
# for i in list1:
#     mul1 += float(i) * 18
# print(mul1)
# for i in list2:
#     mul2 += float(i) * 12
# print(mul1 + mul2)

# series =[]
# n = int(input())
# prime = [2,3,5,7,11,13,17,19]
# squ = [1,4,9,16]
# list1=[]
# count = 0
# count1= 0
# for i in range(1,n):
#     if i in prime:
#         list1.append(2**count)
#         count += 1
#     elif i in squ:
#         list1.append(3 ** count1)
#         count1 +=1
#     else:
#         list1.append(0)
# print(list1)
# for i in range(len(list1)):
#     if i == 0:
#         list1[i] = list1[i-2] + list1[i-1]
#     print(list1)

# str1 = "AdfTu34"
# cap =[]
# nor = []
# num = []
# key = 2
# ans = ""
# for i in range(65,91):
#     cap.append(chr(i))
# print(cap)
# for i in range(97,123):
#     nor.append(chr(i))
# print(nor)
# for i in range(48,58):
#     num.append(chr(i))
# print(num)
# for i in str1:
#     if i in cap:
#         ans += (i + key) 
#     elif i in nor:
#         ans += i 
#     else:
#         ans += i
# print(ans)

# str1 = "AdyZ89"
# ans = []
# key = 2
# for i in str1:
#     ans.append(ord(i)+ key)
# print(ans)
# for i in ans:
#     print(chr(i),end="")

# height = 10
# velocity = 20
# bounce = 5
# en = velocity/bounce
# formula = height * pow(en,2)
# print(int(formula))

# n = 4
# for i in range(n):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print()

# def square_sum(n):
#     sum1 = 0
#     while n>0:
#         dig = n % 10
#         sum1 += dig ** 2
#         n = n//10
#     return sum1
# def is_happy(num):
#     seen = set()
#     while num != 1 and num not in seen:
#         seen.add(num)
#         num = square_sum(num)
#     return num == 1
# num = int(input())
# if is_happy(num):
#     print("True")
# else:
#     print("False")

# num = 371
# num = str(num)
# mul = 0
# for i in num:
#     mul += int(i) ** 3
# print(mul)
# if int(mul) == int(num):
#     print("Armstrong number")
# else:
#     print("Not an armstrong number")

# str1 = "saivamsivamsi"
# k = 5
# print(str1[:k])

# num = 4
# list1= ['ab', 'xyz', 'aab', 'axb']
# fist = list1[0][0]
# sec = list1[0][1]
# print(fist)
# count = 0
# print(sec)
# for i in list1:
#     if fist and sec in i :
#         count += 1
# print(count)

# num1 = 1000000
# num2 = -1000
# if num1 < -10000 or num1 > 10000:
#     print(-1)
#     exit()
# elif num2 < -10000 or num2 > 10000:
#     print(-1)
#     exit()
# else:
#     print(num1 + num2) 

# n = 4
# trees = [-2,3,5,8]
# m = 2
# sprinkers = [1,6] 
# list1 = trees + sprinkers
# list1.sort()
# diff1 = 0
# diff2 = 0
# final = []
# for i in range(len(list1)):
#     if list1[i] in sprinkers:
#         final.append(list1[i] - list1[i-1])
#         final.append(list1[i+1] - list1[i])
# print(max(final))

# n = 9
# str1 = "abcdefggh"
# list1=[]
# count = 0
# for i in range(len(str1)):
#     for j in range(i,len(str1)):
#         if len(str1[i:j]) == 4:
#             list1.append(str1[i:j])
# print(list1)
# for i in range(len(list1)):
#     if list1[i]

#1,2,3,5,7
# num1 = 1
# num2 = 100
# count = 0
# for i in range(num1,num2+1):
#     for j in range(1,i):
#         if i % j == 0:
#             count += 1
#     if count <= 1 :
#         print(i,end=" ")
#     count = 0

# n = 5
# sum = 1
# for i in range(n):
#     for j in range(i+1):
#         print(sum,end=" ")
#         sum += 1
#     print()

# 0 1 1 2 3 5 7

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fib(n-2) + fib(n-1)
# n = 4
# print(fib(n))

# str1 = "abccbaacz"
# for i in range(len(str1)):
#     if str1[i] == str1[i-1]:
#         print(str1[i])
#         break
        
# a = 5
# b = 9
# c = "1010"
# num1 = int(c,2)
# num1 = format(a,'b')
# num2 = format(b,'b')
# print(num1)
# print(num2)
# print(a | b)


# num1 = 5
# num2 = 7
# num3 = num1 * num2
# num4 = num3 % 24
# print(num4)

# arr = [4,5,6,7,8,4]
# list = []
# for i in range(len(arr)):
#     if i%2 == 0:
#         list.append(arr[i])
# print(list)
# ans = sum(list) / len(list)
# print(int(ans))

# div = 8
# quo = 7
# rem = 1
# divi = div * quo + rem
# print(divi)

# n = 4
# list1 = ['teama','teamb','teama','teamb','teama']
# ans1 = list1.count('teama')
# ans2 = list1.count('teamb')
# if ans1 == ans2:
#     print(1)
# elif ans1 > ans2:
#     print('teama')
# else:
#     print('teamb')

# arr  = [8,3,4,1,6,2]
# arr.sort()
# print(arr[1])

# a = 10
# num1 = format(a,'b')
# sum = 0
# for i in range(len(num1)):
#     sum = sum + int(num1[i])
# print(sum)

# stri  = "this is saivamsi"
# let = 'i'
# print(stri.count(let))

# arr = [1,2,6,3,5,3]
# list1 = []
# list2 = []
# for i in arr:
#     if i % 2  == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list2+list1)

# a = "he ll o w or ld"
# b = "hello world"
# counta = 0
# countb = 0
# for i in a:
#     if i == " ":
#         counta += 1
# for j in b:
#     if j == " ":
#         countb +=1
# ans = counta + countb
# if ans%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# n = 3
# arr = ["hello","ccbc","aaeiou"]
# vowels = ['a','e','i','o','u']
# count = 0
# list= []
# for i in range(n):
#     for j in arr[i]:
#         if j not in vowels:
#             count += 1
#     list.append(count)
#     count = 0
# print(list)
# list1 = []
# for i in list:
#     if i == 0 :
#         list1.append(1)
#     else:
#         for j in range(1,i):
#             i = i * j
#         list1.append(i)
# print(max(list1))

# n = 10
# arr = [1,2,3,4,5,6,7,8,9,10]
# k = 4
# list1 = []
# list2 = []
# for i in range(n):
#     if i < 4:
#         list1.append(arr[i])
#     elif i == 4:
#         continue
#     else:
#         list2.append(arr[i])
# print(sum(list2) - sum(list1))

# arr1 = [1,2,3]
# arr2 = [1,1]
# count = 0
# list =[]
# for i in arr1:
#     for j in arr2:
#         if i == j:
#             list.append(i)
# print(max(list))

# n = 5
# arr = [6,4,1,15,5]
# m = 5
# ans = 0
# arr.sort()
# count = 0
# count1 = 0
# for i in arr:
#     if i%n == 0:
#         count+=1
# for i in arr:
#     ans = ans +i
#     count1 += 1
#     if ans > m:
#         break
# print(count + count1-1)

# arr =[2,58,58,2,60,60,60]
# count = 0
# sum = 0
# for i in arr:
#     sum = sum + i
#     if sum >= 60:
#         count += 1
#         sum = 0
# print(count-1)

# def fib(n):
#     if n <= 1:
#         return n
#     if n > 1:
#         return fib(n-1) + fib(n-2)
# n = 6
# print(fib(n))

# s ="RGB"
# t ="RRR"
# for i in range(len(s)):
#     if s[i] != t[i]:
#         print(i+1)
#         break

# arr =[12,24,3,5,6,7,8,9,18]
# sum = 0
# count = 0
# for i in arr:
#     if i % 3 == 0 and i % 2== 0:
#         count += 1
#         sum = sum +i
# print(int(sum/count))

# arr = [3,3,4,4,4,5,5]
# point = 0
# arr1  = max(arr)
# print(arr1)
# max1 = arr1+1
# min1 = arr1 - 1
# for i in arr:
#     if min1 == i:
#         arr.remove(i)
#     elif max1 == i:
#         arr.remove(i)
# print(arr)


# dice = 3
# arr = [1,2,3,4]
# list1 = []
# list2 = []
# if dice % 2 == 0:
#     for i in arr:
#         if i % 2 ==0:
#             list1.append(i)
#     print(sum(list1))
# else:
#     for i in arr:
#         if i % 2 != 0:
#             list2.append(i)
#     print(sum(list2))


# str = "applesarefallingfromthrskies"
# vowels = ['a','e','i','o','u']
# out = ""
# out1 = ""
# for i in range(len(str)):
#     if str[1] in vowels:
#         out1 += str[1]
#     elif str[i] in vowels and str[i-1] and str[i+1] not in vowels:
#         out += str[i]
#     else:
#         out1 += str[i]
# print(out1,end=" ")

# str = "saivamsi"
# c = input()
# count = 0
# for i in str:
#     if i == c:
#         count +=  1
# print(count)

# s= "abbccdee"
# vowels = ['a','e','i','o','u']
# count = 0
# for i in s:
#     if i not in vowels:
#         count += 1
# print(count)

# arr = [1,2,2,3,2,3]
# arr.sort()
# count = 0
# list = []
# for i in arr:
#     if i not in list:
#         list.append(i)
# ele = list[-2]
# for i in arr:
#     if i == ele :
#         count += 1
# print(count)

# arr = [1,2,2,3]
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         print("Even",end= "")
#     else:
#         print("odd",end= "")

# arr = [1,2,3,4,5,6,7]
# k = 4
# print(arr[-k:] + arr[:-k])

# num = 14
# bin = format(num,'b')
# print(bin)
# sum = 0
# for i in bin:
#     sum = sum + int(i)
# print(sum)

# arr = [5,4,3,1,2]
# arr.sort()
# print(arr[-2])

# l = 5
# print(3.14*l*l)

# str = "hello.world.from.saivamsi"
# len = 0
# max_len = 0


# arr = [1,2,3,4,5,6]
# arr.reverse()
# sum = 0
# for i in range(len(arr)):
#     if i % 2== 0 :
#         sum = sum + arr[i]
# print(sum)
