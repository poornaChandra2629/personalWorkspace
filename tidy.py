t = int(input())
for case in range(1,t+1):
    string = input()
    i=len(string)-1;
    length = len(string)
    summ=0
    while(i>0):
        if(string[i]<string[i-1]):
            string = int(string)-(int(string[i])*(10*(length-i-1))+summ+1)
            string = str(string)
            summ=10**(length-i)-1
        else:
            summ = (int(string[i])*(10*(length-i-1)))+summ
        i-=1
    if(i==0):
        print("Case #{}: {}".format(case,string))