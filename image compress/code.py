from PIL import Image
img =  Image.open('2.jpg')  
h,w =  img.size
img = img.resize((h,w),Image.ANTIALIAS)
img.save('2_compressed.jpg')
print("Image Compression Process Successfully Completed !! ")
