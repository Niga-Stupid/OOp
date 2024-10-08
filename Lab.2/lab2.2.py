def pattern1(n, current=1):
    if current < n:
        print('*' * current)
        pattern1(n, current + 1)

def pattern2(n):
    if n > 0:
        print('*' * n)
        pattern2(n - 1)

def pattern3(n, current=0):
    if current < n:
        print(' ' * (n - current - 1) + '*' * (2 * current + 1))
        pattern3(n, current + 1)

def pattern4(n, current=0):
    if current < n:
        print(' ' * current + '*' * (2 * (n - current) - 1))
        pattern4(n, current + 1)

def patterns(n):
    pattern1(n)
    print()
    pattern2(n)
    print()
    pattern3(n)
    print()
    pattern4(n)

# รับค่า n และ row จากผู้ใช้
n = int(input("Enter value for n: "))


# เรียกใช้งานฟังก์ชัน patterns() ด้วยค่าที่ผู้ใช้ป้อนเข้ามา
patterns(n)
