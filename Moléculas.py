import turtle
from time import sleep

count = 1


# NEXT STEP ADDDDDDDDDDDDDDDDDDD 2 SUS

def sus_len(x, direction, count=0):
    if direction == 'Up':
        turtle.left(45)
    if direction == 'Down':
        turtle.right(45)
    count = 1
    for i in range(x):
        if count == x:  # this break only here since this for is the foward statement
            print('first brek')
            break
        turtle.forward(50)
        count += 1
        turtle.right(90)
        if count == x:  # this break only here since this for is the foward statement
            break
        turtle.forward(50)
        count += 1
        turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    if x % 2 == 1:
        print('retocede')
        for i in range(count):  # going back statement
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.right(90)
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.left(90)
        turtle.forward(50)
        if direction == 'Up':
            turtle.left(135)
        if direction == 'Down':
            turtle.right(135)
    if x % 2 == 0:
        print('xx')
        for i in range(count):  # going back statement
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.left(90)
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.right(90)
        turtle.forward(50)
        if direction == 'Up':
            turtle.left(135)
        if direction == 'Down':
            turtle.right(135)



# this function is just to go up an down, i still need to work on this, dont midn for now
def straight(x):
    if x == 'Up':
        turtle.left(90)
        turtle.forward(50)
    if x == 'Down':
        turtle.right(90)
        turtle.forward(50)


# this function is to attach the sus on the main chain
# the main chain function has the message for invalid sus_loc
def ch(number, sus_loc=0, sus_type=0, sus_loc_nd=0, count=1):
    down = 'Down'
    up = 'Up'
    print(str(sus_loc) + ' = sus_loc')
    print(str(sus_type) + ' = sus_len')
    print(str(sus_loc_nd) + ' = sus_loc_nd')
    # if the number is 1 dont do anything since methane is just a dot

    if number == 1:
        turtle.left(90)
        pass
    # for number of Carbons do up and down until number of carbons == count
    for i in range(number):
        # this is to avoid changing chain size, if sus_len to large chain name changes
        if sus_type > sus_loc:
            print('Invalid, Sus will change the chain name.\nsus_loc must be greater than sus_len')
            break
        if sus_type > number - sus_loc:
            print('Invalid, Sus will change the chain name.\nsus_len cant be greater than number - sus_loc')
            break
        # if C number is reached
        if count == number:
            turtle.shape('circle')
            turtle.shapesize(0.5)
            break
        straight(up)
        count += 1
        # if sus_loc == count then proceed to create the sus_len sus
        if sus_loc == count:
            sus_len(sus_type, up)
        if sus_loc_nd == count:
            sus_len(sus_type, up)
        # if sus == count CHECK THIS
        for n in range(number):
            # for number of C
            if count == number:
                turtle.shape('circle')
                turtle.shapesize(0.5)
                break
            straight(down)
            count += 1
            # start sus creation in position = count
            if sus_loc == count:
                sus_len(sus_type, down)
            if sus_loc_nd == count:
                sus_len(sus_type, down)
            break
    # variable global count if count == carbonos: stop!


def name_check(x):
    if met in x:
        return 1
    if et in x:
        return 2
    if prop in x:
        return 3
    if but in x:
        return 4
    if pent in x:
        return 5
    if hex in x:
        return 6
    if hept in x:
        return 7
    if oct in x:
        return 8
    if non in x:
        return 9
    if dec in x:
        return 10
    if ico in x:
        return 20


def number_of_carbons_on_main_chaing(x):
    # if the name is just a simple chain
    # prefix = [met, et, prop, but, pent, hex, hept, oct, non, dec, 'Icosane'] # fix this part because we are supposed to use vars not strings
    if len(name) == 1:
        if met in name[0]:
            ch(x)
        if et in name[0]:
            ch(x)
        if prop in name[0]:
            ch(x)
        if but in name[0]:
            ch(x)
        if pent in name[0]:
            ch(x)
        if hex in name[0]:
            ch(x)
        if hept in name[0]:
            ch(x)
        if oct in name[0]:
            ch(x)
        if non in name[0]:
            ch(x)
        if ico in name[0]:
            ch(x)
    # if the name has 3 characters on it must be sus location-susType-chain#
    if len(name) == 3:
        if name[-3] == 0:
            ch(x)
        #         print('invalid, sus_loc cant be first nor final ')
        ch(x, int(name[-3]), name_check(name[-2]))

    if len(name) == 4:
        ch(x, int(name[-3]), name_check(name[-2]), int(name[-4]))


print('please input the name of the molecule in format\nnumber-substituentName-chain(ending in ane only)\nor\nnumber-number-(prefix)substituentName-chain(ending in ane only)')
molecule = input(': ')

name = []
numbers = range(1, 20)
dash = '-'
comma = ','
if dash in molecule:
    molecule = molecule.replace('-', ' ')
if comma in molecule:
    molecule = molecule.replace(',', '')
molecule_split = molecule.split()

for i in molecule_split:
    name.append(i.capitalize())

print(name)
print(name[-1])

met = 'Meth'
et = 'Eth'
prop = 'Prop'
but = 'But'
pent = 'Pent'
hex = 'Hex'
hept = 'Hept'
oct = 'Oct'
non = 'Non'
dec = 'Dec'
undec = 'Undec'
dodec = 'Dodec'
hexdec = 'hexadec'
octadec = 'octadec'
ico = 'Ico'
left = 'left'.capitalize()
right = 'right'.capitalize()
screen = turtle.Screen()
screen_x = 800
screen_y = 600
screen.setup(screen_x, screen_y)
turtle.penup()
turtle.shape()
turtle.shapesize(1.5)
turtle.goto(-screen_x / 2 + 50, 0)
turtle.pensize(2)
turtle.speed(10)
turtle.pendown()
turtle.right(45)

if met in name[-1]:
    number_of_carbons_on_main_chaing(1)

if et in name[-1]:
    number_of_carbons_on_main_chaing(2)

if prop in name[-1]:
    number_of_carbons_on_main_chaing(3)

if but in name[-1]:
    number_of_carbons_on_main_chaing(4)

if pent in name[-1]:
    number_of_carbons_on_main_chaing(5)

if hex in name[-1]:
    number_of_carbons_on_main_chaing(6)

if hept in name[-1]:
    number_of_carbons_on_main_chaing(7)

if oct in name[-1]:
    number_of_carbons_on_main_chaing(8)

if non in name[-1]:
    number_of_carbons_on_main_chaing(9)

if dec in name[-1]:
    number_of_carbons_on_main_chaing(10)

# i am not activating this because undec has dec so it will recognized as 10 not 11, i still need to fix this
# if undec in name[-1]:
#     number_of_carbons_on_main_chaing(11)
#
# if dodec in name[-1]:
#     number_of_carbons_on_main_chaing(12)
#
# if hexdec in name[-1]:
#     number_of_carbons_on_main_chaing(16)
#
# if octadec in name[-1]:
#     number_of_carbons_on_main_chaing(18)

if ico in name[-1]:
    number_of_carbons_on_main_chaing(20)

screen.mainloop()