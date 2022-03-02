n = int(input("Enter how many apples you have : "))
mn = int(input("Enter two numbers for dividing apple"))
mx = int(input())
if mn==mx :
    print("this is not a range")

for i in range(mn,mx+1) :
    check_no = n%i
    if check_no == 0 :
        print(f"You can give apple {n/i} apple to {i} students or vice-versa")
    elif check_no != 0 :
        print(f"You can't divide {n} apple into student {i}")

