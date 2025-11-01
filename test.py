#1. Check if a number is even or odd
a = int(input("Enter any number :"))
if a%2== 0:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")
    print()

#2. Check if a number is positive, negative, or zero
while True:
    a = int(input("Enter any number :"))
    if a > 0:
        print(f"{a} is Positive Number")
    elif a<0:
        print(f"{a} is Negative Number")
    else:
        print(f"{a}is Zero ")
        break

#3. Find the largest of three numbers
a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
if a>b and a>c:
    print(f"{a} is Largest Number ")
elif b>a and b>c:
    print(f"{b} is Largest Number ")
elif c>a and c>b:
    print(f"{c} is Largest Number ")
else:
    print("All are Equal Number ")

#4. Check if a year is a leap year
while True:
    a = int(input("Enter any year :"))
    if a%4==0:
        print(f"{a} is Leap Year ")
    else:
        print(f"{a} is Not a Leap Year ")
        break

#5. Determine grade from marks
while True:
    a = int(input("Enter numbers:"))
    if a >= 60:
        print(f"Grade is A")
    elif a >= 35:
        print(f"Grade is C")
    elif a >= 45:
        print(f"Grade is B")
    elif a>= 80:
        print(f"Grade is A+")
    else:
        print("Fail")
        break
        
#6. Check if a character is a vowel or consonant
while True:
    v = ['a', 'e', 'i', 'o', 'u']
    a = input("Enter a letter ")
    if a.lower() in v:
        print(f"{a} is Vowel ")
    else:
        print(f"{a} is consonent ")
    choice = input("Would you check more ( Yes/No)").strip()
    if choice=="yes":
        continue
    else:
        break

#7. Find whether a number is divisible by 5 and 11
while True:
    a = int(input("Enter any number :"))
    if a%5==0 and a%11==0:
        print(f"{a} is divisiable number by 5 and 11")
    else:
        print(f"{a} is not divisiable number by 5 and 11")
    choice = input("Would you check more ? (Yes/No)").strip()
    if choice== "yes":
        continue
    else:
        break

#8.  Check if a character is uppercase or lowercase
while True:
    a = input("Enter character ")
    if a.islower():
        print(f"{a} is lowercase character")
    elif a.isupper():
        print(f"{a} is uppercase character")
    else:
        print(f"{a} is not an uppercase or lowercase alphabetic character")
    choice = input("Need more checks, (Yes/No)").strip().lower()
    if choice == "yes":
        continue
    else:
        break


#9.  Check if a number is in a given range
while True:
    i = int(input("Enter any number :"))
    if i in range(1,100):
        print(f"{i} is in Range")
    else:
        print(i, "is out of Range")
        break
        
#10. Print "Hello" if a number is less than 100

a = int(input("Enter your number :"))
if a < 100:
    print(" Hellow")
else:
    print("Niklow")
    
#11. Check eligibility to vote
while True:
    a = int(input("Enter you Age :"))
    if a >= 18:
        print("Eligible to Cast a Voat")
    else:
        print("Your are not Eligible for Voting")
        break

17.	Determine triangle type (isosceles, scalene, equilateral)
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")

18.	Check if a number is Armstrong
num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

19.	Convert temperature Celsius to Fahrenheit and vice versa
choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? ").upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid input. Please choose 'C' or 'F'.")

20.	Find the profit or loss on selling a product.
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit of {profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss of {loss}")
else:
    print("No profit, no loss")

#12. Check if a number is a multiple of 3 or 7
while True:
    num = int(input("Enter your number: "))
    if num % 3 == 0 and num % 7 == 0:
        print(f"{num} is a multiple of both 3 and 7")
    elif num % 3 == 0:
        print(f"{num} is a multiple of 3")
    elif num % 7 == 0:
        print(f"{num} is a multiple of 7")
    else:
        print(f"{num} is not a multiple of 3 or 7")
    choice = input("Check More Multiples (Yes/No): ").strip().lower()
    if choice != "yes":
        break

#13. Determine the quadrant of a point (x, y) 
def determine_quadrant(x, y):
    if x == 0 and y == 0:
        return "The point is at the origin."
    elif x == 0:
        return "The point lies on the y-axis."
    elif y == 0:
        return "The point lies on the x-axis."
    elif x > 0 and y > 0:
        return "The point lies in Quadrant I."
    elif x < 0 and y > 0:
        return "The point lies in Quadrant II."
    elif x < 0 and y < 0:
        return "The point lies in Quadrant III."
    elif x > 0 and y < 0:
        return "The point lies in Quadrant IV."

def main():
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    result = determine_quadrant(x, y)
    print(result)

if __name__ == "__main__":
    main()

#15. Check if a year is a century year
while True:
    year = int(input("Enter any year :"))
    if year%100==0:
        print(f"{year} is a Century Year")
    else:
        print(f"{year} is not a Century Year")
    choice = input("Check  More? (Yes/No)").strip().lower()
    if choice != "yes":
        break
    
#16. Check if a triangle is valid (angle sum = 180)
a = int(input("Enter angel A value :"))
b = int(input("Enter angel B value :"))
c = int(input("Enter angel C value :"))
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("This is a Valid Triangel ")
else:
    print("This is not a Valid Triangel ")
    
'''Grading System with Nested Conditions:
17. Determine a student's grade based on score ranges with nested if-else—for example,
if score > 90 then "A", if between 80 and 90 check further for "A-" or "B+", else lower grades accordingly.​'''

Math = int(input("Enter you Obtain Marks in Math :"))
Physics = int(input("Enter you Obtain Marks in Physics :"))
Chemistry = int(input("Enter you Obtain Marks in Chemistry :"))
Biology = int(input("Enter you Obtain Marks in Biology :"))
SST = int(input("Enter you Obtain Marks in SST :"))
Hindi = int(input("Enter you Obtain Marks in Hindi :"))
English = int(input("Enter you Obtain Marks in English :"))
Total_Marks = 700
Total_Obtain_Marks = Math+Physics+Chemistry+Biology+SST+Hindi+English
Percentage = (Total_Obtain_Marks/Total_Marks)*100
if Percentage > 90:
    Grade = "A"
elif 80 < Percentage <= 90:
    Grade = "B+"
elif 75 < Percentage <= 80:
    Grade = "B"
elif 60 < Percentage <= 75:
    Grade = "C"
elif 45 < Percentage <= 60:
    Grade = "D"
else:
    Grade = "Fail"
print(f"Total Marks Obtained: {Total_Obtain_Marks}")
print(f"Percentage: {Percentage:.2f}%")
print(f"Grade: {Grade}")

#Leap Year Checker:
#Write a program that checks if a given year is a leap year using if-else statements considering
#the rules for leap years (divisible by 4, but not 100 unless also divisible by 400).​
year = int(input("Enter any year :"))
if year%4==0 and year%100 !=0 or year%400==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# Another Method
count = 0
print("Leap years between 2000 and 3000 are:")
for year in range(2000, 3001):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year,end=" ")
        count += 1
print(f"Total number of leap years: {count}")

















