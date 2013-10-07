# Kirk Sefchik
# UTA ID 1000814472
# 10/03/13
# Description: Show all the actions and states that the machine (the computer) goes through as it runs the folowing program. You must show the state after each instruction is executed.

L = []
x = 13
count = 0
while x > 0:
    if (x % 4) == 0:
        x = x // 2
    else:
        if (x % 3) == 0:
            x = x // 3
        else:
            x = x - 1        
    print(count, x)
    L.append([count,x])
    count = count + 1
    
print(count, x)
print("L: ",L)
print("Bye")
