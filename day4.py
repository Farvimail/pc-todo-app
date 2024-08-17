

for i in range(1,4):
    for j in range(1,4):
        print("*" , end="")
    print()

#
# size = 5  # اندازه‌ی مربع را انتخاب کنید
#
# for i in range(size):
#         for j in range(size):
#             print('*', end=' ')
#         print()
#
# n=10
# for i in range(1,n):
#     for j in range(i):
#         print("*", end="")
#     print()


list = [1,9,2,5,5,5,58,6,4,7]
number= int(input ("Enter a number of list :"))
new=input ("Enter a new :")
list[number] =new
print(list)
for item in list :
    print (item)
