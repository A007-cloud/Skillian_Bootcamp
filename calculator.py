#calculator

num1 = int(input('Enter first number:'));
num2 =int(input('Enter second number:'));

operator = input('Enter operation(+,-,*,/):');

if operator == "+":
    ans = num1 + num2;
elif operator == "-":
    ans = num1 - num2;
elif operator == "*":
    ans = num1 * num2;
elif operator == "/":
    ans = num1 / num2;

print(ans);