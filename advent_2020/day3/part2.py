from get_input import get_data
import pygame
import time

HEIGHT = 540
WIDTH = 780
FONT_HEIGHT = 20

X_FACTOR_SCALE = 1.6
FONT_WIDTH = FONT_HEIGHT/X_FACTOR_SCALE
FONT_WIDTH = int(FONT_WIDTH)

PIXEL_X = ((WIDTH-FONT_WIDTH*3)//FONT_WIDTH)-4
PIXEL_Y = HEIGHT//FONT_HEIGHT

TREE = '#'
ICON = 'U'

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

X_OVER = 1
Y_OVER = 2

INTERP = 1

ENTIRE_FOREST = get_data()
class V():
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Cam():
    def __init__(self,l):
        self.x = l.x
        self.y = l.y
        self.w = PIXEL_X
        self.h = PIXEL_Y
        self.c = V(0,0)
    def camera_scoot(self,sled):
        self.c = sled.l

        self.x = self.c.x - self.w//2
        self.y = self.c.y - self.h//2



class Sled():
    def __init__(self,x,y):
        self.l = V(x,y)
        self.trees_met = 0
        self.prev = []

    def move(self):
        self.prev.append(V(self.l.x,self.l.y))
        if len(self.prev) > PIXEL_Y+1:
            self.prev.pop(0)
        self.l.x += X_OVER
        self.l.y += Y_OVER
        if self.l.y > len(ENTIRE_FOREST)+PIXEL_Y:
            global DONE
            DONE = True


    def __str__(self):
        return f"x: {self.l.x} y: {self.l.y} Trees Met:{self.trees_met}"


def render_trees(list_of_strings,screen,cam,interframe):
    font = pygame.font.Font('./cour.ttf', FONT_HEIGHT)
    max_num_screen_line = HEIGHT // FONT_HEIGHT
    for i, string in enumerate(list_of_strings):
        if i > max_num_screen_line-1:
            return
        text = font.render(f"{string}", True, GREEN)
        textRect = text.get_rect()
        y_off = i*FONT_HEIGHT+13+(interframe/2)*(FONT_HEIGHT/3)

        textRect.center = (((WIDTH // 2)+FONT_WIDTH*4 - ((FONT_WIDTH/2)*(INTERP-interframe))), y_off)
        screen.blit(text, textRect)
        text = font.render(f"{cam.y + i}",True, GREEN)
        textRect = text.get_rect()
        textRect.center = (FONT_WIDTH*3,  y_off)
        screen.blit(text, textRect)
    text = font.render(f"{ICON}", True, GREEN)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2 + FONT_WIDTH*X_OVER,  HEIGHT//2 + (FONT_HEIGHT/2)*Y_OVER)
    screen.blit(text, textRect)


def look_at_forest(sled,cam):
    sled.move()
    cam.camera_scoot(sled)
    r_forest = []

    # print(sled)
    for y in range(0, cam.h):
        if cam.y + y > len(ENTIRE_FOREST)-1 :
            pass
        else:
            x_dimension = ENTIRE_FOREST[cam.y + y]
        temp_str = ''
        for x in range(0,cam.w):
            x_offset = (cam.x + x) % 31
            if cam.y + y < 0 or cam.y + y > len(ENTIRE_FOREST)-1 or x_offset < 0:
                temp_str += ' '
            elif cam.y + y == sled.l.y and cam.x+x == sled.l.x:
                temp_str += ICON

                if x_dimension[x_offset] == TREE:
                    sled.trees_met += 1
                #CHECK IF HIT TREE

            else:
                prev_flag = False
                for p in sled.prev:
                    if cam.y + y == p.y and cam.x+x == p.x:
                        prev_flag = True
                        if x_dimension[x_offset] == TREE:
                            temp_str += 'X'
                        else:
                            temp_str += '0'
                        break

                if not prev_flag:
                    # print(x_offset,x_dimension)
                    temp_str += x_dimension[x_offset]
        r_forest.append(temp_str)
    return r_forest
DONE = False
def main():
    global DONE
    DONE = False

    tobagan = Sled(0,0)
    visible_forest = []
    eyes = Cam(tobagan.l)

    pygame.init()
    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("DAY 3 Solution")
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('GeeksForGeeks\naqrefawerafe\nawerqwerrqwe\n', True, GREEN, BLUE)
    # textRect = text.get_rect()
    # textRect.center = (WIDTH // 2, HEIGHT // 2)

    # Loop until the user clicks the close button.

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    done = False
    while not done:

        if DONE:
            tobagan.l.x = 0
            tobagan.l.y = 0
            tobagan.trees_met = 0
            DONE = False
            print("reset")


        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # --- Game logic should go here
        visible_forest = look_at_forest(tobagan,eyes)
        # update_strings()
        for f in reversed(range(0,INTERP)):
            # --- Screen-clearing code goes here
            screen.fill(BLUE)

            # --- Drawing code should go here

            render_trees(visible_forest, screen, eyes,f)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(120)
            # time.sleep(.05)
        if tobagan.l.y >= len(ENTIRE_FOREST):
            print(tobagan.trees_met)


    pygame.quit()


if __name__ == "__main__":
    main()
