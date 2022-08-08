#1541 - 잃어버린 괄호
#시간복잡도 계산 과정


#입력
s = input()
ls=[]
num=''
for i in s:
    if i=='-' or i=='+':
        ls.append(int(num))
        num=''
        ls.append(i)
    else:
        num+=i
if num!='':
    ls.append(int(num))


plus=0
minus=0
flag=True
for i in range(len(ls)):
    if ls[i]=='+':
        continue
    if ls[i]!='-':
        if flag==True:
            plus+=ls[i]
        else:
            minus+=ls[i]
    elif ls[i]=='-':
        flag=False
#출력
print(plus-minus)


