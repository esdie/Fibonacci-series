a,b=0,1
while True:
    try:
        print('Enter n value: ')
        n=int(input())
        break
    except:
        print('Please enter an integer value')
for i in range(n):
    print(a,end=' ')
    b,a=a+b,b
