#/usr/bin/python
import RPi.GPIO as GPIO
import thread
import time
import requests

from subprocess  import call 

call(["fswebcam", "a"])
