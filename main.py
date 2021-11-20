# Initial Values
term = 1
total = 0
n = 1

# The while loop
while term > 0.0000000000001:
    term = 1/n**2
    n += 1
    total += term

# The answer
print("Total:", total)

#Quit
quit()