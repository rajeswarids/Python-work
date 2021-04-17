from datetime import date

x = int(input("Year :"))
y = int(input("Month :"))
z = int(input("Day :"))
d = date(x, y, z)20
print(d)


def year():
    if 1599 < x < 1700:
        return 6
    elif 1699 < x < 1800:
        return 4
    elif 1799 < x < 1900:
        return 2
    elif 1899 < x < 2000:
        return 0
    elif 1999 < x < 3000:
        return 6


def month():
    if y == 1:
        return 0
    elif y == 2:
        return 3
    elif y == 3:
        return 3
    elif y == 4:
        return 6
    elif y == 5:
        return 1
    elif y == 6:
        return 4
    elif y == 7:
        return 6
    elif y == 8:
        return 2
    elif y == 9:
        return 5
    elif y == 10:
        return 0
    elif y == 11:
        return 3
    elif y == 12:
        return 5


year1 = year()
month1 = month()
lastwo = x % 100
dbyfour = lastwo // 4

yourday = (lastwo + dbyfour + year1 + z + month1) % 7

if y == 2:
    yourday = yourday + 6


def yday():
    if yourday == 0 or yourday == 7:
        print("Sunday")
    elif yourday == 1 or yourday == 8:
        print("Monday")
    elif yourday == 2 or yourday == 9:
        print("Tuesday")
    elif yourday == 3 or yourday == 10:
        print("Wednesday")
    elif yourday == 4 or yourday == 11:
        print("Thursday")
    elif yourday == 5 or yourday == 12:
        print("Friday")
    elif yourday == 6 or yourday == 13:
        print("Saturday")


yday()
