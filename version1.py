############################    STORAGE Algorithm     ###########################
# Version 1

import pandas as pd
from openpyxl import Workbook

wb = Workbook(); ws = wb.active
df = pd.read_excel('/set/your/path/walmartSales.xlsx', sheet_name='Walmart sales')
# Decide where to save the data
path = "/set/your/path/walmart_version1.xlsx"
d={i[0]:i[1].split() for i in df.values}

for g in d:
    for k,f in enumerate(d[g]):
        d[g][k]=int(f)
# Transform numbers into letters
def letters(x):
    y=str(x)
    if len(y)==1: l='zabcdefghi'[int(y)]
    else:
         l='';
         for i in y: l+='zabcdefghi'[int(i)]
    return l
# Transform letters back into numbers
def InvLetters(x):
    n=''
    for i in x:
        for j in range(10):
            if i=='zabcdefghi'[j]:
                n+=str(j)
                break
    return int(n)



q=1
for b in d:
    x=d[b]
    last=' ';kk=0;k=kk+1;
    while k<=len(x):   
        kk=k-1;k=kk+1;
        while x[kk:k]==[x[kk]]*(k-kk):     k=k+1
        if last[-1].isdigit() and ((k-kk-1) > 1 or x[kk] > 9):   last += f' {x[kk]}{letters(k-kk-1)}'
        elif (k-kk-1)>1 or x[kk]>9 : last+=f'{x[kk]}{letters(k-kk-1)}'
        else: last+=f'{x[kk]}'
    last=last[1:];   ws[f'A{q}'] = b;   ws[f'B{q}'] = last;q+=1
    # This code below verifies if I can return to the initial data
c=[];g=0
while g<len(last)-1:
        for i in range(g+1,len(last)+1):
            if i==len(last) or last[i].isdigit() and not last[i-1].isdigit():  break
        todo=last[g:i];g=i;
        if todo[-1]==' ':c+=[int(h) for h in todo[:-1]]
        elif not todo[-1].isdigit() and todo[-1]!=' ':
            k=0
            while todo[k].isdigit(): k=k+1
            c+=[int(todo[:k])]*InvLetters(todo[k:])
        else: c+=[int(h) for h in todo]
if g<len(last): c+=[int(h) for h in last[g:]]
if x!=c: print(b)
wb.save(path)
print(f"Process completed! File saved in: {path}")