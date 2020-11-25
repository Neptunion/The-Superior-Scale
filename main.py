import sys,time,os,math,string
print("y/n")
s = input()
while s == "y":
    print("enter big number")
    print("end number with x to make it bigger")
    alphabetList = list(string.ascii_lowercase)
    vowelList = [0,4,8,14,20]
    i = input()
    if i.endswith("x"):
        i = i[:-1]
        print("times 10^what?")
        x = input()
        ix = int(i)*(10**int(x))
    else:
        ix = float(i)
    if (ix == math.inf):
        ix = int(i)
    if (ix != math.inf):
        sys.stdout.write("b")
        for x in range(25):
            sys.stdout.write("r")
            sys.stdout.flush()
            time.sleep(0.01)
        f = False
        n=int(round((math.log(ix,10))/3,0)-1)
        print(" ")
        if (n>=0):    
            front=str(round(int(ix)/10**(3*(n+1)),2))
            if front.endswith('.0'):
                front= front[:-2]
            vowel = [vowelList[min(math.floor(max((n/25)-1,0)),4)]]
            print("db",math.floor(max((n/25)-1,0)))
            print("db",ix,n,front,vowel)
            print(front, end=" ")
            z=0
            while n > 25:
                z+=1
                n -= 26
                if z > 4:
                  vowel.append("n")
                  vowel.append(vowelList[z-5])
                if z == 9:
                    z = 0
            if n == 0:
                f = True
            if f == False:
                print(str(alphabetList[n]), end="")
            for x in range(len(vowel)):
                m = x
                m = min(len(vowel)-1,m)
                if vowel[m] == "n":
                    if f == False:
                        vowel[m] = n
                    else:
                        vowel[m] = "/"
            for x in range(len(vowel)):
                try:
                    print(str(alphabetList[vowel[x]]), end="")
                except:
                    print(vowel[x],end="")
            if f == True:
                print("llium")
            else:
                print("lliun")
        else:
            print("number too small")  
    else:
        print("scientific notation number too big, uses 0s")
    print("~~~~~~~~~~~~~~~~~~~")
