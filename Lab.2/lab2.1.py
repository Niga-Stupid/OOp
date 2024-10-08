row = int (input('Enter numder : '))



for i in range(1, row+1):
    print('*' * i)
print()



for i in range (row,0,-1):    #range(star,stop,step)
    print('*' *i)
print()


for i in range(row):
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))
print()


for i in range(row , 0, -1):
    print(' ' * (row - i) + '*' * (2 * i - 1))
print()   
