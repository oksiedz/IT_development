import colorgram as c

AMOUNT_OF_COLOURS = 30
IMAGE_NAME = 'image.jpg'
# extract colours from picture
colors = c.extract(IMAGE_NAME, AMOUNT_OF_COLOURS)

list_of_colors_tuples = []

# loop populating list with most common colours from photo
for i in range(0, AMOUNT_OF_COLOURS):
    # assignment of color object into variable
    first_color = colors[i]
    # extract rgb
    rgb = first_color.rgb
    # assignment rbg into separate variables
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    # creation of tuple
    color_tuple = (red, green, blue)
    # appending the list of tuples
    list_of_colors_tuples.append(color_tuple)

print(colors)
print(list_of_colors_tuples)