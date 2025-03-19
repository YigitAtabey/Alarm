from datetime import datetime
import pygame
import time
i=int(input("Ne kadar tekrarlanması gerektiğini giriniz : "))
x=0


saat=input("Saati giriniz : ")
dakika=input("Dakikayı giriniz : ")
saniye=input("Saniyeyi giriniz : ")
while True:
	suan=datetime.now()
	dt=datetime.strftime(suan,'%H:%M:%S')
	print(dt)
	time.sleep(1)
	if dt == f"{saat}:{dakika}:{saniye}":
		while x<i:

			pygame.init()
			pygame.mixer.music.load("alarm.mp3")
			pygame.mixer.music.play()
			x += 1
			while pygame.mixer.music.get_busy():
				pygame.event.get()







