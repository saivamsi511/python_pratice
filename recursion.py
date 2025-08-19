# # Recusion:-a function calling itself
# # entity ->call function

# def sayhi():
#     print("hi")
#     sayhi()
# sayhi()

# # o/p:hi 
# # hi 
# # hi 
# # .
# # .
# # .
# # hi
# ex:factorial
# n! = n*n-1*n-2*n-3....
# fact(n) = n*n-1*n-2*n-3. ... 3*2*1
# fact(n-1) = n-1*n-2*n-3. ... 3*2*1
# fact(n) = n*fact(n-1)

# Recursion

# base ccondition

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
