import os # import the os package
import time #import time package
def function():
	os.system("wget -O index.html http://www.bing.com") #download the bing index
	str1 = open('index.html', 'r').read() # extract the file path using split
	str2=str1.split("g_img={url: \"")[1]
	str3=str2.split(".jpg")[0]
	os.system("wget -O image.jpg http://www.bing.com" + str3 + ".jpg") # download the daily image
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/Wallpaper/image.jpg")

while True:
	function()
	time.sleep(24*60*60)


