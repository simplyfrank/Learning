from PIL import Image

# Load the Image
img = Image.open('data/oxygen.png')

print(img.width)
print(img.height)

# get Pixelinformation for the middle row of the image
row = [img.getpixel((x, img.height/2)) for x in range(img.width)]

# Removing the duplicated data at the end
ords = [r for r,g,b,a in row if r == g == b]
# print(ords)

# Turning the Greyscale values into Character Data
text = [chr(s) for s in ords[::7]]
print(''.join(text))

# Extracting the solution
goal = [105, 110, 116, 101, 103, 114, 105, 116, 121]
goal = ''.join([chr(s) for s in goal])
print(goal)