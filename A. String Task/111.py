str=input().strip()
yuan=["a","e","i","o","u","A","E","I","O","U",'y',"Y"]
resuit=[]
for i in str:
    if i not in yuan:
        iw=i.lower()
        resuit.append(f'.{iw}')
print(''.join(resuit))