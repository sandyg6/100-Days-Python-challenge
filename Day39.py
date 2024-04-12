month = int(input('Enter the month: '))
year = int(input('Enter the year: '))
if(month == 2 and (year%400 == 0) or ((year%100 != 0) and (year%4 == 0))):
    print('Number of days is 29')
elif(month == 2):
    print('Number of days is 28')
elif(month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12):
    print('Number of days is 31')
else:
    print('Number of days is 30')
