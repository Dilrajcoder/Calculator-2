exp=input("Enter:")
num=[]
ops=[]
y=''
for x in exp:
    if(x=='+' or x=='-' or x=='*' or x=='/'):
        num.append(int(y))
        ops.append(x)
        y=''
        continue
    else:
        y+=x
num.append(int(y))
a=0
b=0
while(len(ops)>0):
    if(ops[a]=='/' or ops[a]=='*'):
        if(ops[a]=='/'):
            b=num[a]/num[a+1]
        else:
            b=num[a]*num[a+1]
        num[a]=b
        num.pop(a+1)
        ops.pop(a)
        a=0
    else:
        if((a+1 < len(ops)) and(ops[a+1]=='/' or ops[a+1]=='*')):
            a=a+1
            # if(ops[a]=='/'):
            #     b=num[a]/num[a+1]
            # else:
            #     b=num[a]*num[a+1]
            # num[a]=b
            # num.pop(a+1)
            # ops.pop(a)
            # a=0
        else:
            if ops[a]=='+':
                b=num[a]+num[a+1]
            else:
                b=num[a]-num[a+1]
            num[a]=b
            num.pop(a+1)
            ops.pop(a)
print(num[0])
