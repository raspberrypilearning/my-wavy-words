from turtle import *
from random import randint

line1 = list('my wavy words')  # List from a string
line2 = list('growing up')  
line3 = list('falling down')  
line4 = list('moving round and ')  

penup()
hideturtle()
style1 = ('Courier', 16)
style2 = ('Times New Roman', 14)

# down line
goto(-170, 100)
right(90)
for i in range(len(line1)):  #  Gets length of a list
    write(line1[i], font=style1, align='center')
    forward(15)

# up line
forward(30)
left(90)
forward(30)
left(90)
for i in range(len(line2)): 
    write(line2[i], font=style1, align='center')
    right(randint(-5,5))
    forward(15)
 
# falling down
right(120)
forward(30)
color('green')
for i in range(len(line3)): 
    write(line3[i], font=style1, align='center')
    forward(randint(15,20))
    right(randint(2,3))

# circle here
goto(80, 100)
color('orange')
for i in range(len(line4)):
    write(line4[i], font=style2, align='center')
    forward(20)
    right(360 / len(line4)) #  turn fraction of a circle
