# todo clean code
# todo optimize painting
# todo add more color and optimize
# todo add more color for one picture

from PIL import Image, ImageDraw

length = 101
width = 101
short_color_set = ("black", "blue", "coral", "gold", "gray", "indigo", "navy", "white", "yellow")

img = Image.new('RGB', (length, width))
draw = ImageDraw.Draw(img)

for color1 in short_color_set:
    for color2 in short_color_set:
        flag = True
        for i in range(0, length):
            for j in range(0, width):
                if flag:
                    draw.point([i, j], fill=color1)
                    flag = False
                else:
                    draw.point([i, j], fill=color2)
                    flag = True

        image_name = color1 + "_" + color2 + "_" + ".png"
        img.save(image_name)




