# import PAINT as paint
# paint.paint1()
# paint.paint2()
# paint.paint3()
# paint.paint4() #pretty good - multiple brush sizes

#they only work out of the function, on the main.py page


# import Paint
# Paint.paint4()

def paint4():
   from tkinter import *
   from tkinter.colorchooser import askcolor

   class Paint(object):

      DEFAULT_PEN_SIZE = 5.0
      DEFAULT_COLOR = 'black'

      def __init__(self):
         self.root = Tk()

         self.pen_button = Button(self.root, text='pen', command=self.use_pen)
         self.pen_button.grid(row=0, column=0)

         self.brush_button = Button(self.root, text='brush', command=self.use_brush)
         self.brush_button.grid(row=0, column=1)

         self.color_button = Button(self.root, text='color', command=self.choose_color)
         self.color_button.grid(row=0, column=2)

         self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
         self.eraser_button.grid(row=0, column=3)

         self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
         self.choose_size_button.grid(row=0, column=4)

         self.c = Canvas(self.root, bg='white', width=600, height=600)
         self.c.grid(row=1, columnspan=5)

         self.setup()
         self.root.mainloop()

      def setup(self):
         self.old_x = None
         self.old_y = None
         self.line_width = self.choose_size_button.get()
         self.color = self.DEFAULT_COLOR
         self.eraser_on = False
         self.active_button = self.pen_button
         self.c.bind('<B1-Motion>', self.paint)
         self.c.bind('<ButtonRelease-1>', self.reset)

      def use_pen(self):
         self.activate_button(self.pen_button)

      def use_brush(self):
         self.activate_button(self.brush_button)

      def choose_color(self):
         self.eraser_on = False
         self.color = askcolor(color=self.color)[1]

      def use_eraser(self):
         self.activate_button(self.eraser_button, eraser_mode=True)

      def activate_button(self, some_button, eraser_mode=False):
         self.active_button.config(relief=RAISED)
         some_button.config(relief=SUNKEN)
         self.active_button = some_button
         self.eraser_on = eraser_mode

      def paint(self, event):
         self.line_width = self.choose_size_button.get()
         paint_color = 'white' if self.eraser_on else self.color
         if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
         self.old_x = event.x
         self.old_y = event.y

      def reset(self, event):
         self.old_x, self.old_y = None, None

   #if __name__ == '__main__':
   Paint()





# import Paint
# Paint.paint3()

def paint3():
   import pygame as pg

   # pip install pygame==2.0.0.dev10

   """
   With this program you can draw on the 
   screen with pygame


   pythonprogramming.altervista.org
   """

   def init():
      global screen

      pg.init()
      screen = pg.display.set_mode((400, 400))
      mainloop()

   drawing = False
   last_pos = None
   w = 1
   color = (255, 0, 255)

   def draw(event):
      global drawing, last_pos, w

      if event.type == pg.MOUSEMOTION:
         if (drawing):
            mouse_position = pg.mouse.get_pos()
            if last_pos is not None:
               pg.draw.line(screen, color, last_pos, mouse_position, w)
            last_pos = mouse_position
      elif event.type == pg.MOUSEBUTTONUP:
         mouse_position = (0, 0)
         drawing = False
         last_pos = None
      elif event.type == pg.MOUSEBUTTONDOWN:
         drawing = True

   def mainloop():
      global screen

      loop = 1
      while loop:
         # checks every user interaction in this list
         for event in pg.event.get():
            if event.type == pg.QUIT:
               loop = 0
            if event.type == pg.KEYDOWN:
               if event.key == pg.K_s:
                  pg.image.save(screen, "image.png")
            draw(event)
         pg.display.flip()
      pg.quit()

   init()






# import Paint
# Paint.paint2()

def paint2():
   #from tkinter import *
   # by Canvas I can't save image, so i use PIL
   import PIL
   from PIL import Image, ImageDraw

   def save():
      filename = 'image.png'
      image1.save(filename)

   def paint(event):
      x1, y1 = (event.x), (event.y)
      x2, y2 = (event.x + 1), (event.y + 1)
      cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
      #  --- PIL
      draw.line((x1, y1, x2, y2), fill='black', width=10)

   root = Tk()

   cv = Canvas(root, width=640, height=480, bg='white')
   # --- PIL
   image1 = PIL.Image.new('RGB', (640, 480), 'white')
   draw = ImageDraw.Draw(image1)
   # ----
   cv.bind('<B1-Motion>', paint)
   cv.pack(expand=YES, fill=BOTH)

   btn_save = Button(text="save", command=save)
   btn_save.pack()

   root.mainloop()



# import Paint
# Paint.paint1()

def paint1():
   """"Paint program by Dave Michell.

   Subject: tkinter "paint" example
   From: Dave Mitchell <davem@magnet.com>
   To: python-list@cwi.nl
   Date: Fri, 23 Jan 1998 12:18:05 -0500 (EST)

     Not too long ago (last week maybe?) someone posted a request
   for an example of a paint program using Tkinter. Try as I might
   I can't seem to find it in the archive, so i'll just post mine
   here and hope that the person who requested it sees this!

     All this does is put up a canvas and draw a smooth black line
   whenever you have the mouse button down, but hopefully it will
   be enough to start with.. It would be easy enough to add some
   options like other shapes or colors...

                                                   yours,
                                                   dave mitchell
                                                   davem@magnet.com
   """

   #from tkinter import *  # pip install tkinter

   """paint.py: not exactly a paint program.. just a smooth line drawing demo."""

   b1 = "up"
   xold, yold = None, None

   def main():
      root = Tk()
      drawing_area = Canvas(root)
      drawing_area.pack()
      drawing_area.bind("<Motion>", motion)
      drawing_area.bind("<ButtonPress-1>", b1down)
      drawing_area.bind("<ButtonRelease-1>", b1up)
      root.mainloop()

   def b1down(event):
      global b1
      b1 = "down"  # you only want to draw when the button is down
      # because "Motion" events happen -all the time-

   def b1up(event):
      global b1, xold, yold
      b1 = "up"
      xold = None  # reset the line when you let go of the button
      yold = None

   def motion(event):
      if b1 == "down":
         global xold, yold
         if xold is not None and yold is not None:
            event.widget.create_line(xold, yold, event.x, event.y, smooth=TRUE)
            # here's where you draw it. smooth. neat.
         xold = event.x
         yold = event.y

   #if __name__ == "__main__":
   main()
