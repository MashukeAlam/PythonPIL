from PIL import Image
from tkinter import Tk


root = Tk()
Monitor_Height = root.winfo_screenheight()
Monitor_Width = root.winfo_screenwidth()
Thickness = int(Monitor_Height / 9);
colors = ((82, 255, 51),(255, 51, 51),(255, 252, 51),(51, 255, 136),(51, 255, 246),(51, 114, 255),(120, 51, 255),(186, 51, 255),(255, 51, 199))


img = Image.new("RGB", (Monitor_Width, Monitor_Height))

def SingleStripe(i, color):
    for x in range(Monitor_Width):
        for y in range(i * Thickness, Thickness * (i + 1)):
            img.putpixel((x, y), color)

for i in range(9) :
    SingleStripe(i, colors[i])


img.save("wallpaper.png", "PNG")


