# def add_two_vlue(x, y):
#     return x + y


# num_1 = 10
# num_2 = 12
# sum = add_two_vlue(num_1, num_2)
# print(f"{num_1} + {num_2} = {sum}")


# ---------------------------
# --- Arithmethic operators
# ---------------------------

# x = 20
# y = 30
# add = x + y
# sub = x - y
# multiply = x * y
# division = x / 5
# division_result = x // 2
# division_remainder = x % 2

# print(f"Addition: {add}")
# print(f"Substraction: {sub}")
# print(f"Multiply: {multiply} ")
# print(f"Divission: {division} ")
# print(f"Division_result: {division_result}")
# print(f"Division_remainder: {division_remainder} ")


# ---------------------------
# --- List in python
# ---------------------------

# grocery_list = ['Rice', 'Potato', 'Banana', 'Tometo']

# print(grocery_list[-1])
# grocery_list.sort()
# print(grocery_list)

# numbers = [20, -12, 34, 3, 54, 2, 1]
# numbers.sort()
# print(numbers)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)


# ---------------------------
# --- Condition in python
# ---------------------------

# marks = int(input('Enter You Mark: '))


# def show_grade(grade):
#     print(f"You Have Got {grade}")


# if marks >= 80:
#     show_grade("A+")
# elif marks < 80 and marks >= 70:
#     show_grade("A")
# elif marks < 70 and marks >= 60:
#     show_grade("A-")
# elif marks >= 33:
#     show_grade("Passed")
# else:
#     show_grade("F")


# ---------------------------
# --- Loop in python
# ---------------------------

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# starting = 0
# while starting < 50:
#     if is_even(starting):
#         print(f"{starting} is Even")
#     else:
#         print(f"{starting} is Odd")

#     starting += 1


# starting = 0
# even_numbers = []
# limit = int(input("Enter a number: "))
# while starting <= limit:
#     if is_even(starting):
#         even_numbers.append(starting)

#     starting += 1


# print(even_numbers)
# print('Loop Is Done')

# grocery = ['Rice', 'Potato', 'Tomato', 'Banana']

# for i in range(0, len(grocery)):
#     print(grocery[i])

# for i in grocery:
#     print(i)


# ---------------------------
# --- File system in python
# ---------------------------

# with open("test.txt", mode="r") as test_file:
#     for line in test_file.readlines():
#         print(line.strip())


# with open("test.txt", mode="r") as test_file:
#     all_words = []
#     for line in test_file.readlines():
#         words = line.strip().split(" ")
#         all_words += words
#     print(all_words)
#     print(len(all_words))

# print('Done')


# with open("test.txt", mode="r") as test_file:
#     all_words = []
#     for line in test_file.readlines():
#         words = line.strip().split(" ")
#         all_words += words
#     uniq_words = set(all_words)
#     print(uniq_words)
#     print(len(uniq_words))
#     print(len(all_words))

# print('Done')


# with open("test.txt", mode="r") as test_file:
#     all_words = []
#     for line in test_file.readlines():
#         words = line.strip().split(" ")
#         all_words += words
#     uniq_words = set(all_words)

#     with open('uniq_words.txt', mode="w") as write_file:
#         for word in sorted(uniq_words):
#             write_file.write(word)
#             write_file.write("\n")

# print('Done')


# ---------------------------
# --- Prime Number system in python
# ---------------------------

# import math
# user_number = int(input("Upper limit for prime: "))


# def is_prime(num):
#     for i in range(2, int(math.sqrt(num) + 1)):
#         if num % i == 0:
#             return False
#     return True


# for i in range(2, user_number + 1):
#     if is_prime(i):
#         print(i)
