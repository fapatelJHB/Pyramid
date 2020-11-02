

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    while shape != "pyramid" and shape != "square" and shape != "triangle" and shape != "diamond" and shape != "rhombus" and shape != "rectangle":
        shape = input("Shape?: ").lower()
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    while height.isdigit() == False or int(height)>80:
        height = input("Height?: ")
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if (outline == True):
        for i in range(1, height+1):
            for j in range(1, 2*height):
                if i == height or i + j ==height+1 or j - i == height-1:
                    print ("*", end = "") 
                elif j - i > height-1:
                    pass
                else:
                    print(" ", end="")
            print()
    else:
        for i in range (1, height+1):
            print(" "*(height-i) + "*" *(2*i-1))


# TODO: Step 3
def draw_square(height, outline):
    if (outline == True):
        for i in range(1, height+1):
            if i == 1:
                print('*' * (height))
            elif i == height:
                print('*' * (height))
            else:
                print("*" + " " * (height-2) + "*")
    else:
        for i in range(1, height+1):
            print ('*' *height)


# TODO: Step 4
def draw_triangle(height, outline):
    if (outline == True):
        if height == 1:
            print("*")
        else:
            print("*")
            print("**")
            var = 1
            storeHeight = height
            while height > 3:
                print("*" + (" " * var) + "*")
                var += 1
                height -= 1
            print("*" * storeHeight)
    else:
        for i in range (1, height+1):
            print('*'*i)


# TODO: Steps 2 to 4, 6 - add support for other shapes

def draw_rhombus(height, outline):
   if (outline == True):
        for i in range(1, height+1):
                if i == 1:
                    print(' ' * (height-1)+'*' * (height))
                elif i == height:
                    print('*' * (height))
                else:
                    print(" " * (height-i) + "*" + " " * (height-2) + "*")

   else:
        for i in range (1, height+1):
            print(" "*(height-i) + "*" *(height))
        

def draw_diamond(height, outline):
    if (outline == True):
        for i in range(height-1):
            print (" " *(height-i-1)+ "*", end="")
            if i >= 1:
                print(" " *(2*i-1)+ "*", end="")
            print()
        for i in range (height):
            print (" " *i+ "*", end = "")
            if i != height-1:
                print(" " *(2*height-2*i-3)+ "*", end="")
            print()
    else:
        for i in range(height):
            print(' '*(height-i-1)+'* '*(i+1))
        for i in range (height-1):
            print(' '*(i+1)+ '* ' * (height-i-1)) 

def draw_rectangle(height, outline):
    if (outline == True):
        for i in range(1, height+1):
            if i == 1:
                print(('*'*2) * (height))
            elif i == height:
                print(('*'*2) * (height))
            else:
                print("*" + (" "*2) *(height-1) + "*")
    else:
        for i in range(1, height+1):
            print ('* ' *(height*2))

def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    if shape == "square":
        draw_square(height, outline)
    if shape == "triangle":
        draw_triangle(height, outline)
    if shape == "diamond":
        draw_diamond(height, outline)
    if shape == "rhombus":
        draw_rhombus(height, outline)
    if shape == "rectangle":
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N) :").lower()
    if outline =="y":
        return True
    else:
        return False
    return outline


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

