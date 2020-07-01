from PIL import Image

img_file = r'cobra.png'
img = Image.open(img_file)
img.save('icon.ico',format = 'ICO', sizes = [(256,256)])

         
