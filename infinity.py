s=(-78,-96,45)
f1=s1=float("-inf")
for i in s:
    if i>f1:
        s1=f1
        f1=i
    elif i>s1 and i!=f1:
        s1=i
print(s1) 
