import time
from plyer import notification


while True:
    notification.notify(title = "Please drink some water" , message = "Water is very essential for your health.")
    time.sleep(60*60)