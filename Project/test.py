result = [0, 0, 0]
diff = 22
for a in range(int(200/21.99) + 1):
    for b in range(int((200 - 21.99*a)//18.05)+1):
        c = int((200 - 21.99 * a - 18.05 * b)//15.99) + 1
        if diff > (21.99 * a + 18.05 * b + 15.99 * c - 200):
            diff = 21.99 * a + 18.05 * b + 15.99 * c - 200
            result = [a, b, c]

print(result)
print(diff)