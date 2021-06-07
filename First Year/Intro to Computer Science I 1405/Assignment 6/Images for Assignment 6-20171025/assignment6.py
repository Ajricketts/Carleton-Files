import pygame
from sys import argv

def instruc():
    print("\n\nFor this program to work, you first need to provide two filenames,")
    print("one for the background image and one for the ghost image.")
    print("This will be done using command line arguments, the first command line argument you")
    print("give being the background image and the second being the ghost image.")
    print("Next the program will ask you for x and y co-ordinates on the background image")
    print("where it should center the ghost image.")
    print("Once all those are given, the program will run and overlay your ghost image")
    print("on top of the background\n")
    pygame.time.wait(2000)

# First task, ask the user if they require instructions.
print("\nDo you need instructions on what you'll need to give the computer in")
print("order for it to copy the ghost image on to your background?")
instruc_needed = input("\nNeed Instructions? (yes or no): ").upper()

# This will print the instructions if the user needs them, if not it will move on to the program.
if instruc_needed == "YES":
    instruc()
else:
    print("On to the program then...")

background = "abandoned_circus.bmp"    # This will set the images the user specified
ghost = "ghost_with_crutches.bmp" # in comand line arguments to variables.

back_surface = pygame.image.load(background) # Loads the images in to the program.
ghost_surface = pygame.image.load(ghost)

back_size = back_surface.get_rect().size  # Sets the dimensions of each picture to variables for future use.
ghost_size = ghost_surface.get_rect().size

screen = pygame.display.set_mode(back_size)
screen.blit(back_surface, (0,0))          # Creates the screen and copies the background image on to it.
pygame.display.update()

# Let x1 and y1 be the width and height of the background respectively
# Let x2 and y2 be the width and the height of the background respectively
x1,y1 = back_size
x2,y2 = ghost_size

# Ask the user for the x and y co-ordinates at which you must center the ghost.
flag = True
while flag:
    coordinate_x = float(input("At what x co-ordinate should I center the ghost?: "))
    coordinate_y = float(input("At what y co-ordinate should I center the ghost?: "))

    if coordinate_x > x1 or coordinate_y > y1:
        print("I cannot center the ghost at a point that is off the background photo")
        print("You need to pick points less than", back_size)
    else:
        flag = False

for i in range(x2):
    for j in range(y2):
        if ghost_surface.get_at((i,j)) != (0,255,0):
            ghost_surface_widthavg = int((coordinate_x - (x2 / 2) + i))
            ghost_surface_heightavg = int((coordinate_y - (y2 / 2) + j))

            (red1, green1, blue1, extra1) = ghost_surface.get_at((i,j))

            if (ghost_surface_widthavg >= x1 or ghost_surface_heightavg >= y1) or (ghost_surface_widthavg <= 0 or ghost_surface_heightavg <= 0):
                None
            else:
                (red2, green2, blue2, extra2) = screen.get_at((ghost_surface_widthavg, ghost_surface_heightavg))
                averaged_colour = ((red1 +red2) / 2, (green1 + green2) / 2, (blue1 +blue2) / 2)
                screen.set_at((ghost_surface_widthavg, ghost_surface_heightavg), (averaged_colour))

while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
        pygame.display.update()
