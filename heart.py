import time
name = input("Enter your Name: ")
finalName = name

k=0
z=0
flag=0
l=len(name)
for i in range(0,15):
    for j in range(0,50):
        if (i>=0 and i<=1) or (i>=13 and i<=14):
            if j>13:
                print(name[k%l],end='')
                k+=1
            else:
                print(' ',end='')
            flag=0
        else:
            if j==30 or j==31 or j==32:
                print(name[z%l],end='')
                flag=1
            else:
                print(' ',end='')
    if(flag==1):
        z+=1
    
    print()

for y in range(15, -15, -1):
    for x in range(-30, 30):
        if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0:
            print(''.join((finalName[(x-y) % len(finalName)])),end='')
        else:
            print(' ',end='')
    print()
k=0
z=0
flag=0
l=len(name)
for i in range(0,20):
    for j in range(0,50):
        if (i==16):
            if j>15 and j<48:
                print(name[k%l],end='')
                k+=1
            else:
                print(' ',end='')
            flag=0
        elif i==17:
            if j>17 and j<46:
                print(name[k%l],end='')
                k+=1
            else:
                print(' ',end='')
            flag=0
        elif i==18:
            if j>19 and j<44:
                print(name[k%l],end='')
                k+=1
            else:
                print(' ',end='')
            flag=0
        elif i==19:
            if j>21 and j<42:
                print(name[k%l],end='')
                k+=1
            else:
                print(' ',end='')
            flag=0
        else:
            if j==14 or j==15 or j==16 or j==47 or j==48 or j==49:
                print(name[z%l],end='')
                flag=1
            else:
                print(' ',end='')
    if(flag==1):
        z+=1
    
    print()
print("\n\n\n\n\n")
print("                                              ",end='')
for i in " @Rt By PoOrNa ChAnDrA rEdDy....!  :)":
    time.sleep(0.10)
    print(i,end='')
print("\n\n\n\n\n")
