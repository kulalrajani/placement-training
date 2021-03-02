#To print the pattern
#   * * * * * * * * * * *
#   * *               * *
#   *   *           *   *
#   *     *       *     *
#   *       *   *       *
#   *         0         *
#   *       *   *       *
#   *     *       *     *
#   *   *           *   *
#   * *               * *
#   * * * * * * * * * * *


n = int(input("Enter a value : "))

for i in range(1,n+1):
    if i == 1 or i == n: 
        for j in range(1,n+1):
            print("*",end=" ")
    else:
        for j in range(1,n+1):
            if j == 1 or j == n:
                print("*",end=" ")
            else:
                if i == j and i == n // 2+1:
                    print("BTS",end=" ")
                elif i == j or j == n - i + 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    print("")
