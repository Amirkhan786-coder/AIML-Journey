print("----loops----")

print("1.----for loop----")
for i in range(5):
    print(i)

print("range() Function")

for i in range(2, 10, 2):
    print(i)

print("2.----while loop----")
i = 1
while i <= 5:
    print(i)
    i += 1

print("break Statement")
for i in range(10):
    if i == 5:
        break
    print(i)

print("continue Statement")
for i in range(10):
    if i == 5:
        continue
    print(i)

print("pass Statement")
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)

print("----Nested Loops----")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")