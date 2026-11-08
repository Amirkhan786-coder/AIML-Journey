print("----conditions----")

print("1.----if statement----")
age = 20
if age >= 18:
    print("You are eligible to vote.")


print("2.----if-else statement----")
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print("3.----if-elif-else statement----")
age = 20
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are not eligible to vote, but you can register to vote.")
else:
    print("You are not eligible to vote.")


print("4.----nested if statement----")
age = 20
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible for certain benefits.")
else:
    print("You are not eligible to vote.")


print("5.----ternary operator----")
age = 20
is_eligible = "You are eligible to vote." if age >= 18 else "You are not eligible to vote."
print(is_eligible)
