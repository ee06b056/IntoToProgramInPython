inputCount = 10
maxInput = None
while inputCount != 0:
    input = int(raw_input('Please input: '))
    if input % 2 == 1:
        if maxInput == None or maxInput < input:
            maxInput = input
    inputCount -= 1
if maxInput == None:
    print('No odd number inputed.')
else:
    print(maxInput)
