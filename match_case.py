num=int(input("Enter the first number"))
op=input("Enter the operation")
num2=int(input("Enter the 2nd number"))
match op:
    case("+"):
        print("sum is:",num+num2)
    case("-"):
        print("result is:",num-num2)
    case("*"):
        print("result is:",num*num2)
    case("/"):
        print("result is:",num/num2)
    case("%"):
        print("result is:",num%num2)
    case(""):
        print("Invalid input")