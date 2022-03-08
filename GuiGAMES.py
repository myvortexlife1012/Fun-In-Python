# GUI GAMES

#games to make:
# Ping Pong
# Volley Ball
# Hand Ball
# games where you're chasing something
#----------

# import GuiGAMES as g
# g.PongPlay()
# g.SudokuPlay()
# g.BattleshipPlay()
# g.MinesweeperPlay() # #take it out of the function - it doesn't run like this
# g.ticTacToePlay()
# g.firstGame()

#------------------------------------------------

# import GuiGAMES as g
# g.tkinterGame1()

def tkinterGame1():
    import tkinter
    import time

    Window_Width = ww = 800
    Window_Height = wh = 600
    Ball_Start_XPosition = 50
    Ball_Start_YPosition = 50
    Ball_Radius = 30
    Ball_min_movement = 5
    Refresh_Sec = 0.01

    def create_animation_window():
        Window = tkinter.Tk()
        Window.title("Ball Moving In Bounds - Python Guides")

        Window.geometry(f'{Window_Width}x{Window_Height}')
        print(f'ww:{ww} x wh:{wh}')
        return Window

    def create_animation_canvas(Window):
        canvas = tkinter.Canvas(Window)
        canvas.configure(bg="Blue")
        canvas.pack(fill="both", expand=True)
        return canvas

    def create_circle(x, y, r, canvasName):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill="Red", outline="Black", width=4)


    def animate_ball(Window, canvas, xinc, yinc):
        #you assign it to a variable, when you want to move it later
        ball = create_circle(Ball_Start_XPosition, Ball_Start_YPosition, Ball_Radius, canvas)

        while True:
            canvas.move(ball, xinc, yinc)
            Window.update()
            time.sleep(Refresh_Sec)
            ball_pos = canvas.coords(ball)
            # unpack array to variables
            al, bl, ar, br = ball_pos
            if al < abs(xinc) or ar > Window_Width - abs(xinc):
                xinc = -xinc
            if bl < abs(yinc) or br > Window_Height - abs(yinc):
                yinc = -yinc

    Animation_Window = create_animation_window()
    Animation_canvas = create_animation_canvas(Animation_Window)
    animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)



#------------------------------------------------



from pygame.locals import *


# prices = ticksToPricesOnly(ticks)
def ticksToPricesOnly(ticks):
    prices = []
    for tick in ticks:
        price = priceFromTickJSONdata(tick)
        prices.append(price)
    return prices


# import GuiGAMES as g
# string="ticks[0] : [ETH-USD][0] {'trade_id': 215131057, 'price': '2575.56', 'size': '0.49265816', 'time': '2022-01-30T00:48:56.801899Z', 'bid': '2574.94', 'ask': '2575.45', 'volume': '134313.62568946'}"
# price = g.priceFromTickJSONdata(string)
def priceFromTickJSONdata(string):
    tPrice1 = string.split("'price': '")
    tPrice2 = tPrice1[1].split("'")
    tPrice = float(tPrice2[0])
    return tPrice

#----------------------------------------------



#--------------------------

# import GuiGAMES as g
# g.liveCryptoTickerPlot1()

#I MADE THE LINES, CIRCLES, AND LINES FROM PRICE TO PRICE
def liveCryptoTickerPlot1():
    import GuiGAMES as g
    #load the tick data
    import OPENsomething as open
    filename = "crypto_tick_data-eth.txt"
    cryptoName = "ETHERIUM - ETH - Live Crypto Data Simulation"
    ticks = open.readFile(filename) # array of lines
    # print(f"ticks[0] : {ticks[0]}")
    prices = ticksToPricesOnly(ticks)
    print(f"prices : {prices}")

    #plot 1, wait 1 sec, plot the 2nd one
    #set up the lines of 10 plot points
    import pygame, sys
    #from pygame.locals import *
    ww = 600  # window width
    wh = 400  # window height

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE) #x-,y|

        #title of graph
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Times', 18)
        textsurface = myfont.render(cryptoName, False, BLUE)
        DISPLAY.blit(textsurface, (ww/2-180, 10))  # x-,y|,w,h

        #put the line - across equally the width
        pygame.draw.line(DISPLAY, BLUE, (ww/11*1, 50), (ww/11*1, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*2, 50), (ww/11*2, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*3, 50), (ww/11*3, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*4, 50), (ww/11*4, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*5, 50), (ww/11*5, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*6, 50), (ww/11*6, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*7, 50), (ww/11*7, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*8, 50), (ww/11*8, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*9, 50), (ww/11*9, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*10, 50), (ww/11*10, wh-10), 1)
        #pygame.draw.line(surface, color, start_pos, end_pos, width)

        # price from tick string
        # import GuiGAMES as g
        # price = g.priceFromTickJSONdata(ticks[0])
        # print(f"price: {price}")
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*9+30, 100), 4, 0)#x-,y|
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*8+30, 150), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*9+30, 100), (ww/11*8+30, 150), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*7+30, 130), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*8+30, 150), (ww/11*7+30, 130), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*6+30, 140), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*7+30, 130), (ww/11*6+30, 140), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*5+30, 165), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*6+30, 140), (ww/11*5+30, 165), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*4+30, 150), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*5+30, 165), (ww/11*4+30, 150), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*3+30, 130), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*4+30, 150), (ww/11*3+30, 130), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*2+30, 160), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*3+30, 130), (ww/11*2+30, 160), 1)
        pygame.draw.circle(DISPLAY, BLUE, (ww/11*1+30, 180), 4, 0)#x-,y|
        pygame.draw.line(DISPLAY, BLUE, (ww/11*2+30, 160), (ww/11*1+30, 180), 1)
        #pygame.draw.circle(surface, color, center, radius)


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            pygame.time.delay(10)


    main()



#--------------------------

# import GuiGAMES as g
# g.liveCryptoTickerPlot2()

#create the high and low of the chart, and replot it
#then animate the points - every second
def liveCryptoTickerPlot2():
    import GuiGAMES as g
    #load the tick data
    import OPENsomething as open
    filename = "crypto_tick_data-eth.txt"
    cryptoName = "ETHERIUM - ETH - Live Crypto Data Simulation"
    ticks = open.readFile(filename) # array of lines
    # print(f"ticks[0] : {ticks[0]}")
    prices = ticksToPricesOnly(ticks)
    print(f"prices : {prices}")

    #plot 1, wait 1 sec, plot the 2nd one
    #set up the lines of 10 plot points
    import pygame, sys
    #from pygame.locals import *
    ww = 600  # window width
    wh = 400  # window height

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE) #x-,y|

        #title of graph
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Times', 18)
        textsurface = myfont.render(cryptoName, False, BLUE)
        DISPLAY.blit(textsurface, (ww/2-180, 10))  # x-,y|,w,h

        #put the line - across equally the width
        pygame.draw.line(DISPLAY, BLUE, (ww/11*1, 50), (ww/11*1, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*2, 50), (ww/11*2, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*3, 50), (ww/11*3, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*4, 50), (ww/11*4, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*5, 50), (ww/11*5, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*6, 50), (ww/11*6, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*7, 50), (ww/11*7, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*8, 50), (ww/11*8, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*9, 50), (ww/11*9, wh-10), 1)
        pygame.draw.line(DISPLAY, BLUE, (ww/11*10, 50), (ww/11*10, wh-10), 1)
        #pygame.draw.line(surface, color, start_pos, end_pos, width)

        # price from tick string
        # import GuiGAMES as g
        # price = g.priceFromTickJSONdata(ticks[0])
        # print(f"price: {price}")


        counter = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            pygame.time.delay(10)

            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 9 + 30, 100), 4, 0)  # x-,y|
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 8 + 30, 150), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 9 + 30, 100), (ww / 11 * 8 + 30, 150), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 7 + 30, 130), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 8 + 30, 150), (ww / 11 * 7 + 30, 130), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 6 + 30, 140), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 7 + 30, 130), (ww / 11 * 6 + 30, 140), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 5 + 30, 165), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 6 + 30, 140), (ww / 11 * 5 + 30, 165), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 4 + 30, 150), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 5 + 30, 165), (ww / 11 * 4 + 30, 150), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 3 + 30, 130), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 4 + 30, 150), (ww / 11 * 3 + 30, 130), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 2 + 30, 160), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 3 + 30, 130), (ww / 11 * 2 + 30, 160), 1)
            pygame.display.update()
            pygame.time.delay(500)
            pygame.draw.circle(DISPLAY, BLUE, (ww / 11 * 1 + 30, 180), 4, 0)  # x-,y|
            pygame.draw.line(DISPLAY, BLUE, (ww / 11 * 2 + 30, 160), (ww / 11 * 1 + 30, 180), 1)
            pygame.display.update()
            pygame.time.delay(10)
            # pygame.draw.circle(surface, color, center, radius)

            counter += 1


    main()






#-------------------------------------
# import GuiGAMES as g
# g.pygame1()

#I MADE THE SQUARE
def pygame1():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    main()

#-------------------------
# import GuiGAMES as g
# g.pygame2()
#I MADE THE SQUARE FALL
def pygame2():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))
        x = 100
        y = 100
        velocity = 0
        acceleration = 0.1
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            DISPLAY.fill((255, 255, 255))
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))
            y += velocity
            velocity += acceleration
            if keys[pygame.K_SPACE]:
                print("key was pressed")
                velocity = -3

            pygame.display.update()
            pygame.time.delay(10)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame3()
# arrow keys move the block around
def pygame3():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))
        x = 100
        y = 100
        velocity = 0
        acceleration = 0.1
        while True:


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        x = x + 0
                        y = y - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        x = x + 0
                        y = y + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        x = x - 50
                        y = y + 0
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        x = x + 50
                        y = y + 0

            DISPLAY.fill((255, 255, 255))
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))

            #y += velocity
            #velocity += acceleration

            pygame.display.update()
            pygame.time.delay(10)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame4()
# box falls to the ground - keys move it
def pygame4():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))
        x = 100
        y = 100
        velocity = 0
        acceleration = 0.01
        while True:


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        x = x + 0
                        y = y - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        x = x + 0
                        y = y + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        x = x - 50
                        y = y + 0
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        x = x + 50
                        y = y + 0
            if y>350:
                y=350
            print(f"x:{x},y:{y},velocity:{velocity},acceleration:{acceleration}")
            DISPLAY.fill((255, 255, 255))
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))

            if y<350:
                y += velocity
                velocity += acceleration

            pygame.display.update()
            pygame.time.delay(10)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame5()
# box moves around in bounds - like pong, the x,y values change together
def pygame5():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))
        x = 100
        y = 100
        velocity = 3
        direction = "l"
        direction2 = "u"
        #acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        x = x + 0
                        y = y - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        x = x + 0
                        y = y + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        x = x - 50
                        y = y + 0
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        x = x + 50
                        y = y + 0

            print(f"x:{x},y:{y}")
            DISPLAY.fill((255, 255, 255))
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))

            # move it right or left here
            if direction == "r":
                x += velocity
            if direction == "l":
                x -= velocity
            #move it up or down here
            if direction2 == "u":
                y -= velocity
            if direction2 == "d":
                y += velocity

            #go the other way when it reaches the right side
            if x>420: #on the right side
                direction="l"
                #print("changing direction to going left")
            if x<30: #on the left side
                direction="r"
                #print("changing direction to going right")
            if y<20: #on the top side
                #print("you're at the top")
                direction2 = "d"
                #print("changing direction to going down")
            if y>340: #on the bottom side
                direction2 = "u"
                #print("changing direction to going up")

            pygame.display.update()
            pygame.time.delay(50)

    main()



#-------------------------
# import GuiGAMES as g
# g.pygame6()
# box moves SHAKY around in bounds - like pong, the x,y values change together
def pygame6():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))
        x = 100
        y = 100
        velocity = 5
        direction = "l"
        direction2 = "u"
        #acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        x = x + 0
                        y = y - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        x = x + 0
                        y = y + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        x = x - 50
                        y = y + 0
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        x = x + 50
                        y = y + 0

            #print(f"x:{x},y:{y}")
            DISPLAY.fill((255, 255, 255))
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))

            import random
            r = random.randint(1,10)
            r2 = random.randint(1,10)
            # move it right or left here
            if direction == "r":
                if(r2>5):
                    x += velocity + r2
            if direction == "l":
                if(r2>5):
                    x -= velocity + r2
            #move it up or down here
            if direction2 == "u":
                if(r>5):
                    y -= velocity*.5 + r
            if direction2 == "d":
                if(r>5):
                    y += velocity*.5 + r

            #go the other way when it reaches the right side
            if x>420: #on the right side
                direction="l"
                #print("changing direction to going left")
            if x<30: #on the left side
                direction="r"
                #print("changing direction to going right")
            if y<20: #on the top side
                #print("you're at the top")
                direction2 = "d"
                #print("changing direction to going down")
            if y>340: #on the bottom side
                direction2 = "u"
                #print("changing direction to going up")

            pygame.display.update()
            pygame.time.delay(50)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame7()
# pong - both player boards are moving up and down
def pygame7():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        ww=500 #window width
        wh=400 #window height
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        TEXTCOLOR = (0, 0, 0)

        #DISPLAY.fill(BLACK)
        #pygame.draw.line(surface, color, start_pos, end_pos, width)
        #pygame.draw.circle(DISPLAY, WHITE, (200, 150), 12, 0)
        #pygame.draw.circle(surface, color, center, radius)
        #pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        #pygame.draw.rect(DISPLAY, WHITE, (100, 50, 200, 30)) #x-,y|,w,h
        #pygame.draw.rect(DISPLAY, WHITE, (100, 420, 200, 30))
        x = ww/2
        y = wh/2
        circleRadius = 12
        barH = 150
        barW = 20
        xP1 = 30 #30, 120 # x-,y|
        xP2 = 450 #450, 120 # x-,y|
        yP1 = 120 # x-,y|
        yP2 = 120 # x-,y|
        velocity = 3
        direction = "l"
        direction2 = "u"
        #acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #print(f"x:{x},y:{y}")

            if yP1>wh-barH-10:
                direction2="u"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height
            elif yP1<10:
                direction2="d"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height

            if direction2 == "d":
                yP1 = yP1 + velocity
                yP2 = yP2 + velocity
            if direction2 == "u":
                yP1 = yP1 - velocity
                yP2 = yP2 - velocity

            #yP2 = 120  # x-,y|


            DISPLAY.fill(BLACK)
            # pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(DISPLAY, WHITE, (x, y), circleRadius)
            pygame.draw.rect(DISPLAY, WHITE, (xP1, yP1, barW, barH))  # x-,y|,w,h
            # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT)) # x-,y|,w,h
            pygame.draw.rect(DISPLAY, RED, (xP2, yP2, barW, barH))  # x-,y|,w,h


            pygame.display.update()
            pygame.time.delay(50)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame8()
# pong - both player boards are moving up and down
# get the ball moving - and set the game up on autopilot
#pong automatic - next version - Store/Show Player Points, extend the screen
def pygame8():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        ww=500 #window width
        wh=400 #window height
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        TEXTCOLOR = (0, 0, 0)

        #DISPLAY.fill(BLACK)
        #pygame.draw.line(surface, color, start_pos, end_pos, width)
        #pygame.draw.circle(DISPLAY, WHITE, (200, 150), 12, 0)
        #pygame.draw.circle(surface, color, center, radius)
        #pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        #pygame.draw.rect(DISPLAY, WHITE, (100, 50, 200, 30)) #x-,y|,w,h
        #pygame.draw.rect(DISPLAY, WHITE, (100, 420, 200, 30))
        x = ww/2
        y = wh/2
        circleRadius = 12
        barH = 150
        barW = 20
        xP1 = 30 #30, 120 # x-,y|
        xP2 = 450 #450, 120 # x-,y|
        yP1 = 120 # x-,y|
        yP2 = 120 # x-,y|
        p1points = 0
        p2points = 0
        directionBall = "l"
        directionBall2 = "d"
        velocity = 6
        direction = "l"
        direction2 = "u"
        #acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #print(f"x:{x},y:{y}")

            if yP1>wh-barH-10:
                direction2="u"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height
            elif yP1<10:
                direction2="d"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height

            if direction2 == "d":
                yP1 = yP1 + velocity
                yP2 = yP2 + velocity
            if direction2 == "u":
                yP1 = yP1 - velocity
                yP2 = yP2 - velocity

            #yP2 = 120  # x-,y|
            # move it right or left here
            #directionBall = "l"
            if directionBall == "r":
                x += velocity
            if directionBall == "l":
                x -= velocity
            #move it up or down here
            #directionBall2 = "u"
            if directionBall2 == "u":
                y -= velocity*.5
            if directionBall2 == "d":
                y += velocity*.5


            ballInP2barArea = True
            #if y matches between, yP1 - yP1+BarHeight
            if y>=yP1 and y<=yP1+barH:
                ballInP1barArea = True
            else:
                ballInP1barArea = False
            if y>=yP2 and y<=yP2+barH:
                ballInP2barArea = True
            else:
                ballInP2barArea = False

            #go the other way when it reaches the right side
            if x>440 and ballInP2barArea==True: #on the right side #x-,y|,w,h
                directionBall="l"
                #print("changing direction to going left")
            if x<65 and ballInP1barArea==True: #on the left side #x-,y|,w,h
                directionBall="r"
                #print("changing direction to going right")
            if y<20: #on the top side  #x-,y|,w,h
                #print("you're at the top")
                directionBall2 = "d"
                #print("changing direction to going down")
            if y>380: #on the bottom side #x-,y|,w,h
                directionBall2 = "u"
                #print("changing direction to going up")

            # RESETTING:
            # Assigning Points:
            if x<10 and ballInP1barArea==False: #on the left side #x-,y|,w,h
                pass
                #start a new game - center the 3 elements - start over
                #p2points += 1 ... #change all the x's and y's ... and save the point
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p2points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"
            if x > 500 and ballInP2barArea==False:
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p1points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"

            DISPLAY.fill(BLACK)
            # pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(DISPLAY, WHITE, (x, y), circleRadius)
            pygame.draw.rect(DISPLAY, WHITE, (xP1, yP1, barW, barH))  # x-,y|,w,h
            # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT)) # x-,y|,w,h
            pygame.draw.rect(DISPLAY, RED, (xP2, yP2, barW, barH))  # x-,y|,w,h


            pygame.display.update()
            pygame.time.delay(50)

    main()


#-------------------------
# import GuiGAMES as g
# g.pygame9()
# pong automatic
# - this version - Store/Show Player Points, extend the screen
#add in keypresses - to move the 2 bars up and down
def pygame9():
    import pygame, sys
    #from pygame.locals import *

    def main():
        pygame.init()
        ww=500 #window width
        wh=400 #window height
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        TEXTCOLOR = (0, 0, 0)

        #DISPLAY.fill(BLACK)
        #pygame.draw.line(surface, color, start_pos, end_pos, width)
        #pygame.draw.circle(DISPLAY, WHITE, (200, 150), 12, 0)
        #pygame.draw.circle(surface, color, center, radius)
        #pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        #pygame.draw.rect(DISPLAY, WHITE, (100, 50, 200, 30)) #x-,y|,w,h
        #pygame.draw.rect(DISPLAY, WHITE, (100, 420, 200, 30))
        x = ww/2
        y = wh/2
        circleRadius = 12
        barH = 150
        barW = 20
        xP1 = 30 #30, 120 # x-,y|
        xP2 = 450 #450, 120 # x-,y|
        yP1 = 120 # x-,y|
        yP2 = 120 # x-,y|
        p1points = 0
        p2points = 0
        directionBall = "l"
        directionBall2 = "d"
        velocity = 6
        direction = "l"
        direction2 = "u"
        #acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                #add in keypresses - to move the 2 bars up and down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        yP1 = yP1 - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        yP1 = yP1 + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        yP2 = yP2 - 50
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        yP2 = yP2 + 50

                    #fix it for going off the edges - and getting messed up - maybe
                    if yP2<0:
                        yP2=0
                    if yP2 > wh:
                        yP2 = wh-barH
                    if yP1 < 0:
                        yP1 = 0
                    if yP1 > wh:
                        yP1 = wh - barH

            #print(f"x:{x},y:{y}")

            #if top of the bar goes off screen, bring it back
            if yP1>wh-barH-10:
                direction2="u"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height
            elif yP1<10:
                direction2="d"  # x-,y| .. barH=150 ... ww = 500  # window width ... wh = 400  # window height

            #move things here - based on the direction
            if direction2 == "d":
                yP1 = yP1 + velocity
                yP2 = yP2 + velocity
            if direction2 == "u":
                yP1 = yP1 - velocity
                yP2 = yP2 - velocity

            #yP2 = 120  # x-,y|
            # move it right or left here
            #directionBall = "l"
            if directionBall == "r":
                x += velocity
            if directionBall == "l":
                x -= velocity
            #move it up or down here
            #directionBall2 = "u"
            if directionBall2 == "u":
                y -= velocity*.5
            if directionBall2 == "d":
                y += velocity*.5


            ballInP2barArea = True
            #if y matches between, yP1 - yP1+BarHeight
            if y>=yP1 and y<=yP1+barH:
                ballInP1barArea = True
            else:
                ballInP1barArea = False
            if y>=yP2 and y<=yP2+barH:
                ballInP2barArea = True
            else:
                ballInP2barArea = False

            #go the other way when it reaches the right side
            if x>440 and ballInP2barArea==True: #on the right side #x-,y|,w,h
                directionBall="l"
                #print("changing direction to going left")
            if x<65 and ballInP1barArea==True: #on the left side #x-,y|,w,h
                directionBall="r"
                #print("changing direction to going right")
            if y<20: #on the top side  #x-,y|,w,h
                #print("you're at the top")
                directionBall2 = "d"
                #print("changing direction to going down")
            if y>380: #on the bottom side #x-,y|,w,h
                directionBall2 = "u"
                #print("changing direction to going up")

            # RESETTING:
            # Assigning Points:
            if x<10 and ballInP1barArea==False: #on the left side #x-,y|,w,h
                pass
                #start a new game - center the 3 elements - start over
                #p2points += 1 ... #change all the x's and y's ... and save the point
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p2points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"
            if x > 500 and ballInP2barArea==False:
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p1points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"

            DISPLAY.fill(BLACK)
            # pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(DISPLAY, WHITE, (x, y), circleRadius)
            pygame.draw.rect(DISPLAY, WHITE, (xP1, yP1, barW, barH))  # x-,y|,w,h
            # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT)) # x-,y|,w,h
            pygame.draw.rect(DISPLAY, RED, (xP2, yP2, barW, barH))  # x-,y|,w,h

            pygame.font.init()  # you have to call this at the start,
            # if you want to use this module.
            myfont = pygame.font.SysFont('Comic Sans MS', 16)
            textsurface = myfont.render(f'Player 1 Points: {p1points}', False, WHITE)
            DISPLAY.blit(textsurface, (50, wh-30)) # x-,y|,w,h
            textsurface2 = myfont.render(f'Player 2 Points: {p2points}', False, WHITE)
            DISPLAY.blit(textsurface2, (350, wh-30)) # x-,y|,w,h

            pygame.display.update()
            pygame.time.delay(50)

    main()


# -------------------------
# import GuiGAMES as g
# g.pygame10()
# pong automatic
# - this version
# - take off auto move of the 2 player bars
# - use up and down keys - for Player 1
# - use left and right keys - for Player 2
# - next version - when I hit up and down keys - it moves smoothly instead of jumping
def pygame10():
    import pygame, sys
    # from pygame.locals import *

    def main():
        pygame.init()
        ww = 500  # window width
        wh = 400  # window height
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        TEXTCOLOR = (0, 0, 0)

        # DISPLAY.fill(BLACK)
        # pygame.draw.line(surface, color, start_pos, end_pos, width)
        # pygame.draw.circle(DISPLAY, WHITE, (200, 150), 12, 0)
        # pygame.draw.circle(surface, color, center, radius)
        # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        # pygame.draw.rect(DISPLAY, WHITE, (100, 50, 200, 30)) #x-,y|,w,h
        # pygame.draw.rect(DISPLAY, WHITE, (100, 420, 200, 30))
        x = ww / 2
        y = wh / 2
        circleRadius = 12
        barH = 150
        barW = 20
        xP1 = 30  # 30, 120 # x-,y|
        xP2 = 450  # 450, 120 # x-,y|
        yP1 = 120  # x-,y|
        yP2 = 120  # x-,y|
        p1points = 0
        p2points = 0
        directionBall = "l"
        directionBall2 = "d"
        velocity = 6
        direction = "l"
        direction2 = "u"
        # acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # add in keypresses - to move the 2 bars up and down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        yP1 = yP1 - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        yP1 = yP1 + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        yP2 = yP2 - 50
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        yP2 = yP2 + 50
            # print(f"x:{x},y:{y}")

            # if top of the bar goes off screen, bring it back
            # if it touches the bottom:
            if yP1 > wh - barH - 10: # x-,y|
                pass
            # if it touches the top
            elif yP1 < 10: # x-,y|
                pass

            # yP2 = 120  # x-,y|
            # move it right or left here
            # directionBall = "l"
            if directionBall == "r":
                x += velocity
            if directionBall == "l":
                x -= velocity
            # move it up or down here
            # directionBall2 = "u"
            if directionBall2 == "u":
                y -= velocity * .5
            if directionBall2 == "d":
                y += velocity * .5

            ballInP2barArea = True
            # if y matches between, yP1 - yP1+BarHeight
            # player 1
            if y >= yP1 and y <= yP1 + barH:
                ballInP1barArea = True
            else:
                ballInP1barArea = False
            # player 2
            if y >= yP2 and y <= yP2 + barH:
                ballInP2barArea = True
            else:
                ballInP2barArea = False

            # go the other way when it reaches the right side
            if x > ww-60 and ballInP2barArea == True:  # on the right side #x-,y|,w,h
                directionBall = "l"
                # print("changing direction to going left")
            if x < 65 and ballInP1barArea == True:  # on the left side #x-,y|,w,h
                directionBall = "r"
                # print("changing direction to going right")
            if y < 20:  # on the top side  #x-,y|,w,h
                # print("you're at the top")
                directionBall2 = "d"
                # print("changing direction to going down")
            if y > wh-20:  # on the bottom side #x-,y|,w,h
                directionBall2 = "u"
                # print("changing direction to going up")

            # RESETTING The Game Board & Points for Both Players:
            # Assigning Points:
            #if the ball goes past the P1 Bar, and goes out:
            if x < 10 and ballInP1barArea == False:  # on the left side #x-,y|,w,h
                pass
                # start a new game - center the 3 elements - start over
                # p2points += 1 ... #change all the x's and y's ... and save the point
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p2points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"
            # if the ball goes past the P2 Bar, and goes out:
            if x > 500 and ballInP2barArea == False:
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p1points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"

            DISPLAY.fill(BLACK)
            # pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(DISPLAY, WHITE, (x, y), circleRadius)
            pygame.draw.rect(DISPLAY, WHITE, (xP1, yP1, barW, barH))  # x-,y|,w,h
            # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT)) # x-,y|,w,h
            pygame.draw.rect(DISPLAY, RED, (xP2, yP2, barW, barH))  # x-,y|,w,h

            pygame.font.init() # you have to call this at the start of using fonts
            myfont = pygame.font.SysFont('Comic Sans MS', 16)
            textsurface1 = myfont.render(f'Player 1 Points: {p1points}', False, WHITE)
            DISPLAY.blit(textsurface1, (50, wh - 30))  # x-,y|,w,h
            textsurface2 = myfont.render(f'Player 2 Points: {p2points}', False, WHITE)
            DISPLAY.blit(textsurface2, (350, wh - 30))  # x-,y|,w,h

            pygame.display.update()
            pygame.time.delay(50)

    main()




# -------------------------
# import GuiGAMES as g
# g.pygame11()
# pong automatic - #ping pong - pong
# - this version
# - when I hit up and down keys - it moves smoothly instead of jumping
def pygame11():
    import pygame, sys
    # from pygame.locals import *

    def main():
        pygame.init()
        ww = 500  # window width
        wh = 400  # window height
        DISPLAY = pygame.display.set_mode((ww, wh), 0, 32)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        TEXTCOLOR = (0, 0, 0)

        # DISPLAY.fill(BLACK)
        # pygame.draw.line(surface, color, start_pos, end_pos, width)
        # pygame.draw.circle(DISPLAY, WHITE, (200, 150), 12, 0)
        # pygame.draw.circle(surface, color, center, radius)
        # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        # pygame.draw.rect(DISPLAY, WHITE, (100, 50, 200, 30)) #x-,y|,w,h
        # pygame.draw.rect(DISPLAY, WHITE, (100, 420, 200, 30))
        x = ww / 2
        y = wh / 2
        circleRadius = 12
        barH = 150
        barW = 20
        xP1 = 30  # 30, 120 # x-,y|
        xP2 = 450  # 450, 120 # x-,y|
        yP1 = 120  # x-,y|
        yP2 = 120  # x-,y|
        p1points = 0
        p2points = 0
        directionBall = "l"
        directionBall2 = "d"
        velocity = 6
        direction = "l"
        direction2 = "u"
        # acceleration = 0.01
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # add in keypresses - to move the 2 bars up and down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up key pressed")
                        yP1 = yP1 - 50
                    elif event.key == pygame.K_DOWN:
                        print("down key pressed")
                        yP1 = yP1 + 50
                    elif event.key == pygame.K_LEFT:
                        print("left key pressed")
                        yP2 = yP2 - 50
                    elif event.key == pygame.K_RIGHT:
                        print("right key pressed")
                        yP2 = yP2 + 50
            # print(f"x:{x},y:{y}")

            # if top of the bar goes off screen, bring it back
            # if it touches the bottom:
            if yP1 > wh - barH - 10: # x-,y|
                pass
            # if it touches the top
            elif yP1 < 10: # x-,y|
                pass

            # yP2 = 120  # x-,y|
            # move it right or left here
            # directionBall = "l"
            if directionBall == "r":
                x += velocity
            if directionBall == "l":
                x -= velocity
            # move it up or down here
            # directionBall2 = "u"
            if directionBall2 == "u":
                y -= velocity * .5
            if directionBall2 == "d":
                y += velocity * .5

            ballInP2barArea = True
            # if y matches between, yP1 - yP1+BarHeight
            # player 1
            if y >= yP1 and y <= yP1 + barH:
                ballInP1barArea = True
            else:
                ballInP1barArea = False
            # player 2
            if y >= yP2 and y <= yP2 + barH:
                ballInP2barArea = True
            else:
                ballInP2barArea = False

            # go the other way when it reaches the right side
            if x > ww-60 and ballInP2barArea == True:  # on the right side #x-,y|,w,h
                directionBall = "l"
                # print("changing direction to going left")
            if x < 65 and ballInP1barArea == True:  # on the left side #x-,y|,w,h
                directionBall = "r"
                # print("changing direction to going right")
            if y < 20:  # on the top side  #x-,y|,w,h
                # print("you're at the top")
                directionBall2 = "d"
                # print("changing direction to going down")
            if y > wh-20:  # on the bottom side #x-,y|,w,h
                directionBall2 = "u"
                # print("changing direction to going up")

            # RESETTING The Game Board & Points for Both Players:
            # Assigning Points:
            #if the ball goes past the P1 Bar, and goes out:
            if x < 10 and ballInP1barArea == False:  # on the left side #x-,y|,w,h
                pass
                # start a new game - center the 3 elements - start over
                # p2points += 1 ... #change all the x's and y's ... and save the point
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p2points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"
            # if the ball goes past the P2 Bar, and goes out:
            if x > 500 and ballInP2barArea == False:
                x = ww / 2
                y = wh / 2
                xP1 = 30  # 30, 120 # x-,y|
                xP2 = 450  # 450, 120 # x-,y|
                yP1 = 120  # x-,y|
                yP2 = 120  # x-,y|
                p1points += 1
                print(f"p1points: {p1points} ... p2points: {p2points}")
                directionBall = "r"
                directionBall2 = "d"

            DISPLAY.fill(BLACK)
            # pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(DISPLAY, WHITE, (x, y), circleRadius)
            pygame.draw.rect(DISPLAY, WHITE, (xP1, yP1, barW, barH))  # x-,y|,w,h
            # pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT)) # x-,y|,w,h
            pygame.draw.rect(DISPLAY, RED, (xP2, yP2, barW, barH))  # x-,y|,w,h

            pygame.font.init() # you have to call this at the start of using fonts
            myfont = pygame.font.SysFont('Comic Sans MS', 16)
            textsurface1 = myfont.render(f'Player 1 Points: {p1points}', False, WHITE)
            DISPLAY.blit(textsurface1, (50, wh - 30))  # x-,y|,w,h
            textsurface2 = myfont.render(f'Player 2 Points: {p2points}', False, WHITE)
            DISPLAY.blit(textsurface2, (350, wh - 30))  # x-,y|,w,h

            pygame.display.update()
            pygame.time.delay(50)

    main()





#------------------------------------------------




# import GuiGAMES as guiGames
# guiGames.firstGame()

#draws a circle where you click - diff colors
def firstGame():
    # Import statements are to enable the code to use the functions from the library
    import pygame
    import sys
    import os
    import random

    # instructions to windows to center the game window in the center of
    # the screen, which it might ignore
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    # initialize pygame
    pygame.init()

    # Right way
    SCREENWIDTH = 500
    SCREENHEIGHT = 500
    SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
    SCREEN = pygame.display.set_mode(SCREENSIZE)

    # caption for the game
    pygame.display.set_caption("My first game in pygame")

    RADIUS = 20
    ZEROINTENSITY = 0
    MAXINTENSITY = 255

    while True:
        pos = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Here for any commands inside the for loop
            if events.type == pygame.MOUSEBUTTONDOWN:
                COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY),
                         random.randint(ZEROINTENSITY, MAXINTENSITY))
                # note- we have skipped the last parameter and by default, 0 is taken
                pygame.draw.circle(SCREEN, COLOR, pos, RADIUS)

        # beware of the positioning of this line. It should be inside the while
        # for all the commands that need to be executed inside the while
        pygame.display.update()


# v1
# import GuiGAMES as gui_games
# gui_games.PongPlay()

def PongPlay():
    # !/usr/bin/env python

    """
        Pong

        One of the most important video games.
        Pong was created by Al Alcorn and it did not use a microprocessor

        This demo is based on some initial code by Siddharth Natamai

        In 2021, it was reworked by Jay Nabaonne into this version you see today.

        A big

         ###### ##  ## ###### ##  ## ##  ##   ##  ## ###### ##  ##    ##
           ##   ##  ## ##  ## ### ## ## ##    ##  ## ##  ## ##  ##    ##
           ##   ###### ##  ## ###### ####     ##  ## ##  ## ##  ##    ##
           ##   ##  ## ###### ## ### ####     ###### ##  ## ##  ##    ##
           ##   ##  ## ##  ## ##  ## ## ##      ##   ##  ## ##  ##
           ##   ##  ## ##  ## ##  ## ##  ##    ####  ###### ######    ##

        to Jay for making it a smooth playing game.
        @jaynabonne https://github.com/jaynabonne

        Copyright 2021 PySimpleGUI, Jay Nabonne
    """

    import PySimpleGUI as sg
    import random
    import datetime

    GAMEPLAY_SIZE = (700, 400)
    BAT_SIZE = (20, 110)
    STARTING_BALL_POSITION = (327, 200)
    BALL_RADIUS = 12
    BACKGROUND_COLOR = 'black'
    BALL_COLOR = 'green1'
    BALL_SPEED = 300
    BAT_SPEED = 400

    UP_ARROW = 38
    DOWN_ARROW = 40

    player1_up_keycode = ord('W')
    player1_down_keycode = ord('S')
    player2_up_keycode = UP_ARROW
    player2_down_keycode = DOWN_ARROW

    num_rounds = 10

    class Bat:
        def __init__(self, graph: sg.Graph, colour, x, field_height):
            self.graph = graph
            self.field_height = field_height
            self.width = BAT_SIZE[0]
            self.height = BAT_SIZE[1]
            self.current_x = x
            self.current_y = self.field_height / 2 - self.height / 2
            self.id = graph.draw_rectangle(
                (self.current_x, self.current_y),
                (self.current_x + self.width, self.current_y + self.height),
                fill_color=colour
            )
            self.vy = 0

        def stop(self):
            self.vy = 0

        def up(self):
            self.vy = -BAT_SPEED

        def down(self):
            self.vy = BAT_SPEED

        def is_hit_by(self, pos):
            bat_p0 = (self.current_x, self.current_y)
            bat_p1 = (bat_p0[0] + self.width, bat_p0[1] + self.height)
            return bat_p0[0] <= pos[0] <= bat_p1[0] and bat_p0[1] <= pos[1] <= bat_p1[1]

        def update(self, delta: float):
            new_y = self.current_y + self.vy * delta
            if new_y <= 0:
                new_y = 0
                self.stop()
            if new_y + self.height >= self.field_height:
                new_y = self.field_height - self.height
                self.stop()
            self.current_y = new_y

            self.graph.relocate_figure(self.id, self.current_x, self.current_y)

    class Ball:
        def __init__(self, graph: sg.Graph, bat_1: Bat, bat_2: Bat, colour):
            self.graph = graph  # type: sg.Graph
            self.bat_1 = bat_1
            self.bat_2 = bat_2
            self.id = self.graph.draw_circle(
                STARTING_BALL_POSITION, BALL_RADIUS, line_color=colour, fill_color=colour)
            self.current_x, self.current_y = STARTING_BALL_POSITION
            self.vx = random.choice([-BALL_SPEED, BALL_SPEED])
            self.vy = -BALL_SPEED

        def hit_left_bat(self):
            return self.bat_1.is_hit_by((self.current_x - BALL_RADIUS, self.current_y))

        def hit_right_bat(self):
            return self.bat_2.is_hit_by((self.current_x + BALL_RADIUS, self.current_y))

        def update(self, delta: float):
            self.current_x += self.vx * delta
            self.current_y += self.vy * delta
            if self.current_y <= BALL_RADIUS:  # see if hit top or bottom of play area. If so, reverse y direction
                self.vy = -self.vy
                self.current_y = BALL_RADIUS
            if self.current_y >= GAMEPLAY_SIZE[1] - BALL_RADIUS:
                self.vy = -self.vy
                self.current_y = GAMEPLAY_SIZE[1] - BALL_RADIUS
            if self.hit_left_bat():
                self.vx = abs(self.vx)
            if self.hit_right_bat():
                self.vx = -abs(self.vx)

            self.position_to_current()

        def position_to_current(self):
            self.graph.relocate_figure(self.id, self.current_x - BALL_RADIUS, self.current_y - BALL_RADIUS)

        def restart(self):
            self.current_x, self.current_y = STARTING_BALL_POSITION
            self.position_to_current()

    class Scores:
        def __init__(self, graph: sg.Graph):
            self.player_1_score = 0
            self.player_2_score = 0
            self.score_1_element = None
            self.score_2_element = None
            self.graph = graph

            self.draw_player1_score()
            self.draw_player2_score()

        def draw_player1_score(self):
            if self.score_1_element:
                self.graph.delete_figure(self.score_1_element)
            self.score_1_element = self.graph.draw_text(
                str(self.player_1_score), (170, 50), font='Courier 40', color='white')

        def draw_player2_score(self):
            if self.score_2_element:
                self.graph.delete_figure(self.score_2_element)
            self.score_2_element = self.graph.draw_text(
                str(self.player_2_score), (550, 50), font='Courier 40', color='white')

        def win_loss_check(self):
            if self.player_1_score >= num_rounds:
                return 'Left player'
            if self.player_2_score >= num_rounds:
                return 'Right player'
            return None

        def increment_player_1(self):
            self.player_1_score += 1
            self.draw_player1_score()

        def increment_player_2(self):
            self.player_2_score += 1
            self.draw_player2_score()

        def reset(self):
            self.player_1_score = 0
            self.player_2_score = 0
            self.draw_player1_score()
            self.draw_player2_score()

    def check_ball_exit(ball: Ball, scores: Scores):
        if ball.current_x <= 0:
            scores.increment_player_2()
            ball.restart()
        if ball.current_x >= GAMEPLAY_SIZE[0]:
            scores.increment_player_1()
            ball.restart()

    def goto_menu(window):
        window['-MAIN_MENU-'].update(visible=True)
        window['-GAME-'].update(visible=False)

    def pong():
        sleep_time = 10

        inner_layout = [[sg.Graph(GAMEPLAY_SIZE,
                                  (0, GAMEPLAY_SIZE[1]),
                                  (GAMEPLAY_SIZE[0], 0),
                                  background_color=BACKGROUND_COLOR,
                                  key='-GRAPH-')],
                        [sg.Button('Back to Menu', key="-MENU-")]]

        main_menu_layout = [[sg.Text("Pong", font="Courier 40", justification="center", size=(None, 1))],
                            [sg.Text("-- Instructions --", font="Courier 16")],
                            [sg.Text("Left player controls: W and S", font="Courier 12")],
                            [sg.Text("Right player controls: \u2191 and \u2193", font="Courier 12")],
                            [sg.Text("Escape to pause game", font="Courier 12")],
                            [sg.Text("", font="Courier 8")],
                            [sg.Text("Winner is first to 10 points", font="Courier 12")],
                            [sg.Text("", font="Courier 8")],
                            [sg.Button("Start", key='-START-', font="Courier 24"),
                             sg.Button("Quit", key='-QUIT-', font="Courier 24")]]

        layout = [[sg.pin(sg.Column(main_menu_layout, key='-MAIN_MENU-', size=GAMEPLAY_SIZE)),
                   sg.pin(sg.Column(inner_layout, key='-GAME-', visible=False))]]

        window = sg.Window('Pong', layout, finalize=True, use_default_focus=False)

        window.bind("<Key>", "+KEY+")
        window.bind("<KeyRelease>", "-KEY-")

        graph_elem = window['-GRAPH-']  # type: sg.Graph

        scores = Scores(graph_elem)
        bat_1 = Bat(graph_elem, 'red', 30, GAMEPLAY_SIZE[1])
        bat_2 = Bat(graph_elem, 'blue', GAMEPLAY_SIZE[0] - 30 - BAT_SIZE[0], GAMEPLAY_SIZE[1])
        ball_1 = Ball(graph_elem, bat_1, bat_2, 'green1')

        start = datetime.datetime.now()
        last_post_read_time = start

        game_playing = False

        while True:
            pre_read_time = datetime.datetime.now()
            processing_time = (pre_read_time - last_post_read_time).total_seconds()
            time_to_sleep = sleep_time - int(processing_time * 1000)
            time_to_sleep = max(time_to_sleep, 0)

            event, values = window.read(time_to_sleep)
            now = datetime.datetime.now()
            delta = (now - last_post_read_time).total_seconds()
            # read_delta = (now-pre_read_time).total_seconds()
            last_post_read_time = now
            # print("**", event, delta, time_to_sleep, processing_time, read_delta)
            if event in (sg.WIN_CLOSED, "-QUIT-"):
                break
            elif event == "-START-":
                scores.reset()
                ball_1.restart()
                window['-MAIN_MENU-'].update(visible=False)
                window['-GAME-'].update(visible=True)
                sg.popup('\nPress a key to begin.\n',
                         no_titlebar=True,
                         font="Courier 12",
                         text_color=sg.BLUES[0],
                         background_color=sg.YELLOWS[1],
                         any_key_closes=True,
                         button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
                last_post_read_time = datetime.datetime.now()
                game_playing = True
            elif event == "-MENU-":
                game_playing = False
                goto_menu(window)
            elif game_playing:
                if event == "+KEY+":
                    if window.user_bind_event.keycode == player1_up_keycode:
                        bat_1.up()
                    elif window.user_bind_event.keycode == player1_down_keycode:
                        bat_1.down()
                    elif window.user_bind_event.keycode == player2_up_keycode:
                        bat_2.up()
                    elif window.user_bind_event.keycode == player2_down_keycode:
                        bat_2.down()
                elif event == "-KEY-":
                    if window.user_bind_event.keycode in [player1_up_keycode, player1_down_keycode]:
                        bat_1.stop()
                    elif window.user_bind_event.keycode in [player2_up_keycode, player2_down_keycode]:
                        bat_2.stop()
                    elif window.user_bind_event.keycode == 27:
                        sg.popup('\nPaused. Press a key to resume.\n',
                                 no_titlebar=True,
                                 font="Courier 12",
                                 text_color=sg.BLUES[0],
                                 background_color=sg.YELLOWS[1],
                                 any_key_closes=True,
                                 button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
                        last_post_read_time = datetime.datetime.now()

            if game_playing:
                ball_1.update(delta)
                bat_1.update(delta)
                bat_2.update(delta)

                check_ball_exit(ball_1, scores)

                winner = scores.win_loss_check()
                if winner is not None:
                    sg.popup('Game Over', winner + ' won!!', no_titlebar=True)
                    game_playing = False
                    goto_menu(window)

        window.close()

    # if __name__ == '__main__':
    pong()


# v1

# import GuiGAMES as guiGames
# guiGames.SudokuPlay()


def SudokuPlay():
    import PySimpleGUI as sg, random
    import numpy as np
    from typing import List, Any, Union, Tuple, Dict

    """
        Sudoku Puzzle Demo

        How to easily generate a GUI for a Sudoku puzzle.
        The Window definition and creation is a single line of code.

        Code to generate a playable puzzle was supplied from:
        https://github.com/MorvanZhou/sudoku

        Copyright 2020 PySimpleGUI.com

    """

    def generate_sudoku(mask_rate):
        """
        Create a Sukoku board

        :param mask_rate: % of squares to hide
        :type mask_rate: float
        :rtype: List[numpy.ndarry, numpy.ndarry]
        """
        while True:
            n = 9
            solution = np.zeros((n, n), np.int)
            rg = np.arange(1, n + 1)
            solution[0, :] = np.random.choice(rg, n, replace=False)
            try:
                for r in range(1, n):
                    for c in range(n):
                        col_rest = np.setdiff1d(rg, solution[:r, c])
                        row_rest = np.setdiff1d(rg, solution[r, :c])
                        avb1 = np.intersect1d(col_rest, row_rest)
                        sub_r, sub_c = r // 3, c // 3
                        avb2 = np.setdiff1d(np.arange(0, n + 1),
                                            solution[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                        avb = np.intersect1d(avb1, avb2)
                        solution[r, c] = np.random.choice(avb, size=1)
                break
            except ValueError:
                pass
        puzzle = solution.copy()
        puzzle[np.random.choice([True, False], size=solution.shape, p=[mask_rate, 1 - mask_rate])] = 0
        return puzzle, solution

    def check_progress(window, solution):
        """
        Gives you a visual hint on your progress.
        Red - You've got an incorrect number at the location
        Yellow - You're missing an anwer for that location

        :param window: The GUI's Window
        :type window: sg.Window
        :param solution: A 2D array containing the solution
        :type solution: numpy.ndarray
        :return: True if the puzzle has been solved correctly
        :rtype: bool
        """
        solved = True
        for r, row in enumerate(solution):
            for c, col in enumerate(row):
                value = window[r, c].get()
                if value:
                    try:
                        value = int(value)
                    except:
                        value = 0
                    if value != solution[r][c]:
                        window[r, c].update(background_color='red')
                        solved = False
                    else:
                        window[r, c].update(background_color=sg.theme_input_background_color())
                else:
                    solved = False
                    window[r, c].update(background_color='yellow')
        return solved

    def main(mask_rate=0.7):
        """"
        The Main GUI - It does it all.

        The "Board" is a grid that's 9 x 9.  Even though the layout is a grid of 9 Frames, the
        addressing of the individual squares is via a key that's a tuple (0,0) to (8,8)
        """

        def create_and_show_puzzle():
            # create and display a puzzle by updating the Input elements
            rate = mask_rate
            if window['-RATE-'].get():
                try:
                    rate = float(window['-RATE-'].get())
                except:
                    pass
            puzzle, solution = generate_sudoku(mask_rate=rate)
            for r, row in enumerate(puzzle):
                for c, col in enumerate(row):
                    window[r, c].update(puzzle[r][c] if puzzle[r][c] else '',
                                        background_color=sg.theme_input_background_color())
            return puzzle, solution

        # It's 1 line of code to make a Sudoku board.  If you don't like it, then replace it.
        # Dude (Dudette), it's 1-line of code.  If you don't like the board, write a line of code.
        # The keys for the inputs are tuples (0-8, 0-8) that reference each Input Element.
        # Get an input element for a position using:    window[row, col]
        # To get a better understanding, take it apart. Spread it out. You'll learn in the process.
        window = sg.Window('Sudoku',
                           [[sg.Frame('', [
                               [sg.I(random.randint(1, 9), justification='r', size=(3, 1), key=(fr * 3 + r, fc * 3 + c))
                                for
                                c in range(3)] for r in range(3)]) for fc in range(3)] for fr in range(3)] +
                           [[sg.B('Solve'), sg.B('Check'), sg.B('Hint'), sg.B('New Game')],
                            [sg.T('Mask rate (0-1)'), sg.In(str(mask_rate), size=(3, 1), key='-RATE-')], ],
                           finalize=True)

        # create and display a puzzle by updating the Input elements

        puzzle, solution = create_and_show_puzzle()

        while True:  # The Event Loop
            event, values = window.read()
            if event is None:
                break

            if event == 'Solve':
                for r, row in enumerate(solution):
                    for c, col in enumerate(row):
                        window[r, c].update(solution[r][c], background_color=sg.theme_input_background_color())
            elif event == 'Check':
                solved = check_progress(window, solution)
                if solved:
                    sg.popup('Solved! You have solved the puzzle correctly.')
            elif event == 'Hint':
                elem = window.find_element_with_focus()
                try:
                    elem.update(solution[elem.Key[0]][elem.Key[1]], background_color=sg.theme_input_background_color())
                except:
                    pass  # Likely because an input element didn't have focus
            elif event == 'New Game':
                puzzle, solution = create_and_show_puzzle()

        window.close()

    # if __name__ == "__main__":
    mask_rate = 0.7  # % Of cells to hide
    main(mask_rate)



# v1

# import GuiGAMES as guiGames
# guiGames.BattleshipPlay()

def BattleshipPlay():
    import PySimpleGUI as sg
    from random import randint

    def Battleship():
        sg.change_look_and_feel('Dark Blue 3')
        MAX_ROWS = MAX_COL = 10
        # Start building layout with the top 2 rows that contain Text elements
        layout = [[sg.Text('BATTLESHIP', font='Default 25')],
                  [sg.Text(size=(15, 1), key='-MESSAGE-', font='Default 20')]]
        # Add the board, a grid a buttons
        layout += [
            [sg.Button(str('O'), size=(4, 2), pad=(0, 0), border_width=0, key=(row, col)) for col in range(MAX_COL)] for
            row in range(MAX_ROWS)]
        # Add the exit button as the last row
        layout += [[sg.Button('Exit', button_color=('white', 'red'))]]

        window = sg.Window('Battleship', layout)

        while True:  # The Event Loop
            event, values = window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break
            if randint(1, 10) < 5:  # simulate a hit or a miss
                window[event].update('H', button_color=('white', 'red'))
                window['-MESSAGE-'].update('Hit')
            else:
                window[event].update('M', button_color=('white', 'black'))
                window['-MESSAGE-'].update('Miss')
        window.close()

    Battleship()


# v1

# import GuiGAMES as guiGames
# guiGames.MinesweeperPlay()

#take it out of the function - it doesn't run like this
def MinesweeperPlay():
    import PySimpleGUI as sg
    import random
    import sys

    '''
    The classic Minesweeper game
    Original code was posted here:
    https://pysimplegui.trinket.io/sites/minesweeper

    Requires PySimpleGUI version 4.11.0 and higher
    '''

    blank = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAA5SURBVEhL7c0xAQAgDMTABynVU7MohAUN6ZJbMmbV6ZsB+xfnGOMY4xjjGOMY4xjjGOMY4xgzNE4euGMCWklhg+IAAAAASUVORK5CYII='
    bomb = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAHLklEQVR4nMWVTYydVRnHf+fjfd+59/bOnbnMTL2WthRaa2qlAhEwgpSSWIiKCXFWuHCBuHOhiQs3DcRENy5cmKiRkBgXkEESNEY0VKtGUm2RBGIsWFPDjJ3OR++d+/l+nXMeF3NbB+wAmhCf5Gzek/f5nf85z/N/FO9hnP0+0d6dTCSaBIuq/5HL6jECgHovgCJoFqgPKuw2iqZx9AtFgWNtR5O2uhdn/5fEJ06c0KdOndIAc3NzsrCwEARAUAsLqO7PmbR19sWWwwhHMKSxcEESVgY9zgCr71ax4s23E7ZuagWb5LHis1TdGreHiIfE8zHTZYcIb/gaP9Ga0ysD/vZ2ihX33GNOHD0aHnv88YCIbLKF+c9/dd8rr7z4mSiK7I5686XTp577rcjxZPWZS7flo436+oV8ojYzOqDj0UfNuj+oz8lEaElT1zkbDOcnYWkbxfMG9YxHrsqYiuN4riiK6PinHm52up1nB/2NGWVi6tOzPHSw89KN4dULH2iGP/c3imKiKe+7br8+PLUr3Vspyuv1miRMyWKo8HSAk4NFzrwVrEAAJcDszFzr4Xpj5sE4qR5WSjXTUd9UqjUazRaDXtu5MuWTuy6qxTVjVqc/sfHiSXczPL0IkP2UD6qYW6XCncpyk0pZ8YqXtfCH+D5etm+GIqBozuz8cmvPwa/vufHDOyenZnGuoMwzFv/xVw4cPMTuPTfIUz9+wraqI86czzj9935x8PDrU3feVf3eN+/js68vP6qK7AeXE8OrMuKiKCaUomLgjcsrvNZSiN0CBai8f/dNPzp0y9HPHbrlbmZmZlzpnHJlqdN0hNJWfejIrdxz7Jhqt1f59fPPMRxWmJnKTOfS6yLF5Ma9j+Hn5zv60XnWWSAdJKz2c4J0GO76EummuKvVOq9hQe3ac+BnR+44fv/Hjz1YTjVqtlJNlAiUpSPPC1ZX1lhfWeLILR+hDJZfPPskS6/9nlF/zZf50BSl++FK238RsIB7m8LFMj+vWVjwrV03fHvvgSP333738aLVui6uVhLiyCBAUTiyLAKBoij4zQu/orexzoVzL9FeXiTWpZms4Scsj/hJfXK9F54CDOC3By8s+JmZ1q31qbmv3LD/Ztdq7YxqlZhKNSGyhiCC1ooQBG0UjakpmjMtVv55nmq1QnXXTqZrXbTPVLdXSJqH7zQa/LLbZePfdfOfoQGSau1rU9e1mG7OkiSxspElsgajNVZrjDForbDWIhLwIVDd0aRWb1JvTBPZCpVE68kavl6ROYt+ZAw02ynW1Wq1FSUTD0xUdyCICcEjIpt+Mf5bRAhB8M6jtcYai3eOLMsZpSX9QcCVQmRRsVVitTw8FrXtVeuJidpdkU0mlVIhy3I1HKbkeUleOIrSURQleV6SZTlZntPv9el12xR5Slk6sjzgvKZwBvFoo1FayaEkSfaOz62v+cai9GGUwhWF9DYus7qyShxbnPdENiKEQJbl9HoDet0+3U6HYa+DdwUoKJwgziFlSSUSFYIEDVFi3f485wLbTEALMh28I0v7jAYbXFxaBBRT0w2stXjvyfOcQX9I+/I67fVl+r3LDAcdRoMu6ShDuwKnPWUMbmy0IfjGmHFtsPfelWVBng7odVbRxjIc9JhuzrJjsoE2hrIo6G20aa8v0728TLd9idGgS56NSNMR4kokUpSlIEC52cHbvu8muCyWijwly4Z0Oyv44MlGfbrtS1Sqk9g4xpcF6ajPoNem11khHQ0YDXukwz5lkRO8IC5gdUCBLhx47PLYQ67ZTtb78k95NhQbxZtFIJCN+kRxgtab7ePKnLIocGVGnqfk2Yg8HeF8iYRAWTqK4IgMohXKBdXJito56MJbZvdVcJZlZ7SJzxs73C8hBO+dtjZCa4vW47NIwDtHOR4WRZFRlhlFnuHKAufKzXYLeKMwIvwOuhu8jXtZIHe+eCJPB98K3nnvSm1shLEWrQ2CgAjeX1GebR6izPHe4b272vMhoAIoY/R33+GJUWz2WS2Ok7/EycRuY6w3NjLWRltMRPBuE+JdSQiB4B3e+61gB1il1PMi8sA47zWv+QrYAN4Yc8wYe1JrHZTWaG20UpvDSyQQQkBCIAQ/XmGrw12BriVJcluWZUvj3NuCr4QBiCL9BWutRFEscRyXcZyEOE4kjmOJokissWKMEa21KKVknLgERCnVsdbeMc53TbfaLiyAMebTSqklpZQopURrHYwxQWsdxt8CqDCGyiaUs1EUHd4q4r8NC5AkjX3G2CeVUhtXkl9rKa0vGhN9Y3p6+opLvWvoVjvTjcaehk7s9ZG1czaKZrN8eFc27B11RbovBF8VEZTSoo3px0ntXKVSf8Em1bNFlnaUDxeVGlxcW1sbso1pbAcGsLOzhyZEBvVgmY6jSlW0rYsvG96XNXFilNXO2qiv0RulK4ai/NB63dE6HSwvL+e8Ux/9v+NflpbtGxq9lrUAAAAASUVORK5CYII='
    flag = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAE9ElEQVR4nL2WTWxUVRTHf+fe+147pbQKFChUipREKUYEEhAT2SgGNP0IpkkXsDCwIWHVdMWGuDEkRIwJC+OCEQkbiCB2ISQkiiHRlCIsnBqirZCWr1JqKRPBmXn3uJg37bR0qNHqP3nJzP363XPOPedeUVURESUvAbRlTf0zodWGocePrl3ovZeO+0KgAngAFMY7wDMhib9cUVsIZIr+o6pipkBpe7UuIWQuOOu/r51T/jbwprX2hDHmJ2NMyhhzVUQ+rK2tXeacyznnvHPOG2M8EMVQsda+IyKfAXOL1wcQERWKtB8MQOqVpTseRdH+c6mhPg9bmCJjDLlcbgT4CPgauAsEZWVlz2cymc0i0gysBUa89yuAsYKxxa4plgD6+Y6X5yS7b9258OtIZexKLbhRRDSKIr9x40bX3NxMTU0Nt2/f/iOZTAbXr18PrLWoKrH1t733rcCP8XxPCQnAx1tXlm1bvbi/PHQRIpExRo0xGgSBioju2bNH0+m0T6fT2YGBAe3v79f79+/rhg0bIhHJOuciY0wuntcRr21LQSfBW9bU/lBdESpIzsZg55wCOjw8rMlkUltbW3Xnzp26adMmr6r+0KFDCmgYhj6GPmCaGE+rtrb8zt5du+TUouqEgmRtkcXOOd27d6+mUim9ePGinjlzRs+fP68DAwPa0NCggDrn1BgTxd858id7EthMBQ8N5QeEVgYTgQF0fIr3nlwux+HDh+nu7iaRSBAEAXV1dTQ2NmKtpby8nCiKIB9PA3xDPp0mudqVstwZO5AIJsbGJ5nOzk6uXLlCT08Ply5dIp1OM2/ePFpaWjh27Bi7du3iyJEjOOckiiJUdR1P5vuTFhcUWBkod/luEYP3nvnz53Pw4EHOnj1LfX09XV1dnD59mqqqKjo7Ozl+/DgLFixAZMKrItJDnNtPtXjhwnyuOSe3yvJggyree6IoYvv27aRSKXbv3k1vby9jY2OMjo7S3NxMX18fxhhEhCiKBEBVXwc+AR7GcJ3W4saT+Y4glDuBNR7EeFUNgoDR0VGGh4e1o6NDV61axYEDB2hqauLo0aMkk0my2Szt7e1473HOeSASkc1ANUXFo5QEYP9bjfPeeHHhiLVGjTG5IAiyIuLb29u1r69P169fr7ELFdDq6mrdt2+fr6+vz4lIZK3VOKV6gFXxuiVDOw4+0dZmt7206JdEvogUFlFghHyJ1DAM1TmXC8MwS75SKaDGGBWRq8aY95g4zU/P41gGoHXNku+enVOmIL9ZkQ+cc69VVlYuAKorKirWicipwoastRqG4Ygx5gtrbQuTz8/fgo4XkdY1tV+9sHjup0BVqZnW2iZjzC5r7RZg4dTuUtBp87hQRECG1j9X/e21Ow/HltVTfuMGGSYOiQAaRVHXNDDI521UyrinBhv0VjqTWw3I8uXkmLiptOi3jQ0oWBcxEe+SmgHMoMUsmmGRwuU/I2xGcKGIqJhBRWuK22ZL08a4UEQM3CSf/Jw8WfoS/yea1uL3Y5f9mcncVaFs68qVZUy8Qv47cEF3E/fui6KJxKOa2QLOBFZALl8mq8LjyEWLAfb/Hxa3teX7BPndqCwF6G2bPXDJh8B4EVEdEqRuUtssaKY8BpFbQN1sAWcEj+etMojo1Br8r1XS1Zwk5upNYMWkzcyCjKpOG7cT8eNMA/kZ+BJmr4ioqvwF0Vn06LBZVccAAAAASUVORK5CYII='

    # On Windows runs best with board size of 20 x 14 and bombs = 80
    font = 'Courier 16 bold'
    width = 10  # Board Width
    height = 8  # Board Height
    all = 10  # BOMBS
    new_start = True
    size = (30, 30)
    # 0: 0, 1: hidden card, 2: bomb card, 3: flag card, 4: shown card
    im = ['', blank, bomb, flag, '']
    color = [('grey', 'grey'), ('black', 'green'),
             ('black', 'green'), ('black', 'green'), ('black', 'grey')]

    def binding_all():  # Bind right button of mouse to cell object

        for x in range(width):
            for y in range(height):
                window[b[x][y].key].bind(
                    '<Button-3>', '+RIGHT')

    # Setting for top buttons
    def button1(text, key=None, disabled=False, button_color=('white', 'green')):

        return sg.Button(text, pad=(10, 10), font=font, focus=False, key=key,
                         disabled=disabled, button_color=button_color)

    def button2(x, y):  # define cell as instance of button and

        b[x][y] = button(x, y)  # bulid Button
        return b[x][y].button

    def check_blank(x, y):  # Check if cell near 0-bomb cel

        if b[x][y].num == 0: return False
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0: continue
                if ((0 <= x + i < width) and (0 <= y + j < height) and
                        (b[x + i][y + j].num == 0)): return True
        return False

    def check_num():  # check number of bombs, flags and hides

        bomb_count = flag_count = hide_count = 0
        for x in range(width):
            for y in range(height):
                if b[x][y].state == 1:
                    hide_count += 1
                elif b[x][y].state == 2:
                    bomb_count += 1
                elif b[x][y].state == 3:
                    flag_count += 1
        return bomb_count, flag_count, hide_count

    # Count number of bombs about cell
    def count_bomb(x, y):

        global bomb
        if bomb[x][y] == 10: return 10
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0: continue
                if ((0 <= x + i < width) and (0 <= y + j < height) and
                        (bomb[x + i][y + j] == 10)):
                    count += 1
        return count

    # set position for all boms
    def deal():

        global bomb
        bomb_list = random.sample(range(width * height), all)
        bomb = [[0 for y in range(height)] for x in range(width)]

        for x in range(width):
            for y in range(height):
                if x * height + y in bomb_list: bomb[x][y] = 10

        for x in range(width):
            for y in range(height):
                bomb[x][y] = count_bomb(x, y)

        return

    def new_card():  # refresh all cells to hidden card

        for x in range(width):
            for y in range(height):
                b[x][y].state = 1
                b[x][y].num = bomb[x][y]
                b[x][y].color = color[1]
                b[x][y].update(1)

    def show_blank():  # Show all cell not around by any bomb

        for x in range(width):
            for y in range(height):
                if b[x][y].num == 0:
                    b[x][y].update(0)
                elif check_blank(x, y):
                    b[x][y].update(4)

    # Class for each button object
    class button():

        def __init__(self, x, y):

            self.x = x
            self.y = y
            self.state = 1
            self.color = color[self.state]
            self.disabled = False
            self.key = (x, y)  # keys can be ANYTHING, not just strings
            self.num = bomb[x][y]
            self.button = sg.Button(' ',
                                    auto_size_button=False,
                                    border_width=2,
                                    button_color=self.color,
                                    disabled=self.disabled,
                                    focus=False,
                                    font=font,
                                    image_size=size,
                                    # image_filename=im[self.state],
                                    image_data=im[self.state],
                                    key=self.key,
                                    pad=(1, 1))

        def right_click(self):  # Right_click handler

            if self.state == 1:
                self.update(3)
            elif self.state == 3:
                self.update(1)

        def update(self, state):  # update state of cell

            self.state = state
            if state == 0:
                self.disabled = True
                text = ' '
            elif state in [1, 2, 3]:
                self.disabled = False
                text = ' '
            elif state == 4:
                self.disabled = True
                text = str(self.num)
            self.color = color[self.state]
            window[self.key].Widget['disabledforeground'] = 'white'
            self.button.Update(text=text, disabled=self.disabled,
                               # image_filename=im[self.state],
                               image_data=im[self.state],
                               image_size=size,
                               button_color=self.color)

    # Check platform, only for Windows. Maybe wrok on other platform
    # if not sys.platform.startswith('win'):
    #     sg.popup_error('Sorry, you gotta be on Windows')
    #     sys.exit(0)

    # set theme for window
    sg.change_look_and_feel('DarkGreen')

    deal()  # Initial position of bombs
    b = [[0 for j in range(height)] for i in range(width)]

    layout = [[button1('New Game', key='-New Game-'),  # Layout of window
               button1('Game Over', key='-Game Over-'),
               button1('Target:' + str(all), key='-Target-'),
               button1('Bomb:0', key='-Count-Bomb-'),
               button1('Flag:0', key='-Count-Flag-')]] + [
                 [button2(x, y) for x in range(width)] for y in range(height)]

    window = sg.Window('MineSweeper', layout=layout, finalize=True)  # Create window
    binding_all()  # Binding right button event handler of all cells
    show_blank()  # Show all cells near no-bomb cell

    new_start = True  # Flag for new game
    message = False  # Flag for game over message sent

    while True:

        if new_start:  # Actions for new game

            deal()
            new_card()
            show_blank()
            message = False
            new_start = False
            pass

        event, values = window.read()  # read window event

        if event == None or event == '-Game Over-':  # Window close / Game over
            break

        elif event == '-New Game-':  # New Game, set the flag
            new_start = True

        elif isinstance(event, tuple):  # buttons have tuple for event
            right_click = False
            if isinstance(event[0], tuple):  # if the tuple has a tuple, then it's a right click event
                x, y = event[0]
                right_click = True
            else:
                x, y = event
            if not right_click:
                if b[x][y].state == 1:
                    if b[x][y].num == 10:
                        b[x][y].update(2)
                    else:
                        b[x][y].update(4)
            else:
                b[x][y].right_click()
        # Update number onf bombs, flags
        bomb_num, flag_num, hide_num = check_num()
        window['-Count-Bomb-'].Update(text='Bomb:' + str(bomb_num))
        window['-Count-Flag-'].Update(text='Flag:' + str(flag_num))

        # Check if game over
        if hide_num == 0 and (bomb_num + flag_num == all) and (not message):
            message = True
            sg.popup('Game Over', title='Note')

    window.close()


# v1

# import GuiGAMES as guiGames
# guiGames.ticTacToePlay()

def ticTacToePlay():
    import PySimpleGUI as sg

    layout = [[sg.Text('X Starts First')]]
    layout += [[sg.Button(size=(3, 2), key=(row, col)) for col in range(3)] for row in range(3)]
    layout += [[sg.Button('Reset'), sg.Button('Cancel')]]

    window = sg.Window('Window Title', layout, use_default_focus=False)

    board, player = {}, 0

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Reset':
            board = {}
            for row in range(3):
                for col in range(3):
                    window[(row, col)].update(' ')
        elif event not in board:
            board[event] = player
            window[event].update('O' if player else 'X')
            player = (player + 1) % 2
    window.close()


