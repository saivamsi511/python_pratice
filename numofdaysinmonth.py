year = int(input())
month="feb"
if (year%4==0 and year%100!=0) or year%400 ==0:
    print("leap year")
    if month=="januvary" or month =="march" or month == "may" or month == "july" or month == "augest" or month =="october" or month == "december":
        print("31 days")
    elif month == "feb":
        print("28 days")
    else:
        print("30 days")
else:
    print("not a leap year")
    if month=="januvary" or month =="march" or month == "may" or month == "july" or month == "augest" or month =="october" or month == "december":
        print("31 days")
    elif month == "feb":
        print("29 days")
    else:
        print("30 days")
