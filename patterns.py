# 2 loops 
# outer loop - rows
# inner loop - columns

#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

# n=int(input("Enter number:-"))
# for i in range(n):
#     for j in range(i+1):
#         print(" *",end="")
#     print("")


#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

# n=int(input("Enter number:-"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(" *",end="")
#     print("")

#  1
#  2 2
#  3 3 3
#  4 4 4 4
#  5 5 5 5 5

# n=int(input("Enter number:-"))
# for i in range(1,6):
#     for j in range(i):
#         print("",i,end="")
#     print()


# 5 5 5 5 5
#  4 4 4 4
#  3 3 3
#  2 2
#  1

# n=int(input("Enter number:-"))
# for i in range(5,0,-1):
#     for j in range(i):
#         print("",i,end="")
#     print()

# 1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5

# n=int(input("Enter number:-"))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("",j,end="")
#     print()

#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1

# n=int(input("Enter number:-"))
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("",j,end="")
#     print()


#  1
#  2 3 4
#  5 6 7 8 9
#  10 11 12 13 14 15 16

# n=int(input("Enter number:-"))
# col = 1
# num = 1
# for i in range(1,n):
#     for j in range(1,col+1):
#         print("",num,end="")
#         num=num+1
#     col = col + 2
#     print()

#  1
#  1 2 1
#  1 2 3 2 1
#  1 2 3 4 3 2 1
#  1 2 3 4 5 4 3 2 1

# n=int(input("Enter number:-"))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("",j,end="")
#     for k in range(j-1,0,-1):
#         print("",k,end="")
#     print()

#              * 
#           *  *
#        *  *  *
#     *  *  *  *
#  *  *  *  *  *

# n=int(input("Enter number:-"))
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end="  ")
#     for k in range(1,i+1):
#         print(" *",end=" ")
#     print()

#  *  *  *  *  * 
#     *  *  *  *
#        *  *  *
#           *  *
#              *
# n=int(input("Enter number:-"))
# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end="  ")
#     for k in range(1,i+1):
#         print(" *",end=" ")
#     print()


# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(5):
#     for j in range(i,5):
#         print("*",end=" ")
#     print()

# * * * * * 
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()

#  * * * * * 
#     * * * *
#       * * *
#         * *
#           *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     for l in range(i):
#         print("*",end=" ")
#     print()

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     for l in range(i,n-1):
#         print("*",end=" ")
#     print()

#   * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     for l in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     for l in range(i,n-1):
#         print("*",end=" ")
#     print()

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     for l in range(i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print('',end="")
#     print()

# *   * 
# *   *
# *   *
# *   *
# *   *

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print("*",end=" ")
#         else:
#             print('',end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==j or i+j==n-1):
#             print("*",end=" ")
#         else:
#             print('',end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print('',end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("  *",end= " ")
#     print()

    #         * 
    #       *   *
    #     *   *   *
    #   *   *   *   *
    # *   *   *   *   *
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("  *",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("  *",end=" ")
#     print()

    # *   *   *   *   * 
    #   *   *   *   *
    #     *   *   *
    #       *   *
    #         *
    #         *
    #       *   *
    #     *   *   *
    #   *   *   *   *
    # *   *   *   *   *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     for l in range(2*(n-i)):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for l in range(i+1):
#         print("   ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()

# *                     * 
# * *                 * *
# * * *             * * *
# * * * *         * * * *
# * * * * *     * * * * *
# * * * * *     * * * * *
# * * * *         * * * *
# * * *             * * *
# * *                 * *
# *                     *

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1: 
#             print(" *",end="")
#         else:
#             print(" ",end=" ")
#     print()

#  * * * * *
#  *       *
#  *       *
#  *       *
#  * * * * *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for l in range(i+1):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for k in range(i,n-1):
#         print(" ",end=" ")
#     for l in range(i+1):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

#           *                 * 
#         * * *             * * *
#       * * * * *         * * * * *
#     * * * * * * *     * * * * * * *
#   * * * * * * * * * * * * * * * * * *

# n=5
# count=0
# for i in range(1,n+1):
#     for j in range(i):
#         count=count+1
#         print(count,end=" ")
#     print()