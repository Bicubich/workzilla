print("Введите год(1900...2100) и месяц(1...12):")
yy = int(input())
mm = int(input())
if yy > 2100 or yy < 1900 or mm < 1 or mm > 12:
    print("Неверный ввод, попробуйте ещё!")
    print("Введите год(1900...2100) и месяц(1...12):")
    yy = int(input())
    mm = int(input())
month ={1:'янв', 2:'фев', 3:'март', 
        4:'апр', 5:'май', 6:'июн', 7:'июл',
        8:'авг', 9:'сен', 10:'окт',
        11:'ноя', 12:'дек'}
   
# code below for calculation of odd days
day =(yy-1)% 400
day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
day = day % 7
  
nly =[31, 28, 31, 30, 31, 30, 
      31, 31, 30, 31, 30, 31]
ly =[31, 29, 31, 30, 31, 30, 
     31, 31, 30, 31, 30, 31]
s = 0
  
if yy % 4 == 0:
    for i in range(mm-1):
        s+= ly[i]
else:
    for i in range(mm-1):
        s+= nly[i]
  
day += s % 7
day = day % 7
   
# variable used for white space filling 
# where date not present
space =''
space = space.rjust(2, ' ')
  
# code below is to print the calendar
print(month[mm], yy)
print('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
  
if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
    for i in range(31 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
elif mm == 2:
    if yy % 4 == 0:
        p = 30
    else:
        p = 29
          
    for i in range(p + day):
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print() 
else:
    for i in range(32 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()