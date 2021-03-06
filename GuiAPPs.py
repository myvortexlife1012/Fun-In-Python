#GUI APPS

# import GuiAPPs as apps
# apps.basicCanvasDrawing1() # LEARNING - tkinter canvas - drawing
#
# apps.fileListWithOpen()
#
"""
import GuiAPPs as apps
#imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\png.png'
#imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
apps.openImage4Canvas(imagePath,500,500) # w and h
"""
# guiApps.notificationMESSAGE()
#
# apps.simpleWindow1()
#
# apps.guiBGchangeShow()
# apps.guiAppShow()
# apps.guiBallMovePlay()
# apps.guiCalcShow()
# apps.guiColorsShow()
# apps.GuiCOMMISSIONshow()
# apps.GuiCOOLdesignShow()
# apps.guiDateShow()
# apps.guiPhotoGalleryShow() # "z-IMAGES_1\0.cool\"
# apps.HTMLlikeDesignShow()
# apps.GuiMACLauncherShow()
# apps.GuiSplashSCREENshow()
# apps.GuiTIMERshow()
# apps.GuiWEATHERshow()
# import GuiAPPs as apps
# apps.GuiWindowLAYOUTSshow() #cycles thru them as you close them
# apps.GuiWithImageBUTTONSshow()
# apps.GUIphotosViewerBroke()

from tkinter import * #some programs need this out of the function



#--------------------------------




# import GuiAPPs as a
# a.pdnaBankSHOWMyPeople() # photo gallery layout
#
# make images buttons or links
#
# 6 Clickable Images with Filenames # a photo gallery layout # buttons that do things
def pdnaBankSHOWMyPeople():
    #import OPENsomething as o
    #peopleCSV = o.pdnaBankGetMyPeopleCSV()
    import listAllFILES as f
    nameImgs = [ ["Woman", "image.jpg"], ["Woman2", "image2.jpg"] ] # [] list of ... name, thumbImgPath
    print(f"\n--nameImgs ({len(nameImgs)}): {nameImgs}")
    c=0
    for nameImg in nameImgs:
        if c <= 10:
            name = nameImg[0]
            thumbPath = nameImg[1]
            print(f" ({c}) name/thumbPath ... {name} / {thumbPath}")
        else:
            break
        c += 1
    return nameImgs


#------------------------------------------

# import GuiAPPs as g
# x,y = g.getPixelxyFromDeg360(deg360=191.1)
def getPixelxyFromDeg360(deg360=191.1, position=0):
    #-------------------------------------------------
    # the 0 is having problems getting plotted right
    # -------------------------------------------------
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    #locations for the xy around the circle - accoring to each 30 degrees - a px to px line to draw the values on
    xyLoc = m.xyLoc # 0: {'start-deg': 0, 'end-deg': 30, 'minXY': [80, 340], 'maxXY': [120, 340]},

    #print(f"deg360: {deg360}")
    deg360 = float(deg360)

    #looping through all of the start and end degrees
    #when it matches - determine the right pixel location - along - from min-to-max
    # - EXAMPLE: 18Libra=18/30=0.6, so it would be .6 * the pixel distance from min to max + plus min
    for i in range(len(xyLoc)):
        loc = xyLoc[i]

        start_deg = loc['start-deg'] #start of the 12th cut piece
        end_deg = loc['end-deg'] #end of the 12th cut piece

        #if deg360<=30:
            #pass
            #leftover_deg = deg360
            #print(f"HELP - deg360 ({deg360}) >= start_deg ({start_deg}) and deg360 ({deg360}) < end_deg ({end_deg})")
        # this is the degree group I'm in - found
        if deg360>=start_deg and deg360<end_deg: #if it falls within:
            leftover_deg = f.round_down4(deg360-start_deg) # how much is left - % of /30 - that is how far - between minxy and maxxy
            #for now just return the minxy value - to get things going

            # it will be a percentage between these pixel locations
            minX, minY = loc['minXY']
            maxX, maxY = loc['maxXY']
            #print(f"minY: {minY} / maxY: {maxY}") #340 - 340 = 0
            pxDistanceDiffX = maxX - minX
            if pxDistanceDiffX<0:
                pxDistanceDiffX = minX - maxX
            #print(f"pxDistanceDiffX: {pxDistanceDiffX}")
            pixelX_add = int(f.round_down(pxDistanceDiffX / 30 * leftover_deg))
            pxDistanceDiffY = maxY - minY
            if pxDistanceDiffY<=0:
                pxDistanceDiffY = minY - maxY
            #print(f"pxDistanceDiffY: {pxDistanceDiffY}") #DiffY is 0 - when deg is under 30
            pixelY_add = int(f.round_down(pxDistanceDiffY / 30 * leftover_deg))
            #----------------------------
            positionMoveX = position * 15 # x--
            positionMoveY = position * 15 # y|
            #positionMoveX = 0
            #positionMoveY = 0

            if minX < maxX:
                x = minX + pixelX_add + positionMoveX # x--
            else: # if minX > maxX:
                x = minX - pixelX_add - positionMoveX # x--

            if minY < maxY:
                y = minY + pixelY_add + positionMoveY # y|
            else: # if minY > maxY:
                y = minY - pixelY_add - positionMoveY # y|

            #print(f"{i}) deg360: {deg360}, leftover_deg: {leftover_deg}  / NEW X,Y - / minX: {minX}, NEW-x: {x}, maxX: {maxX} / minY: {minY}, NEW-y: {y}, maxY: {maxY}  /  pxDistanceDiffX: {pxDistanceDiffX}, pxDistanceDiffY: {pxDistanceDiffY}  /  pixelX_add: {pixelX_add}, pixelY_add: {pixelY_add}")

            return x, y

#------------------------------------------

# import GuiAPPs as g
# g.chartWheel()
def chartWheel():
    show = True
    #---------------------------------------
    # UNCOMMENT LAST LINE - TO SEE OUTPUT
    #---------------------------------------
    import GuiAPPs as g
    import ASTROLOGYfunctions as aa
    import FUNCTIONS as f
    #me = aa.me()
    #planets2 = me['planets']['360']
    today = aa.today()
    planets2 = today['planets']['360']

    geo = []
    helio = []
    #remove helio - or seperate them
    for planetLine in planets2:
        #print(f"planetLine: {planetLine}")
        p1=planetLine.split(": ")
        planetName = p1[0]
        DegRxDecDisSpeed = p1[1]
        d = DegRxDecDisSpeed.split("/")
        degrees = d[0]
        #Rx = d[1]
        #declination = d[2]
        #distance = d[3]
        #speed = d[4]

        if "_g" in planetName:
            geo.append(planetLine)
        if "_h" in planetName:
            helio.append(planetLine)

    planets = geo
    #planets = helio
    #----------------------------------------
    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('Astrology Chart Wheel for Magi')
    w.geometry('880x685')  # window width and height
    w.config(bg='#345')  # window background color
    # THE CANVAS (w) - is tied in below with the passed 'w' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=650,  # it's a square area, w-h
        width=700,
        bg="#fff"  # canvas background color
    )
    canvas.pack(side = TOP, anchor = NW, padx = 70, pady = 20)
    #-------------------------------------------
    # title
    canvas.create_text(350, 20, fill="darkblue", font="Times 18 italic bold", text="Astrology Chart Wheel for Magi")
    # -------------------
    # the chart circle:
    canvas.create_oval(110, 110, 570, 570)
    # -------------------
    canvas.create_text(80, 340, fill="darkblue", font="Times 10 italic bold", text="0 deg")
    canvas.create_text(120, 475, fill="darkblue", font="Times 10 italic bold", text="30 deg")
    canvas.create_text(212, 565, fill="darkblue", font="Times 10 italic bold", text="60 deg")
    canvas.create_text(340, 600, fill="darkblue", font="Times 10 italic bold", text="90 deg")
    canvas.create_text(470, 575, fill="darkblue", font="Times 10 italic bold", text="120 deg")
    canvas.create_text(570, 480, fill="darkblue", font="Times 10 italic bold", text="150 deg")
    canvas.create_text(600, 340, fill="darkblue", font="Times 10 italic bold", text="180 deg")
    canvas.create_text(570, 200, fill="darkblue", font="Times 10 italic bold", text="210 deg")
    canvas.create_text(470, 110, fill="darkblue", font="Times 10 italic bold", text="240 deg")
    canvas.create_text(340, 80, fill="darkblue", font="Times 10 italic bold", text="270 deg")
    canvas.create_text(210, 105, fill="darkblue", font="Times 10 italic bold", text="300 deg")
    canvas.create_text(113, 200, fill="darkblue", font="Times 10 italic bold", text="330 deg")

    canvas.create_line(80, 340, 600, 340)  # line, x1,y1, x2,y2
    canvas.create_line(340, 600, 340, 80)  # line, x1,y1, x2,y2
    canvas.create_line(120, 475, 570, 200)  # line, x1,y1, x2,y2
    canvas.create_line(212, 565, 470, 110)  # line, x1,y1, x2,y2
    canvas.create_line(470, 575, 210, 105)  # line, x1,y1, x2,y2
    canvas.create_line(570, 480, 113, 200)  # line, x1,y1, x2,y2

    #---------------------------
    # plot all the planets with their name - around the circle - geo longitudes
    # if there is already one planet that is in that location - conjuction - move it away - to see it

    used5degSection = {}
    c=0
    for i in range(72):
        used5degSection[i * 5] = 0
        c += 5

    #print(f"used5degSection ({len(used5degSection)}):")
    #f.print2(used5degSection)
    #print("exiting")
    #exit()
    for planet in planets:
        p1=planet.split(": ")
        planetName = p1[0]
        DegDecDisSpeed = p1[1]
        d = DegDecDisSpeed.split("/")
        degrees = f.round_down1(float(d[0]))
        degreesRoundedDownTo5 = aa.degreesRoundedDownToA5(degrees)
        used5degSection[degreesRoundedDownTo5] += 1
        numberInThatPosition = used5degSection[degreesRoundedDownTo5]
        #declination = d[1]
        #distance = d[2]
        #speed = d[3]
        x,y = g.getPixelxyFromDeg360(deg360=degrees, position=numberInThatPosition)

        #based on the degrees - plot around the cirlce - the planet name
        text1 = f"{planetName} ({degrees})"
        canvas.create_text(x, y, fill="darkblue", font="Times 6", text=text1) # italic bold
        #text1 = canvas.create_text( 140, 68, fill="darkblue", font="Times 10 italic bold", text="Chiron")


    if show==True:
        w.mainloop() # starts it



"""
#use the lines to Connect Planets
#canvas.create_line(50, 50, 200, 100) #line, x1,y1, x2,y2
#
#canvas.create_line(300, 35, 300, 200, dash=(4, 2)) # dashed line
#canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85) # triangle

#-----------------------------

# These draw the lines - so it looks like divided by 12 signs / sections
#
canvas.create_text(80, 340, fill="darkblue", font="Times 10 italic bold", text="0 deg")
canvas.create_text(120, 475, fill="darkblue", font="Times 10 italic bold", text="30 deg")
canvas.create_text(212, 565, fill="darkblue", font="Times 10 italic bold", text="60 deg")
canvas.create_text(340, 600, fill="darkblue", font="Times 10 italic bold", text="90 deg")
canvas.create_text(470, 575, fill="darkblue", font="Times 10 italic bold", text="120 deg")
canvas.create_text(570, 480, fill="darkblue", font="Times 10 italic bold", text="150 deg")
canvas.create_text(600, 340, fill="darkblue", font="Times 10 italic bold", text="180 deg")
canvas.create_text(570, 200, fill="darkblue", font="Times 10 italic bold", text="210 deg")
canvas.create_text(470, 110, fill="darkblue", font="Times 10 italic bold", text="240 deg")
canvas.create_text(340, 80, fill="darkblue", font="Times 10 italic bold", text="270 deg")
canvas.create_text(210, 105, fill="darkblue", font="Times 10 italic bold", text="300 deg")
canvas.create_text(113, 200, fill="darkblue", font="Times 10 italic bold", text="330 deg")
"""



#------------------------------------------

# import GuiAPPs as a
# a.pdnaBankGallery3() # photo gallery layout
#
# make images buttons or links
#
# 6 Clickable Images with Filenames # a photo gallery layout # buttons that do things
# 3 across, 3 down, 9 total per page
def pdnaBankGallery3():
    s = 24 #0, 24, 48, etc #startingNumber
    #print(f"\n--nameImgs ({len(nameImgs)}): {nameImgs}")
    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('pdnaBank Gallery')
    w.geometry('850x700')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=650,  # it's a square area, w-h
        width=700,
        bg="#fff"  # canvas background color
    )

    #canvas.pack()  # maybe it gets it ready for you to draw on it
    canvas.pack(side = TOP, anchor = NW, padx = 70, pady = 20)  # maybe it gets it ready for you to draw on it

    """
    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle
    """
    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    imageFilepath = "C:/Users/myvor/PycharmProjects/pythonProject/z-IMAGES_1/grassy_hills.jpg"
    img1 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img2 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img3 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img4 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img5 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img6 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img7 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img8 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img9 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img10 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img11 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img12 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img13 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img14 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img15 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img16 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img17 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img18 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img19 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img20 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img21 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img22 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img23 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)
    img24 = ImageTk.PhotoImage(Image.open(imageFilepath))  # img = PhotoImage(file=imagePath)

    # -------------------

    #---------------------------
    #row 1
    button1 = Button(w, image=img1, command=quit)#.pack() #make the image clickable
    button1.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button1.place(x=80, y=68) # x-y|
    text1 = canvas.create_text( 140, 68, fill="darkblue", font="Times 10 italic bold",
        text="Grassy Hills") #nameImgs[0][0] # x-y| # "Person's Name Here"

    button2 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button2.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button2.place(x=300, y=68) # x-y|
    text2 = canvas.create_text( 370, 68, fill="darkblue", font="Times 10 italic bold",
        text="Grassy Hills") #nameImgs[0][0] # x-y| # "Person's Name Here"

    button3 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button3.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button3.place(x=530, y=68)  # x-y|
    text3 = canvas.create_text(600, 68, fill="darkblue", font="Times 10 italic bold",
        text="Grassy Hills") #nameImgs[0][0] # x-y| # "Person's Name Here"

    #---------------------------
    # row 2
    button4 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button4.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button4.place(x=80, y=130) # x-y|
    text4 = canvas.create_text( 140, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]

    button5 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button5.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button5.place(x=300, y=130) # x-y|
    text5 = canvas.create_text( 370, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[3][0]

    button6 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button6.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button6.place(x=530, y=130)  # x-y|
    text6 = canvas.create_text(600, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 3
    button7 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button7.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button7.place(x=80, y=200) # x-y|
    text7 = canvas.create_text( 140, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button8 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button8.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button8.place(x=300, y=200) # x-y|
    text8 = canvas.create_text(370, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button9 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button9.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button9.place(x=530, y=200)  # x-y|
    text9 = canvas.create_text(600, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]

    #---------------------------
    #row 4
    button10 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button10.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button10.place(x=80, y=270) # x-y|
    text10 = canvas.create_text( 140, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button11 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button11.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button11.place(x=300, y=270) # x-y|
    text11 = canvas.create_text(370, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button12 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button12.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button12.place(x=530, y=270)  # x-y|
    text12 = canvas.create_text(600, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 5
    button13 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button13.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button13.place(x=80, y=340) # x-y|
    text13 = canvas.create_text( 140, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button14 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button14.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button14.place(x=300, y=340) # x-y|
    text14 = canvas.create_text(370, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button15 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button15.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button15.place(x=530, y=340)  # x-y|
    text15 = canvas.create_text(600, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 6
    button16 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button16.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button16.place(x=80, y=410) # x-y|
    text16 = canvas.create_text( 140, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button17 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button17.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button17.place(x=300, y=410) # x-y|
    text17 = canvas.create_text(370, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button18 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button18.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button18.place(x=530, y=410)  # x-y|
    text18 = canvas.create_text(600, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]



    #---------------------------
    #row 7
    button19 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button19.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button19.place(x=80, y=480) # x-y|
    text19 = canvas.create_text( 140, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button20 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button20.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button20.place(x=300, y=480) # x-y|
    text20 = canvas.create_text(370, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button21 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button21.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button21.place(x=530, y=480)  # x-y|
    text21 = canvas.create_text(600, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]



    #---------------------------
    #row 8
    button22 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button22.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button22.place(x=80, y=550) # x-y|
    text22 = canvas.create_text( 140, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button23 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button23.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button23.place(x=300, y=550) # x-y|
    text23 = canvas.create_text(370, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button24 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button24.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button24.place(x=530, y=550)  # x-y|
    text24 = canvas.create_text(600, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #-------------------------------------------
    #at the top
    button1btn = Button(w, text="Quit", command=quit, anchor=W)
    button1btn.configure(width=20, activebackground="#33B5E5", relief=FLAT)
    button1btn.place(x=620, y=30) # x-y|

    canvas.create_text(350, 20, fill="darkblue", font="Times 18 italic bold",
        text=f"Create the Astrology Wheel for Magi") #nameImgs[2][0] # x-y|

    #MAKING TEXT clickable
    canvas.tag_bind(text1, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text2, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text3, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text4, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text5, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text6, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text7, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text8, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text9, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text10, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text11, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text12, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text13, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text14, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text15, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text16, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text17, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text18, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text19, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text20, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text21, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text22, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text23, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text24, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes




# import GuiAPPs as a
# a.pdnaBankGallery2() # photo gallery layout
#
# make images buttons or links
#
# 6 Clickable Images with Filenames # a photo gallery layout # buttons that do things
# 3 across, 3 down, 9 total per page
def pdnaBankGallery2():
    import listAllFILES as f
    nameImgs = f.returnNameImgs()
    print(f"\n--nameImgs ({len(nameImgs)}): {nameImgs}")
    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('pdnaBank Gallery')
    w.geometry('850x700')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=650,  # it's a square area, w-h
        width=700,
        bg="#fff"  # canvas background color
    )

    #canvas.pack()  # maybe it gets it ready for you to draw on it
    canvas.pack(side = TOP, anchor = NW, padx = 70, pady = 20)  # maybe it gets it ready for you to draw on it

    """
    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle
    """
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    #img = ImageTk.PhotoImage(Image.open(imagePath)) #img = PhotoImage(file=imagePath)

    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    img1 = ImageTk.PhotoImage(Image.open(nameImgs[0][1]))  # img = PhotoImage(file=imagePath)
    img2 = ImageTk.PhotoImage(Image.open(nameImgs[1][1]))  # img = PhotoImage(file=imagePath)
    img3 = ImageTk.PhotoImage(Image.open(nameImgs[2][1]))  # img = PhotoImage(file=imagePath)
    img4 = ImageTk.PhotoImage(Image.open(nameImgs[3][1]))  # img = PhotoImage(file=imagePath)
    img5 = ImageTk.PhotoImage(Image.open(nameImgs[4][1]))  # img = PhotoImage(file=imagePath)
    img6 = ImageTk.PhotoImage(Image.open(nameImgs[5][1]))  # img = PhotoImage(file=imagePath)

    # -------------------
    showBtns = True
    #-------------------


    #---------------------------
    #row 1
    button1 = Button(w, image=img1, command=quit)#.pack() #make the image clickable
    button1.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button1.place(x=80, y=68) # x-y|
    text1 = canvas.create_text( 140, 68, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[0][0] # x-y|

    button2 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button2.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button2.place(x=300, y=68) # x-y|
    text2 = canvas.create_text( 370, 68, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[1][0]

    button3 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button3.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button3.place(x=530, y=68)  # x-y|
    text3 = canvas.create_text(600, 68, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]

    #---------------------------
    # row 2
    button4 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button4.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button4.place(x=80, y=130) # x-y|
    text4 = canvas.create_text( 140, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]

    button5 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button5.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button5.place(x=300, y=130) # x-y|
    text5 = canvas.create_text( 370, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[3][0]

    button6 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button6.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button6.place(x=530, y=130)  # x-y|
    text6 = canvas.create_text(600, 130, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 3
    button7 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button7.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button7.place(x=80, y=200) # x-y|
    text7 = canvas.create_text( 140, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button8 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button8.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button8.place(x=300, y=200) # x-y|
    text8 = canvas.create_text(370, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button9 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button9.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button9.place(x=530, y=200)  # x-y|
    text9 = canvas.create_text(600, 210, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]

    #---------------------------
    #row 4
    button10 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button10.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button10.place(x=80, y=270) # x-y|
    text10 = canvas.create_text( 140, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button11 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button11.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button11.place(x=300, y=270) # x-y|
    text11 = canvas.create_text(370, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button12 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button12.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button12.place(x=530, y=270)  # x-y|
    text12 = canvas.create_text(600, 280, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 5
    button13 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button13.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button13.place(x=80, y=340) # x-y|
    text13 = canvas.create_text( 140, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button14 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button14.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button14.place(x=300, y=340) # x-y|
    text14 = canvas.create_text(370, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button15 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button15.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button15.place(x=530, y=340)  # x-y|
    text15 = canvas.create_text(600, 350, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #---------------------------
    #row 6
    button16 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button16.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button16.place(x=80, y=410) # x-y|
    text16 = canvas.create_text( 140, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button17 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button17.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button17.place(x=300, y=410) # x-y|
    text17 = canvas.create_text(370, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button18 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button18.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button18.place(x=530, y=410)  # x-y|
    text18 = canvas.create_text(600, 420, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]



    #---------------------------
    #row 7
    button19 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button19.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button19.place(x=80, y=480) # x-y|
    text19 = canvas.create_text( 140, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button20 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button20.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button20.place(x=300, y=480) # x-y|
    text20 = canvas.create_text(370, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button21 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button21.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button21.place(x=530, y=480)  # x-y|
    text21 = canvas.create_text(600, 490, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]



    #---------------------------
    #row 8
    button22 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button22.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button22.place(x=80, y=550) # x-y|
    text22 = canvas.create_text( 140, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[4][0]

    button23 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button23.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button23.place(x=300, y=550) # x-y|
    text23 = canvas.create_text(370, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[5][0]

    button24 = Button(w, image=img1, command=quit)  # .pack() #make the image clickable
    button24.configure(width=50, height=50, activebackground="#33B5E5", relief=FLAT)
    button24.place(x=530, y=550)  # x-y|
    text24 = canvas.create_text(600, 560, fill="darkblue", font="Times 10 italic bold",
        text="Person's Name Here") #nameImgs[2][0]


    #-------------------------------------------
    #at the top
    button1btn = Button(w, text="Quit", command=quit, anchor=W)
    button1btn.configure(width=20, activebackground="#33B5E5", relief=FLAT)
    button1btn.place(x=620, y=30) # x-y|

    canvas.create_text(350, 20, fill="darkblue", font="Times 18 italic bold",
        text=f"Your PDNABank ({len(nameImgs)})") #nameImgs[2][0] # x-y|

    #MAKING TEXT clickable
    canvas.tag_bind(text1, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text2, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text3, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text4, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text5, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text6, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text7, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text8, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text9, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text10, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text11, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text12, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text13, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text14, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text15, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text16, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text17, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text18, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text19, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text20, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text21, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text22, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text23, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".
    canvas.tag_bind(text24, "<Button-1>", quit)  ## when the square is clicked runs function "clicked".

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes






# import GuiAPPs as a
# a.pdnaBankGallery1() # photo gallery layout
#
# make images buttons or links
#
# 6 Clickable Images with Filenames # a photo gallery layout # buttons that do things
def pdnaBankGallery1():
    import listAllFILES as f
    nameImgs = f.returnNameImgs()
    print(f"\n--nameImgs ({len(nameImgs)}): {nameImgs}")
    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('pdnaBank Gallery')
    w.geometry('800x700')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=650,  # it's a square area, w-h
        width=650,
        bg="#fff"  # canvas background color
    )

    #canvas.pack()  # maybe it gets it ready for you to draw on it
    canvas.pack(side = TOP, anchor = NW, padx = 70, pady = 20)  # maybe it gets it ready for you to draw on it

    """
    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle
    """
    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    #img = ImageTk.PhotoImage(Image.open(imagePath)) #img = PhotoImage(file=imagePath)

    # nameImgs[0][0]=name ... nameImgs[0][1]=thumbnail

    img1 = ImageTk.PhotoImage(Image.open(nameImgs[0][1]))  # img = PhotoImage(file=imagePath)
    img2 = ImageTk.PhotoImage(Image.open(nameImgs[1][1]))  # img = PhotoImage(file=imagePath)
    img3 = ImageTk.PhotoImage(Image.open(nameImgs[2][1]))  # img = PhotoImage(file=imagePath)
    img4 = ImageTk.PhotoImage(Image.open(nameImgs[3][1]))  # img = PhotoImage(file=imagePath)
    img5 = ImageTk.PhotoImage(Image.open(nameImgs[4][1]))  # img = PhotoImage(file=imagePath)
    img6 = ImageTk.PhotoImage(Image.open(nameImgs[5][1]))  # img = PhotoImage(file=imagePath)

    # -------------------
    showBtns = True
    showImgs = False
    #-------------------

    #row 1
    if showImgs == True:
        canvas.create_image(
            20,
            10,
            anchor=NW,
            image=img1
        )
    if showBtns==True:
        button1 = Button(w, image=img1, command=quit)#.pack() #make the image clickable
        button1.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button1.place(x=120, y=68)
    if showImgs==True:
        canvas.create_image(
            290,
            10,
            anchor=NW,
            image=img2
        )
    canvas.create_text(
        130,
        220,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[0][0]
    )
    if showBtns==True:
        button2 = Button(w, image=img2, command=quit)  # .pack() #make the image clickable
        button2.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button2.place(x=390, y=68)
    canvas.create_text(
        400,
        220,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[1][0]
    )
    # row 2
    if showImgs==True:
        canvas.create_image(
            20,
            200,
            anchor=NW,
            image=img3
        )
    if showBtns==True:
        button3 = Button(w, image=img3, command=quit)  # .pack() #make the image clickable
        button3.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button3.place(x=120, y=258)
    canvas.create_text(
        140,
        400,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[2][0]
    )
    if showImgs==True:
        canvas.create_image(
            290,
            200,
            anchor=NW,
            image=img4
        )
    if showBtns==True:
        button4 = Button(w, image=img4, command=quit)  # .pack() #make the image clickable
        button4.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button4.place(x=390, y=258)
    canvas.create_text(
        400,
        400,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[3][0]
    )
    #row 3
    if showImgs==True:
        canvas.create_image(
            20,
            380,
            anchor=NW,
            image=img5
        )
    if showBtns==True:
        button5 = Button(w, image=img5, command=quit)  # .pack() #make the image clickable
        button5.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button5.place(x=120, y=435)
    canvas.create_text(
        140,
        590,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[4][0]
    )
    if showImgs==True:
        canvas.create_image(
            290,
            380,
            anchor=NW,
            image=img6
        )
    if showBtns==True:
        button6 = Button(w, image=img6, command=quit)  # .pack() #make the image clickable
        button6.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button6.place(x=390, y=435)
    canvas.create_text(
        400,
        590,
        fill="darkblue",
        font="Times 10 italic bold",
        text=nameImgs[5][0]
    )
    #at the top
    button1 = Button(w, text="Quit", command=quit, anchor=W)
    button1.configure(width=20, activebackground="#33B5E5", relief=FLAT)
    button1.place(x=320, y=30)

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes








""" TKINTER CANVAS:
The Canvas widget can support the following standard items ???

arc ??? Creates an arc item, which can be a chord, a pieslice or a simple arc.

coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=150, fill="blue")
image ??? Creates an image item, which can be an instance of either the BitmapImage or the PhotoImage classes.

filename = PhotoImage(file = "sunshine.gif")
image = canvas.create_image(50, 50, anchor=NE, image=filename)
line ??? Creates a line item.

line = canvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
oval ??? Creates a circle or an ellipse at the given coordinates. It takes two pairs of coordinates; the top left and bottom right corners of the bounding rectangle for the oval.

oval = canvas.create_oval(x0, y0, x1, y1, options)
polygon ??? Creates a polygon item that must have at least three vertices.

oval = canvas.create_polygon(x0, y0, x1, y1,...xn, yn, options)
"""

#--------------------------------


# import GuiAPPs as apps
# apps.wholeImageIsAButton()

def wholeImageIsAButton():
    def do():
        print("Hello World")

    # from tkinter import *

    ws = Tk()
    ws.title('Image Is A Button - click it')
    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    img = PhotoImage(file=imagePath)
    Button(
        ws,
        image=img,
        command=do
    ).pack()

    ws.mainloop()


#-----------------------------


# import GuiAPPs as apps
# apps.photoWithCaption()
def photoWithCaption():
    # from tkinter import *
    from PIL import ImageTk, Image

    ws = Tk()
    ws.title('View Image with Caption')
    ws.geometry('500x500')

    canvas = Canvas(
        ws,
        width=500,
        height=400
    )
    canvas.pack()
    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
    img = ImageTk.PhotoImage(Image.open(imagePath))

    canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
    )
    Label(
        ws,
        text=f'width: {img.width()} height: {img.height()}'
    ).pack()

    ws.mainloop()


#---------------------------


# combine parseBirthchartHTML with tkinter - read it to the screen, going down
# see if you can read it in one text command with \n

# import GuiAPPs as a
# a.seeBirthchartSigns()

def seeBirthchartSigns(): #as text
    import ASTROLOGYfunctions as aa
    import FUNCTIONS as f
    import OPENsomething as o
    me = aa.me()
    planets = me['planets']['360']

    print(f"planets: {planets}")
    # combine it all to a string with /n's
    string = "My Birthchart:\n\n"
    for planet in planets:
        string += planet + "\n"

    print(f"string: {string}")
    # -----------------------------
    """
    #add it into a GUI - show the whole string
    import GuiAPPs as a
    a.photoWithBigCaption(string=string)
    """

    # Import Module
    import tkinter as tk

    # Create Object
    ws = tk.Tk()
    ws.title('View Birthchart Signs')
    ws.geometry('300x300')

    # Create Label and add some text
    the_label = tk.Label(ws, text="Some Birchart Data for a Person, Birthday, Lat & Long")
    # using place method we can set the position of label # x-y|
    the_label.place(relx=.02, rely=0.05, anchor='nw')
    # Create Label and add some text
    the_label2 = tk.Label(ws, text=string)
    # using place method we can set the position of label # x-y|
    the_label2.place(relx=.25, rely=0.2, anchor='nw')
    # Execute Tkinter
    ws.mainloop()





# import GuiAPPs as a
# a.photoWithBigCaption(string="")
def photoWithBigCaption(string=""):
    # from tkinter import *
    from PIL import ImageTk, Image

    ws = Tk()
    ws.title('View Image with Caption')
    ws.geometry('500x500')

    canvas = Canvas(
        ws,
        width=500,
        height=400
    )
    canvas.pack()
    imagePath = 'C:\\Users\\myvor\\PycharmProjects\\pythonProject\\z-IMAGES_1\\grassy_hills.jpg'
    img = ImageTk.PhotoImage(Image.open(imagePath))

    canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
    )
    textLabel = Label(
        ws,
        text=f'width: {img.width()} height: {img.height()}\n\n{string}'
    ).pack()
    textLabel.place(relx=0.5, #x-y|
                       rely=0.5,
                       anchor='center')
    ws.mainloop()


#--------------------------------

# import GuiAPPs as apps
# apps.simpleWindow1()

def simpleWindow1():
    import PySimpleGUI as sg
    sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()



# import GuiAPPs as apps
# apps.simpleWindow2()

def simpleWindow2():
    import PySimpleGUI as sg

    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


#---------------------------







# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
# apps.openImage1(imagePath)

#opens as a background in tkinter

#using LABELS:
def openImage1(imagePath="c:/path/to.jpg"):
    import tkinter
    #from tkinter import *
    from PIL import Image, ImageTk

    root = Tk()

    # Create a photoimage object of the image in the path
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
    image1 = Image.open(imagePath)
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=10, y=10) #label1.place(x=<x_coordinate>, y=<y_coordinate>)
    root.mainloop()




# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
# apps.open1PngGif(imagePath)

# opens pngs and gifs - tkinter - #it goes full screen for large images
# USES LABELS
def open1PngGif(imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\png.png'):
    # from tkinter import *
    ws = Tk()
    ws.title('Image Viewer')
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\png.png'
    img = PhotoImage(file=imagePath)
    Label(
        ws,
        image=img
    ).pack()

    ws.mainloop()





# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
# apps.openImage2(imagePath,500,500) # w and h

#opens as a background in tkinter
#using LABELS:
def openImage2(imagePath="c:/path/to.jpg",width=500, height=500):
    #from tkinter import *
    from PIL import ImageTk, Image
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
    img = ImageTk.PhotoImage(Image.open(imagePath))
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.mainloop()




# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
# apps.openImage3Canvas(imagePath,500,500) # w and h
#uses canvas and photomethod
def openImage3Canvas(imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif',width=500,height=500):
    #from tkinter import *
    ws = Tk()
    ws.title('View an Image')
    ws.geometry(f'{width}x{height}')

    canvas = Canvas(
        ws,
        width = width,
        height = height
        )
    canvas.pack()
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\png.png'
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    img = PhotoImage(file=imagePath)
    #img = ImageTk.PhotoImage(Image.open(imagePath))
    canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
        )
    ws.mainloop()



# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
# apps.openImage4Canvas(imagePath,500,500) # w and h
#uses canvas and PhotoImage - ACCEPTS MORE FILETYPES - JPG
def openImage4Canvas(imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif',width=500,height=500):
    #from tkinter import *
    from PIL import ImageTk, Image

    ws = Tk()
    ws.title('View an Image')
    ws.geometry(f'{width}x{height}')

    canvas = Canvas(
        ws,
        width = width,
        height = height
    )

    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imagePath))
    #img = PhotoImage(file=imagePath)
    canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
    )
    ws.mainloop()





# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
# apps.openGIF(imagePath)

#tkinter #shows a GIF image
def openGIF(imagePath=""):
    # has to be a GIF - to show using just tkinter
    #from tkinter import *
    root = Tk()
    canvas = Canvas(root, width = 300, height = 300)
    canvas.pack()
    #imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    img = PhotoImage(file=imagePath)
    canvas.create_image(20,20, anchor=NW, image=img)
    mainloop()





# import GuiAPPs as a
# a.photoGallery1() # photo gallery layout
#
# make images buttons or links
#
# 6 Clickable Images with Filenames # a photo gallery layout # buttons that do things
def photoGallery1():
    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('6 Clickable Images with Filenames')
    w.geometry('800x700')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=650,  # it's a square area, w-h
        width=650,
        bg="#fff"  # canvas background color
    )

    #canvas.pack()  # maybe it gets it ready for you to draw on it
    canvas.pack(side = TOP, anchor = NW, padx = 70, pady = 20)  # maybe it gets it ready for you to draw on it

    """
    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle
    """
    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    #img = ImageTk.PhotoImage(Image.open(imagePath)) #img = PhotoImage(file=imagePath)

    import listAllFILES as filelist
    folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
    filenamesThumbs = filelist.listAllThumbnails(folder_path)
    counter=0
    th=[] #thumbImagePath
    # filenamesThumbs[0]-filenamesThumbs[6]
    for thumbImagePath in filenamesThumbs:
        print(f"thumbImagePath {counter}): {thumbImagePath}")
        th.append(thumbImagePath)
        if counter==7:
            break
        counter += 1
    img1 = ImageTk.PhotoImage(Image.open(th[0]))  # img = PhotoImage(file=imagePath)
    img2 = ImageTk.PhotoImage(Image.open(th[1]))  # img = PhotoImage(file=imagePath)
    img3 = ImageTk.PhotoImage(Image.open(th[2]))  # img = PhotoImage(file=imagePath)
    img4 = ImageTk.PhotoImage(Image.open(th[3]))  # img = PhotoImage(file=imagePath)
    img5 = ImageTk.PhotoImage(Image.open(th[4]))  # img = PhotoImage(file=imagePath)
    img6 = ImageTk.PhotoImage(Image.open(th[5]))  # img = PhotoImage(file=imagePath)

    # -------------------
    showBtns = True
    showImgs = False
    #-------------------

    #row 1
    if showImgs == True:
        canvas.create_image(
            20,
            10,
            anchor=NW,
            image=img1
        )
    if showBtns==True:
        button1 = Button(w, image=img1, command=quit)#.pack() #make the image clickable
        button1.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button1.place(x=120, y=68)
    if showImgs==True:
        canvas.create_image(
            290,
            10,
            anchor=NW,
            image=img2
        )
    canvas.create_text(
        130,
        220,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_1.jpg"
    )
    if showBtns==True:
        button2 = Button(w, image=img2, command=quit)  # .pack() #make the image clickable
        button2.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button2.place(x=390, y=68)
    canvas.create_text(
        400,
        220,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_2.jpg"
    )
    # row 2
    if showImgs==True:
        canvas.create_image(
            20,
            200,
            anchor=NW,
            image=img3
        )
    if showBtns==True:
        button3 = Button(w, image=img3, command=quit)  # .pack() #make the image clickable
        button3.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button3.place(x=120, y=258)
    canvas.create_text(
        140,
        400,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_3.jpg"
    )
    if showImgs==True:
        canvas.create_image(
            290,
            200,
            anchor=NW,
            image=img4
        )
    if showBtns==True:
        button4 = Button(w, image=img4, command=quit)  # .pack() #make the image clickable
        button4.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button4.place(x=390, y=258)
    canvas.create_text(
        400,
        400,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_4.jpg"
    )
    #row 3
    if showImgs==True:
        canvas.create_image(
            20,
            380,
            anchor=NW,
            image=img5
        )
    if showBtns==True:
        button5 = Button(w, image=img5, command=quit)  # .pack() #make the image clickable
        button5.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button5.place(x=120, y=435)
    canvas.create_text(
        140,
        590,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_5.jpg"
    )
    if showImgs==True:
        canvas.create_image(
            290,
            380,
            anchor=NW,
            image=img6
        )
    if showBtns==True:
        button6 = Button(w, image=img6, command=quit)  # .pack() #make the image clickable
        button6.configure(width=240, height=150, activebackground="#33B5E5", relief=FLAT)
        button6.place(x=390, y=435)
    canvas.create_text(
        400,
        590,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_6.jpg"
    )
    #at the top
    button1 = Button(w, text="Quit", command=quit, anchor=W)
    button1.configure(width=20, activebackground="#33B5E5", relief=FLAT)
    button1.place(x=320, y=30)

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes







# import GuiAPPs as a
# a.basicCanvasDrawing3() # LEARNING - tkinter canvas - drawing
#
# 6 images with Filenames # a photo gallery layout # buttons that do things
def basicCanvasDrawing3():
    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('6 images with Filenames')
    w.geometry('600x600')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=550,  # it's a square area, w-h
        width=550,
        bg="#fff"  # canvas background color
    )

    #canvas.pack()  # maybe it gets it ready for you to draw on it
    canvas.pack(side = TOP, anchor = NW, padx = 20, pady = 20)  # maybe it gets it ready for you to draw on it

    """
    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle
    """
    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    img = ImageTk.PhotoImage(Image.open(imagePath)) #img = PhotoImage(file=imagePath)

    #row 1

    canvas.create_image(
        20,
        10,
        anchor=NW,
        image=img
    )
    canvas.create_text(
        130,
        160,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_1.jpg"
    )
    canvas.create_image(
        290,
        10,
        anchor=NW,
        image=img
    )
    canvas.create_text(
        400,
        160,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_2.jpg"
    )
    # row 2
    canvas.create_image(
        20,
        200,
        anchor=NW,
        image=img
    )
    canvas.create_text(
        140,
        350,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_3.jpg"
    )
    canvas.create_image(
        290,
        200,
        anchor=NW,
        image=img
    )
    canvas.create_text(
        400,
        350,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_4.jpg"
    )
    #row 3
    canvas.create_image(
        20,
        380,
        anchor=NW,
        image=img
    )
    canvas.create_text(
        140,
        530,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_4.jpg"
    )
    canvas.create_image(
        290,
        380,
        anchor=NW,
        image=img
    )

    canvas.create_text(
        400,
        530,
        fill="darkblue",
        font="Times 10 italic bold",
        text="image_name_that_is_long_4.jpg"
    )
    button1 = Button(w, text="Quit", command=quit, anchor=W)
    button1.configure(width=20, activebackground="#33B5E5", relief=FLAT)
    button1.place(x=220, y=30)

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes






# import GuiAPPs as apps
# apps.basicCanvasDrawing2() # LEARNING - tkinter canvas - drawing

def basicCanvasDrawing2():
    from PIL import ImageTk, Image
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('Add 2 images in')
    w.geometry('400x300')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=200,  # it's a square area, w-h
        width=200,
        bg="#fff"  # canvas background color
    )

    canvas.pack()  # maybe it gets it ready for you to draw on it

    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle

    imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\grass.gif'
    img = ImageTk.PhotoImage(Image.open(imagePath)) #img = PhotoImage(file=imagePath)
    canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
    )
    canvas.create_image(
        100,
        100,
        anchor=NW,
        image=img
    )


    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes


#--------------------------------



#--------------------------------

# import GuiAPPs as apps
# apps.basicCanvasDrawing1() # LEARNING - tkinter canvas - drawing

def basicCanvasDrawing1():
    # from tkinter import *
    w = Tk()  # the window - attributes
    w.title('Draw a Square in Python')
    w.geometry('400x300')  # window width and height
    w.config(bg='#345')  # window background color

    # THE CANVAS (ws) - is tied in below with the passed 'ws' var:
    canvas = Canvas(  # this is what you can draw on - a canvas square
        w,
        height=200,  # it's a square area, w-h
        width=200,
        bg="#fff"  # canvas background color
    )

    canvas.pack()  # maybe it gets it ready for you to draw on it

    canvas.create_rectangle(  # you can draw a box - onto the canvas
        30, 30, 180, 120,  # xy, xy - of the 200px-w-h canvas - where do we draw a box?
        outline="#fb0",  # outline color - 1px
        fill="#345")  # the fill color - inside the box
    # orange = #fb0 #inside the rectangle

    # you add everything onto the canvas, and then you call the mainloop()
    # which starts it
    w.mainloop()  # the ws from the beginning - the window sizes

#--------------------------------



# I tested it with opening an image in paint, and choosing a large brush size
# if it changes, like using live matplotlib, you can load the new image and see it change

# import GuiAPPs as apps
# imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'
# apps.refreshLoadImageEveryHalfSec(imagePath)

# refreshes the image in tkinter - every .5 seconds
def refreshLoadImageEveryHalfSec(imagePath):
    from PIL import Image, ImageTk
    import tkinter as tk

    # ------------------------------------------------------------------------------
    # Code to simulate background process periodically updating the image file.
    # Note:
    #   It's important that this code *not* interact directly with tkinter
    #   stuff in the main process since it doesn't support multi-threading.
    import itertools
    import os
    import shutil
    import threading
    import time

    def update_image_file(dst):
        """ Overwrite (or create) destination file by copying successive image
            files to the destination path. Runs indefinitely.
        """
        TEST_IMAGES = 'test_image1.png', 'test_image2.png', 'test_image3.png'

        for src in itertools.cycle(TEST_IMAGES):
            shutil.copy(src, dst)
            time.sleep(.5)  # pause between updates

    # ------------------------------------------------------------------------------

    def refresh_image(canvas, img, imagePath, image_id):
        try:
            pil_img = Image.open(imagePath).resize((400, 400), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(pil_img)
            canvas.itemconfigure(image_id, image=img)
        except IOError:  # missing or corrupt image file
            img = None
        # repeat every half sec
        canvas.after(500, refresh_image, canvas, img, imagePath, image_id)

    root = tk.Tk()
    # imagePath = 'C:\\Users\\myvor\\Desktop\\Backgrounds\\will-turner-GTPT_fNFQiE-unsplash.jpg'

    # ------------------------------------------------------------------------------
    # More code to simulate background process periodically updating the image file.
    th = threading.Thread(target=update_image_file, args=(imagePath,))
    th.daemon = True  # terminates whenever main thread does
    th.start()
    while not os.path.exists(imagePath):  # let it run until image file exists
        time.sleep(.1)
    # ------------------------------------------------------------------------------

    canvas = tk.Canvas(root, height=400, width=400)
    img = None  # initially only need a canvas image place-holder
    image_id = canvas.create_image(200, 200, image=img)
    canvas.pack()

    refresh_image(canvas, img, imagePath, image_id)
    root.mainloop()


#---------------------------


# import GuiAPPs as apps
# apps.fileListWithOpen2()

def fileListWithOpen2(folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront", width=50, height=20):
    # from tkinter import *
    import tkinter.messagebox as box

    window = Tk()
    window.title('<title>')

    frame = Frame(window)
    import listAllFILES as filelist
    #folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
    picsNames = filelist.listFilenameOnly(folder_path)

    listbox = Listbox(frame)
    for name in picsNames:
        listbox.insert('end', name)
    """listbox.insert(1, '<filename>')
    listbox.insert(2, '<filename>')
    listbox.insert(3, '<filename>')
    """
    listbox.config(width=width, height=height)


    def dialog():
        box.showinfo('Selection', 'Your Choice: ' + \
                     listbox.get(listbox.curselection()))

    btn = Button(frame, text='View Info', command=dialog)

    btn.pack(side=RIGHT, padx=5)
    listbox.pack(side=LEFT)
    frame.pack(padx=30, pady=30)

    window.mainloop()





# import GuiAPPs as apps
# apps.fileListWithOpen1()

def fileListWithOpen1(width=50, height=20):
    # from tkinter import *
    import tkinter.messagebox as box

    window = Tk()
    window.title('<title>')

    frame = Frame(window)
    listbox = Listbox(frame)
    listbox.insert(1, '<filename>')
    listbox.insert(2, '<filename>')
    listbox.insert(3, '<filename>')

    listbox.config(width=width, height=height)


    def dialog():
        box.showinfo('Selection', 'Your Choice: ' + \
                     listbox.get(listbox.curselection()))

    btn = Button(frame, text='View Info', command=dialog)

    btn.pack(side=RIGHT, padx=5)
    listbox.pack(side=LEFT)
    frame.pack(padx=30, pady=30)

    window.mainloop()


#--------------------------



# NEEDS the ICO and the TEXT FILE - to work - without errors
# it has a start page, and 2 other pages - with buttons
# it plots the graph, but it is not live

# import GuiAPPs as apps
# apps.threeButtons3Pages1Graph()
def threeButtons3Pages1Graph():
    # The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    # License: http://creativecommons.org/licenses/by-sa/3.0/

    import matplotlib # UPDATE: pip install --update matplotlib
    matplotlib.use("TkAgg")
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    import matplotlib.animation as animation
    from matplotlib import style

    import tkinter as tk
    from tkinter import ttk


    LARGE_FONT= ("Verdana", 12)
    style.use("ggplot")

    f = Figure(figsize=(5 ,5), dpi=100)
    a = f.add_subplot(111)


    def animate(i):
        pullData = open("other-5gb/plot-sample-points.txt", "r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))

        a.clear()
        a.plot(xList, yList)




    class SeaofBTCapp(tk.Tk):

        def __init__(self, *args, **kwargs):

            tk.Tk.__init__(self, *args, **kwargs)

            tk.Tk.iconbitmap(self, default="other-5gb/files/icon.ico")
            tk.Tk.wm_title(self, "Sea of BTC client")


            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand = True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (StartPage, PageOne, PageTwo, PageThree):

                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()


    class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self ,parent)
            label = tk.Label(self, text="Start Page", font=LARGE_FONT)
            label.pack(pady=10 ,padx=10)

            button = ttk.Button(self, text="Visit Page 1",
                                command=lambda: controller.show_frame(PageOne))
            button.pack()

            button2 = ttk.Button(self, text="Visit Page 2",
                                 command=lambda: controller.show_frame(PageTwo))
            button2.pack()

            button3 = ttk.Button(self, text="Graph Page",
                                 command=lambda: controller.show_frame(PageThree))
            button3.pack()


    class PageOne(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
            label.pack(pady=10 ,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            button2 = ttk.Button(self, text="Page Two",
                                 command=lambda: controller.show_frame(PageTwo))
            button2.pack()


    class PageTwo(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
            label.pack(pady=10 ,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            button2 = ttk.Button(self, text="Page One",
                                 command=lambda: controller.show_frame(PageOne))
            button2.pack()


    class PageThree(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
            label.pack(pady=10 ,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()





            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw() #canvas.show()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    app = SeaofBTCapp()
    ani = animation.FuncAnimation(f, animate, interval=1000)
    app.mainloop()



#--------------------------------------



# import GuiAPPs as apps
# apps.fileListGui()
def fileListGui():
    import PySimpleGUI as sg

    # set the theme for the screen/window
    sg.theme('SandyBeach')
    # define layout
    layout = [[sg.Text('File Browser', size=(20, 1), font='Lucida', justification='left')],
              [sg.Text('List of Files:', size=(30, 1), font='Lucida', justification='left')],
              [sg.Listbox(values=['File1.jpg', 'File2.jpg', 'File3.jpg', 'File4.jpg', 'File5.jpg', 'File6.jpg', 'File7.jpg', 'File8.jpg', 'File9.jpg', 'File10.jpg', 'File11.jpg', 'File12.jpg', 'File13.jpg', 'File14.jpg', 'File15.jpg'],
                           select_mode='extended', key='fac', size=(30, 12))],
              [sg.Button('SAVE', font=('Times New Roman', 12)), sg.Button('CANCEL', font=('Times New Roman', 12))]]
    # Define Window
    win = sg.Window('Browse Files', layout)
    # Read  values entered by user
    e, v = win.read()
    # close first window
    win.close()
    # access the selected value in the list box and add them to a string
    strx = ""
    for val in v['fac']: # you can select more than one
        strx = strx + " " + val + ","

    # display string in a popup
    #sg.popup()
    sg.popup('Thank you', ' You picked the file: ' + strx[1:len(strx) - 1])





#--------------------------
#
# import GuiAPPs as apps
# apps.note("Hello World")

def note(title="Hello World", message=""):
    notificationMESSAGE(title=title, message=message)

#--------------------------


"""
import GuiAPPs as guiApps
title="-- Quick Reminder --"
message=" *** This is what you wanted to be reminded of *** "
guiApps.notificationMESSAGE(title=title, message=message)
"""

# import GuiAPPs as guiApps
# title="Notification Title"
# message="This is the notification message"
# guiApps.notificationMESSAGE(title=title, message=message)

#appears near the clock - on the task bar
def notificationMESSAGE(title="Hello World", message=""):
    import PySimpleGUI as sg
    import SOUND as sound
    sound.beep()
    #title = 'Notification Title'
    #message = 'This is the notification message'
    if message=="":
        message = title
    sg.SystemTray.notify(title, message)


# import GuiAPPs as apps
# apps.onBrowseItHasIconsForFilesFolders()

# there is folder and file ICONS
def onBrowseItHasIconsForFilesFolders():
    from pathlib import Path
    import PySimpleGUI as sg

    def popup_paths(path=Path.home(), width=60):

        def short(file, width):
            return file[:width // 2 - 3] + '...' + file[-width // 2:] if len(file) > width else file

        def create_win(path):
            files = sorted(sorted(Path(path).iterdir()), key=lambda x: Path(x).is_file())
            treedata = sg.TreeData()
            for i, file in enumerate(files):
                f = str(file)
                treedata.insert("", i, short(f, width - 8), [f], icon=folder_icon if Path(f).is_dir() else file_icon)
            layout = [
                [sg.Tree(data=treedata, headings=['Notes', ], pad=(0, 0),
                         show_expanded=True, col0_width=width, auto_size_columns=False,
                         visible_column_map=[False, ], select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                         num_rows=15, row_height=16, font=('Courier New', 10), key="TREE")],
                [sg.Button('OK'), sg.Button('Cancel'), sg.Button('UP')],
            ]
            window = sg.Window("Select files or directories", layout, modal=True, finalize=True)
            tree = window['TREE']
            tree.Widget.configure(show='tree')  # Hide Tree Header
            tree.bind("<Double-1>", "_DOUBLE_CLICK")
            while True:
                event, values = window.read()
                if event == 'TREE_DOUBLE_CLICK':
                    if values['TREE'] != []:
                        value = values['TREE'][0]
                        path = treedata.tree_dict[value].values[0]
                        if Path(path).is_dir():
                            result = path
                            break
                    continue
                elif event in (sg.WINDOW_CLOSED, 'Cancel'):
                    result = []
                elif event == 'OK':
                    result = [treedata.tree_dict[i].values[0] for i in values['TREE']]
                elif event == 'UP':
                    result = str(Path(path).parent)
                break
            window.close()
            return result

        while True:
            result = create_win(path)
            if isinstance(result, str):
                path = result
            else:
                break
        return result

    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    sg.theme('DarkBlue3')
    sg.set_options(font=("Courier New", 12))

    layout = [[sg.Button("Browse")]]

    window = sg.Window('title', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Browse':
            files = popup_paths(path='C:/', width=80)
            print(files)

    window.close()





def changeBGs_cool_only():
    # Change the background automatically
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool"  # folder_path="z-IMAGES_1/0.cool"
    array = lfs.listAllImages(folder_path)
    length = array[0]
    pics = array[1]

    # keep it in the same folder of images - so it feels consistent
    import BackgroundCHOOSE as bgcrand
    bgcrand.BackgroundChooseRANDOM(array)


def changeBGs():
    # Change the background automatically
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool"  # folder_path="z-IMAGES_1/0.cool/premium_wallpapers_rock_stacks"
    array = lfs.listAllImages(folder_path)

    # keep it in the same folder of images - so it feels consistent
    import BackgroundCHOOSE as b
    b.BackgroundChooseRANDOM(array)


def changeBGs_mountain():
    # Change the background automatically
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool/beautiful wallpapers mountains snow landscape"  # folder_path="z-IMAGES_1/0.cool"
    array = lfs.listAllImages(folder_path)

    # keep it in the same folder of images - so it feels consistent
    import BackgroundCHOOSE as bgcrand
    bgcrand.BackgroundChooseRANDOM(array)


def changeBGs_sunset():
    # Change the background automatically
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool/beautiful wallpapers mountains sunset"  # folder_path="z-IMAGES_1/0.cool"
    array = lfs.listAllImages(folder_path)

    # keep it in the same folder of images - so it feels consistent
    import BackgroundCHOOSE as bgcrand
    bgcrand.BackgroundChooseRANDOM(array)



# v1
# import GuiAPPs as guiApps
# guiApps.guiAppShow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def guiBGchangeShow():
    import PySimpleGUI as sg

    """
        Demo - A simple minimal window with a material design feel

        Contains base64 images for:
        * The PSG Yellow Graphic
        * The 2 toggle buttons
        * The large spinning animation

        Copyright 2021 PySimpleGUI
    """

    def main():
        sg.theme('light grey')
        BLUE_BUTTON_COLOR = '#FFFFFF on #2196f2'
        GREEN_BUTTON_COLOR = '#FFFFFF on #00c851'
        LIGHT_GRAY_BUTTON_COLOR = f'#212021 on #e0e0e0'
        DARK_GRAY_BUTTON_COLOR = '#e0e0e0 on #212021'

        layout = [[sg.Col([[sg.T('Welcome to my: '),sg.T('Background Change App')],
                           [sg.T()],
                           #[sg.T('Your license status: '), sg.T('Activated Version', k='-LIC STATUS-')],
                           [sg.B('Rock Stack', size=(14, 2), button_color=BLUE_BUTTON_COLOR),
                            sg.B('Cool Image', size=(14, 2), button_color=GREEN_BUTTON_COLOR),
                            sg.B('Exit', size=(14, 2), button_color=LIGHT_GRAY_BUTTON_COLOR)],
                           [sg.T()],

                           [sg.Image(data=PSG_GRAPHIC)],
                           [sg.B(image_data=T_OFF, k='-TOGGLE1-', metadata=False,
                                 button_color=sg.theme_background_color()),
                            sg.B(image_data=T_ON, k='-TOGGLE2-', button_color=sg.theme_background_color(),
                                 metadata=True)],
                           [sg.T()],
                           [sg.B('Mountain Snow', size=(10, 2), button_color=LIGHT_GRAY_BUTTON_COLOR),
                            sg.B('Sunset', size=(10, 2), button_color=DARK_GRAY_BUTTON_COLOR)],

                           [sg.T()],
                           [sg.Image(data=BLANK, k='-GIF-', metadata=0)],
                           [sg.T('The end of "my App"')]], element_justification='c', k='-TOP COL-')]]

        window = sg.Window('Changing the Background Image - Window Title', layout)
        show_animation = False

        while True:  # Event Loop
            event, values = window.read(timeout=100)
            if event == sg.WIN_CLOSED or event == 'Exit':
                print("Exit button clicked")
                break
            if event.startswith('-TOGGLE'):
                state = window[event].metadata = not window[event].metadata
                window[event].update(image_data=T_ON if state else T_OFF)
                print("Toggle")
                changeBGs()
            elif event == 'Mountain Snow':
                print("Mountain Snow - button clicked")
                changeBGs() # changeBGs_mountain()
            elif event == 'Sunset':
                print("Sunset - button clicked")
                changeBGs() # changeBGs_sunset()

            elif event == 'Rock Stack':
                print("Change Bkng - button clicked")
                changeBGs()
                #show_animation = True # LOADS an image at the bottom
                #window['-GIF-'].metadata = 0
            elif event == 'Cool Image':
                print("Cool Image - button clicked")
                changeBGs() # changeBGs_cool_only()
                #sg.popup_no_titlebar('This is where you would do', 'the upgrade window code',
                                     #background_color='black',
                                     #text_color='white')
            # Do the animation stuff
            if show_animation:
                window['-GIF-'].update_animation(LOADING_GIF, time_between_frames=100)
                window['-GIF-'].metadata += 1
                if window['-GIF-'].metadata > 50:
                    show_animation = False
                    window['-GIF-'].update(data=BLANK)

        window.close()

    #if __name__ == '__main__':
    BLANK = b'iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAB7SURBVHhe7cExAQAAAMKg9U9tDQ8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADtQAkK8AAT0JXwIAAAAASUVORK5CYII='
    T_OFF = b'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'
    T_ON = b'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'
    PSG_GRAPHIC = b'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'
    LOADING_GIF = b'R0lGODlhoACgAPcAAAD/AGZ5j2d6j2d6kGh7kGh7kWl8kWp8kmp9kmt9k2t+k2x+k21/lG6AlW+BlnCBlnCClnGCl3GDl3KEmHOEmHOFmXSFmXSGmnWGmnaHmnaHm3eIm3eInHiJnHmJnXmKnXqKnXqLnnuLnnyMn32NoH6OoX+PoYCQooGRo4KRo4KSpIOSpIOTpYSTpYWUpYWUpoaVpoaVp4eWp4iWqIiXqImXqImYqYqZqYuZqouaqoyaq4ybq42brI6crI+drZCerpGerpGfr5Kfr5KgsJOgsJShsJShsZWisZWjspajspeks5ils5iltJmmtJqmtZqntZuntpuotpyot52pt56quJ+ruaCruaCsuqGtuqKuu6Ouu6OvvKSvvKSwvaWwvaaxvqeyvqeyv6izv6mzwKm0wKq0waq1wau1wqy2wq23w624w664xK+5xK+5xbC6xbG7xrK7xrK8x7O8x7O9yLS9yLW+yba/yba/yrfAyrjAy7jBy7nCzLrDzLvDzbvEzbzEzrzFzr3Fz77Gz77G0L/H0MDI0cHI0cHJ0sLJ0sTL1MTM1MXM1MXN1cbN1cfO1sjP18nQ18rQ2MrR2MvR2cvS2czS2s3T2s3T287U28/V3NDV3NDW3dHX3dHX3tLY3tPY39PZ39TZ39Ta4NXa4Nbb4dfc4tjd4tnd49ne49re5Nrf5Nvf5dzg5dzh5t3h5t3i5t7i59/j59/j6ODk6ODk6eHl6eLl6eLm6uPm6uPn6+Tn6+Xo7Obp7efq7ejr7uns7+rt8Ovt8Ovu8ezu8ezv8e3v8u7w8u7w8+/x8+/x9PDy9PHy9PHz9fLz9fL09vP09vT19/T29/X2+PX3+Pb3+Pf4+fj5+vn6+/r6+/r7+/v7/Pv8/Pz8/f39/f39/v7+/v7+/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH/C05FVFNDQVBFMi4wAwEAAAAh+QQFBAAAACwAAAAAoACgAIcA/wBmeY9neo9nepBoe5Boe5FpfJFqfJJqfZJrfZNrfpNsfpNtf5RugJVvgZZwgZZwgpZxgpdxg5dyhJhzhJhzhZl0hZl0hpp1hpp2h5p2h5t3iJt3iJx4iZx5iZ15ip16ip16i557i558jJ99jaB+jqF/j6GAkKKBkaOCkaOCkqSDkqSDk6WEk6WFlKWFlKaGlaaGlaeHlqeIlqiIl6iJl6iJmKmKmamLmaqLmqqMmquMm6uNm6yOnKyPna2Qnq6Rnq6Rn6+Sn6+SoLCToLCUobCUobGVorGVo7KWo7KXpLOYpbOYpbSZprSaprWap7Wbp7abqLacqLedqbeeqrifq7mgq7mgrLqhrbqirrujrrujr7ykr7yksL2lsL2msb6nsr6nsr+os7+ps8CptMCqtMGqtcGrtcKstsKtt8OtuMOuuMSvucSvucWwusWxu8ayu8ayvMezvMezvci0vci1vsm2v8m2v8q3wMq4wMu4wcu5wsy6w8y7w827xM28xM68xc69xc++xs++xtC/x9DAyNHByNHBydLCydLEy9TEzNTFzNTFzdXGzdXHztbIz9fJ0NfK0NjK0djL0dnL0tnM0trN09rN09vO1NvP1dzQ1dzQ1t3R193R197S2N7T2N/T2d/U2d/U2uDV2uDW2+HX3OLY3eLZ3ePZ3uPa3uTa3+Tb3+Xc4OXc4ebd4ebd4ube4uff4+ff4+jg5Ojg5Onh5eni5eni5urj5urj5+vk5+vl6Ozm6e3n6u3o6+7p7O/q7fDr7fDr7vHs7vHs7/Ht7/Lu8PLu8PPv8fPv8fTw8vTx8vTx8/Xy8/Xy9Pbz9Pb09ff09vf19vj19/j29/j3+Pn4+fr5+vv6+vv6+/v7+/z7/Pz8/P39/f39/f7+/v7+/v////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8I/wCzheMWTiBBgwUHJjyoEKHDhhAZSlxI8eFEixUjZryoEaPHjiA5TgzXLdw3kiZRniy5MiVLlTBfynRJs6XNmDVx3py5MydPnUB/CvVZU+TGox+NJkUakqnSpkujQp1KtKfVoFWxXh26NStXrWC/ipX6tKzTs2SvBSiwYIKFFjuugBGk6Zi1qWbJom0a1qvfroD7RgsQYADhwocNHyhBRZAsbH/7BhZbdG9evJYzZ7MW4MDazp89FwA9ugEMPK40Y9b7MTLlya5jn3xmmHBtxLYTJ4Yw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'
    main()


# v1
# import GuiAPPs as apps
# apps.guiBallMovePlay()

def guiBallMovePlay():
    # Importing arcade module
    import arcade

    # Creating MainGame class
    class MainGame(arcade.Window):
        def __init__(self):
            super().__init__(600, 600, title="Player Movement")

            # Initializing the initial x and y coordinated
            self.x = 250
            self.y = 250

            # Initializing a variable to store
            # the velocity of the player
            self.vel_x = 0
            self.vel_y = 0

        # Creating on_draw() function to draw on the screen
        def on_draw(self):
            arcade.start_render()

            # Drawing the rectangle using
            # draw_rectangle_filled function
            arcade.draw_circle_filled(self.x, self.y, 25,
                                      arcade.color.GREEN)

        # Creating on_update function to
        # update the x coordinate
        def on_update(self, delta_time):
            self.x += self.vel_x * delta_time
            self.y += self.vel_y * delta_time

        # Creating function to change the velocity
        # when button is pressed
        def on_key_press(self, symbol, modifier):

            # Checking the button pressed
            # and changing the value of velocity
            if symbol == arcade.key.UP:
                self.vel_y = 300
                print("Up arrow key is pressed")
            elif symbol == arcade.key.DOWN:
                self.vel_y = -300
                print("Down arrow key is pressed")
            elif symbol == arcade.key.LEFT:
                self.vel_x = -300
                print("Left arrow key is pressed")
            elif symbol == arcade.key.RIGHT:
                self.vel_x = 300
                print("Right arrow key is pressed")

        # Creating function to change the velocity
        # when button is released
        def on_key_release(self, symbol, modifier):

            # Checking the button released
            # and changing the value of velocity
            if symbol == arcade.key.UP:
                self.vel_y = 0
            elif symbol == arcade.key.DOWN:
                self.vel_y = 0
            elif symbol == arcade.key.LEFT:
                self.vel_x = 0
            elif symbol == arcade.key.RIGHT:
                self.vel_x = 0

    # Calling MainGame class
    MainGame()
    arcade.run()


# v1
# import GuiAPPs as guiApps
# guiApps.guiAppShow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def guiAppShow():
    import PySimpleGUI as sg

    """
        Demo - A simple minimal window with a material design feel

        Contains base64 images for:
        * The PSG Yellow Graphic
        * The 2 toggle buttons
        * The large spinning animation

        Copyright 2021 PySimpleGUI
    """

    def main():
        sg.theme('light grey')
        BLUE_BUTTON_COLOR = '#FFFFFF on #2196f2'
        GREEN_BUTTON_COLOR = '#FFFFFF on #00c851'
        LIGHT_GRAY_BUTTON_COLOR = f'#212021 on #e0e0e0'
        DARK_GRAY_BUTTON_COLOR = '#e0e0e0 on #212021'

        layout = [[sg.Col([[sg.T('Welcome to my App')],
                           [sg.T('Your license status: '), sg.T('Trial', k='-LIC STATUS-')],
                           [sg.B('Light', size=(10, 2), button_color=LIGHT_GRAY_BUTTON_COLOR),
                            sg.B('Dark', size=(10, 2), button_color=DARK_GRAY_BUTTON_COLOR)],
                           [sg.T()],
                           [sg.Image(data=PSG_GRAPHIC)],
                           [sg.B(image_data=T_OFF, k='-TOGGLE1-', metadata=False,
                                 button_color=sg.theme_background_color()),
                            sg.B(image_data=T_ON, k='-TOGGLE2-', button_color=sg.theme_background_color(),
                                 metadata=True)],
                           [sg.T()],
                           [sg.B('Do Something', size=(14, 2), button_color=BLUE_BUTTON_COLOR),
                            sg.B('Upgrade', size=(14, 2), button_color=GREEN_BUTTON_COLOR),
                            sg.B('Exit', size=(14, 2), button_color=LIGHT_GRAY_BUTTON_COLOR)],
                           [sg.Image(data=BLANK, k='-GIF-', metadata=0)],
                           [sg.T('The end of "my App"')]], element_justification='c', k='-TOP COL-')]]

        window = sg.Window('Window Title', layout)
        show_animation = False

        while True:  # Event Loop
            event, values = window.read(timeout=100)
            if event == sg.WIN_CLOSED or event == 'Exit':
                print("Exit button clicked")
                break
            if event.startswith('-TOGGLE'):
                state = window[event].metadata = not window[event].metadata
                window[event].update(image_data=T_ON if state else T_OFF)
                print("Toggle")
            elif event == 'Light':
                print("Light - button clicked")
            elif event == 'Dark':
                print("Dark - button clicked")

            elif event == 'Do Something':
                print("Do Something - button clicked")
                changeBGs()

                show_animation = True
                window['-GIF-'].metadata = 0
            elif event == 'Switch Images':
                print("Switch Images button clicked")
                #sg.popup_no_titlebar('This is where you would do', 'the upgrade window code',
                                     #background_color='black',
                                     #text_color='white')
            # Do the animation stuff
            if show_animation:
                window['-GIF-'].update_animation(LOADING_GIF, time_between_frames=100)
                window['-GIF-'].metadata += 1
                if window['-GIF-'].metadata > 50:
                    show_animation = False
                    window['-GIF-'].update(data=BLANK)

        window.close()

    # if __name__ == '__main__':
    BLANK = b'iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAB7SURBVHhe7cExAQAAAMKg9U9tDQ8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADtQAkK8AAT0JXwIAAAAASUVORK5CYII='
    T_OFF = b'iVBORw0KGgoAAAANSUhEUgAAAFAAAAA8CAYAAADxJz2MAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAgmSURBVHhe7ZpdbFTHFcfPzBrb613bGLt4/VEC2AVaQ0RIkNIWJN7iB6TyUiXqawrJY0yEhJEiWYpa06oFqr600Ic8VGqlpGqkShWWeCCqpSIRJwURCGVDDP5a24vX66/1x+6dnv/cucv1F14M9l7T+5NW996ZK8v73zNzzpxzyMfHx8fHx8fH5/8SYa6r5u3T5xqlEMf402BlMhEpAhFLWBFBYrt5xRMoUt2KRDxAKpYRIiaV+kYJcfnSL1v+Y15ZFasS8N0zv9urlHpTWdZRkmK/Gd6oRFmETzMZ629/+vX718xYzjyVgLC2gJAf8u/5lhmigoIAbauNUOWWMgqVFFMoGORrkMKhoHnDG0xMpmgqNU2T/JmamqZ4Ikl9A0M0PTNr3iCySFwWQrU+jVXmJOCJ939TJYoKPrQs9XMhqCAgA7S7cRsLV0011ZUkeHAjwquIhuIJetg3SHe/eUizc3P2hFB/lpb44A9nW7rtgeVZ8ZsfP3N+v1DqH/xqPYRq3FFHr+3bQ8FgsXnjxWCGxbv5VZRu/7ebMlaGzVGN8h7500tnW66YV5bkiQIeP3PuLbbrSyxceGtVBf344MtUUV5qZl9MsNSvdd2ih/2DbKGUZps5dbG95YKZXsSyAp5oPf8eX87jvmF7PR06uI8CgQAeF1ESLKIt5SEqKS6iTbwn4gPSGYvm5tKUmpmjxNgEjU9O63Gvg6XddfMu3bwTNSN0gUVsMffzWFJAWJ5Q4i9seeqVvbvE/qbvmZnHcNhCtVsr6DvsPAo3FZjRJ5NOZ2g4MU59QyPEXs+Mepd793up8/oNLSjL2nqx/eRZe+Yxi0wKex4v27+zeIUH9u1eUrytLNquHbW0uSzEVinN6MpIKak0VEzVleWIy9gjzpgZb1JZUUZl4RJ60BtjEcWRg4feuN7V2ZE1SzBPQO1tA+IzFq8Ky/b1A01mxibAAjRuq9aWh/vVIqWg8tISFjNIyfEpYu9uZrzHls1l2gIHh0ck/5fHXjn0xsdfdnaMmGmapwJCFXhbOAzseW6wr/2goY73urAZeXbKwkFqaqynYFGhGfEmvBLppfoIwrVwgbD9gkNWQATJdpwntLd1OwxY2x5esnAWz5uiwk20Z2dt1vF4lR+9uhd7PduiOPru6fNHzPBjAXHCYO0KEOctDFV2fnfrmojnACe0a3uNpwNyxL1Nu3fqfzAjiVeqjRYQZ1scz3DCQJDsBg7jeS7b5QjzMbCO91Yv8/L3G7SQQtGh462/PYoxLSASA7jieOY+YSBUqY9Umqe1p4YF9PJSxrbWtMtOMvFq0ZrZAiKrwuBs6wbedj2/0Hr/YKthe32NvvJe2NzW1lYg4TyQkkJWBYkBNwiS15uqitJnCpHWmrLSkP7wMq7qmy4/wiGZOIYJpKTcmzicRq4njOcJrBDhjZd5qS6ir3xQ+wkEbMAD8nlucLbNF+vhtJ6FqsrN+mqRbJRIw+MByVA3SAzki5JibwfWIeNopWVF2AIDtoDB+csmn95wUx62jqcBGXdgSRmRKAC5Bx3yKqCHQxngrFZJKsLHetI/98JTgJdPBV5CWiRiuJmcSukBh7l0xtytP8gbeplUyk4MK0FxPrwpW0Az6IBMcr7I54+XC45WwrJiEkVmPKDU5wZp+HyRcpUavciko5WQMYkKPe5Hkkk95oAaRr5IjE2aO2/yKGFrxX4iKtHegIeeviE96IACUD72ImR/vS5gT9+gvvL/2iFNFT6KCv3gcDZTrYmPjpu79QPiebnghOX7aHQM4k3MFiUv61M7Byyf4trTP98KewfXt3oG6+sZeGSevMmD3gH7RonLH7W1TWsB0ViD69fRB7pC7wDx+ocT5mntGRoZo+nZ/DmvlcAPfPue6fYIKK2ZFtB0JV1BbwjaG9wMDI/S2MT8GHEtgOf1uvXdYfHGxnl/VtatusKxTzCWTbxxUHgKV/SGoL3BAapHH8ZoZg0tA5Z+rztGGcu7ex9W5o3bxriE/KCtrU0HylkBbWci/orGGvSGQDgHBLZ3vx2g2TUIriHe3e5+z8d+X9z4mlLTMzC0zovtLdpngKyAgGPCVnQlobEGvSFu8AVv3euhiQUB97OAv/lVtNfzPTN32DfgwzaVlkLN65GZl/b4vLNj9MDh5i6+/dlQfESGS0p0e4MDOgjiCQ5t2G2jirbahAOsGw4j+mCQZtP5OzLmQn8sTp/9+0vzRG9fbD/5T3OvWZQ3+qKz4/5rh5sRADb3DQyp0lBQoL3BDZzKMAuAOkqwuDBnISEc4jzsd4gx3duEF4F4V/51XVmWhS944dLZll/ZM49ZMvHW1dlx7dXDzZv5C/7QbqxRVFNdZWZtYI0QYzCe1Ms6qwWL6RSFcJKZmU3zEk3pcOh+75C2YLS9eR0sWVgexFMWfVJXnHzn6tWri/7xJ5rOidZzp5USumMBvSFob3jROlMXAm8LhwEBDRdqi5KnHK+7kBXX3junzzWz7B/zMg2jNwTtDajQL9dsuVHBKkOch1BFe1t2GDx8nJftR/YbS5PT5oXasRDy95JUM55hhXt379DlPdRINzI42+J4hhOGDpIZhCrwtn/8xcnP9cATyG33N6ArSZFoV0K9boaovCyshazcUq6rVaitLKzweQVkkpEM1QmBRFJnVZAYyMInDATJ7jhvJZ5KQAc01vCSfhPtDajQm+ENCS/dCSQGcLbF8Wy5vW45ViWgA3pD0N6ACr1dZLYiutRHyi7dewzUMJCGRyYZyVAWrwMpKWRVzCs+Pj4+Pj4+Pj4+OUD0P0U7YihhTsPyAAAAAElFTkSuQmCC'
    T_ON = b'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'
    PSG_GRAPHIC = b'iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAYAAAA5ZDbSAAAACXBIWXMAAAsSAAALEgHS3X78AAAOAElEQVR42u2de3RU9bXHP2cm74TwDAkGkEegECCAgCKPSgUEBSt6ReBWFB9YFCu6qKvoLVqrtbVoKyrVXm8rilpv0eICfLRYDT4Kt/Iw8n5HwAQIEJJMwiNk5v7xnWEykwkBhJCE/VnrrCQzZ86c/L7n9/vt3z577+MQSiowFBji39oB0Rh1mXIgF8j2b/8E9kbasQ+wAPAAPtvq5ebxa9gnIKpTSdzZwEAAxwG3Sz+Nuo/PBxVe/fTzKXAvsMbxD8svAWMcB1qnwsRrYNK1cHEriI6yBqzT4/Nx+CYf5i6Cee/D7r0nhH4XmOIGxgDTgJg2afD0/XDXDdCyqXqxUbdxu6BZYxjYSx1y+Voo9gDQBljvBn4C9HccmHqTxI01s6reEeWGjDZwqAQ+/wqAGOCAA2wGOkW5Yf3b2smov2zdBZk3wvEKALa4/EshHEdd3KjfXNwqxDhu56q8zjWDqv4TpmG0mVENHBPYBDZMYMMENkxgwwQ2TGDDBDaBDRPYMIENE9gwgQ0T2DCBTWDDBDZMYMMENkxgwwQ2TGDDBDaBDRPYMIENE9gwgY0zodbzCXfthV4ToLi05n07pkP3DLikC/TsrO2iFuCq4bI8fBTyCuCrTbB8DeTvh8WfQekRvR8XAwOyoG0adL4YLu0G/bpBQlzN5+T1QmEJbP9Wx964A3bugQ+XBfdpkgSXdtfxMztA947QsbX+rm0cVJ2F6Cg4uvzcf+HOPZA1/kSZgVOmUaJEuW8CXNkXYmMi77fnAMxdCAs/hVUb4Vh5zcfu9T2Y+wvI6nTy/UoPw6JPdex/LIeDRad27slJMKgnLJ5dO6LG9lftjvPSg8+UklL4+zLIzYdHJ8N/DK2az7xzD9z7FGSvBE/ZqR+7okI982TsyINHXoQly2Ff4emde7EHlq25QIboaq/yRF3pjr/B8/ZH3m9TLsx4Hlq1gCv6BF8vKIQHntFQfLb5+Et4eA78e63NwWfMyAEq3eRyQXk5/HsdrNmqxg2fr3fugbf+ERTY64PsFfDZ6qrHjY+FvpnQpys0bxycRw8Uwd6DsGrDyc9r/Xb46bOaz6ubOnp2hjap0LSR6lUdKIIiDyzLAc9hExiAtq1geP9g6aaRA2H/IXh1ETz0QkiRLwDezYZZ0yApAY4fhy++1v4hc1EM3DceJt8g4ywuVq/7fHDkqIyu3XthxQaNHuEUFMIv/htyNld9z+2CMUPgltGau5MSZLz5fDLyjpXD7n266N74AL7dd4ELHKkBU5vBtAnwzj/hy/VV57W8/dC5rXrNtl0ReleCxO2QHmZZOhAfp61FExlZ4Rwrh1cXwwdfVL24WjaDn06E6RODpQIrk5Sgn+kt4bLucO9N8OG/bB0ckZhoLTmqLFd8sO9gzUuaIs+Zfe/eg7DgE1nOlWmcBNNvhrtvjCxuJOJiYcwPTOBqiVT9xwGiooK/R1rDFpXCU3NV6q8mKzmcL76ClRHm52GXwR3XQWK8ebLOCuXH4f8iWK8uF7Tz1/WKilIvD6/QV1EBf10CY6bDnPmQmxdcH9bEZ6sjr6FvGa3SgfWFOi1whVcOhWVfV30vqxOkNPEL7Iah/aBrh8jHydkMDz4Ldz4Os16Tde6vBFct2Ssjv96/uy2Tzoijx6CoJOiG3P6t1rTz3otw0m64dTS43cHXMjvCT8bBwy9o/oxkNH38pS6Wee/BdUM01HZIDz0OyEMVyeq9rLuWQuH85UN4el7N/2NmB3jintqtKFhnBH7+LW2nYrCMGw7XXxlmjEWpDHJyIjz6R1nVRyMMsYePwqZv4LevwvwlsoQnjpLFHcBzuKrlDJDWnIiWVUEhrN50Co3t1oVsy6RqcBy4fgg8fHtweA75Z6JkrbZOVa/688KTuyx35Mkr5imDu8eGitxQqBcCx0TLI3XLaPjZrXJTVleN3u3S3aHM9vCjq+FvH8spsnOPem84njKY81fo0g5GD9YU4XJF7qmbd/qtcbcJfNo0S/a7Ep2gUI0S5GEaeimMGiTR3O5T6+mNEnULsF83uHecHA0vL5CBFS70rr3w0jtw5aWQFA+tW6ogekmYi3TDDs3N7cMcJ53awthhwb+PV2jIzs0zgU9w9UAVI3c5weG2cRI0TZZH67uQ3hJu+yEM6Am/f0NGVvj8/K8cyNun+8MAA3vCtt1Vj7Xs66oCXz1QW4CSMrj/aXhloQl8glYpEuBcPUbA5dIw/KupsGUnLF0V+n5xaajXa0BPeC2CBT9nPlyeBe0uqh8PLWkQITter4bZmpwYjgMpTaFHRs3HvDxLPT+c1Rvhly/rvrQ5OmqJY8dh9psylmryT+cVRPaMgaaEAB3StdaOjw3d58gxmP8RTHkS1m6Tt8yMrHOMz6e17R//JpHHXSWnREaboM+49DDkbIE/vatQnnAG94a0FsG/E+Lh5mv0gIvPVoeui8uOKLJjxFTFi40cIAMxKUG3LLfu0pxuAp9lSg/LMHryz6f3ueREuPlqSKx0w8JBc/YzD8Adv4Svt1T9XP5+eO9zbTZE11HiY+H2H8p1GWkJ1qcrPDtdI0J9pEEI7Pjnz+oiLatznqQ11437mXfpJn51fP8SeP0JeOzHcrLEncb3uF3QpBF0aK2lWmpzG6JP39MVAw/dpiF11UbdbCj2aC4MrHfdbjn5mySpkXt1lnOiR6eal2Yul+KaZ06GawYpuvPLdbDnIBw4JAs+4GN2HEWZNEqUsJ3awJX9ZJVflHJ+Lv5ajYsuPQLvf151SdO1vRr9u6wtvV445JHz31MmX3Pgnq7bJR91cqKWSs0bn/ljhALB7wWFUFgsyzxwITmOLPCkeHnhUpqeXo8/G1SOi651gY3aFdhykxo4JrAJbJjAhglsmMCGCWyYwIYJbAIbJrBhAhsmsGEC1xJrtsK0WQ3v/zpnN/zXbYdR9ymH1+3WfdI7r4frrqgaqViZI8dg3TaY+ptgwFzLZvCnRxSxcfevFVUx845gAvjZoKhEtTpOlR15CuALpLZ6fdA2FZ6YqnvPU56ERyarAEyALTvhd6/DQ7erKNrGXJj0KCz5gwIE6pXA+BSluGi2UlDWbVNBk5QminCo7sb+yg3KMnxnVjAuec1W3a92OXDtYB3PdR7HnrXb4K2/K2XliXv0WoVXlXjiYxVkECk70d8sIXh99bQHh9OxtbYNO2BIX3B8Ermy0BVe5f706hwa3lI5UH3UYEUpOI4axwk0kg8cly4Cr1cN7DihF0L4/nDyXCefL1j6IXDsQyXw4nzlS91QKYXV7VKAHijCo8EP0ZEa63iFhtWCQnj0JbhxmGpeOCifZ8hdMONWpYwM6i2hkyqldHq9KqnUvDE88COlfjZKUOxVbj5kZSgmesEnqm8VEw1zH1MlneJSePxlDY1LVylmK38//HZaaF5RgMJieOb1YO2tHhnw2BTV+4iOhkG9LvA5OJycLapJNWGEGjyrkwLXftBXidHZK1SDcuxwXQi/mavaVjcN10UQiUMlEmLODA2LP35SWYLPPahYqOm/V5WASdf651mPxH3550pqW7sVJj2mwLtw3v5I57V4tkaCGc+p3kfbNF0cgTgrz2F4bTF86++1t45WPNYFYUXnF8DoaTB0Cjz+PzBjkoSNcsPAXiqpcOSotjc/gPEj9LkJI+H5B1WldeaLathIc1rTZImfnKiLJj3FX7ujqd6/pEtofY+4WFUBaOIvw9A9Awb3kvETzv8uUcpqdJTOd0gf2HtA5xEdBS7/0B4brayI7/eGFeth++4LqAe3SlEPiJQ537W9yv/lbFH5hbQWodVe26ersuzY4TD+IejZSUZNZaKjVD4pMI+7nFAL3esNrXMVG60hv/K8nxCn/KLoSnNx2RHZCg/ODs126J+lWOriUtXxSIrXOfTIkEHYwl91wOXS3F4elrdU4dU5upwGOESHExutHjvvPeXkXtJVPSWctOYKQw3Uev4uHPIoOS1ggBV5ZKGPH6FlUmXR+2bCzDtDlzmBYT69parw3DIq8vckxctO2JQLl/cIvp5XoAuiNmtsnVdHx+Deaqjtu6Ffphr9lYWwdKWMrpIy5f0UllRNuj4TSg/D6+9rviwpg1+/oiD1Lu2q7nvjUCWz7cjTvl/kaG2fnAi3XavSEG9+GDzPQ8WaalwuCfifI1UnJGez3i8oVCmJq/qHZjHW2x7cKFHzW9RJliEJcTJKDhYFSwslJcDv3gju06UdvPtMcJmT2UFDvuNomE+rlArSPSO0GkDrVM3DAdJTVEB05h/gYLFSUqbepF7VrHGoZTzuKg2p9z+tv/t1g3vG6nu7ddQ5PfUq3Pzz4GeGXaZjOI6WUanN4b/mBEes6RNDc5ySEjR3R53Dmh/nPfB97M9g8vW6ss8lgWXSyAFq/IbMea/47vNpuPxkhQqeDO6N0ZCMrOJSePFtLSvmPX5y3/TZImDttmx2YQlsuUkNfIi224UNHBPYBDZMYMMENkxgwwQ2TGDDBDaBDRPYMIENE9gwgQ0T2DCBTWDDBDZMYKMuCnziGWCn+vBko+4SpmG5C8gFhbJ+k28NVN/5Jj8kUS/XBWSDovjnLor8zF2jfnC0XBpWeE+8lO0GkoERQExuvlJIMtqc23QK49yIu3CpnkTufwZjKfCCG9gHZAJdSkph+Vrt0LaVcoDcZobV+Tl3R57qmsyapyR7P+8DzwUyVfsAs4GBoOQpt6t+PF3T0Jxb4Q2Zez8BpgFrKu/XB1gAeFC2g231b/P4NTyRlRzeR1OBYcAVwBCgHRBtfaRuj9L+lVA2sBT4CDgxUP8/BK4kirTGIKUAAAAASUVORK5CYII='
    LOADING_GIF = b'R0lGODlhoACgAPcAAAD/AGZ5j2d6j2d6kGh7kGh7kWl8kWp8kmp9kmt9k2t+k2x+k21/lG6AlW+BlnCBlnCClnGCl3GDl3KEmHOEmHOFmXSFmXSGmnWGmnaHmnaHm3eIm3eInHiJnHmJnXmKnXqKnXqLnnuLnnyMn32NoH6OoX+PoYCQooGRo4KRo4KSpIOSpIOTpYSTpYWUpYWUpoaVpoaVp4eWp4iWqIiXqImXqImYqYqZqYuZqouaqoyaq4ybq42brI6crI+drZCerpGerpGfr5Kfr5KgsJOgsJShsJShsZWisZWjspajspeks5ils5iltJmmtJqmtZqntZuntpuotpyot52pt56quJ+ruaCruaCsuqGtuqKuu6Ouu6OvvKSvvKSwvaWwvaaxvqeyvqeyv6izv6mzwKm0wKq0waq1wau1wqy2wq23w624w664xK+5xK+5xbC6xbG7xrK7xrK8x7O8x7O9yLS9yLW+yba/yba/yrfAyrjAy7jBy7nCzLrDzLvDzbvEzbzEzrzFzr3Fz77Gz77G0L/H0MDI0cHI0cHJ0sLJ0sTL1MTM1MXM1MXN1cbN1cfO1sjP18nQ18rQ2MrR2MvR2cvS2czS2s3T2s3T287U28/V3NDV3NDW3dHX3dHX3tLY3tPY39PZ39TZ39Ta4NXa4Nbb4dfc4tjd4tnd49ne49re5Nrf5Nvf5dzg5dzh5t3h5t3i5t7i59/j59/j6ODk6ODk6eHl6eLl6eLm6uPm6uPn6+Tn6+Xo7Obp7efq7ejr7uns7+rt8Ovt8Ovu8ezu8ezv8e3v8u7w8u7w8+/x8+/x9PDy9PHy9PHz9fLz9fL09vP09vT19/T29/X2+PX3+Pb3+Pf4+fj5+vn6+/r6+/r7+/v7/Pv8/Pz8/f39/f39/v7+/v7+/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH/C05FVFNDQVBFMi4wAwEAAAAh+QQFBAAAACwAAAAAoACgAIcA/wBmeY9neo9nepBoe5Boe5FpfJFqfJJqfZJrfZNrfpNsfpNtf5RugJVvgZZwgZZwgpZxgpdxg5dyhJhzhJhzhZl0hZl0hpp1hpp2h5p2h5t3iJt3iJx4iZx5iZ15ip16ip16i557i558jJ99jaB+jqF/j6GAkKKBkaOCkaOCkqSDkqSDk6WEk6WFlKWFlKaGlaaGlaeHlqeIlqiIl6iJl6iJmKmKmamLmaqLmqqMmquMm6uNm6yOnKyPna2Qnq6Rnq6Rn6+Sn6+SoLCToLCUobCUobGVorGVo7KWo7KXpLOYpbOYpbSZprSaprWap7Wbp7abqLacqLedqbeeqrifq7mgq7mgrLqhrbqirrujrrujr7ykr7yksL2lsL2msb6nsr6nsr+os7+ps8CptMCqtMGqtcGrtcKstsKtt8OtuMOuuMSvucSvucWwusWxu8ayu8ayvMezvMezvci0vci1vsm2v8m2v8q3wMq4wMu4wcu5wsy6w8y7w827xM28xM68xc69xc++xs++xtC/x9DAyNHByNHBydLCydLEy9TEzNTFzNTFzdXGzdXHztbIz9fJ0NfK0NjK0djL0dnL0tnM0trN09rN09vO1NvP1dzQ1dzQ1t3R193R197S2N7T2N/T2d/U2d/U2uDV2uDW2+HX3OLY3eLZ3ePZ3uPa3uTa3+Tb3+Xc4OXc4ebd4ebd4ube4uff4+ff4+jg5Ojg5Onh5eni5eni5urj5urj5+vk5+vl6Ozm6e3n6u3o6+7p7O/q7fDr7fDr7vHs7vHs7/Ht7/Lu8PLu8PPv8fPv8fTw8vTx8vTx8/Xy8/Xy9Pbz9Pb09ff09vf19vj19/j29/j3+Pn4+fr5+vv6+vv6+/v7+/z7/Pz8/P39/f39/f7+/v7+/v////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8I/wCzheMWTiBBgwUHJjyoEKHDhhAZSlxI8eFEixUjZryoEaPHjiA5TgzXLdw3kiZRniy5MiVLlTBfynRJs6XNmDVx3py5MydPnUB/CvVZU+TGox+NJkUakqnSpkujQp1KtKfVoFWxXh26NStXrWC/ipX6tKzTs2SvBSiwYIKFFjuugBGk6Zi1qWbJom0a1qvfroD7RgsQYADhwocNHyhBRZAsbH/7BhZbdG9evJYzZ7MW4MDazp89FwA9ugEMPK40Y9b7MTLlya5jn3xmmHBtxLYTJ4Yw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'
    main()


# v1
# import GuiAPPs as apps
# apps.guiBallMovePlay()

def guiBallMovePlay():
    # Importing arcade module
    import arcade

    # Creating MainGame class
    class MainGame(arcade.Window):
        def __init__(self):
            super().__init__(600, 600, title="Player Movement")

            # Initializing the initial x and y coordinated
            self.x = 250
            self.y = 250

            # Initializing a variable to store
            # the velocity of the player
            self.vel_x = 0
            self.vel_y = 0

        # Creating on_draw() function to draw on the screen
        def on_draw(self):
            arcade.start_render()

            # Drawing the rectangle using
            # draw_rectangle_filled function
            arcade.draw_circle_filled(self.x, self.y, 25,
                                      arcade.color.GREEN)

        # Creating on_update function to
        # update the x coordinate
        def on_update(self, delta_time):
            self.x += self.vel_x * delta_time
            self.y += self.vel_y * delta_time

        # Creating function to change the velocity
        # when button is pressed
        def on_key_press(self, symbol, modifier):

            # Checking the button pressed
            # and changing the value of velocity
            if symbol == arcade.key.UP:
                self.vel_y = 300
                print("Up arrow key is pressed")
            elif symbol == arcade.key.DOWN:
                self.vel_y = -300
                print("Down arrow key is pressed")
            elif symbol == arcade.key.LEFT:
                self.vel_x = -300
                print("Left arrow key is pressed")
            elif symbol == arcade.key.RIGHT:
                self.vel_x = 300
                print("Right arrow key is pressed")

        # Creating function to change the velocity
        # when button is released
        def on_key_release(self, symbol, modifier):

            # Checking the button released
            # and changing the value of velocity
            if symbol == arcade.key.UP:
                self.vel_y = 0
            elif symbol == arcade.key.DOWN:
                self.vel_y = 0
            elif symbol == arcade.key.LEFT:
                self.vel_x = 0
            elif symbol == arcade.key.RIGHT:
                self.vel_x = 0

    # Calling MainGame class
    MainGame()
    arcade.run()



# v1
# import GuiAPPs as guiApps
# guiApps.guiCalcShow()
def guiCalcShow():
    import PySimpleGUI as sg

    # default settings
    bw = {'size': (7, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#F8F8F8")}
    bt = {'size': (7, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#F1EABC")}
    bo = {'size': (15, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#ECA527"), 'focus': True}

    layout = [
        [sg.Text('PyDataMath-II', size=(50, 1), justification='right', background_color="#272533",
                 text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
        [sg.Text('0.0000', size=(18, 1), justification='right', background_color='black', text_color='red',
                 font=('Digital-7', 48), relief='sunken', key="_DISPLAY_")],
        [sg.Button('C', **bt), sg.Button('CE', **bt), sg.Button('%', **bt), sg.Button("/", **bt)],
        [sg.Button('7', **bw), sg.Button('8', **bw), sg.Button('9', **bw), sg.Button("*", **bt)],
        [sg.Button('4', **bw), sg.Button('5', **bw), sg.Button('6', **bw), sg.Button("-", **bt)],
        [sg.Button('1', **bw), sg.Button('2', **bw), sg.Button('3', **bw), sg.Button("+", **bt)],
        [sg.Button('0', **bw), sg.Button('.', **bw), sg.Button('=', **bo, bind_return_key=True)],
    ]
    window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", return_keyboard_events=True)

    ''' calculator functions '''
    var = {'front': [], 'back': [], 'decimal': False, 'x_val': 0.0, 'y_val': 0.0, 'result': 0.0, 'operator': ''}

    # helper functions
    def format_number():
        ''' create a consolidated string of numbers from front and back lists '''
        return float(''.join(var['front']) + '.' + ''.join(var['back']))

    def update_display(display_value):
        ''' update the calculator display after an event click '''
        try:
            window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
        except:
            window['_DISPLAY_'].update(value=display_value)

    # click events
    def number_click(event):
        ''' number button button click event '''
        global var
        if var['decimal']:
            var['back'].append(event)
        else:
            var['front'].append(event)
        update_display(format_number())

    def clear_click():
        ''' CE or C button click event '''
        global var
        var['front'].clear()
        var['back'].clear()
        var['decimal'] = False

    def operator_click(event):
        ''' + - / * button click event '''
        global var
        var['operator'] = event
        try:
            var['x_val'] = format_number()
        except:
            var['x_val'] = var['result']
        clear_click()

    def calculate_click():
        ''' equals button click event '''
        global var
        var['y_val'] = format_number()
        try:
            var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
            update_display(var['result'])
            clear_click()
        except:
            update_display("ERROR! DIV/0")
            clear_click()

    while True:
        event, values = window.read()
        print(event)
        if event is None:
            break
        if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            number_click(event)
        if event in ['Escape:27', 'C', 'CE']:  # 'Escape:27 for keyboard control
            clear_click()
            update_display(0.0)
            var['result'] = 0.0
        if event in ['+', '-', '*', '/']:
            operator_click(event)
        if event == '=':
            calculate_click()
        if event == '.':
            var['decimal'] = True
        if event == '%':
            update_display(var['result'] / 100.0)


# v1

# import GuiAPPs as guiApps
# guiApps.guiColorsShow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def guiColorsShow():
    # very complex - shows all the color swatches
    # if you click on a color square, it copies the web color to clipboard

    import PySimpleGUI as sg

    """
        Demo Theme Color Swatches

        Sometimes when working with themes, it's nice ot know all of the hex values
        for the theme.  Or, maybe you want to scroll through the list of themes and
        look at the colors in the theme as groups of color swatches.  Whatever thr
        reason, this ia good candidate for you.

        Thie program is interactive.  In addition to showing you the swatches, you can
        interact with them.  
        * If you hover with your mouse, you'll get a tooltip popup  that tells you the hex value.  
        * If you left click, then the value it posted to the clipboard.
        * If you right click a swatch, then the right clip menu will show you the hex value.
          If you then select that menu item, it's copied to the clipbard.

        The code has several examples you may want to try out in your prgorams.  Everything from
        using "Symbols" to make the swatches, so generating layouts, integrating (optionally) other
        packages like pyperclip, moving a window based on the size of the window

        This code's pattern is becoming more widespread lately:
        * Have a "create_window' function where the layout and Window is defined
        * Use a "main" program function where the event loop also lives

        Copyright 2020  PySimpleGUI.org
    """

    # Try and import pyperclip. Save if can be used or not.
    try:
        import pyperclip

        pyperclip_available = True
    except:
        pyperclip_available = False

    def create_window():
        # Begin the layout with a header
        layout = [
            [sg.Text('Themes as color swatches', text_color='white', background_color='black', font='Default 25')],
            [sg.Text('Tooltip and right click a color to get the value', text_color='white', background_color='black',
                     font='Default 15')],
            [sg.Text('Left click a color to copy to clipboard (requires pyperclip)', text_color='white',
                     background_color='black', font='Default 15')]]
        layout = [[sg.Column(layout, element_justification='c', background_color='black')]]
        # Create the pain part, the rows of Text with color swatches
        for i, theme in enumerate(sg.theme_list()):
            sg.theme(theme)
            colors = [sg.theme_background_color(), sg.theme_text_color(), sg.theme_input_background_color(),
                      sg.theme_input_text_color()]
            if sg.theme_button_color() != sg.COLOR_SYSTEM_DEFAULT:
                colors.append(sg.theme_button_color()[0])
                colors.append(sg.theme_button_color()[1])
            colors = list(set(colors))  # de-duplicate items
            row = [sg.T(sg.theme(), background_color='black', text_color='white', size=(20, 1), justification='r')]
            for color in colors:
                if color != sg.COLOR_SYSTEM_DEFAULT:
                    row.append(
                        sg.T(sg.SYMBOL_SQUARE, text_color=color, background_color='black', pad=(0, 0),
                             font='DEFAUlT 20',
                             right_click_menu=['Nothing', [color]], tooltip=color, enable_events=True, key=(i, color)))
            layout += [row]
        # finish the layout by adding an exit button
        layout += [[sg.B('Exit')]]
        # place layout inside of a Column so that it's scrollable
        layout = [[sg.Column(layout, scrollable=True, vertical_scroll_only=True, background_color='black')]]
        # create and return Window that uses the layout
        return sg.Window('Theme Color Swatches', layout, background_color='black', finalize=True)

    def main():
        sg.popup_quick_message('This is going to take a minute...', text_color='white', background_color='red',
                               font='Default 20')
        window = create_window()
        sg.theme(sg.OFFICIAL_PYSIMPLEGUI_THEME)
        if window.size[1] > 100:
            window.size = (window.size[0], 1000)
        window.move(window.get_screen_size()[0] // 2 - window.size[0] // 2, window.get_screen_size()[1] // 2 - 500)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if isinstance(event, tuple):  # someone clicked a swatch
                chosen_color = event[1]
            else:
                if event[0] == '#':  # someone right clicked
                    chosen_color = event
                else:
                    chosen_color = ''

            if pyperclip_available:
                pyperclip.copy(chosen_color)
                sg.popup_auto_close(f'{chosen_color}\nColor copied to clipboard', auto_close_duration=1)
            else:
                sg.popup_auto_close(f'pyperclip not installed\nPlease install pyperclip', auto_close_duration=3)

        window.close()

    #if __name__ == '__main__':
    main()


# v1

# import GuiAPPs as guiApps
# guiApps.GuiCOMMISSIONshow()

def GuiCOMMISSIONshow():
    # simple input output
    # sales commission calculator
    #
    import PySimpleGUI as sg

    def compute_bonus(sales):
        return sales * .25

    def main():
        layout = [[sg.Text('Sales Commission Calculator')],
                  [sg.Text('How much did you sell?  $'), sg.Input(size=(8, 1), key='-IN-')],
                  [sg.Text('Your total income: '), sg.Text(size=(15, 1), key='-OUT-')],
                  [sg.Button('Calculate', bind_return_key=True), sg.Button('Exit')]]

        window = sg.Window('Sales Commission Calculator', layout)

        while True:  # Event Loop
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Calculate':
                try:
                    total = float(values['-IN-'])
                    total += compute_bonus(total)
                    window['-OUT-'].update(f'${total:.2f}')
                except:
                    window['-OUT-'].update('Invalid input')

        window.close()

    #if __name__ == '__main__':
    main()



# v1

# import GuiAPPs as guiApps
# guiApps.GuiCOOLdesignShow()

#apparently the design had something to do with Reddit

def GuiCOOLdesignShow():
    import PySimpleGUI as sg

    BG_COLOR = '#1B1B26'
    INPUT_BG_COLOR = '#2C2C37'
    BUTTON_BG_COLOR = BG_COLOR
    TEXT_COLOR = '#FCFDFF'

    def the_gui():
        sg.theme_background_color(BG_COLOR)
        sg.theme_element_background_color(BG_COLOR)
        sg.theme_input_background_color(INPUT_BG_COLOR)
        sg.theme_input_text_color(TEXT_COLOR)
        sg.theme_text_color(TEXT_COLOR)
        sg.theme_button_color((TEXT_COLOR, BUTTON_BG_COLOR))
        sg.set_options(text_element_background_color=BG_COLOR)
        sg.set_options(border_width=0)

        # --------------------- User defined elements ---------------------
        # It would have been better to render the buttons with the red line
        # rather than trying to line up the red line images. Space varies depending on OX
        def top_button(text, image_key, set_as_default=False):
            col = [[sg.Button(text, size=(10, 1), font='Helvetica 13 bold', button_color=(TEXT_COLOR, BG_COLOR))],
                   [sg.T('    ', font='Helvetica 13 bold', pad=(0, 0)),
                    sg.Image(data=red_line if set_as_default else blank_line, key=image_key, pad=(0, 0))]]
            return sg.Column(col, pad=(0, 0))

        # --------------------- BEGIN GUI DEFINITION ---------------------
        # This is the first of 4 Columns. It holds all the stuff to show when
        # the "Tasks" button is selected on top. Each button will have an column
        # When a new top-button is selected, the previous Column is made invisible
        task_col = sg.Column([[sg.Text('3 Tasks', size=(10, 1), font='Helvetica 15 bold', key='-OUT-TASKS-'),
                               sg.In(' ' * 20 + 'Search', size=(28, 1), key='-SEARCH-', font='Helvetica 13'),
                               sg.B(image_data=plus_button, key='-PLUS-')],
                              [sg.T('  Store    Product    Size   Profile    Proxies     Status', font='Any 10',
                                    text_color='#505063')],
                              [sg.T(size=(1, 4))],
                              ],
                             key='-COL-TASKS-')

        bottom_buttons_col = sg.Column(
            [[sg.T(background_color=INPUT_BG_COLOR, font='Any 4')],  # some padding at top and bottom of box
             [sg.B(image_data=green_button, key='-GREEN-', button_color=(INPUT_BG_COLOR, INPUT_BG_COLOR)),
              sg.B(image_data=yellow_button, key='-YELLOW-', button_color=(INPUT_BG_COLOR, INPUT_BG_COLOR)),
              sg.B(image_data=red_button, key='-RED-', button_color=(INPUT_BG_COLOR, INPUT_BG_COLOR))],
             [sg.T(background_color=INPUT_BG_COLOR, font='Any 4')], ],
            background_color=INPUT_BG_COLOR, pad=(0, 10))

        layout = [
            [top_button('Tasks', '-L1-', True), top_button('Profiles', '-L2-'), top_button('Proxies', '-L3-'),
             top_button('History', '-L4-')],
            [sg.T()],
            [task_col],  # Add the other main window columns here
            [bottom_buttons_col, sg.T(' ' * 90), sg.Button(image_data=captcha_button, key='-CAPTCHA-')]]

        window = sg.Window('Shopify Mockup', layout, use_default_focus=False, no_titlebar=True)

        top_button_selected = 1
        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            if event in (None, '-RED-'):
                break
            if event == 'Tasks':
                window['-COL-TASKS-'].update(visible=True)
                window[f'-L{top_button_selected}-'].update(data=blank_line)
                top_button_selected = 1
            elif event == 'Profiles':
                window['-COL-TASKS-'].update(visible=False)
                window[f'-L{top_button_selected}-'].update(data=blank_line)
                top_button_selected = 2
            elif event == 'Proxies':
                window['-COL-TASKS-'].update(visible=False)
                window[f'-L{top_button_selected}-'].update(data=blank_line)
                top_button_selected = 3
            elif event == 'History':
                window['-COL-TASKS-'].update(visible=False)
                window[f'-L{top_button_selected}-'].update(data=blank_line)
                top_button_selected = 4
            # indicate which button is currently selected
            window[f'-L{top_button_selected}-'].update(data=red_line)

        window.close()

    #if __name__ == '__main__':
    blank_line = b'iVBORw0KGgoAAAANSUhEUgAAAFgAAAAGCAMAAABwz6mBAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALMw9IgAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAFUlEQVQoU2P4TyMwajAcDDWD//8HAKuCDg94rot1AAAAAElFTkSuQmCC'
    captcha_button = b'iVBORw0KGgoAAAANSUhEUgAAAHMAAAArCAMAAAB8QEdOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAABYWGRQUHBYXHBcYHBgZGxkaHhcXIRkZIRoaIBwbIRwcIRwdIh4eIB0eIx0dJR4eJh8fKR8gJSAfJSAfJyAgIiAhJSAgJiIiJCEiJiQkJiAgKCEhKyIiKCIiKiIiLCMkKCQjKSQkKSQkKiYmKCUmKiQkLCQkLiYnLCYmLicoLCgnLSgnLygoKigpLSkoLioqLCkqLiwtLyYmMCgoMCgoMioqMCoqMioqNCssMCwrMSwrMywsMSwsMi4uMC0uMiwsNCwsNi4vNC4uNi4uOC8wNDAvNDAvNzAwMjAwNTAwNjIyNDEyNjQ0NjAwODAwOjIyODIyOjIyPDM0ODQzODQzOzQ1OTQ0OjY2ODU2OzQ0PDQ0PjY2PDY2Pjc4PTg3PTg3Pzg4Ojg4PTk4Pjk6Pzw8PjY2QDg4QDg4Qjo6QDo6Qjo6RDs8QDw7QDw8QTw9Qj4+QD0+Qj09RTw8Rj4+RD4+RkFBQ0FCRUNERkJBSUJCSkNESEZGS0VGTEpKTkhIUEtMUUxLUExNUU5PVE9QVFBRVVFRWVNUWVVWWlVVXVhYWlhZXVhYYFxcZF9gZGBfZGFiZmZmamxsbmtscW1uc21udHFydnJzeHJyenN0eXR1eXV1fXh5fXx8fnh4gH59gn+AhIGChYOEiIWGiYqKkoyNkoyMlJCQkpKRl5GSl5OUmZeXn5mYnZubo5yboZ2eoqGipKKiqqOkqaurrampsaytsq6utbCxtrO0uLS1ura2vre4vLi4urm6vby8vru8wby7wb2+wsHBxsXGysTEzMbHzMbGzsnKzcvM0czL0M3N0c7P1M7O1s/Q0s/Q1NDP1dDQ0tHS1tPU1tTU2tbX2dbX29fW3NfY3NnZ29nZ3dvc3tzd39ra4dra5Nzb4N3d4t3d5d/g4uHi5+Pk5uHh6ebn6efo7Onp6+jp7ezs7unp8err8Ovr8+vs8O3u8ezs9O/w9PDw8vDx9vP09vT09vLz+PP0+PTz+PX2+vb3/Pf4/fn5/vv8//z7//7+/gAAAFDaIzYAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAG1UlEQVRYR72YDXgbZR3Ai+IUmF1FoBtZk7qapAkb2fXey13W3u4ud1lZd1566bauSTuRDrqVjoIMqw46GHaWMRXUgc5PwPmt42N8jO91aGGPDhUUC0MUdUYmAeLQshv/8H+Ta7KSdGzPQ/jlefrk7t78f/e+9977/7+tyOTxst4ywbJely2hTDidHsLzapmQZZknHtuUd3p4OXupPNDgKmpzrpzTR3j7annhc33NOqmyjN3Mw/vyTlZRNEQpPwI7O+f0UiM9IeQulBU265wtRPG7QMmdLiOaJuBLU4Eji53MKt8TJ3a0YrYStaX2+fIicK5MhUuLCvg4UYl/5Umfdx86mN5MBU7afA9lMffhJU+wJ+IxYwrr4qKKVxNwMFguyrGXe12Xc7kpLggaMYjHaCamQYxmH2lsVrxK1MtiHwQXl4iyXDbo0Qga/niSU5bFHLWdem2939/qUhIXxTQtmqDCGLo5VolpnFfgOLxhTmg2zl9G5vJzlzUajc09shyLYWtN4Lwa3i0XW23HLXAMZ5ipjazrqGcSKMEVWvgIK3B415rR45DJh0yDR+grLp/haSTn9zpmOJY1qsYZhgub4eRIsALemcJ90I5b4BhOXQ+HGH9knQ9/fFEiqiVWX0y7Ks8w+bhJujzoo0sXUc1lvMPXOLfLjHtI89zPrY7iaHBKIoF3yCYupu/gZI7h9Le0+v1t0vtVwyBOp8fHO2d4VFMlXWJNXUhk3KFImPGHxKDYfk710qXB9kDLokBLZ+AUucqjYnYiPhLvIlUOnx23QAmnrRTDp9d36OGOVYbB+9TeuNMR/7TqJIYRnsMs193+C+oi7RLTFJFqFoita8Xq4McW1H1S/OjaFucVvUQ2cdANnpim2mPHLWA7ffS52NhKsTPYEq7s/8lTL/3mBz3vc5jxb9z/2LdIlRza/ewfn37oluEP7Bp95g979/5+31B194//lH7ql2uq1z35aPfSmg2P7exVZfKl/b/eWuXgPcVZA8dAVUs7A62hU67eA6/vB7hnEyHyToCfmXJ81gvw3N8B/jY8+k+AQ4fG/3vJ4AgkXwBrb/upAN0L2nvhpa4qR3ynBXfEiYE5+e3YTr6gzDulVr1+u/XMmtot+2BrDRM5/KqV7A7Pak3CZ88c+C3cNn9hwxhsbmhY9PPxsQtahv8CX2kat7rn6OvhxZVMsC+VOvx6/8ppYd0OW+AYzrbpYeaAtUNqn/O1n36xb+XW9K7RN24W+5h0amgJsyN9O7Ow6VnYLDVNH/v/ju7ASTd+7yb3m3DNWnEIDp6+puUm695HrBuquzum22EL2E4hP4UKcygSqQmm4Wr38tMWu89l3CPw5Zth5GTdDy9+/YZvHoBbgpI4BtdLTd0WXD9v3oULP37e2Rb8G8CCA5I+7QHYtg1G3LpfL1o+7Tl0tHNCWqfXdx6EVf3u5W2VfdLy/8ElA6nx9SH/AUhj3D3BYFjcj05xEQ722Z+49KRPzVwBqYcfvGt3KqlXDkFK6ng5vb5yWvuJOFsrO1oPjm+qZpoGb/yCdCuk7h4B6/uhy96wfvHD727owldQ3g9bZHHxv2Djinlnbv7q5pkAKxoWDsJ426zb0skRbP5tJhI6EWebJNXeCfescV85CtuYkdSRIzAOu88SX/nP5309zhnxCee0hw49+OFLB34H31liwfyZ53XAmC6NQvpI6lXYo0snNrb91aGhJIzctw/GVl0G0Fc7ZyAJw9JfYZMQpclWU56HLYq8aBBe+/OPUtbTSxpeG//M/HkbIR0ZsJLXRPThl63BSv9xOPO5zAySNt+1/7AOw6+uCmyHu+v0lYF9sC3yCiQwT2mYxahTkztPGxrDmfPElUsDb4IkLd6YTrZvh13ucHXwcbi1PzCVc1KSy+drgVeMWOd1Vxk+XDPy2K3yqLjGXXHdBmJfLsJuVoBWBkJ2vS0BvRiNYS4TtFhxepiA1hhKIlY6RCloAWRO7aS1CqZmmoOnjMlqCY1lucLDeSeok0NnyV/QwoVasVDiuOIaw4YmS9rEPjw+2EyFd2ongkocXftkETF2NhfFWsQ+fEeoitZgpZy2UChRRU0iW/1PPQxF4MgptNZ0FmccOVvt5KBbuKOn7iR41cC6wD44DnBPKBMnOkvM9Ik4BgplLFByR8UQ3ueRTZXWR8dF1unAvYODN1GR2w2Xi1yhqBLZ4B3ZfRl5D3aeWSv10h0oOl04CeiMsR90GaCFPzVoysT+M+OyfWWz4nueneJRjiqzzgyW6tmaP9eiHNhWL7XlnBkXXY3K58Tg2RUtp7Sd1IrbHrvJuw4NLBT+LzXhxAEu49DiDGInjJnMW4afJfH6bdHpAAAAAElFTkSuQmCC'
    green_button = b'iVBORw0KGgoAAAANSUhEUgAAABMAAAAWCAMAAAAVQ1dNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAABR4Rh91SB15Rhp5TSV3RyZ8SyV6Ux6HTCaDTiqHWyyDWCiKUSuTViiXVSicWzODXD2BXDCaWjKbYzyZYDKjYTGjaDelaDGoZDmrbzyqazumcj+wcD25cTnCdD3BdTTUcjLeeDrcdT3feDPgbTLiczLjdzPlczDkdjbkdTfldjTmdjXndzPkeDHneTbmeTXmejblfDblfjTnfzXudzHpejHofDfofDTofTXseDnldTnkdzrmdjjmdz/gdj7idT3jdz3mcz3ldjzkdzzmdTvhfTrjfDnifTrjfjrkeTrleznkfjrnfj7heD3ieTzjej3kejzmeT/odT7pdzroeTjoezzoeDzufkCAZUaJZk2SdVSPeUWrakKpcUmkeE23d0DJd0bLfEjCdUrNf0DddEXce0TefkXff0jdd0/cfk3ffUHic0DidUPkckDkc0Pmc0LkdEPldkLmdULmdkDjekHjfEPleEDoeTbmgTvlgjjngDzkgjzsgEi7glu6gl29j26+m0fOgkvEgUrMhk3Lgk3KhkzMgUzOhEzKiELYgUnQgUrTg0jWgkvWhU/ShE3VgE3VgU3UhU3XiUjbgEvagkrag0jfgkjehUjciE/YiFLGiVHLglLJh1LOhlDNi1LNjFfOjFjLhlzMhFnMi1PRh1TUgVbVjlXagVLZjFnTilLckVfbkFvalUPjg0PhhEPghUHihEPihULkgUDmgkDlhkPkh0PnhELmhUXhgEXggkTigUXjhETihUXjhkfih0Tkgkbkg0TkhETiiUfki0HrgUvig0jmh0/gg0zgiFDmjFvjj1LmkFjjkFrokmLGlGfDkGbPl2rCmGPYkmbZnmbgkwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACXBECsAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABQ0lEQVQoU2P4H8X+Hw0w/K+vlWSGcqCA4f+FNcviRVihXDBg+L94Us+VRTE8UD4IMPxfMn1H5vKlSRIcUBGQ2MSDR1Iyso5PleeDCgHFul31ywtzSrbtS5ThgonNdNdQcQzW0q0+sWKeGCNErHGLQZiLlbae0brp6zvl+MFizVsNA52sdEyNN6xVqzmQIMoGFOs45O3nYK1vVrFxk6VJwOSVdYIgMQ9fe2dbi6o9u1TVladcOh/J8L91n5tdtr2Nuc/OaQrHzs6NFQDqbdnrn5Od5xLqlT7lzOomYbAdbbutC3Lzg0I8UycskGaBuCV5v7VLUXFZaVr/Qm6QCEisa7tauKbS0VOzhSAiILH2w5WKm0/2SXFCRUBis1bNON0rywvlgwDD/3OX588Rh/IggOF/w8U4JigHChj+R0dAmVDw/z8AkbkcWUjJmvYAAAAASUVORK5CYII='
    plus_button = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAYCAMAAADTXB33AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAAsbGAUpHQ01Kgo9KhUlIhEjLREqLxkpKB4qKhwtKR4sMBwsORI2KBE2LhY1LRA4LRkwJh00JBsxLh4xLR00Lhs+KBw9LBY3MBk2NB4yOx46MSAfJSEdKjMdLDgfMiM0GSM7GSEnJyAjKiMjLSMmKyUkLSAtJiIpLSIsLSUpLSUuKyglLS4kLCkoLiosKSgtLi4sLyIlMSUjMCYmMCAqMSMpNSYqMScrNCYuMSUtNCQtOCkmMSklNC0nMSkpMioqNCktMikuNS0qMS0qNS0tMSwsNSktOC4uOC0vPCI0JCQ4LSc8LSAxMSEwNSA0MiYwMSUzNCU1MSY2NCEyOiA1OiYwOSc1PiM6MiM5NiA+NCY4MiY7NiU9NyA/OSkxNCk1Ni4yMy4wNCgyOSk2PS8yOS43Pio5My05Oi45PzMnJzUmKzEqLjgpJjUjMzEqMjErNTAuMTEuNjUpMzQvMzYvNzQsODspNzksOz81KTEwNTY5MjU7Ny01QDE6RAJRMQ9XMhtNKh1DNhdZPh5VPg5kJQlmNxVhMCJCNyVANyRCOCZJMyZOMydOOSdOPClAOi9MNihKPC1JPS1NPiVXJCFZKCVUMi9YOCxdPTJAMDRAMjBEOTFSPzhRNDRpOxVeQQ1/QRltSy1ARylFSC9fRy9ZSzFQSDJcRiZiSSBtTS5qSCRxQzNlQDZjTzthVDB6STp2UkJrXURvXEh2XB+KOiicVTSGRDWMVTiIUz6QXzqdbjWgXDKzVjyyXjSlZzK6Zj2+azfDYj3LdzvbbTHXczjYdC/ibTXmdDvrfj/pfD/wfkWaVlGMXEGNZ0uObUKbZUWbbkqQa0mSdFaJaFCTcFeZfUGiXUSpZ0C6cUjDckDVd0PbdkXadkPeeUXff1LBf0HsejjPgD/eimWwkUrKjU/XjUnfhk3YhUvcj03UklbLh1rPi1jEkFvOlV7JlV3NlVPXg1TYhVvZhVvcgkfjgErnjlDngFHljVfhlmbKlmrDl2zLk2DQmGnWk3PelgAAAEiibAcAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAACNElEQVQoU2P4Dwc5/3Ny8p311KDc/1ApHR0958JCQ9eiqiJnG6gkRMquqCop0UDJwMBAz965oMgELAiWcnbWU9UMCg6Kjg4KcHR2cXOxV4FIqdmUudhb+opKd3R1xgbHu7kVubmB5Bj+q9gDWfEZkfxNSzeuW9YfHOBW5ACWY/iv5uDhoaEVwMW74tLjq5smiXBqxms5eLiZ/GcwcbB3CkuTKakWa3vy8v2GCT7egjFWDvYODiYM9g727qYpWjWzpi14+OjpjjU93eIRlg5AYMLg4OaQapIQtXzG+q2Hnj3fvX31qjnpjm4g2xgcPBw8Uv1bzu68fuDWl3v7b+y7sHk20JUgKTcPh6QMgYVvXn+8e/L4iSNfX7y9Mjnew83DwwEkFR/MvPLn30+3Hxw7dfT7jz/nJiZAdbnZO1mJ9F0+c3rP4cPf9l47f3FtbLwbyK8gKTcPJ+2ZClO2HLzzedvUxl5pXyc3V5CUmpubg6eDblalYuvND//mzfUK4vZztAcCNYb/9m5O1u5l2bkK7fdf/Z4+Uz0hNNwCZB5QSs3enUcqRVNfqGHXu19LJklKsrNZuXm42YNC3sQ6RCqUOymdZX59M5Ow5OJFde4ebg6Q+DJ3t0o2Ly7lkOCL43TiNpWVBcuApZT1NDJc5fJsMv2SyypcPCoqXOyBomCp/1ysQUly8i511kZ5eTr2hUWQxAGW4mTkTCqvsDWrNaqocEt01gHLQKQgwNjIwQGWmv7///8fAJ7/NhA3zMv/AAAAAElFTkSuQmCC'
    red_button = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAVCAMAAAB1/u6nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAF0jPF0mO18lPWEYM2EbNWAcM2AfN2QZN2cbNWQeNmEdOWAdPGYaOGQdO2oTNWoVNmwXOGgcNmwZN2gbO2keOmkePG0YOGwdOm4ePXAKL3MKMnMPNXAXNXIXNnIXOHAaPXEcOXIdOnIfOXUZOXcZPXYcOHYdPXwTO3oZPHocPnofPn0ZPWEjOGEhPGQiPWQkPGkgO2ohPGwiO2wgPG0hP2wkPHAgO3YgPXUZQH8bQWwmQGwrQ4cOO4QQNYMWPYAXP4UXPIEdP4UaPYYdPooTO4sVPZMPN5YYPoMdQocfRIsWQYkbQIocQ4geRI0YQo8bQo4aRJsOQpAQQJEUQJUXQpYWRpIZQpUbQpYeRJMbSJIfSpgUQp0VQ5wXRpkaQ5gbRZ4ZRoAhQYUiQYwjS5UhRqQPRqsMRKYSRKEYRqEZSaYeTqsTRqgURK0XR6kSSakVSa0VSK8ZR6sbTKwYSq8bTb0MQ7IQQrAURLAWTLEaT7oTR7oVTb0VSb0VTrkcT70ZTr4ZUaIgTq8gTKYgUqogUakkU6klVLMgVLcjV7MkWbQkWbkjU7ojWMIOS8ENTMUPTMQSTs8TTcUSUMUXVMYeWc0XVMgbUcodVc0ZVMsdWM4aWdcMTNIOUNsPVtYQTdIWU9AWVdQSVdUUU9QVWNAaVdAdVdcaVNMZWNYZW9kSU9sSVtoWVd4RUt0VWN8ZVtsaWdgfWdwaWd8eYcEgUscjWMggW8siWc8gW9MhX9YgXdUjYeMHUeIIVOMMUOoOVu0KVOwPVOgOWO8OWuMRVeMRWOUQWOcWWuQZWOQdXugRV+gWV+4TV+oSWusUWeoVXOwQWO4VWegaWukYXOoYX/IKVfYJVvYMV/ENWPMMWvAOWPMPWvANXPYJWPUNWPYPX/8GVvoHWf8CWv8EWP8EWv4GWP8HW/8FXfoIVfwKVvkKWfkMWfkOXf4JWf4KXP0NXPERWvASXfQQW/YWX/kQX/4QXOEeYukXYO0bYv8OYvYSYfUUYPIYYuIjZucgYQAAAAr+GkYAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABy0lEQVQoU2P4zyjCL2D0HwG4OFn+/2f4Lx6dnRUgBxX7r5ycmuonDhR26N69ojFRTRckKOSYN2Pp9jat/wx6Udu+H76yI17W4P9/E5/CVZ9vnewECouFzb7/5OefhlAvdRXf0gX33r293KH+n4HPdsqv589frdlaHBdTMvPc2yfv1zWZAs2WKZh3992z/f8WTp648Pint2/P1ngyA4W57dPn/npz9cP5Y8fO3rv76sK0GF6QA///18ycef7NtVsf7l17+/XD4gwnoBBImCmpZNG9t6/fv3384OqccjdDqPB/s5i+A+/evn379MW+MndFkAhY2Dx2woF3D54+fXtvbbWHEkxYIrxm9Q2g2pf3Lq6f3uwMCiCgsGho3bqPt699vX7w9KUTa5bl+IuBhPUDJx96/+7ehSPzJy0/ceb66z393jxAYavKY++ePzy1obaiaMvGcw+ePNmbb/mfgTdoyZfnb87P7Il0cY6o3/T60fM3U7z/MwimLbpz88euXDsLM2PthJojb96drXNjY+AInvp386wSVxXW///Z5UNqVn7b2aoDNFujpbcqzlHRBuTc/8KB2V3tKaJAYTFVaSl1a7AgEOhJKkhy//8PAMoKLCsLw4FtAAAAAElFTkSuQmCC'
    red_line = b'iVBORw0KGgoAAAANSUhEUgAAAFgAAAAGCAMAAABwz6mBAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAKMXRqQRR6QfTqwUR6oYR6oYSakZSrEYTrkSSroVTb0WTLsdUK4hVbohWbojWMcPT8IUT8cRTsUTT8QXT8kRT8gWTsISUMMTUcATUsAXUMUTUcYXUMQbUsgRUcgWUMgVVs0TVMwUUM4VUc8WUs8XU88XVc8UWMoYVssYWdEVUtMVU9AWU9EUWNAdV9UYVtcYW9oTVtgXWt4cW90cXdoiXusJU+0LVe0NVu0MWOITV+QSW+QXWuYeX+sRW+gSWOoSWekWW+oUXO0QWe8RWu0QW+8RXO4QXfUKV/EOWfANXPAPXfMPXvcMWfQNW/YNXvoHV/8CWP8DWf0EWP8FWv8HWf4GWv4JWf8JWvwJW/0KWv8LW/4MXPwOXPAQWfERWvMWXPQRWfQSWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK5kYR8AAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAqklEQVQoU2P4zySprquooKGmAwEq5AEtbW0dHVVVVR1lJXlZHtb//xl4Na19/P283eI8KQZxzs5xnuYuDlbGpiL/GfiMvMKCAoMDoigEEVA6PMrDzN5Wn42B38A9MiQ4NCqGchAbCySiY3wtHG312RmYpQzt4xOTEpydXSmDDnYOds6ucZbOTjYmepz/Gf7/Z+GWERMTExaWpghKCAKhsJyogJA4Fwfj//8Ar/aGF89us74AAAAASUVORK5CYII='
    yellow_button = b'iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAMAAABhEH5lAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAALWfL7+lN7esQrinS72mSbirQrmqQ7+oSr2nUsGmPcGlQcOnRMCnSsKnU8OmVsOmWMGnWsGoUcGpU8OqWsSjYMSnY8GoZs2sae/WPvfOJvbPKvrOJfjPKfzMKv/PK/PON/PPPfLOP//HNf/HP/rPM/vMNv3KMf7LMv3KM//LNv/NMP3MMf/MM/7OMP/NNf7ON/jLOvrJPvrOOf/LOf/IPP/LPP/KPf/KPv/MOv/MO//MPP/MPv7OPP/PPf3PPv/OP/PSL/bRK/DYLv/RL//SLfPWMPPVNfHWNPLWNfLWN/fTNPfTN/XVNPXUNfXUN/PUPPPUPvbSOfXSPPbSPvfTP/XUOfDYMPnTNP/RMP3RMv/SMP7SM//RNvrROfnRO/nSOfrQPPnRPv3QOfzQO9nAWe/MTOnPVu3OUezOUunOXe3MWO3QRu/URe/TTu7US+7UTO3ZRufRWe/SVO7WUu/RWfXHTfXLQfXLRfXMQPbJSPXPSP3HQP7GQf/FR//HR//ESP/GSf/GSv/HS//HTPvLQ/nPRfrOR//KQP/KQv/JRP/JRf/IR//KRP/KRf/LRv/LR/7NQP/MQv/MQ/zOQPzOQv/MRP3MRf7ORP/ORfzOR/rOSfrOS/nOTv/JSP/ISf/JS/zLSP/KSfzLSv/JTv7LTP3LTvzNSfzNS/PPVPfOWvfOXPbOXf/GUP/GUv/FVP/GVP/HVvrLVfnNUPrMUv/IUP7KUP/LUf7IVP7JV/3KV/vLXfjNXP/IXv3LXPPSRfDWQ/bRQvbQRPbQRfbQR/bWR/TSSvbVSvHZQ/nQQPnQRPjUSPrWTvzQS/PQUPPRU/DTU/LQVPLTVPXTVffTWOTMaubMa+zFYO/Hb+/KYO/PYu/Ia+DOfOfRbu3TZO7SbvPFZ/bJbPTNbvrKY/jMYfPMcfPTZPLUYvfQZ/TRafbVavLRcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN+7z/YAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABYUlEQVQoUwFWAan+AP8LCgUEAwYIDQYHCQ4MAgH//wBlz8bQdHHIx8sZwNPUzMVtcv8A6ngxeSFBQi4rGhsxMiYlUtAUAOihPJeUXEQvLR8uNyQjJ2PTEADhuKC4t5mTn5+Jj7GvgH2FrBUA4K6CuLijoq2tfqS9vbWep6wYAOSijaadw8qlpZqcurmilcnRDwC8ljuHxFFQyoZUwbOzlV9SbhIAqpEwyVFIV09WSErDw19LSG8SAKuRMGJTV0NOTkZJwsJgS05wEwDjkDuYwU9NX2FMU5uolF9TcxEA44w4kJdfXpKSP5W2to09YtERAL6KNYyQPDyMgY6isK+LO2TODgC7jTQ4ODo2f4GKi4SDiDuUqQ8A181jW0VZMJKWQDkqKCwze9oWAOtmIB0cHil8fZg+XVpYVdLfFwD/db9STGKHtLJ2enciImxn1f8A/9ZqaWhr2dvY5eLp5ufe3dz/ZdGaljRkmtwAAAAASUVORK5CYII='
    the_gui()



# v1

# import GuiAPPs as guiApps
# guiApps.guiDateShow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def guiDateShow():
    import PySimpleGUI as sg
    import sys
    from datetime import datetime
    from datetime import timedelta
    """
        Desktop Widget - Display the date
        Simple display of the date in the format of:
        Day of week      Day    Month     Year
        You can change the format by modifying the function get_date_string
        Copyright 2021 PySimpleGUI
    """

    ALPHA = 0.9  # Initial alpha until user changes
    THEME = 'Dark green 3'  # Initial theme until user changes
    refresh_font = title_font = 'Courier 16'
    main_info_font = sg.user_settings_get_entry('-main info font-', 'Courier 70')

    main_info_size = (12, 1)
    UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour by default until set by user


    def choose_theme(location, size):
        """
        A window to allow new themes to be tried out.
        Changes the theme to the newly chosen one and returns theme's name
        Automaticallyi switches to new theme and saves the setting in user settings file
        :param location: (x,y) location of the Widget's window
        :type location:  Tuple[int, int]
        :param size: Size in pixels of the Widget's window
        :type size: Tuple[int, int]
        :return: The name of the newly selected theme
        :rtype: None | str
        """
        layout = [[sg.Text('Try a theme')],
                  [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
                  [sg.OK(), sg.Cancel()]]

        window = sg.Window('Look and Feel Browser', layout, location=location)
        old_theme = sg.theme()
        while True:  # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
                break
            sg.theme(values['-LIST-'][0])
            window.hide()
            # make at test window to the left of the current one
            test_window = make_window(location=((location[0] - size[0] * 1.2, location[1])), test_window=True)
            test_window.read(close=True)
            window.un_hide()
        window.close()

        # after choice made, save theme or restore the old one
        if event == 'OK' and values['-LIST-']:
            sg.theme(values['-LIST-'][0])
            sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
            return values['-LIST-'][0]
        else:
            sg.theme(old_theme)
        return None


    def make_window(location, test_window=False):
        """
        Defines the layout and creates the window for the main window
        If the parm test_window is True, then a simplified, and EASY to close version is shown
        :param location: (x,y) location to create the window
        :type location: Tuple[int, int]
        :param test_window: If True, then this is a test window & will close by clicking on it
        :type test_window: bool
        :return: newly created window
        :rtype: sg.Window
        """
        #reset settings
        #sg.user_settings_delete_filename()
        #sg.popup('Settings file deleted.  Please restart your program.')
        #
        title = sg.user_settings_get_entry('-title-', '')
        if not test_window:
            theme = sg.user_settings_get_entry('-theme-', THEME)
            sg.theme(theme)
        main_info_font = sg.user_settings_get_entry('-main info font-', 'Courier 60')

        # ------------------- Window Layout -------------------
        initial_text = get_date_string()
        if test_window:
            title_element = sg.Text('Click to close', font=title_font, enable_events=True)
            right_click_menu = [[''], ['Exit', ]]
        else:
            title_element = sg.pin(sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-'))
            right_click_menu = [[''],
                                ['Choose Title', 'Edit Me', 'New Theme', 'Save Location', 'Font', 'Refresh', 'Set Refresh Rate', 'Show Refresh Info', 'Hide Refresh Info', 'Reset',
                                 'Alpha', [str(x) for x in range(1, 11)], 'Exit', ]]


        layout = [[title_element],
                  [sg.Text(initial_text, size=(len(initial_text)+2, 1), font=main_info_font, k='-MAIN INFO-', justification='c', enable_events=test_window)],
                  [sg.pin(
                      sg.Text(size=(15, 2), font=refresh_font, k='-REFRESHED-', justification='c', visible=sg.user_settings_get_entry('-show refresh-', True)))]]

        # ------------------- Window Creation -------------------
        try:
            window = sg.Window(
                               'Desktop Widget Template',
                               layout,
                               location=location,
                               no_titlebar=True, #False
                               grab_anywhere=True,
                               margins=(0, 0),
                               element_justification='c',
                               element_padding=(0, 0),
                               alpha_channel=sg.user_settings_get_entry('-alpha-', ALPHA),
                               finalize=True,
                               right_click_menu=right_click_menu,
                               right_click_menu_tearoff=False
                               )
        except Exception as e:
            if sg.popup_yes_no('Error creating the window', e,
                               'Do you want to delete your settings file to fix?') == 'Yes':
                sg.user_settings_delete_filename()
                sg.popup('Settings file deleted.  Please restart your program.')
                exit()
        return window

    def get_date_string():
        dtime_here = datetime.utcnow() + timedelta(hours=-5)
        return dtime_here.strftime('%a %d %b %Y')


    def main(location):
        """
        Where execution begins
        The Event Loop lives here, but the window creation is done in another function
        This is an important design pattern
        :param location: Location to create the main window if one is not found in the user settings
        :type location: Tuple[int, int]
        """

        window = make_window(sg.user_settings_get_entry('-location-', location))

        refresh_frequency = sg.user_settings_get_entry('-fresh frequency-', UPDATE_FREQUENCY_MILLISECONDS)

        while True:  # Event Loop
            # Normally a window.read goes here, but first we're updating the values in the window, then reading it
            # First update the status information
            window['-MAIN INFO-'].update(get_date_string())
            # for debugging show the last update date time
            if sg.user_settings_get_entry('-title-', 'None') in ('None', 'Hide'):
                window['-TITLE-'].update(visible=False)
            else:
                window['-TITLE-'].update(sg.user_settings_get_entry('-title-', 'None'),visible=True)
            window['-REFRESHED-'].update(datetime.now().strftime("%m/%d/%Y\n%I:%M:%S %p"))

            # -------------- Start of normal event loop --------------
            event, values = window.read(timeout=refresh_frequency)
            print(event, values)
            if event in (sg.WIN_CLOSED, 'Exit'):  # standard exit test... ALWAYS do this
                break
            if event == 'Reset':
                sg.execute_editor(__file__)
                # reset settings
                sg.user_settings_delete_filename()
            if event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Choose Title':
                new_title = sg.popup_get_text('Choose a title for your Widget\nEnter None if you do not want anything displayed', location=window.current_location())
                if new_title is not None:
                    if new_title in ('None', 'Hide'):
                        window['-TITLE-'].update(visible=False)
                    else:
                        window['-TITLE-'].update(new_title, visible=True)
                    sg.user_settings_set_entry('-title-', new_title)
            elif event == 'Show Refresh Info':
                window['-REFRESHED-'].update(visible=True)
                sg.user_settings_set_entry('-show refresh-', True)
            elif event == 'Save Location':
                sg.user_settings_set_entry('-location-', window.current_location())
                sg.popup_notify(f'Saved your current window location:', window.current_location(), title='Saved Location')
            elif event == 'Hide Refresh Info':
                window['-REFRESHED-'].update(visible=False)
                sg.user_settings_set_entry('-show refresh-', False)
            elif event in [str(x) for x in range(1, 11)]:  # if Alpha Channel was chosen
                window.set_alpha(int(event) / 10)
                sg.user_settings_set_entry('-alpha-', int(event) / 10)
            elif event == 'Set Refresh Rate':
                choice = sg.popup_get_text('How frequently to update window in seconds? (can be a float)',
                                           default_text=sg.user_settings_get_entry('-fresh frequency-', UPDATE_FREQUENCY_MILLISECONDS) / 1000,
                                           location=window.current_location())
                if choice is not None:
                    try:
                        refresh_frequency = float(choice) * 1000  # convert to milliseconds
                        sg.user_settings_set_entry('-fresh frequency-', float(refresh_frequency))
                    except Exception as e:
                        sg.popup_error(f'You entered an incorrect number of seconds: {choice}', f'Error: {e}', location=window.current_location())
            elif event == 'New Theme':
                loc = window.current_location()
                if choose_theme(window.current_location(), window.size) is not None:
                    window.close()  # out with the old...
                    window = make_window(loc)  # in with the new
            elif event == 'Font':
                font = sg.popup_get_text('Enter font string using PySimpleGUI font format (e.g. courier 70 or courier 70 bold)', default_text=sg.user_settings_get_entry('-main info font-'), keep_on_top=True)
                if font:
                    sg.user_settings_set_entry('-main info font-', font)
                    loc = window.current_location()
                    _, window = window.close(), make_window(loc)
        window.close()


    #if __name__ == '__main__':
    # To start the window at a specific location, get this location on the command line
    # The location should be in form x,y with no spaces
    location = (None, None)  # assume no location provided
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    main(location)


# v1

# import GuiAPPs as guiApps
# a.GuiDirectoryOfFILESshow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def GuiDirectoryOfFILESshow():
    import PySimpleGUI as sg
    import os.path

    # --------------------------------- Define Layout ---------------------------------

    # First the window layout...2 columns

    left_col = [[sg.Text('Images Folder'), sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
                [sg.Listbox(values=[], enable_events=True, size=(40, 20), key='-FILE LIST-')]]

    # For now will only show the name of the file that was chosen
    images_col = [[sg.Text('You choose from the list:')],
                  [sg.Text(size=(40, 3), key='-TOUT-')],
                  [sg.Image(key='-IMAGE-')]]

    # ----- Full layout -----
    layout = [[sg.Column(left_col), sg.VSeperator(), sg.Column(images_col)]]

    # --------------------------------- Create Window ---------------------------------
    window = sg.Window('Gui Directory of Files - Viewer', layout)

    # ----- Run the Event Loop -----
    # --------------------------------- Event Loop ---------------------------------
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == '-FOLDER-':  # Folder name was filled in, make a list of files in the folder
            folder = values['-FOLDER-']
            try:
                file_list = os.listdir(folder)  # get list of files in folder
            except:
                file_list = []

            fnames = [f for f in file_list if os.path.isfile(
                os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
            window['-FILE LIST-'].update(fnames)
        elif event == '-FILE LIST-':  # A file was chosen from the listbox
            try:
                filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
                window['-TOUT-'].update(filename)
                window['-IMAGE-'].update(filename=filename)

            except:
                pass  # something weird happened making the full filename

    # --------------------------------- Close & Exit ---------------------------------

    window.close()


# v1

# import GuiAPPs as guiApps
# guiApps.guiPhotoGalleryShow() # "z-IMAGES_1\0.cool\"

# if you click on the image - you see it bigger in it's own window

# ROOT_FOLDER = r'C:\Users\myvor\PycharmProjects\pythonProject\
# z-IMAGES_1\0.cool\beautiful wallpapers 1'  # r'c:\your\images'

def guiPhotoGalleryShow(folder_name="last_folder_thing_name"):
    import PySimpleGUI as sg
    import PIL
    from PIL import Image
    import io
    import base64
    import os

    """
        Using PIL with PySimpleGUI 
        This image viewer uses both a thumbnail creation function and an image resizing function that
        you may find handy to include in your code.
        Copyright 2020 PySimpleGUI.org
    """

    THUMBNAIL_SIZE = (200, 200)
    IMAGE_SIZE = (800, 800)
    THUMBNAIL_PAD = (1, 1)
    root_top_folder = "z-IMAGES_1\\0.cool"
    folder_name = "beautiful wallpapers mountains sunset"
    ROOT_FOLDER = r"C:\Users\myvor\PycharmProjects\pythonProject"+"\\"+root_top_folder+"\\"+folder_name+"\\"  # r'c:\your\images'
    #print("ROOT_FOLDER")
    #print(ROOT_FOLDER)
    screen_size = sg.Window.get_screen_size()
    thumbs_per_row = int(screen_size[0] / (THUMBNAIL_SIZE[0] + THUMBNAIL_PAD[0])) - 1
    thumbs_rows = int(screen_size[1] / (THUMBNAIL_SIZE[1] + THUMBNAIL_PAD[1])) - 1
    THUMBNAILS_PER_PAGE = (thumbs_per_row, thumbs_rows)

    def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
        x, y = im.size
        size = max(min_size, x, y)
        new_im = Image.new('RGBA', (size, size), fill_color)
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        return new_im

    def convert_to_bytes(file_or_bytes, resize=None, fill=False):
        '''
        Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
        Turns into  PNG format in the process so that can be displayed by tkinter
        :param file_or_bytes: either a string filename or a bytes base64 image object
        :type file_or_bytes:  (Union[str, bytes])
        :param resize:  optional new size
        :type resize: (Tuple[int, int] or None)
        :return: (bytes) a byte-string object
        :rtype: (bytes)
        '''
        if isinstance(file_or_bytes, str):
            img = PIL.Image.open(file_or_bytes)
        else:
            try:
                img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
            except Exception as e:
                dataBytesIO = io.BytesIO(file_or_bytes)
                img = PIL.Image.open(dataBytesIO)

        cur_width, cur_height = img.size
        if resize:
            new_width, new_height = resize
            scale = min(new_height / cur_height, new_width / cur_width)
            img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
        if fill:
            img = make_square(img, THUMBNAIL_SIZE[0])
        with io.BytesIO() as bio:
            img.save(bio, format="PNG")
            del img
            return bio.getvalue()

    def display_image_window(filename):
        try:
            layout = [[sg.Image(data=convert_to_bytes(filename, IMAGE_SIZE), enable_events=True)]]
            e, v = sg.Window(filename, layout, modal=True, element_padding=(0, 0), margins=(0, 0)).read(close=True)
        except Exception as e:
            print(f'** Display image error **', e)
            return

    def make_thumbnails(flist):
        layout = [[]]
        for row in range(THUMBNAILS_PER_PAGE[1]):
            row_layout = []
            for col in range(THUMBNAILS_PER_PAGE[0]):
                try:
                    f = flist[row * THUMBNAILS_PER_PAGE[1] + col]
                    # row_layout.append(sg.B(image_data=convert_to_bytes(f, THUMBNAIL_SIZE), k=(row,col), pad=THUMBNAIL_PAD))
                    row_layout.append(sg.B('', k=(row, col), size=(0, 0), pad=THUMBNAIL_PAD, ))
                except:
                    pass
            layout += [row_layout]
        layout += [[sg.B(sg.SYMBOL_LEFT + ' Prev', size=(10, 3), k='-PREV-'),
                    sg.B('Next ' + sg.SYMBOL_RIGHT, size=(10, 3), k='-NEXT-'), sg.B('Exit', size=(10, 3)),
                    sg.Slider((0, 100), orientation='h', size=(50, 15), enable_events=True, key='-SLIDER-')]]
        return sg.Window('Thumbnails', layout, element_padding=(0, 0), margins=(0, 0), finalize=True,
                         grab_anywhere=False, location=(0, 0), return_keyboard_events=True)

    EXTS = ('png', 'jpg', 'gif')

    def display_images(t_win, offset, files):
        currently_displaying = {}
        row = col = 0
        while True:
            if offset + 1 > len(files) or row == THUMBNAILS_PER_PAGE[1]:
                break
            f = files[offset]
            currently_displaying[(row, col)] = f
            try:
                t_win[(row, col)].update(image_data=convert_to_bytes(f, THUMBNAIL_SIZE, True))
            except Exception as e:
                print(f'Error on file: {f}', e)
            col = (col + 1) % THUMBNAILS_PER_PAGE[0]
            if col == 0:
                row += 1

            offset += 1
        if not (row == 0 and col == 0):
            while row != THUMBNAILS_PER_PAGE[1]:
                t_win[(row, col)].update(image_data=sg.DEFAULT_BASE64_ICON)
                currently_displaying[(row, col)] = None
                col = (col + 1) % THUMBNAILS_PER_PAGE[0]
                if col == 0:
                    row += 1

        return offset, currently_displaying

    def main():
        files = [os.path.join(ROOT_FOLDER, f) for f in os.listdir(ROOT_FOLDER) if True in [f.endswith(e) for e in EXTS]]
        files.sort()
        t_win = make_thumbnails(files)
        offset, currently_displaying = display_images(t_win, 0, files)
        # offset = THUMBNAILS_PER_PAGE[0] * THUMBNAILS_PER_PAGE[1]
        # currently_displaying = {}
        while True:
            win, event, values = sg.read_all_windows()
            print(event, values)
            if win == sg.WIN_CLOSED:  # if all windows are closed
                break

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if isinstance(event, tuple):
                display_image_window(currently_displaying.get(event))
                continue
            elif event == '-SLIDER-':
                offset = int(values['-SLIDER-'] * len(files) / 100)
                event = '-NEXT-'
            else:
                t_win['-SLIDER-'].update(offset * 100 / len(files))

            if event == '-NEXT-' or event.endswith('Down'):
                offset, currently_displaying = display_images(t_win, offset, files)
            elif event == '-PREV-' or event.endswith('Up'):
                offset -= THUMBNAILS_PER_PAGE[0] * THUMBNAILS_PER_PAGE[1] * 2
                if offset < 0:
                    offset = 0
                offset, currently_displaying = display_images(t_win, offset, files)

    #if __name__ == '__main__':
    main()



# v1

# import GuiAPPs as guiApps
# guiApps.HTMLlikeDesignShow()

# it's not hooked up to real data - it's just a layout
# cool green style

def HTMLlikeDesignShow():
    import PySimpleGUI as sg

    """
        Demo - Resizable Dashboard using Frames

        This Demo Program looks similar to the one based on the Column Element.
        This version has a big difference in how it was implemented and the fact that it can be resized.

        It's a good example of how PySimpleGUI evolves, continuously.  When the original Column-based demo
            was written, none of these techniques such as expansion, were easily programmed.

        Dashboard using blocks of information.

        Copyright 2021 PySimpleGUI.org
    """

    theme_dict = {'BACKGROUND': '#2B475D',
                  'TEXT': '#FFFFFF',
                  'INPUT': '#F2EFE8',
                  'TEXT_INPUT': '#000000',
                  'SCROLL': '#F2EFE8',
                  'BUTTON': ('#000000', '#C2D4D8'),
                  'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                  'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

    sg.theme_add_new('Dashboard', theme_dict)
    sg.theme('Dashboard')

    BORDER_COLOR = '#C7D5E0'
    DARK_HEADER_COLOR = '#1B2838'
    BPAD_TOP = ((20, 20), (20, 10))
    BPAD_LEFT = ((20, 10), (0, 0))
    BPAD_LEFT_INSIDE = (0, (10, 0))
    BPAD_RIGHT = ((10, 20), (10, 0))

    top_banner = [
        [sg.Text('Dashboard', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False),
         sg.Push(background_color=DARK_HEADER_COLOR),
         sg.Text('Wednesday 27 Oct 2021', font='Any 20', background_color=DARK_HEADER_COLOR)],
    ]

    top = [[sg.Push(), sg.Text('Weather Could Go Here', font='Any 20'), sg.Push()],
           [sg.T('This Frame has a relief while the others do not')],
           [sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]

    block_3 = [[sg.Text('Block 3', font='Any 20')],
               [sg.Input(), sg.Text('Some Text')],
               [sg.T('This frame has element_justification="c"')],
               [sg.Button('Go'), sg.Button('Exit')]]

    block_2 = [[sg.Text('Block 2', font='Any 20')],
               [sg.T('This is some random text')],
               [sg.Image(data=sg.DEFAULT_BASE64_ICON, enable_events=True)]]

    block_4 = [[sg.Text('Block 4', font='Any 20')],
               [sg.T('You can move the window by grabbing this block (and the top banner)')],
               [sg.T('This block is a Column Element')],
               [sg.T('The others are all frames')],
               [sg.T('The Frame Element, with a border_width=0\n    and no title is just like a Column')],
               [sg.T('Frames that have a fixed size \n    handle element_justification better than Columns')]]

    layout = [
        [sg.Frame('', top_banner, pad=(0, 0), background_color=DARK_HEADER_COLOR, expand_x=True, border_width=0,
                  grab=True)],
        [sg.Frame('', top, size=(920, 100), pad=BPAD_TOP, expand_x=True, relief=sg.RELIEF_GROOVE, border_width=3)],
        [sg.Frame('', [[sg.Frame('', block_2, size=(450, 150), pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True,
                                 expand_y=True, )],
                       [sg.Frame('', block_3, size=(450, 150), pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True,
                                 expand_y=True, element_justification='c')]],
                  pad=BPAD_LEFT, background_color=BORDER_COLOR, border_width=0, expand_x=True, expand_y=True),
         sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT, expand_x=True, expand_y=True, grab=True), ],
        [sg.Sizegrip(background_color=BORDER_COLOR)]]

    window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,
                       no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
        elif event == 'File Location':
            sg.popup_scrolled('This Python file is:', __file__)
    window.close()


# v1

# import GuiAPPs as guiApps
# guiApps.GuiMACLauncherShow()

def GuiMACLauncherShow():
    import PySimpleGUI as sg

    """
        Demo Launcher Bar

        A 2021 version of a PySimpleGUI based launcher.
        Once making the GUI leap, it's hard to go back.... at least for some people.
        This tool will perhaps help make for a more GUI-like environment for your Python activities


        Copyright 2021 PySimpleGUI
    """

    excel_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAACXBIWXMAAAsSAAALEgHS3X78AAAFB0lEQVRIx51We0xTZxQ/X3t5lZY+QLwgLYgg4MSJOAQCOgED23SgMjedr2mY2UQhwblHNpK5xCxTM+Nkf+Dc2NTMZJCpEF3YsqU6y5ZsGpextSD0AcKlBeVR+rrt/fbHhcv1tlTGSdN8j3O/33mfgxiGAR4hhDDG7D/MTgghAGA5+efcCbdAAgA+jGDLYDzuspuGByZck7JwSZYmw/9dARgAEEHE9Hhp08iAftBooEx6ytg1ZB4YtblpDwCsVKe11ZzlC8sJxNmA3c4A0D7vg0fWbqtZP2gyUCYDZTIO97tozyw2mhGce4t9mv86QggxDNOobW69p+219U+4HQEt5k8xMsXGFWv9zzEGDBghFCImSjJyC1KzCISQrufeXYse/g+FikNTYjVBGMac9vorDb8cPU8Ej5ZZNZAqXiuo4Ftf4I/BMds3utYnODkIDYxa6680AEBRek5GfHLDz5fxtGvyU1aWPpUPABgwxnieAMP20fO3vgcAZaSclMd8+esVzhKEWMwCIEDz10ASGp5GJgEAGRUdERqWpU7HMAWwSBE7HUKAECL8U0ytIqVhEqOt30m7AWBLdkmiitR2/XnH/C/HlhKraT38Gbe9dviMf54DIIwxIchABKhxd31mQurbzacvdrQlL0g4ta3O46MvdLTx2fSUMf/4LkBQtbZyXVr2rnPvcRrsWPP8oeIdAAgBIIREgihiMNOobcYYb88pA4CdeRtDiZCLHW3D9lFBklseUpYRasw5QXu97Jr9PXKMY4wBMCAI7OTWv7R1pXsyE5ZmJy17afUGu8vRqG0R8JDy6N15LwJA7pIVMTLlW2V7AYDVYVViOj+TAwDQXu8Xt1o+qqj+eGuNUhJ17mbL0PiIgCcqQlq6PJ9NaVmYhA0bllSRcn49CRxFzX/8VFuyMyMu2eFxNd5s9mfooszFJ6sA4EjpnucyC0pOvc6Z+sC6yg82HeAKqmiWcg8+zCCExCJROBH2xMYgqIOPmSgAB8Ce/PKFUdF3zP9kaTLeWL/t6HefChiWkomf73wfAC+QKmXhkT/WNcKUE5AqMoorfQAQQAN5hLRq7ZZJt7P28gmnx7U1uyQxOk7AM+6cbO/UtXd29Nj67W5He6eO3bZ36rqGzFOKYAjsg32Fm6Oliku/Xe+x9l27p335mdKDRa8IlKDGhj+58RUAHCnbK5dIT/zQNOODZysLU1cBYBzQBwqJbH/BZi/j+1p3FQCabl/1MUzl6g1qFflYuSZC1CpSrSLlEZEhIkKtWshu1SpSESHjcwo1cNGe8rM1YpGoe8gCAH8/uP9Oy+lFytikmPi+hxTHlk4uvl7bwG11716YLQT8Adw91j5+4/729xv+X963WjadOQQAr+a9kL/k6epLx7mCsHlV0f7CLTMazK/hODwutgkWL8t10u67FgP3Ts7i5Xz5AofpXDpaedZ6AMjSpCklUfsKKrirNcmZ/Flmnv0gXhH7YfmbXKIdqzjoNx1NddB5AozYR5tuXw3e9OUS6VQURYSEiUUi39wGFpbcPrrH1j+TsXhqUoLp1kyIiGPlBxE7AdA+78CotXvIwk5wBsrUa+t3etxBAASTnWCg4wcOgTEOERMaVZxGFVeyLJe9o31e88iggTLqB416ytQ1ZH7wyOqi3YLJzn9uFIBhjINN0ZxEDGYmnJPGkQH9YK+BMjs8TrWSrC7ePhdjBgYPuAgyu8/I63f1H5J3l/PVeWn1AAAAAElFTkSuQmCC'

    # This is your master table.... keys are what will be shown on the bar.  The item is what you want to happen.
    launcher_buttons1 = {sg.SYMBOL_DOWN_ARROWHEAD: None,
                         'PSG Main': sg.main,
                         'Word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                         excel_icon: r"C:\Program Files\Microsoft Office\root\Office16\excel.EXE",
                         'Notepad++': r"C:\Program Files\NotePad++\notepad++.exe",
                         sg.EMOJI_BASE64_PONDER: sg.main_sdk_help,
                         sg.EMOJI_BASE64_HAPPY_IDEA: r'C:\Python\PycharmProjects\PSG\DemoPrograms\Demo_Desktop_Widget_Postit.py',
                         'All Elements': r'C:\Python\PycharmProjects\PSG\DemoPrograms\Demo_All_Elements.py',
                         'Exit': None}

    launcher_buttons2 = {sg.SYMBOL_DOWN_ARROWHEAD: None,
                         'PSG Main': sg.main,
                         'Exit': None}

    panel_rows = (launcher_buttons1, launcher_buttons2)
    col_panel_list = []
    num_panels = len(panel_rows)
    MINIMIZED_IMAGE = sg.EMOJI_BASE64_HAPPY_THUMBS_UP

    DEFAULT_SCREEN_BACKGROUND_COLOR = 'black'
    DEFAULT_BUTTON_SIZE = (None, None)

    def settings(window: sg.Window):
        layout = [[sg.T(f'Screen size = {sg.Window.get_screen_size()}')],
                  [sg.T(f'Your launcher is currently located at {window.current_location()}')],
                  [sg.T('Enable autosave and position your window where you want it to appear next time you run.')],
                  [sg.T('Your Screen Background Color'),
                   sg.In(sg.user_settings_get_entry('-screen color-', DEFAULT_SCREEN_BACKGROUND_COLOR), s=15,
                         k='-SCREEN COLOR-')],
                  [sg.CBox('Autosave Location on Exit',
                           default=sg.user_settings_get_entry('-auto save location-', True), k='-AUTO SAVE LOCATION-')],
                  [sg.CBox('Keep launcher on top', default=sg.user_settings_get_entry('-keep on top-', True),
                           k='-KEEP ON TOP-')],
                  [sg.CBox('Reroute STDOUT to Debug Window',
                           default=sg.user_settings_get_entry('-reroute stdout-', True), k='-REROUTE STDOUT-')],
                  [sg.OK(), sg.Cancel()]]
        event, values = sg.Window('Settings', layout).read(close=True)
        if event == 'OK':
            sg.user_settings_set_entry('-auto save location-', values['-AUTO SAVE LOCATION-'])
            sg.user_settings_set_entry('-keep on top-', values['-KEEP ON TOP-'])
            sg.user_settings_set_entry('-screen color-', values['-SCREEN COLOR-'])
            sg.user_settings_set_entry('-reroute stdout-', values['-REROUTE STDOUT-'])
            if values['-KEEP ON TOP-']:
                window.keep_on_top_set()
            else:
                window.keep_on_top_clear()

    def ToolButton(item, background, tip):
        if isinstance(item, bytes):
            button = sg.Button(image_data=item, key=item, metadata=launcher_buttons1[item], button_color=background,
                               tooltip=tip, border_width=0,
                               pad=1)
        else:
            button = sg.Button(item, key=item, metadata=launcher_buttons1[item], tooltip=tip, border_width=0, pad=1)
        return button

    def make_window():
        global col_panel_list
        screen_background_color = sg.user_settings_get_entry('-screen color-', None)
        old_bg = sg.theme_background_color()
        sg.set_options(border_width=0, background_color=screen_background_color)
        sg.theme_background_color(screen_background_color)
        col_panel_list = []
        for count, launcher_buttons in enumerate(panel_rows):
            button_row = []
            for item in launcher_buttons.keys():
                tip = 'Grab anywhere to move the launcher\nClick an item to launch something\nRight Click to get to settings'
                button = ToolButton(item, screen_background_color, tip)
                button_row.append(button)
            col_panel_list.append(button_row)

        col_up_down = sg.Col([[sg.B(sg.SYMBOL_UP, button_color=screen_background_color)],
                              [sg.B(sg.SYMBOL_DOWN, button_color=screen_background_color)]], p=0, k='-COL UP DOWN-')
        col_buttons = sg.Column([col_panel_list[0], ], p=0, k='-BUTTON COL-', visible=True)
        col_buttons2 = sg.Column([col_panel_list[1], ], p=0, k='-BUTTON COL2-', visible=False, )
        col_minimized = sg.Column([[sg.Button(image_data=MINIMIZED_IMAGE, k='-MINIMIZED IMAGE-',
                                              button_color=screen_background_color, border_width=0)]], visible=False,
                                  k='-MINIMIZED COL-')
        col_panel_list = [col_buttons, col_buttons2, col_up_down]
        layout = [[sg.pin(col_minimized), sg.pin(col_up_down), sg.pin(col_buttons), sg.pin(col_buttons2), ]]

        screen_size = sg.Window.get_screen_size()
        location = screen_size[0] // 2, screen_size[
            1] - 200  # set a default location centered and near the bottom of the screen
        location = sg.user_settings_get_entry('-window location-', location)
        keep_on_top = sg.user_settings_get_entry('-keep on top-', True)

        window = sg.Window('Window Title', layout, location=location,
                           keep_on_top=keep_on_top, no_titlebar=True, grab_anywhere=True,
                           background_color=screen_background_color,
                           auto_size_buttons=True, default_button_element_size=DEFAULT_BUTTON_SIZE,
                           right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT,
                           enable_close_attempted_event=True, use_default_focus=False,
                           transparent_color=screen_background_color)
        sg.theme_background_color(old_bg)

        return window, col_panel_list

    def main():
        if sg.user_settings_get_entry('-reroute stdout-', False):
            mprint = sg.Print
        else:
            mprint = print
        window, col_panel_list = make_window()
        cur_panel = col_panel_list[0]
        count = 0
        while True:
            event, values = window.read(timeout=1000)  # Not needed but handy while debugging
            if event != sg.TIMEOUT_EVENT:
                mprint(event, values)
            else:
                continue
            if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED) or str(event).startswith('Exit'):
                if event != sg.WIN_CLOSED:
                    if sg.user_settings_get_entry('-auto save location-', True):
                        mprint('saving location', window.current_location())
                        sg.user_settings_set_entry('-window location-', window.current_location())
                break
            try:
                elem = window.find_element(event, silent_on_error=True)
                if elem:
                    action = elem.metadata
            except:
                action = None
            if action is not None:
                if isinstance(action, str):
                    if action.endswith(('.py', '.pyw')):
                        sg.execute_py_file(action)
                    else:
                        sg.execute_command_subprocess(action)
                elif callable(action):
                    action()
            event = str(event)
            if event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(sg.get_versions())
            elif event == 'Settings':
                settings(window)
                window.close()
                window, col_panel_list = make_window()
                if sg.user_settings_get_entry('-reroute stdout-', False):
                    mprint = sg.Print
                else:
                    mprint = print
            elif event.startswith(sg.SYMBOL_DOWN_ARROWHEAD):
                window['-BUTTON COL-'].update(visible=False)
                window['-BUTTON COL2-'].update(visible=False)
                window['-BUTTON COL2-'].update(visible=False)
                window['-COL UP DOWN-'].update(visible=False)
                window['-MINIMIZED COL-'].update(visible=True)
                cur_panel = col_panel_list[count]
            elif event == '-MINIMIZED IMAGE-':
                cur_panel.update(visible=True)
                window['-MINIMIZED COL-'].update(visible=False)
                window['-COL UP DOWN-'].update(visible=True)
            elif event.startswith(sg.SYMBOL_UP):
                cur_panel = col_panel_list[count]
                cur_panel.update(visible=False)
                count = (count + (num_panels - 1)) % num_panels  # Decrement - roll over to MAX from 0
                cur_panel = col_panel_list[count]
                cur_panel.update(visible=True)
            elif event == sg.SYMBOL_DOWN:
                cur_panel = col_panel_list[count]
                cur_panel.update(visible=False)
                count = (count + 1) % num_panels  # Increment to MAX then roll over to 0
                cur_panel = col_panel_list[count]
                cur_panel.update(visible=True)
        window.close()

    #if __name__ == '__main__':
    main()




# v1

# import GuiAPPs as guiApps
# guiApps.GuiSplashSCREENshow()

# you can change settings - with the right click menu
# you can save the location for next time you open it

def GuiSplashSCREENshow():
    import PySimpleGUI as sg

    """
        Demo - Splash Screen

        Displays a PNG image with transparent areas as see-through on the center
        of the screen for a set amount of time.

        Copyright 2020 PySimpleGUI.org
    """

    image = b'iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAACXBIWXMAABcRAAAXEQHKJvM/AAAgAElEQVR4nOzdd3gUVdsG8Hu2pfdCCJCA0qQIiIj0pqJ0EBRUioq919eGouBnQ8XepQsCoih2SkBa6L0TQgrpvW+Z+f6gZZOd3dnsbtrcP6693peZs+c8s8hy58ycGUGSJBARERGRemjqugAiIiIiql0MgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDK6ui6AiOjUudzA5KyCdhsPJnUC0PnI2azmJ1Nz/C/slnq2b5YbFRpwMjYy6EC3K6P2XRUTnuSl14l1WbOsirO+sBTGwJjUBKUHIi5sNSJoaDoEfQYMzVOhCzHXaY1EpHqCJEl1XQMRqVBuUZnvr9uO9/5r16lJZzMLBpUbzc0AGJS8tVlYwL6+nWK+v++Wa34NC/Qt8nStDlmKdchbfR0KN05GxZnBEMuiAfgBECq3AlAAXVg6dKGbEHTDXwgeGgdtSCEELb+IiahWMQASUa3KyCv2Wxp3aNrK/448VFJu6uhKX77e+hPj+3Z4a9KgTgujQvzrZkYwa35v5Cx/CZbCW+D8ZTXn4NvlZwT2+w4hY/ZB480vZCKqFQyARFQryipMhs/X7Bq1avPR2aUVprawnh1zhdgiIvC3h0f2eOLma1ufdVOfjplzfHH2uZdQfvIpQPJ1sbdy6MLXIWLqXAQNiYM2kKeIicijGACJyOOOJWc3eWne+o/OpOfdCg9de6zTao7PuKP/baN6tTvgif6tlO4PQdrc71B+cqybezZB33QNQse+hvBJB92XkYmIrDEAEpFHffxL/PB5/+z7HEBMLQyX8+pdA0aN7d1+q8dGKNwYieRX/gCk7h4bAzDDt+sXiLz7Lfh1T/PgOESkUgyAROQROYVlPv/77t+n95xKe1mS4FNb4+p12nMv3N7ntnF9rtri9s4LNzRF6uwVECv6uL1vWwTtGYSMeRVNHlgOja+xVsYk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IAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqMz/B7LJu0uHjbFxAAAAAElFTkSuQmCC'

    FILENAME = r'yourfile.png'  # if you want to use a file instead of data, then use this in Image Element
    DISPLAY_TIME_MILLISECONDS = 4000

    sg.Window('Window Title', [[sg.Image(data=image)]], transparent_color=sg.theme_background_color(), no_titlebar=True,
              keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)



# v1

# import GuiAPPs as guiApps
# guiApps.GuiTIMERshow()

def GuiTIMERshow():
    import PySimpleGUI as sg
    # ----------- Window's Layout -----------
    layout = [[sg.Column([[sg.Text(size=(4, 1), justification='center', font='Courier 20', key='-OUT-')],
                          [sg.Input(size=(4, 1), key='-IN-')],
                          [sg.Button('Set')],
                          [sg.Button('Start')]], element_justification='center')]]
    # ----------- Create Window -----------
    window = sg.Window('Countdown Timer', layout, auto_size_buttons=False)
    # ----------- Event Loop -----------
    amount = 0
    while True:
        event, values = window.read(timeout=1000 if amount else None)
        if event is None:
            break
        elif event == 'Set':
            window['-OUT-'].update(values['-IN-'])
        elif event == 'Start':
            amount = int(values['-IN-'])
        if amount:
            amount -= 1
            window['-OUT-'].update(amount)
    # ----------- Exiting - close window -----------
    window.close()



# v1

# import GuiAPPs as guiApps
# guiApps.GuiWEATHERshow()

# it's not hooked up to real data - it's just a layout
# cool green style

def GuiWEATHERshow():
    import PySimpleGUI as sg
    import datetime
    import base64
    from urllib import request
    import json
    import sys
    import webbrowser

    """
        A Current Weather Widget
        Adapted from the weather widget originally created and published by Israel Dryer that you'll find here:
        https://github.com/israel-dryer/Weather-App
        BIG THANKS goes out for creating a good starting point for other widgets to be build from.
        A true "Template" is being developed that is a little more abstracted to make creating your own
        widgets easy.  Things like the settings window is being standardized, the settings file format too.
        You will need a key (APPID) from OpenWeathermap.org in order to run this widget. It's free, it's easy:
        https://home.openweathermap.org/
        Your initial location is determined using your IP address and will be used if no settings file is found
        This widget is an early version of a PSG Widget so it may not share the same names / constructs as the templates. 
        Copyright 2020 PySimpleGUI - www.PySimpleGUI.com
    """

    SETTINGS_PATH = None  # use the default settings path (OS settings foloder)

    API_KEY = '95fbd4757a377fbc9b245a0edfd502cd'  # Set using the "Settings" window and saved in your config file

    sg.theme('Light Green 6')
    ALPHA = 0.8

    BG_COLOR = sg.theme_text_color()
    TXT_COLOR = sg.theme_background_color()

    APP_DATA = {
        'City': 'New York',
        'Country': 'US',
        'Postal': 10001,
        'Description': 'clear skys',
        'Temp': 101.0,
        'Feels Like': 72.0,
        'Wind': 0.0,
        'Humidity': 0,
        'Precip 1hr': 0.0,
        'Pressure': 0,
        'Updated': 'Not yet updated',
        'Icon': None,
        'Units': 'Imperial'
    }

    def load_settings():
        global API_KEY
        settings = sg.UserSettings(path=SETTINGS_PATH)
        API_KEY = settings['-api key-']
        if not API_KEY:
            sg.popup_quick_message('No valid API key found... opening setup window...', keep_on_top=True,
                                   background_color='red', text_color='white', auto_close_duration=3,
                                   non_blocking=False, location=win_location)
            change_settings(settings)
        return settings

    def change_settings(settings, window_location=(None, None)):
        global APP_DATA, API_KEY

        try:
            nearest_postal = json.loads(request.urlopen('http://ipapi.co/json').read())['postal']
        except Exception as e:
            print('Error getting nearest postal', e)
            nearest_postal = ''

        layout = [[sg.T('Enter Zipcode or City for your location')],
                  [sg.I(settings.get('-location-', nearest_postal), size=(15, 1), key='-LOCATION-')],
                  [sg.I(settings.get('-api key-', ''), size=(32, 1), key='-API KEY-')],
                  [sg.B('Ok', border_width=0, bind_return_key=True),
                   sg.B('Register For a Key', border_width=0, k='-REGISTER-'), sg.B('Cancel', border_width=0)], ]

        window = sg.Window('Settings', layout, location=window_location, no_titlebar=True, keep_on_top=True,
                           border_depth=0)
        event, values = window.read()
        window.close()

        if event == '-REGISTER-':
            sg.popup(
                'Launching browser so you can signup for the "Current Weather" service from OpenWeatherMap.org to get a Free API Key',
                'Click OK and your browser will open', r'Visit https://home.openweathermap.org/ for more information',
                location=window_location)
            # Register to get a free key
            webbrowser.open(r'https://home.openweathermap.org/users/sign_up')

        if event == 'Ok':
            user_location = settings['-location-'] = values['-LOCATION-']
            API_KEY = settings['-api key-'] = values['-API KEY-']
        else:
            API_KEY = settings['-api key-']
            user_location = settings['-location-']

        if user_location is not None:
            if user_location.isnumeric() and len(user_location) == 5 and user_location is not None:
                APP_DATA['Postal'] = user_location
                APP_DATA['City'] = ''
            else:
                APP_DATA['City'] = user_location
                APP_DATA['Postal'] = ''

        return settings

    def update_weather():
        if APP_DATA['City']:
            request_weather_data(create_endpoint(2))
        elif APP_DATA['Postal']:
            request_weather_data(create_endpoint(1))

    def create_endpoint(endpoint_type=0):
        """ Create the api request endpoint
        {0: default, 1: zipcode, 2: city_name}"""
        if endpoint_type == 1:
            try:
                endpoint = f"http://api.openweathermap.org/data/2.5/weather?zip={APP_DATA['Postal']},us&appid={API_KEY}&units={APP_DATA['Units']}"
                return endpoint
            except ConnectionError:
                return
        elif endpoint_type == 2:
            try:
                endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={APP_DATA['City'].replace(' ', '%20')},us&APPID={API_KEY}&units={APP_DATA['Units']}"
                return endpoint
            except ConnectionError:
                return
        else:
            return

    def request_weather_data(endpoint):
        """ Send request for updated weather data """
        global APP_DATA

        if endpoint is None:
            sg.popup_error('Could not connect to api.  endpoint is None', keep_on_top=True, location=win_location)
            return
        else:
            try:
                response = request.urlopen(endpoint)
            except request.HTTPError:
                sg.popup_error('ERROR Obtaining Weather Data',
                               'Is your API Key set correctly?',
                               API_KEY, keep_on_top=True, location=win_location)
                return

        if response.reason == 'OK':
            weather = json.loads(response.read())
            APP_DATA['City'] = weather['name'].title()
            APP_DATA['Description'] = weather['weather'][0]['description']
            APP_DATA['Temp'] = "{:,.0f}??F".format(weather['main']['temp'])
            APP_DATA['Humidity'] = "{:,d}%".format(weather['main']['humidity'])
            APP_DATA['Pressure'] = "{:,d} hPa".format(weather['main']['pressure'])
            APP_DATA['Feels Like'] = "{:,.0f}??F".format(weather['main']['feels_like'])
            APP_DATA['Wind'] = "{:,.1f} m/h".format(weather['wind']['speed'])
            APP_DATA['Precip 1hr'] = None if not weather.get('rain') else "{:2} mm".format(weather['rain']['1h'])
            APP_DATA['Updated'] = 'Updated: ' + datetime.datetime.now().strftime("%B %d %I:%M:%S %p")
            APP_DATA['Lon'] = weather['coord']['lon']
            APP_DATA['Lat'] = weather['coord']['lat']

            icon_url = "http://openweathermap.org/img/wn/{}@2x.png".format(weather['weather'][0]['icon'])
            APP_DATA['Icon'] = base64.b64encode(request.urlopen(icon_url).read())

    def metric_row(metric):
        """ Return a pair of labels for each metric """
        return [sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1)),
                sg.Text(APP_DATA[metric], font=('Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)]

    def create_window(win_location):
        """ Create the application window """
        col1 = sg.Column(
            [[sg.Text(APP_DATA['City'], font=('Arial Rounded MT Bold', 18), pad=((10, 0), (50, 0)), size=(18, 1),
                      background_color=BG_COLOR, text_color=TXT_COLOR, key='City')],
             [sg.Text(APP_DATA['Description'], font=('Arial', 12), pad=(10, 0), background_color=BG_COLOR,
                      text_color=TXT_COLOR, key='Description')]],
            background_color=BG_COLOR, key='COL1')

        col2 = sg.Column(
            [[sg.Text('??', font=('Arial Black', 16), pad=(0, 0), justification='right', background_color=BG_COLOR,
                      text_color=TXT_COLOR, enable_events=True, key='-QUIT-')],
             [sg.Image(data=APP_DATA['Icon'], pad=((5, 10), (0, 0)), size=(100, 100), background_color=BG_COLOR,
                       key='Icon')]],
            element_justification='center', background_color=BG_COLOR, key='COL2')

        col3 = sg.Column(
            [[sg.Text(APP_DATA['Updated'], font=('Arial', 8), background_color=BG_COLOR, text_color=TXT_COLOR,
                      key='Updated')]],
            pad=(10, 5), element_justification='left', background_color=BG_COLOR, key='COL3')

        col4 = sg.Column(
            [[sg.Text('Settings', font=('Arial', 8, 'italic'), background_color=BG_COLOR, text_color=TXT_COLOR,
                      enable_events=True, key='-CHANGE-'),
              sg.Text('Refresh', font=('Arial', 8, 'italic'), background_color=BG_COLOR, text_color=TXT_COLOR,
                      enable_events=True, key='-REFRESH-')]],
            pad=(10, 5), element_justification='right', background_color=BG_COLOR, key='COL4')

        top_col = sg.Column([[col1, col2]], pad=(0, 0), background_color=BG_COLOR, key='TopCOL')

        bot_col = sg.Column([[col3, col4]], pad=(0, 0), background_color=BG_COLOR, key='BotCOL')

        lf_col = sg.Column(
            [[sg.Text(APP_DATA['Temp'], font=('Haettenschweiler', 90), pad=((10, 0), (0, 0)), justification='center',
                      key='Temp')]],
            pad=(10, 0), element_justification='center', key='LfCOL')

        rt_col = sg.Column(
            [metric_row('Feels Like'), metric_row('Wind'), metric_row('Humidity'), metric_row('Precip 1hr'),
             metric_row('Pressure')],
            pad=((15, 0), (25, 5)), key='RtCOL')

        layout = [[top_col],
                  [lf_col, rt_col],
                  [bot_col]]

        window = sg.Window(layout=layout, title='Weather Widget', margins=(0, 0), finalize=True, location=win_location,
                           element_justification='center', keep_on_top=True, no_titlebar=True, grab_anywhere=True,
                           alpha_channel=ALPHA,
                           right_click_menu=[[''], 'Exit'])

        for col in ['COL1', 'COL2', 'TopCOL', 'BotCOL', '-QUIT-']:
            window[col].expand(expand_y=True, expand_x=True)

        for col in ['COL3', 'COL4', 'LfCOL', 'RtCOL']:
            window[col].expand(expand_x=True)

        window['-CHANGE-'].set_cursor('hand2')
        window['-QUIT-'].set_cursor('hand2')
        window['-REFRESH-'].set_cursor('hand2')

        return window

    def update_metrics(window):
        """ Adjust the GUI to reflect the current weather metrics """
        metrics = ['City', 'Temp', 'Feels Like', 'Wind', 'Humidity', 'Precip 1hr',
                   'Description', 'Icon', 'Pressure', 'Updated']
        for metric in metrics:
            if metric == 'Icon':
                window[metric].update(data=APP_DATA[metric])
            else:
                window[metric].update(APP_DATA[metric])

    def main(refresh_rate, win_location):
        """ The main program routine """
        refresh_in_milliseconds = refresh_rate * 60 * 1000

        # Load settings from config file. If none found will create one
        settings = load_settings()
        location = settings['-location-']
        if location is not None:
            if location.isnumeric() and len(location) == 5 and location is not None:
                APP_DATA['Postal'] = location
                APP_DATA['City'] = ''
            else:
                APP_DATA['City'] = location
                APP_DATA['Postal'] = ''
            update_weather()
        else:
            sg.popup_error('Having trouble with location.  Your location: ', location)
            exit()

        window = create_window(win_location)

        while True:  # Event Loop
            event, values = window.read(timeout=refresh_in_milliseconds)
            if event in (None, '-QUIT-', 'Exit'):
                break
            if event == '-CHANGE-':
                x, y = window.current_location()
                settings = change_settings(settings, (x + 200, y + 50))
            elif event == '-REFRESH-':
                sg.popup_quick_message('Refreshing...', keep_on_top=True, background_color='red', text_color='white',
                                       auto_close_duration=3, non_blocking=False,
                                       location=(win_location[0] + 170, win_location[1] + 150))
            elif event != sg.TIMEOUT_KEY:
                sg.Print('Unknown event received\nEvent & values:\n', event, values, location=win_location)

            update_weather()
            update_metrics(window)
        window.close()

    #if __name__ == '__main__':
    if len(sys.argv) > 1:
        win_location = sys.argv[1].split(',')
        win_location = (int(win_location[0]), int(win_location[1]))
    else:
        win_location = (None, None)
    main(refresh_rate=1, win_location=win_location)



# v1

# import GuiAPPs as guiApps
# GuiWindowLAYOUTSshow() #cycles thru them as you close them

def GuiWindowLAYOUTSshow():
    import PySimpleGUI as sg

    """
        PySimpleGUI is designed & authored in Python to take full advantage the awesome Python constructs & capabilities.
        Layouts are represented as lists to PySimpleGUI. Lists are fundamental in Python and have a number of powerful
        capabilities that PySimpleGUI exploits.

        Many times PySimpleGUI programs can benefit from using CODE to GENERATE your layouts.  This Demo illustrates
        a number of ways of "building" a layout. Some work on 3.5 and up.  Some are basic and show concatenation of rows
        to build up a layout.  Some utilize generators.

        These 8 "Constructs" or Design Patterns demonstrate numerous ways of "generating" or building your layouts
        0 - A simple list comprehension to build a row of buttons
        1 - A simple list comprehension to build a column of buttons
        2 - Concatenation of rows within a layout
        3 - Concatenation of 2 complete layouts [[ ]] + [[ ]] = [[ ]]
        4 - Concatenation of elements to form a single row [ [] + [] + [] ] = [[ ]]
        5 - Questionnaire - Using a double list comprehension to build both rows and columns in a single line of code
        6 - Questionnaire - Unwinding the comprehensions into 2 for loops instead
        7 - Using the * operator to unpack generated items onto a single row 
        8 - Multiple Choice Test - a practical use showing list comprehension and concatenated layout
    """

    """
        Construct #0 - List comprehension to generate a row of Buttons

        Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
        are all on the same row.
    """

    def layout0():
        layout = [[sg.Button(i) for i in range(4)]]  # A list of buttons is created

        window = sg.Window('Generated Layouts', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #1 - List comprehension to generate a Column of Buttons

        More list super-power, this time used to build a series of buttons doing DOWN the window instead of across

    """

    def layout1():
        # a List of lists of buttons.  Notice the ] after Button
        layout = [[sg.Button(i)] for i in range(4)]

        window = sg.Window('Generated Layouts', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #2 - List comprehension to generate a row of Buttons and concatenation of more lines of elements

        Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
        are all on the same row, just like the previous example.
        However, here, we want to not just have a row of buttons, we want have an OK button at the bottom.
        To do this, you "add" the rest of the GUI layout onto the end of the generated part.

        Note - you can't end the layout line after the +. If you wanted to put the OK button on the next line, you need
        to add a \ at the end of the first line.
        See next Construct on how to not use a \ that also results in a VISUALLY similar to a norma layout
    """

    def layout2():
        # if want to split, can't add newline after + to do it
        layout = [[sg.Button(i) for i in range(4)]] + [[sg.OK()]]

        window = sg.Window('Generated Layouts', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct # 3 - Adding together what appears to be 2 layouts

        Same as layout2, except that the OK button is put on another line without using a \ so that the layout appears to
        look like a normal, multiline layout without a \ at the end

        Also shown is the OLD tried and true way, using layout.append.  You will see the append technique in many of the
        Demo programs and probably elsewhere.  Hoping to remove these and instead use this more explicit method of +=.

        Using the + operator, as you've already seen, can be used in the middle of the layout.  A call to append you cannot
        use this way because it modifies the layout list directly.
    """

    def layout3():
        # in terms of formatting, the layout to the RIGHT of the = sign looks like a 2-line GUI (ignore the layout +=
        layout = [[sg.Button(i) for i in range(4)]]
        # this row is better than, but is the same as
        layout += [[sg.OK()]]
        # .. this row in that they both add a new ROW with a button on it
        layout.append([sg.Cancel()])

        window = sg.Window('Generated Layouts', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct 4 - Using + to place Elements on the same row

        If you want to put elements on the same row, you can simply add them together.  All that is happening is that the
        items in one list are added to the items in another.  That's true for all these contructs using +
    """

    def layout4():
        layout = [[sg.Text('Enter some info')] + [sg.Input()] + [sg.Exit()]]

        window = sg.Window('Generated Layouts', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #5 - Simple "concatenation" of layouts
        Layouts are lists of lists.  Some of the examples and demo programs use a .append method to add rows to layouts.
        These will soono be replaced with this new technique.  It's so simple that I don't know why it took so long to
        find it.
        This layout uses list comprehensions heavily, and even uses 2 of them. So, if you find them confusing, skip down
        to the next Construct and you'll see the same layout built except for loops are used rather than comprehensions

        The next 3 examples all use this same window that is layed out like this:
            Each row is:
        Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
        Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
        ...

        It shows, in particular, this handy bit of layout building, a += to add on additional rows.
        layout =  [[stuff on row 1], [stuff on row 2]]
        layout += [[stuff on row 3]]

        Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
    """

    def layout5():
        questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                     'Get along with people in your family?', 'Get along with people outside your family?',
                     'Get along well in social situations?', 'Feel close to another person',
                     'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

        layout = [[sg.Text(qnum + 1, size=(2, 2)), sg.Text(q, size=(30, 2))] +
                  [sg.Radio('', group_id=qnum, size=(7, 2),
                            key=(qnum, col)) for col in range(5)]
                  for qnum, q in enumerate(questions)]
        layout += [[sg.OK()]]

        window = sg.Window('Computed Layout Questionnaire', layout)
        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #6 - Computed layout without using list comprehensions
        This layout is identical to Contruct #5.  The difference is that rather than use list comprehensions, this code
        uses for loops.  Perhaps if you're a beginner this version makes more sense?

        In this example we start with a "blank layout" [[ ]] and add onto it.

        Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
    """

    def layout6():
        questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                     'Get along with people in your family?', 'Get along with people outside your family?',
                     'Get along well in social situations?', 'Feel close to another person',
                     'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

        layout = [[]]
        for qnum, question in enumerate(questions):
            # rows start with # and question
            row_layout = [sg.Text(qnum + 1, size=(2, 2)),
                          sg.Text(question, size=(30, 2))]

            # loop through 5 radio buttons and add to row
            for radio_num in range(5):
                row_layout += [sg.Radio('', group_id=qnum,
                                        size=(7, 2), key=(qnum, radio_num))]
            # after row is completed layout, tack it onto the end of final layout
            layout += [row_layout]

        # and finally, add a row to the bottom that has an OK button
        layout += [[sg.OK()]]

        window = sg.Window('Computed Layout Questionnaire', layout)
        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #7 - * operator and list comprehensions 
            Using the * operator from inside the layout
            List comprehension inside the layout
            Addition of rows to layouts
            All in a single variable assignment

        NOTE - this particular code, using the * operator, will not work on Python 2 and think it was added in Python 3.5

        This code shows a bunch of questions with Radio Button choices

        There is a double-loop comprehension used.  One that loops through the questions (rows) and the other loops through
        the Radio Button choices.
        Thus each row is:
        Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
        Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
        Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5

        What the * operator is doing in these cases is expanding the list they are in front of into a SERIES of items
        from the list... one after another, as if they are separated with comma.  It's a way of "unpacking" from within
        a statement.

        The result is a beautifully compact way to make a layout, still using a layout variable, that consists of a
        variable number of rows and a variable number of columns in each row.
    """

    def layout7():
        questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                     'Get along with people in your family?', 'Get along with people outside your family?',
                     'Get along well in social situations?', 'Feel close to another person',
                     'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

        # These are the question # and the question text
        layout = [[*[sg.Text(qnum + 1, size=(2, 2)), sg.Text(q, size=(30, 2))],
                   # finally add an OK button at the very bottom by using the '+' operator
                   *[sg.Radio('', group_id=qnum, size=(7, 2), key=(qnum, col)) for col in range(5)]] for qnum, q in
                  enumerate(questions)] + [[sg.OK()]]

        window = sg.Window('Questionnaire', layout)

        event, values = window.read()

        print(event, values)
        window.close()

    """
        Construct #8 - Computed layout using list comprehension and concatenation
        This layout shows one practical use, a multiple choice test.  It's been left parse as to focus on the generation
        part of the program.  For example, default keys are used on the Radio elements.  In reality you would likely
        use a tuple of the question number and the answer number.

        In this example we start with a "Header" Text element and build from there.
    """

    def layout8():
        # The questions and answers
        q_and_a = [
            ['1. What is the thing that makes light in our solar system',
             ['A. The Moon', 'B. Jupiter', 'C. I dunno']],
            ['2. What is Pluto', ['A. The 9th planet', 'B. A dwarf-planet',
                                  'C. The 8th planet', 'D. Goofies pet dog']],
            ['3. When did man step foot on the moon', ['A. 1969', 'B. 1960', 'C. 1970', 'D. 1869']], ]

        # make Header larger
        layout = [[sg.Text('Astronomy Quiz #1', font='ANY 15', size=(30, 2))]]

        # "generate" the layout for the window based on the Question and Answer information
        for qa in q_and_a:
            q = qa[0]
            a_list = qa[1]
            layout += [[sg.Text(q)]] + [[sg.Radio(a, group_id=q)]
                                        for a in a_list] + [[sg.Text('_' * 50)]]

        layout += [[sg.Button('Submit Answers', key='SUBMIT')]]

        window = sg.Window('Multiple Choice Test', layout)

        while True:  # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'SUBMIT'):
                break
        sg.popup('The answers submitted were', values)
        window.close()

    # ------------------------- Call each of the Constructs -------------------------

    """
    A bunch of window layouts
    even you can give quizzes
    big questionaires as well
    """
    layout0()
    #layout1()
    #layout2()
    #layout3()
    #layout4()
    #layout5()
    #layout6()
    #layout7()
    #layout8()









#assign the first button to run the background change function
#v1
# import GuiAPPs as guiApps
# guiApps.GuiWithImageBUTTONSshow()

def GuiWithImageBUTTONSshow():
    import PySimpleGUI as sg
    import io
    from PIL import Image
    import base64

    """
    Shows some fancy button graphics with the help of PIL
    Usually when you create Base64 buttons to embed in your PySimpleGUI code, you make the exactly the correct size.  Resizing isn't an option when
        using the tkinter version of PySimpleGUI (except for crude "Scaling")
    The PIL code resizes the button images prior to creating the sg.B
    """


    DEF_BUTTON_COLOR = ('white', 'black')


    def resize_base64_image(image64, size):
        '''
        May not be the original purpose, but this code is being used to resize an image for use with PySimpleGUI (tkinter) button graphics
        :param image64: (str) The Base64 image
        :param size: Tuple[int, int] Size to make the image in pixels (width, height)
        :return: (str) A new Base64 image
        '''
        image_file = io.BytesIO(base64.b64decode(image64))
        img = Image.open(image_file)
        img.thumbnail(size, Image.ANTIALIAS)
        bio = io.BytesIO()
        img.save(bio, format='PNG')
        imgbytes = bio.getvalue()
        return imgbytes


    def GraphicButton(text, key, image_data, color=DEF_BUTTON_COLOR, size=(100, 50)):
        '''
        A user defined element.  Use this function inside of your layouts as if it were a Button element (it IS a Button Element)
        Only 3 parameters are required.
        :param text: (str) Text you want to display on the button
        :param key:  (Any) The key for the button
        :param image_data: (str) The Base64 image to use on the button
        :param color: Tuple[str, str] Button color
        :param size: Tuple[int, int] Size of the button to display in pixels (width, height)
        :return: (PySimpleGUI.Button) A button with a resized Base64 image applied to it
        '''
        return sg.Button(text, image_data=resize_base64_image(image_data, size), button_color=color, font='Any 15', pad=(0, 0), key=key, border_width=0)






    #def ShowMeTheButtons():



    #if __name__ == '__main__':

    # To convert your images, use the PySimpleGUI program - Demo_Base64_Image_Encoder.py located on the GitHub (http://www.PySimpleGUI.com)

    orange64 = 'iVBORw0KGgoAAAANSUhEUgAAAiIAAADLCAMAAABkvgh7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANtvJ99sId5tIt5uI91tJNxuJNxuJttvKN90NN91Ntt3PN52ONx3Otx3PNt4Pdp4Ptx4PepfD+pfEOtgD+piD+tkD+ttD+dnFOdoE+doFOVoFuNqG+JrHOFrHuFsHuRpGORpGuRqGORqGupgEOpiEOpkEOlmEOhnEupoEOpoEupqFettEetsF+tuFOxqFetrGOtsGetvHOxrGOxsGOxtGuxuG+xuHexxFutwH+xxGOxyGOxyGuxxHuBsIOJvJ+NvKORvKONwKeNwKuJxLONyLeJyLuRwKeRwKuRxLOtxIexyIexzJOx0JOx1Ju11KOx2KOx2Kux5Iux4Kux5Le1/LeFyMOFzMuB0NOB1Nux7MOx8MOx8Mu19NO1+NO1+Ntd7RdV8RtN+S9J/TdF/TtV9SNR9Stl5QNl6Qdh6Qth7RK+Tfa+Tfq6Ufr+JZb+JZr+KZ7uMbr6KaL6LaryMbLyNb7yOb7WPdLuNcLqOcLmOcrmPdLOQd7SQdrKReLKRerGSerCTfLCTfrmQde2AN+2AOO2BOu2COu6DPO6EPe6EPsWDV8OFXcOFXsOGXcOGXsaDWMSEWsqCVs+AUM2AUs6CU82CVMqDWMmEWtCAT9CAUMKHYMCIYsCIZMCKZu6FQO6GQe6GQu6HRO6IRe6JRu6KR+6KSO+LSu+MS++MTO+OTe+OTu+OUO+RUu+TVfCNTvCOTvCPUPCQUfCQUvCSU/CRVPCSVPCSVvCUV/CUWPCVWvGWWvGXXPGYXvCWYPGaYfGcYvGcZPKdZvKeZ/GdavKeaPKebfKebvKgavKhbPKibfGibvKjcPGkcfKmdPKiePOod/OpePSpePSqevSrfPSsfPSsfvSqg/SugfWwgvWwhPWyhfWyhvWxi/Wyj/W0ifW2jfa4j/a1kPW2kva2lfW2lvW4kPa6kfa7kva5lvW7lPa8lPW8lve+l/a4mva5nPa6nPa7nva+mPa+mva/nPa8oPa9ovbAm/bAnfXAnvbCofbEo/XGp/bGqPbIqQAAAC/NnaUAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAAJXElEQVR4Xu3de3zVdR3H8Xb9/sJh60LlOTtubdIZEyckSdedMzkdZyRGIePmZdqki8s0KllJmtGCTAXRlUAyrireUeZga2JRkooYRWR0JbXMLsIqZ5fT7/L5nRvj9/md0/fhw/Px/fyHP+D33fb4vPj+LvsxXpMA8IREgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgJF7Ih1Xf3bVsuu/AYXu+mUrL+u8iqbqIcdErvhme0V8SjQCIpwWe+0nli+k2R5NTolc0jYzqpQBcigV+UDltZ57SQ6JfLqyRRXRyiCIis7u7qAhj8B3Ip1tLdg/pFLR0Z+hOR/JbyIrWxGIZCp289E2Ep+J3HzEFqLKy0qhUJUfeUkZnf8lGnYWX4l0tDfTOg5VEqoJNNTXh6EgmaMLBKuaymmcJFLRSfPO5CuRtgitYisPBehDQUFrqC3O2EtUxRdo4Bn8JHJhlNawlNZh85Aj2JQeiRp9JY08nY9Euk+nFUwq1ECLgww1ZTRaS+R8mnk6PpEF8dTDkNIgLQxiHFdNw7U0d9PU07CJdLw+tRUVpy5Cxo19+bz9lYI+n5cNfdhcjWGZf2jsCTTJcDiUmnBR/HKaewqbSHfqQqSJrkLGvuuctZu3jOgBD1u99B7Fg6a+Vwrrk8kNfRX+0XE2+qg527adsc38M723d01yK3lbqhH1SZp7CpfIolnJw4udQk44ddPOn/3q6b+M6K8+/c2vF+jXVw29X/ALI7N+Z3jome+f/QZ7pOG6VCMtl9Dkk7hElifvd0uPs1cbs/SJ5/4+9OLw8ItQ2IaH//vvJ6Y7O0mIhmxuI/Np8klMIhdXuH0p50r1zVue+8fQ0GEQYeg/w32TrLHWF9OYDSO2gGbvYhJZfRodaFTZhYzpe4lWBxmGfzBnnDnYQPJRa+RjNHsXk8hF7iZSYl+IvPGefx0+BJIc/v2OudZoq2jQhhr1FRo+8U7kU6MoEVVjLROedujQn0GYfd99nznahlJn0oYxJetM453IpTE6rNgu5E0/fOlPIMzzf9zVY51q6mjURiTr8Zl3Ite5D0Vq7UQ+8jwtC5Ls7W00h9vgXo2oNpo+8U7kBjrPlDnfmdnwzz+APAf632NN93hn1oYaTdMn3om0USLVdiFje59+9hmQ5tmDg3YiQfe6c1bm287eiVTSUc555i0DB2lVkIQSSZ5pZl5B43d4J3KMk4hyvn3XOHjwtyDPwR3vtefrPj6LZ7595p3IaCeRMue7M+MHfvcbkOfXg04i7lP4WB6JlNgrhBsHzOVAGjMR68FI6rY3n0Sa7BXMRA7QqiDJgQEnkRp72Pkl4tzQhBv7f0mLgiS/oF0kSK8X5pPI8fYK4cbtPz8A8jxFu4h71/v/7CLb9j8F8uzXmEjffpBIYyIP7qM1QZT+99vz1ZFI7959IFC/vl1kKxIRabu+XQSJiPTTbdp2kfH3//gnIM/ePn2JbNmzF+R5sm+qPV8tiex+EuTZ06svkTt27wF5dm/VmMjju0GgB/Qlsvmxx0GgO7Xd9I6/7VFaE0S5T2Miux57FOTRmMitj/wI5Nl1j75ENu18BAS6W18iGx/eCQLdqi+RDTu+9zDIs2myPV8diawf3AECbdSXyDokItIGfYmsHXxoEORZry2RiT0DtCaIsk5jIv0DIFDPO+z5aklkez8ItGaiPV8diazpox//C6Is1beL3NJLP0IaRFmibRc5aemdd4E8W7t0JgISaUxkyZb7QaDF2hI58ev33gcC6UtkQtdmkOi8k+z56thFum4Dic450Z6vjkQWbwKJ5ulL5KvrN4JAGhM5d916EGiOxkR61vaAOGtnaEzkljUg0Aznf4HQkci8JUtBoOn6EpnbBRJ9WF8ic74GEk3Tl8iMxSDRh6z/+ExTIueBRFM17iLngkRT9e0iH50HEulMZC5INFlfItNngETOP6PRkUjDWbQkyOK8UaQlkWnTQSKdiZwFEiERYGhM5MxpIJHz6qqWRKaeCRIhEWA4bxRpSeSDIBISAYbGRN5NS4IsOhMBkTQmMhlEQiLAQCLAcF4605LIO08FifQlMm4iiKQxkQm0JMiicxeZAALpTOSUSSCRxkROPuVkEEhnIiCS8wI8EoGj0pdIuAFEQiLAoPHqSGQciETj1ZEIiIZEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgBG0h51fIk20BohWaw87v0RKaA0Qrcoedn6JlLs/xwYkq7aHnV8iKkiLgGQl9rANI55LIq9zEjGqaBEQLEDDNuJfpPE7vBP5OB1VTKuAYO7VatHMRTR+h3ci7ZSICtAyIFeTM2tDzbqYxu/wTmRFhA4L0TIgVvI8oypp+sQ7kVVROqwM9zTShWjUhrqApk+8E+mM02G4YJUuUE6TNiLX0PSJdyLuXa9hlONqRDb3oYhhxBbS8AmTyA3uxQi+TyNbrbsXGOpYmr2LSWRBjA40VB0tBgIFymjM5nlmOc3exSSSqEzVhUesYtW7D1atpyKZD874RFaeToealyNoRKgG95GIKft+hk8kcWxyGzHK0IhI9WmFFMUvp8EnsYmsbqGDTeW1tCgIEiim8Voi36a5p7CJJNqTNzXmLhSqp3VBiprUlao54FFfprGn8Iksmp061RhGKTYSUQLV6dM1Yt+hqafhE0lcFi+iBSyqCVckYrw1lHymamu+iWaezkciiWvSLkdMqqQqgPNN4QvUNmXsIOaFyEU08Qx+Ekl0t6TvIyZVWl1VEwwGA1CIgsGaulBJ5gZiirR10MAz+Eok8a1YVm8WBQUr66+8rbl9xEJ8JpJY1TpCIyCIOmMFzTqbz0QSnfObEYlgkdmradJH8JuIebJpjSASoVTswsz3VdP5TySxaEVrFJHIoyLxtktpxiPJIREzkmWV8ah5sUNrQ6ErUioypeLGrHeIsuSUiKnzuguOmRWPTYHCF4u3VrR1Lxj5PiYl10QsV1298HOfh4K3sPNKmqinfBKBVxUkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAgwkAp4Sif8BKbOKvRIFiXEAAAAASUVORK5CYII='
    green_pill64 = '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'
    red_pill64 = 'iVBORw0KGgoAAAANSUhEUgAAAYEAAACCCAYAAACgunQ+AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAl2cEFnAAABgQAAAIIAb/yLCQAAF7hJREFUeNrt3XmUXGd55/Hvc++trat6UXdrX7CNFtsysh072MaKsEmwgZBZwjiEIcmBTMgk4TjAxB5D4sEWJmYmYLIME47P5GQ4k7AEH5IzJIRgwDGObSy8ypElZEmWhXa1WktXVXct977P/NFqjum+t7p6rWrp+ZzTx3K9de99q/54f/Uu972iqhhjjLkwea2ugDHGmNaxEDDGmAuYhYAxxlzAglZXoJX2rpNMOEIhGibv+2RbXR9jzPwKHMOBo3TRGc5ygU6Qyvn6uQ+tllypzlpPWSuwVmGtKutF6BPodkqPgABIJpORVDrd6jobY+aXGy6Xcc6d+98KUFY4CxwG9nqwV2FvBHuH1/DqNc9ovdV1nm3nTQj8cJX0eXW24NiswhZgvYB4hc7OVtfNGLOwuVKxqEpdhO0I/yIhj4+keHLTMS23um4ztXBDQET2LmOLi7gF5ecQLrNf9MaY+eBKxaKCE3hO4BEnfH3DcX2x1fWajgUXAruXyiaUX0J5lwgr7Ze+MabVzvUUdonHV/2Qr75+UA+2uk7NWhAhsHOjpIOT3A7cjtJrDb8xpl1FpeKQB99X5W/Xn+QvUHUzP+vcaesQ2LtcFruQ31bhA0C3Nf7GmIXClYpFFQ7i+LPCSf7vKtWRVtcpTluGwI4+WR14fEiFX/M78r14nj/dczlgKFKG3Ojf2UipqRIq1IH6uX+H7fc1GGPmWCCQEkiJkJLRNfMZEXp8ocsTunyh4MnoMsJpcqViEeGUKp+v1nnwqtN6ptWf+7XaKgReXCb5lONjqvy239nZO51zFJ1yLHQcD5VTznEmap/PZ4xZmHp9od/3WBZ4LA+EjEw9FtxwuazOnUb55OWjw0RRqz8XtEsIiMjOXm7D4z5g+VSGfRxwsO44ETleqUfU2+DjGGPOb92esCLwWBl4LA28KfUUXKlYdMoO8blz43F9otWfpeUh8NJyuVxDPi9wdbONvwLHQ8erdcfB0Bp+Y0zr5ER4XcrjopRPr998HLhScUiFrwn8/sYTeqxV9W9dCIh4O/v5sFP+oNmhn7rCv1ZDXq5FzMZ0u4jQvWoNQTqNn8kQ/PgvCzMaBTTGtCclqtcJq1WiWpWwWiWsVBg+PUi1WJzx2bs9YUPa55K03/TGbK5UPAR8cOOAfr0V30hLQuClJbLMOR4U4eZmfv0PO2V3zbGvHk1rAjeVy7F4w2Us3nAZ+b5+8v2Lyff1k+3unvfPboxpTy6KKB47SvnkAOWBAU7t38fg/lcYOnoYpthO5kRYn/FYm/JJNfF70pWKRZT/UxzkozfM8yqieQ+Bl5bKrU75vJcvXDzZe0OFHdWIPTXHVGqZzudZdc0b6V+/gf51G+hYNK05ZmOMwUURg/v2cPrAqxx6ehunDuxvOhR84NKMx2WZyXsGrlwqAbucz/uvPKovzdfnm78QEJHti/mUwAe9fKHQ8MsA9tQcu6rN//LvXrWalVdfy7IrNtG9ajVMY/beGGMmUx8Z5sgLz3F85w6OPPdMU5uP5kTYlPVYnZp8kCgql4bE4z9vOqZfmY/PMy8hsHOjpOsD/Dnw7skC4HiobK9GlNzk9Urlcqz8qZ9mzfU30r1qzXx8X8YY82O1UpGDz2zj4FNPUDw++dxuvy9cmfXp9hr/SI3KpaIoW68c0Afm+jPMeQhs65OujMcXgZsaBUCo8Hw14nA4+ZRvpqubDW9/Jyuvvhbx7Lk4xpjWO/HDnfzoqSc4sXPHpO99fcrjiozfcPnJueGhv9hzkjtum8N7CuY0BJ5fLCtU+ZoIVzQKgNOR8mw1YniSX//5xUu55Ka3sGzTVYhY42+MaT/Fo0d45dHvcHznjoZzB72+cE3WJ9dg6PpcEHzDpfj1a47o8FzUd85C4Add0hek+RevULgs6T0KvFJz/LAWNZz4TeU62PCOX2DJFZts4aYxZkEoDZxg5989RPHokcT3pAQ2ZXyWB8k/as8FwQ+6enjH2j1ane16zkkI/KBL+vwM35J05g2SSsXu7x8Bz46EnGywrYN4HiuveSMXbbkJP52Z9XoaY8xcO7FzB/u++zC1UvJ9CGvODQ8lceVSSYVvyRreM9tPN5v1EHhisXSm4RteOnNdUgDUdDQAzjYY/iksXc7G//BuUh35Wa2fMcbMN41CDjzxGIe2fT/xPcsCj03Z5KWkrlwqoXz12kE+MJvbU89qCHx/teSCCn8rsDlpDqDslGcrjcf/V1x9LWtu3IL409481Bhj2s7p/fvY++1vEo7E3w/W6wtXZ4PEG8zGJouvHdCPzFadZi8EROTpPh5S4VY/IQCGnPJMJUxc+x/kcrz+LbfQveai2fp8xhjTVmrlEvu+808UjxyOLc+KcF3OT9ypNBrtEdz3xpP6R7NRn1kLgW198mGE+5ICoOSUZ6th4mZv2Z5FrLv150nbc2OMMec5dcqPnnyMkz/cGVue94RrM8k9gqhcGvLgF3/6pH53pnWZlRDY1iubncffB/lCT1z5iCrPVUKqCZfKL1nKxTe/lSBjk7/GmAvH8X99gaPPPxtb1uUJV2cCkjYmDculA56y+bpBPTSTOsw4BLYtlaUu4nE/X1gbV15V5flKRCXhOp3LV/K6LTfbTV/GmAvS6f37OPRU/GMFenxhUyZoNFn8z11LedvlL2ltutefUQg8JOKv7OURv1DYEltB4LlKmDgJXFi2gtVv+hkLAGPMBe3Mq69w5JltsWW9vnBFJogti8qlkiifv2FQ/+t0rz2jEHhyifyuOv4waR5gdzViIIpfyZTr62fV9ZvxbAWQMcZwat8eBl56MbbsopTPqoTN58Jyqegrb7thUJ+cznWnHQKPrZTVfo2nvY7C0rjyY6HjlVp8AKQLnax602Y8P8AYY8yowZd3cXrf3gmvC7Ax69OVsPGcK5eeH1rEDW+fxh3F026FpcYD0pFfqjEbPpSc8mrdxe7m7AUBS6+8CpzDuWkPYxljzHmn5+JLqJ49w8jgyQlle2oRb8jEP6TGCesLp/k94P6pXnNaPYHHFsm/wedLfkd+wu28DnixGiWuBOq//Ao6+hbP/bdpjDELkAvrHH3uaaLqxB/1nZ5weTp+WMiVy6c05PotZ3XPVK435RB4WCSf6WOX35FfHVd+oO44kbAfUGH5CrovumR+vkljjFmg6qUiJ3a8GLsL6cUpj/6EdaNuuPytLSf1bVO51pSHgzL9/A5K7PMay04ZiDR2p08/k6Fz+Qq0ZkNAxhjTSJDOUFiyjPLxoxPKDoWOHs8niGloFTZ/r0/e+uZB/XbT15pKxR4VKdDH7X5HPj8+nxQ4EGriVs+dy1eiYTilZwUbY8yFKr94MZVTJ3H1n9w0NNLRIHhdzGohryOfd8PljwJzEwLaz2+i9MY15AOhUnHxIZAudJLK5nC1Wd0B1Rhjzmv5xUspHZl4Q/CpSOnzlXzMaiEH1z3SL295y0l9pJlrNB0CDy+TvK/8bhDTC4iA45FL7AXkevtwdRsGMsaYqUjlcgSZLFG1MqHsSKisTU9sdc/1Bj4GzG4I+HV+A6E/rhcwGCkOYpeEBh0dCIpaCBhjzJRlujoZOTkxBEZUGXJKZ3xv4IZvL5Y3v3VAvzfZ+ZsKga0i3o29fNDP5fPjJ6sdMBgm9wLSuQ5caMNAxhgzHX6Qwg8CXBhOKBsIlULMjQNeLp/Xcvl3gNkJget7eLPCirhewKmxXkBMmRekELAVQcYYMwNBJks9LE14vaJKySXODdzy8DJZcssxPdHw3M1UQDx+xUtYEXS6wVyAHwQTZraNMcZMjed5ie3sYKR0xISA39HRHVWG3w38z0bnnjQEvr5YOjPKL8T1AopOiRocqyjOegHGGDNj4nmom7gf24gqNWXidhIiosp7mWkIpJV3qdCRFAJJ6YQIWq/bfQHGGDMLpEHZkHP0+hPvG1C44h8XyVXvOK0vJB07+XCQ8stxewSFCiONQkAVoghjjDGzI6m9LTmlN2ZXfr8jn5eR8i8DLySds2EIPCySd4u4Lm67opIq0iiajDHGzIsIGFYlF9MoO+VnGx3bMATqvWwWJRW3x1y5US/AGGPMvCo7JevFhsCl/7hElr3jhB6LO67xcJBys9fRkR//zICI0eEgsRgwxpi2UHWg3sRf7H5HRyEaHr4J+ErccQ1DQIWb4yZ2q4o1/8YY00YcUFdidxd1ws1MNQS+2SmLNc3G+BCwoSBjjGk3VQU/fovpm5KOSQyBeoo3eplsLi4E6s56AsYY025qquTiW+dV/9AvK995Ug+PL/ASzyZswPM8ZfTO4LG/UMEWfhpjTPup6U+212N/Xq6jox6yIe6YxJ6Agw1xeRKCLQ01xpg2FRH/614CNhCzvXRiCKhjfdzS0MgmhY0xpm1FLv6HuotYH/f+5BAQ1sfNBzhsUtgYY9pVBMTcPIzKFIaD/q5TlpCiJ67MWU/AGGPalkOJbaWVdXHvjw0BF7DSz+ZiVwYlnN4YY0wbcBC7cacKy7eKePeo/sRWpLEhEEGnJ8nTvxYCxhjTphQ0vpGWtb0UgKHXvhgbAiJ0Jm0BbQFgjDHtLWkUJy100kwIRI6Cl3ASWx5qjDHtS4gPAS/X0eGKw4XxrwcJJ+mMWx5q8wHGGNP+NGEoJ/LoHP9a/MSwJvcEjDHGtLfEtlporiegQsbmBIwxZmFKar+dIzP+tfibxbzRh8THsWcIGGNMe0tqv1UmFsT3BJThuFMI1hMwxph25xJeV4+R8a8FCSco+gknsRAwxpiFyVOK41+LXx2kFJPWmQaWAsYY07aUhNVBqlpPNxkCERS9hJkFu0/AGGPaW+wO0JVKxQubDAHfp2Srg4wxZuEZe5BM3OuVTkrjX48NgXqNM54bGfGzuVzciZIfR2aMMaaVVONDIFJqv3lEh8e/HtueB3kOuHM9ivF/zu4YM8aYtjW2i+j4P4H9ce+P7Qn86jEt/2WPHFImPonGYUNCxhjTrqKEuwQcvBz3/uQniym740NA7YYxY4xpU1HCcBDC7riXk0PA4+XYcSVshZAxxrSriPgQcDLVnkDE7rhlRnUFsZlhY4xpO5HGz9uGlZERdKo9gYBd9crISDBuhZACoULKegPGGNNW6glDQQ60EEwxBNLdPFM7xQgwYZloXSFtIWCMMW2llvAgAU95/r2DOhRXlhgC79uvlQe75UmFd44vq6pSsMlhY4xpK9XknsA/Jx0TNDgf6vFofAiM/tdiwBhj2kNdRyeFxwsrIyMiPJp0XMMQAB4JKyMVP5vNvvZFBaoq5GyZkDHGtIUR1dg7BBxUq508mXRcwxA4fobtS3o4rbB8fFlZlZxnIWCMMe2grC7piWJPfeSgjiQd1zAE7lF1f94j31Tl1ydcMFL6fNtHyBhjWq2iSi3mSTLqnEP5RqNjJxsOwsEXtVL5j3FDQmWndFlvwBhjWqoUxW8VUa/Xyjj+ptGxk4bA4Fke7e3ioAfrxpcNRUq3hYAxxrSMAkWX8FRhx7duL+pAo+MnDYF7VN3nuuWLCveOLxtRpapK1iaIjTGmJc46jV0VFFUqFQd/Ndnxk4YAgAp/Xa9W7goy2Qk3jp2MlNX2zEljjJl3CgxGLmmvoMEzq/inyc7RVAjcfkb3/WmPPA68dXxZyVlvwBhjWuGsU+rJz3j50j0vaW2yczQVAgAoD4SVys+MnyAGGIiUNbaZkDHGzBsFBhJ6AVGlMuQF/Fkz5xHV5h8V9ifd8rifyd4YV7Y+45O1HDDGmHlxOlIO1l1sWVitfO4jZ/X2Zs7TfE8AcHC/q1S+FsT0Bg7XHWvTdteAMcbMtQg4Gsb3AsJqpagen2n2XFNqtf/LEN9U4fm451cWnTIY2QOIjTFmrh2pO2oa/yxh4K9/77QeaPZcU+oJoKrSJffXK5WHYnsDoaPH87HFQsYYMzfKThlI+MEdVivDCJ+eyvmmNCcw5jNd8g9+NvvzcWV9vnBJyoaFjDFmtimws+oYjmm3w0qlIsIDd5zVu6dyzqn1BMYq4vGheqXypiCbXTS+7GSk9PrKIruT2BhjZtXh0FFO/uH+alee+6d6zmn1BAD+qEvuUrg3blgoEHiDrRYyxphZcyZSdtUSVgNVKhVP+Pd3ntVJbw4bb9ohsFUkne1im5/OXBVXnveETdnAdhk1xpgZqqqyvRLG3hgWVatVlK/dVdT3Tufc0w4BgE91yY0C3/UzmUxc+bLAY13ab9HXZowxC58C2yshRRffVkfV6jEJuPSuU3p2OuefUQgAfKpT7hbh7qQgWJf2WR5Yf8AYY6ZjVzViIIofBqpXqxUffumuIf376Z5/WhPDr1UrcX+qi+vFubeL501o7V+uRfjAUgsCY4yZkn31iBMJARBVq1Xgj2cSADALDwa7R9XVlfdFYX1/3I0LCuyqRXYjmTHGTMGBuuNHdUdSu6rC4/UiH5/pdWY8HDTmvg65TlJ8J0hnCnHlHnBVNrClo8YYM4lDoWN3LUosD2vVH4UR191b0mMzvdashQDAH/bIber4q6T5AV9gUyag37cgMMaYOAfqjpcbBEBUqxYVfva/ndWnZ+N6sxoCAPd1yR0on0wKAgE2ZnxW2l3FxhjzYwrsrkYcSNgZFCCsVUuecNvd07gfIMmshwDA1k75pMAdSUEAo6uGbNdRY4wBB2yvRBwLkwMgqlZH8Hn/x8/o3zR/5snNSQggIlsLfE7hPwUNgmBF4HFl1rcbyowxF6xQ4QeVkNMNFs+E1WpVhdu3Dun/nu3rz00IAIjIvXm+oMK7GwVBpyf8VNanyyaMjTEXmOOh8kI1pNagGQ5Hl4J+aGtRH5yLOsxdCACIyD0F7lO4o1EQ+IzOE1xs8wTGmAuAA3ZWI/Y1GP8HCGvVIo7f+kRJvzRXdZnbEDjn453yW8ADQSbT0eh9ywLh2kxgzyMwxpy3KgpPjYSccY3b3rBaHRDlPVtL+t25rM+8hADAPV3yb53yhSCT6Wn0vkBgQ8pnXdqzuQJjzHmjprCzFrG/Hv9YyNeKatVX8fl3nzit2+e6XvMWAgB398i1EvF1xOv3U6lUo/cWPOHKrM8y6xYYYxYwBV6tOXZUo4Zj/3Bu/F/YT8QtnxzWg/NRv3kNAYCP9cgiCflfAr/YaJ5gzNJAuDTts8TCwBizgChwsO7YVXUMucnb2bBaHRHhgYESn3hQtT5f9Zz3EBjzB13yGyif9tPpnmbe3+d7XJrxWRl4WBwYY9pVBOyvReyuRZSaaPyjWq0GHHPw/k8V9ZH5rm/LQgDgrrys8H3+H8omP51ON3NMlyesTftckvJJWRoYY9pERZVd1Yg99Yhm98uMarUawsOZFO+9Z1CHWlHvloYAwFaRYKTABwTu8VKpJSLSVNMuwPLA46KUx+rAtxVFxph5V1HlQN2xvz61nZLPNf77Fe787zPcCnqmWh4CY36/UxZH8AmB9/npdHYqx44FwvLAY6nv0euLDRkZY2adAwYix7HQcSzUxL3+k2gURVEUFYHP5Pp54N79Wmn1Z2qbEBhzR05e5wV8QeBNzQ4RjeczuiVFn+/R4wldvtDtiS05NcY0LQJOR8qQU846x4lIOR5Ovrwz8Xy1WlWFhwL48P1DOtjqzzem7UJgzEe7ZLNT7kS51U+nJ11F1IyCNxoGKYGUjP43EEghNpxkzAWorlBHCfXcv3X036ciZWSW2sawXisBX/aEB/7HkO5u9Wcer21DYMydBdmkcIfAu/x0umPmZzTGmLnlwjB0zg0J/GXk+JPPDuvhVtcpSduHwJgP52RN4PEr4vF+lDXTHSoyxpi5EtVqVYVtKF92AV/97Fk91eo6TWbBhMBr3ZGXa/B5jzpuE1hmgWCMaZVz6/xfRvmyi/jKZyv6SqvrNBULMgRe684uuUEjblaPNwvcgJKxUDDGzJVzjf4QwmMK3/OURz9d0hdbXa/pWvAh8FpbRYJyJzdEyq0oFwNvEFgHeBYMxpipimq1mkIo8BKwU4XnfOWxT5fZrudJ43lehUCcrSJeOcPFYcA6gSsQenB0IXSKUAA6ceRVmNK9CcaYhU9gWKCkQkmVIkJZ4AzCYanzciTs+eMRjpwvDX7sd3AefzZjjDGTsPunjDHmAmYhYIwxFzALAWOMuYBZCBhjzAXs/wOhrcv9WD6DSAAAADt0RVh0Y29tbWVudABFZGl0ZWQgYnkgUGF1bCBTaGVybWFuIGZvciBXUENsaXBhcnQsIFB1YmxpYyBEb21haW40zfqqAAAAJXRFWHRjcmVhdGUtZGF0ZQAyMDA4LTEwLTE0VDE2OjQwOjIwLTA0OjAwm68KQgAAACV0RVh0bW9kaWZ5LWRhdGUAMjAwOC0xMC0xNFQxNjo0MDoyMC0wNDowMMQefHYAAAAASUVORK5CYII='
    button64 = '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'


    sg.theme('Black')

    frame_layout = [[sg.Text('Windows can look good when using tkinter?', size=(45, 3))],
                    [sg.Text(
                        'All of these buttons are part of the code itself', size=(45, 2))],
                    [GraphicButton('Next', '-NEXT-', button64),
                     GraphicButton('Change BGs', '-CHANGEBGS-', red_pill64),
                     GraphicButton('READwiki', '-READWIKI-', green_pill64),
                     GraphicButton('Exit', '-EXIT-', orange64)], ]

    layout = [[sg.Frame('Nice Buttons', frame_layout, font=(
        'any 18'), background_color='black')]]

    window = sg.Window('Demo of Nice Looking Buttons', layout,
                       grab_anywhere=True,
                       keep_on_top=True,
                       no_titlebar=True,
                       use_default_focus=False,
                       font='any 15',
                       background_color='black')

    # ---===--- The event loop --- #
    while True:
        event, values = window.read()
        print(event)
        if event in ('-EXIT-', None):  # Exit button or X
            break
        if event in ('-READWIKI-', None):  # Exit button or X
            print("Read Wikipedia - open url in browser")
            link = "http://wikipedia.org"
            import webbrowser
            webbrowser.open_new(link)
        if event in ('-CHANGEBGS-', None):  # Exit button or X
            changeBGs()
        if event in ('-NEXT-', None):  # Exit button or X
            changeBGs()


#Demo programs on github:
#https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms
#
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Buttons_Nice_Graphics.py


#----------------

"""
from PIL import Image, ImageTk
from urllib import request
import PySimpleGUI as sg

# Get one PNG file from website and save to file
url = (
    "https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/"
    "images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png")
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
if response.status != 200:
    print("Failed to load image from website !")
    exit()
data = response.read()

filename = "example.png"
with open(filename, "wb") as f:
    f.write(data)

# Resize PNG file to size (300, 300)
size = (300, 300)
im = Image.open(filename)
im = im.resize(size, resample=Image.BICUBIC)

sg.theme('DarkGreen3')

layout = [
    [sg.Image(size=(300, 300), key='-IMAGE-')],
]
window = sg.Window('Window Title', layout, margins=(0, 0), finalize=True)

# Convert im to ImageTk.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)

# update image in sg.Image
window['-IMAGE-'].update(data=image)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
"""



#----------------

"""
# Required:
# pip install PySimpleGUI Pillow

# image_viewer.py
import io
import os
import PySimpleGUI as sg
from PIL import Image
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()
"""


def GUIphotosViewerBroke():
    # img_viewer.py

    import PySimpleGUI as sg
    import os.path

    # First the window layout in 2 columns

    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)

            except:
                pass

    window.close()