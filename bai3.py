'''
Bài 3:Viết chườn trình nhập vào toạ độ (xC,yC) là tâm của một 
đường tròn, và R là bán kính đường tròn đó.Nhập vào toạ độ (xM,yM)
của điểm M. Xác định điểm M nằm trong hay nằm ngoài đường tròn.
'''
import math
print('Nhập toạ độ điểm tâm C(xC,yC)')
xC = float(input())
yC = float(input())
R = float(input('Nhập bán kính R : '))
print('Nhập toạ độ điểm M(xM,yM)')
xM = float(input())
yM = float(input())
S = math.sqrt((xM - xC)**2 + (yM - yC)**2)  
if S < R:
    print("M nằm trong đường tròn")
elif S > R:
    print("M nằm ngoài đường tròn")
else:
    print("M nằm trên đường tròn")
    
