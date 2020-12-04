print("Hello! My name is Chitti.")
print("I was created in 2020.")
print("Please, remind me your name.")
your_name = input()
print("What a great name you have, " + your_name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(your_age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
count = 0
while count <= num:
    print(str(count) + "!")
    count += 1
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")


def ans_check():
    num = int(input())
    if num == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")
        ans_check()

ans_check()



