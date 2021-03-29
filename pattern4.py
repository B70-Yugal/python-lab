'''
****
***
**
*
'''
n=eval(input('enter number of rows'))
for i in range(1,n+1):
    print((n+1-i)*'*')
'''
****
 ***
  **
   *
'''
m=eval(input('enter number of rows'))
for i in range(1,m+1):
    print((i-1)*' '+(m+1-i)*'*')