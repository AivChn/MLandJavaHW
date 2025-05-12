from PIL import Image
from PIL.ImageFile import ImageFile

# Amishav Cohen

if __name__ == '__main__':
    im = Image.open(r'C:\Users\amish\PycharmProjects\MLandJavaHW\python\Fruits Classification\test\Apple\Apple (12).png')
    im = im.resize((im.width//2, im.height//2))
    im = im.convert('L')

    im.show()

