# Accept a list of 5 float numbers as an input from the user

a=[]
for i in range(1,6):
    print("Enter number",i,":")
    #Accept float number from the user
    num=float(input())
    a.append(num)
print("User number list :",a)