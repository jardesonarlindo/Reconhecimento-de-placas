##! /usr/bin/python -u
SAVEDIR = "/home/pi/webcan"
import pygame, sys
import pygame.camera
import time, random
import os

c=raw_input()
if(c=="br"):
	c="eu"
while(1):
	pygame.init()
	pygame.camera.init()
	cam = pygame.camera.Camera("/dev/video0", (640,480))

	cam.start()
	image = cam.get_image()
	cam.stop()
	timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
	filename = "%s/%s.jpg" % (SAVEDIR, timestamp)
	pygame.image.save(image, filename)

	os.system("alpr -c"+" "+c+" "+filename)
	os.system("cd webcan")
	os.system("fbi -t 2 -1 "+filename)
	os.system("rm "+filename)


