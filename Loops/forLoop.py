
# n = int(input("Enter a number: " ))
# sum = 0
# for i in range(n):
 
#     print("Hello ", i)
#     sum +=i +1
#     print("sum till now is: ", sum)



# print("Final sum is : ", sum)


# arr =[2,4,6]
# sum=0
# for i in arr:
#     sum +=i
# print("Sum is : ", sum)

n = int(input("Enter a number: " ))

str = ""
for i in range(0,n):
   
   if(i%2==0):
      str +="0"

   else:
      str +="*"
   
print(str)
