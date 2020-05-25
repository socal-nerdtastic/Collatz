while True:
    try:
        userNum = int(input("Type an integer:  "))
        break
    except:
        print("Error: Invalid entry. Try again.")

steps = 0
def Collatz(num):
    global steps
    cnum = num
    if cnum == 1:
        print("returned")
        return steps
    else:
        if cnum % 2 == 0:
            cnum = cnum/2
        else:
            cnum = (3*cnum)+1
        steps += 1
        return Collatz(cnum)

print(Collatz(userNum))
