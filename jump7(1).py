i=1
while i<101:
    a = int(input("请您输入一个数字:"))
    if a%7==0 or a%10==7 or a//10==7:
        print("跳过")
    else:
        print(a)
    i+=1