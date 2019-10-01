import webbrowser #allows opening webpages
import time #uses sleep to delay loop, to make time for user to interact
import random

while True:
	visit = 'https://google.com'
	webbrowser.open(visit)
	seconds = random.randrange(5, 20)
	time.sleep(seconds)
