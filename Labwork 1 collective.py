import math
def ex1():
    r = float(input("Enter radius(r):"))
    s = float(r*r*3.14)
    if r < 0:
        print("Sorry, the radius must be positive")
    else:
        print("Your number is:", s)

def ex2():
    c = float(input("Degrees in celsius(C):"))
    f = float((c*1.8)+32)
    print("Your degrees in Fahrenheit is:", f)

def ex3():
    n = int(input("Input a prime number:"))
    if n < 2:
        is_prime = False
        is_prime = True
        for i in range(1, int(math.sqrt(n)+1)):
            if(n % i ==0):
                is_prime = False
                break

        if is_prime:
            print(n,"is a prime.")
        else:
            print("Invalid number.")

def ex4():
    a = int(input("Input any integer:"))
    def get_divisors(a):
        if a <= 0:
            return []
        divisors = []
        for i in range(1, int(math.sqrt(a)) + 1):
            if a % i == 0:
                divisors.append(i)     
                if i != a // i:
                    divisors.append(a // i)        
        return sorted(divisors)

    divisors = [1]
    for i in divisors:
        sum += 1
    if sum == a:
        print("It's perfect.")
    else:
        print("It ain't perfect.")

def ex5():
    colors = ("Red", "Yellow", "Blue", "Green")
    Coloure = input("What is your favorite color?")
    for i in range (0, len(colors)):
        if Coloure.lower() == colors[i]:
            print("Your color is at index {i+1} in my list")
            break
    print("Sorry, can't find your color.")

def ex6():
    range1 = range(0, 6+1, 1)
    range2 = range(1, 10+1, 3)
    range3 = range(5, 1-1, -1)
    range4 = range(6, -2-1, -2)
    print(f"range1: {list(range1)}")
    print(f"range2: {list(range2)}")
    print(f"range3: {list(range3)}")
    print(f"range4: {list(range4)}")

def ex7():
    Yarn = input("Enter a string with dollar signs ($):")
    NewYarn = "" 
    b = 0
    for i in range(0, len(Yarn)):
        if Yarn[i] == '$':
            NewYarn += Yarn[b:i]
            b = i + 1
    NewYarn += Yarn[b:]
    print("The new string is", NewYarn)

def ex8():
    user_input = list(input("Enter a list of integers:").split(""))
    even_digits = []
    for i in user_input:
        if int(i) % 2 == 0:
            even_digits.append(i)
    print("The new string is", even_digits)

def ex9():
    def factorial(n):
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")     
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    n = int(input("Insert your number (n) :"))
    factorial(n)
    print(factorial(n))

def ex10():
    user_input = int(input("Enter a number:"))
    num = user_input
    if(num<0):
        print("Not a positive integer, try again.")
    divisors = [1]
    for i in range (2, int(num/2)+1):
        if (num % i ==0):
            divisors.append(i)

    print(f"Divisors of {num} is {divisors}.")

def ex11():
    a = int(input("Input x coordinates of point 1:"))
    b = int(input("Input y coordinates of point 1:"))
    c = int(input("Input x coordinates of point 2:"))
    d = int(input("Input y coordinates of point 1:"))
    point1 = [a,b]
    point2 = [c,d]

    distance = math.dist(point1, point2)
    print(f"The distance is: {distance:.4f}")

def ex12():
    InputW = int(input("Insert height of m?:"))
    m = InputW
    InputH = int(input("Insert width of n?:"))
    n = InputH

    for i in range(0,m):
        for j in range (0,n):
            if(i==0 or i == m-1):
                print('*',end="")
            elif(j==0 or j == m-1):
                print('*',end="")
            else:
                print(' ',end="")
        print(' ')



def main():
    ex1()
    #ex2()
    #ex3()
    #ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()
    #ex11()
    #ex12()
    #REMINDER: remove the # from the begining of the specific program you want to run