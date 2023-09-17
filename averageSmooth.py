image = open("baseImage.bmp", "rb")
script = open("converted.bmp", "wb")

#2160 x 2700

script.write(image.read(54))
print(int.from_bytes(image.read(4), "little"))
while True:
    #image.read(54)
    chunk = image.read(3)
    if chunk == b"":
        break
    image.seek(-3, 1)

    red = (int.from_bytes(image.read(1), "little"))
    green = (int.from_bytes(image.read(1), "little"))
    blue = (int.from_bytes(image.read(1), "little"))

    grayscaleV = (0.299*red) + (0.587*green) + (0.114*blue)
    #print(grayscaleV)

    script.write(int(grayscaleV).to_bytes(1, "little")*3)

    #grayScaleArr = []

image.close()
script.close()

script.close()


#image =open("converted.bmp", "rb")
image = open("converted.bmp", "rb")

smoothed_script = open("smoothed.bmp", "wb")

smoothed_script.write(image.read(54))

area_size = 3
half_area = area_size // 2

width = 124
height = 124

for y in range(height):
    for x in range(width):
        red_sum = 0
        green_sum = 0
        blue_sum = 0
        pixel_count = 0

        for ky in range(-half_area, half_area + 1):
            for kx in range(-half_area, half_area + 1):
                px = x + kx
                py = y + ky

                if 0 <= px < width and 0 <= py < height:
                    image.seek(54 + (py * width + px) * 3)

                    red = int.from_bytes(image.read(1), "little")
                    green = int.from_bytes(image.read(1), "little")
                    blue = int.from_bytes(image.read(1), "little")

                    red_sum += red
                    green_sum += green
                    blue_sum += blue
                    pixel_count += 1 #probably a better way to count pixels through the loop but this works

        average_red = red_sum // pixel_count
        average_green = green_sum // pixel_count
        average_blue = blue_sum // pixel_count #uses wierd division lol

        smoothed_script.write(average_blue.to_bytes(1, "little"))
        smoothed_script.write(average_green.to_bytes(1, "little"))
        smoothed_script.write(average_red.to_bytes(1, "little"))

image.close()
smoothed_script.close()
