a={1:1,2:2,3:3};
b=''
for i in a.values():
    if b == '':
       b=str(i);
    else:
       b=b+','+str(i);
print b
