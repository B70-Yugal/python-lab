'''
    *
   * *
  *   *
 *     *
*       *
'''
n=eval(input("enter the rows"))
m=0
n-=1
print(' '*(n-m)+'*')
for i in range(1,n+1):
    print(' '*(n-i)+'*'+' '*i+' '*(i-1)+'*')
