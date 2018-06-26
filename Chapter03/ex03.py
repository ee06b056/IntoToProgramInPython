x = int(input('Enter: '))
epsilon = 0.01
ans = x/2.0
numGuesses = 0
while abs(ans**2 - x) >= epsilon:
    ans = ans - (ans**2 - x)/(2*ans)
    numGuesses += 1
print('numGuesses: ',numGuesses)
print('Answer: ', ans)