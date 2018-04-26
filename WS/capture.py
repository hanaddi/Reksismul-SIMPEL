'''

https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
https://wiki.python.org/moin/UdpCommunication

'''

import numpy as np
import cv2
import time 
import json
import requests
import datetime

cap = cv2.VideoCapture(0)
count = 0
now = ''

# gambar
bagi = 4
imgw = int(cap.get(3)/bagi)
imgh = int(cap.get(4)/bagi)
matrix = []

def lapor(img) :
	print '---Lapor---'
	# call(["fswebcam", "a"])
	url = 'http://192.168.1.8/reksismul/up.php'
	url = 'http://192.168.1.7/reksti/up.php'
	# url = 'http://www.ga.hol.es/REKSTI/up.php'
	# files = {'file' : open('a','rb')}
	files = {'file' : img}
	r = requests.post(url, files=files)
	print (r.text)


def capture () :
	global count, matrix, cap, now
	firstTime = True
	while(True):
		count = (count+1)
		ret, frame = cap.read()

		if ret :
			now = datetime.datetime.now().isoformat()
			if firstTime :
				matrix = []
				for i in range(0, imgw ) :
					matrix.append([])
					for j in range(0, imgh ) :
						try :
							matrix[i].append([
								int(frame.item(j*bagi,i*bagi,0)/5),
								int(frame.item(j*bagi,i*bagi,1)/5),
								int(frame.item(j*bagi,i*bagi,2)/5)
							]);
						except :
							matrix[i].append([0,0,0])
							print ("error", i, j)
			else :
				for i in range(0, imgw ) :
					for j in range(0, imgh ) :
						try :
							matrix[i][j] = [
								int(frame.item(j*bagi,i*bagi,0)/5),
								int(frame.item(j*bagi,i*bagi,1)/5),
								int(frame.item(j*bagi,i*bagi,2)/5)
							];
						except :
							matrix[i][j] = [0,0,0]
							print ("error", i, j)

		# Jika terdeteksi pelanggaran
		if count == 5 and False :
			_, img_encoded = cv2.imencode('.png', frame)
			lapor(img_encoded.tostring())

		file = open("frame.txt","w") 
		file.write(json.dumps({'m':matrix,'d':now})) 
		# file.flush()
		file.close()
		firstTime = False


capture()


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
