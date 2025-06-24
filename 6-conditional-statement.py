#make greading system

Marks = int(input('give your marks:'));

if Marks >= 90:
    print('A+');
elif 80 <= Marks and Marks < 90:
    print('A');
elif 70 <= Marks and Marks < 80:
    print('B');
elif 60 <= Marks and Marks < 70:
    print('C');
elif 50 <= Marks and Marks < 60:
    print('D')
elif 40<= Marks and Marks < 50:
    print('E');
else:
    print('fail');