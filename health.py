# import required modules
from pygame import mixer
from time import time
from time import sleep
import pyttsx3

def getdate():
	
	
	import datetime
	return (str(datetime.datetime.now()))
print("\n\t\t\t\tEnter the name of the user:\n")
rm = input()
def musicloop(stopper):
	mixer.init()
	mixer.music.load("music.mp3")
	
	
	mixer.music.play()
	while True:
		x = input(
			"Please type c to continue the alarm or EXIT to stop the program : ")
		
		
		if (x.upper() == stopper):
			print("\nGreat! Get back to work:)\n")
			mixer.music.stop()
			return True
			break
		
		
		elif (x.upper() == "EXIT"):
			return False



total_water = 0
total_physical_exercises = 0
total_eye_exercises = 0

if __name__ == '__main__':
	print("\n\t\t\t\tHey",rm,"Welcome to your health clock\n")
  
    
	time_phy = time()
	time_drink = time()
	time_eyes = time()

	eyes_delay = 1
	drink_delay = 2
	phy_delay = 3

	while(True):
		
		
		if (time() - time_drink > drink_delay):
			print("Hey! Please drink some water (at least 200 ml).")

			
			if(musicloop("C")):
				pass
			else:
				break

			
			time_drink = time()
			
			
			total_water += 200
			
			
			f = open("drank.txt", "at")
			f.write("[ " + getdate() + " ] \n")
			f.close()

		
		if (time() - time_eyes > eyes_delay):

			print("Hey! Please do an Eye Exercise.")

			if (musicloop("C")):
				pass
			else:
				break

			time_eyes = time()
			total_eye_exercises += 1
			f = open("eye.txt", "at")
			f.write("[ " + getdate() + " ] \n")
			f.close()

		
		if (time() - time_phy > phy_delay):
			print("Hey! Please do a Physical Exercise.")

			if (musicloop("C")):
				pass
			else:
				break

			time_phy = time()
			total_physical_exercises += 1
			f = open("phy_exer.txt", "at")
			f.write("[ " + getdate() + " ] \n")
			f.close()

	print()
	print(f"Total water taken today : {total_water}.")
	
	try:
		f = open("drank.txt", "rt")
		print("\nDetails :")
		print(f.read())
		f.close()
	except:
		print("Details not found!")

	print(f"Total eye exercise done today : {total_eye_exercises}.")
	
	try:
		f = open("eye.txt", "rt")
		print("\nDetails :")
		print(f.read())
		f.close()
	except:
		print("Details not found!")

	print(f"Total physical exercises done today : {total_physical_exercises}.")
	
	try:
		f = open("phy_exer.txt", "rt")
		print("\nDetails :")
		print(f.read())
		f.close()
	except:
		print("Details not found!")

	sleep(5)
