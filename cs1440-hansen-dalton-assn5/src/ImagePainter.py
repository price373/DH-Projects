
import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
class ImagePainter:
    def __init__(self,fractal, palette, fractalInfo):
        self.fractal = fractal
        self.palette = palette
        self.fractalInfo = fractalInfo
        self.winSize = int(fractalInfo['pixels'])
        self.window = Tk()
        self.fractalPicture = PhotoImage(width=self.winSize, height=self.winSize)
        self.canvas = Canvas(self.window, width=self.winSize, height=self.winSize, bg='#000000')
        self.centerx = float(fractalInfo['centerx'])
        self.centery = float(fractalInfo['centery'])
        self.axislength = float(fractalInfo['axislength'])
        self.min = ((float(self.fractalInfo['centerx']) - float(self.fractalInfo['axislength']) / 2.0),
                    (float(self.fractalInfo['centery']) - float(self.fractalInfo['axislength']) / 2.0))
        self.max = ((float(self.fractalInfo['centerx']) + float(self.fractalInfo['axislength']) / 2.0),
                    (float(self.fractalInfo['centery']) + float(self.fractalInfo['axislength']) / 2.0))
        self.canvas.create_image((self.winSize/2, self.winSize/2), image=self.fractalPicture, state="normal")
        self.canvas.pack()

        self.pixelSize = abs(self.max[0] - self.min[0]) / self.winSize
    def paintImage(self):
       before = time.time()
       for row in range(self.winSize, 0, -1):
           colPixels = []
           for col in range(self.winSize):
               x = self.min[0] + col * self.pixelSize
               y = self.min[1] + row * self.pixelSize
               pixelColor = self.palette.getColor(self.fractal.count(complex(x,y)))
               colPixels.append(pixelColor)
           pixels = '{' + ' '.join(colPixels) + '}'
           self.fractalPicture.put(pixels, (0, self.winSize - row))
           self.window.update()
           print(self.__imageProgress__(row), end="\r", file=sys.stderr)
       after = time.time()
       print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
       print("Close the image self.window to exit the program", file=sys.stderr)
       mainloop()
    def __imageProgress__(self, rowNum):
        portion = (self.winSize - rowNum) / self.winSize
        status_percent = '{:>4.0%}'.format(portion)
        status_bar_width = 34
        status_bar = '=' * int(status_bar_width * portion)
        status_bar = '{:<33}'.format(status_bar)
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
