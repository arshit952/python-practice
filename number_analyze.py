
def analyze(x):
    print("\nAnalysis Result")
    print("----------------")
    if x%2==0:
        print("the number is even")
    else:
        print("The number is odd")
    if num>0:
        print("The number is positive")
    elif num<0:
        print("tne number is negative")
    
num=int(input("Enter the number you want to analyze"))
analyze(num)