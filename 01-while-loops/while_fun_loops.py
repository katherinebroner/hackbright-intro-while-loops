# count = 1
# while count < 21:
#     print count
#     count += 1

# count = 1
# while count < 21:
#     if count == 13:
#         print "hello"
#     else:
#         print count
#     count += 1

# count = 0
# while count < 101:
#     print count 
#     count += 10

# count = 0
# while count <= 10:
#     if count % 2 != 0:
#         print count
#     count += 1

# count = 10
# while count >= 0 and count <=10:
#     if count == 0:
#         print "Blastoff!"
#     else:     
#         print count
#     count -= 1

# fruits = ["apples", "oranges", "bananas"]
# index = 0
# while index < len(fruits):
#     print fruits[index] 
#     index += 1

# def sum_nums(num):
#     count = 0
#     num_sum = 0
#     while count < num:
#         num_sum += count
#         count += 1   
#     return num_sum

# print sum_nums(3)

# def sum_nums(num):
#     count = 0
#     num_sum = 0
#     while count <= num:
#         num_sum += count
#         count += 1   
#     return num_sum

# print sum_nums(3)

# def sum_nums2(num):
#     count = 0
#     num_sum = 0
#     while count != num:
#         if count >= num:
#             count -= 1
#             num_sum += count
#         else:
#            count += 1
#            num_sum += count
#     return num_sum

# print sum_nums2(-3)

def fizz_buzz():
    count = 0
    while count < 101:
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print "FizzBuzz"
        elif count %3 == 0 :
            print "Fizz"
        elif count % 5 == 0:
            print "Buzz"
        else:
            print count

fizz_buzz()





