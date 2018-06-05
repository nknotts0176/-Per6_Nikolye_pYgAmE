from gpiozero import Button
left_button = Button(2)
right_button = Button(3)



#What I need to do:
#- code it so that buttons give a true/false input depending on if they're being pushed
#- then they have to return whatever direction they're being pushed in
#- then we have to code Nik's game to recognize that and move with it

def move(left, right):
    if left.is_pressed:
        print("Left")

    if right.is_pressed:
         print("Right")


while True:
    move(left_button, right_button)
