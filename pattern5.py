'''
*****
 ***
  *
'''
n=eval(input("enter rows"))
for i in range(1,n+1):
    print((i-1)*' '+(n+1-i)*'*'+(n-i)*'*')
