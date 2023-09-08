# AlarmClock Project:


from playsound import playsound

import time

clear = '\033[2J'
clear_and_return = '\033[H'


def alarm(seconds):
    time_elapsed = 0
    print(clear)

    while time_elapsed < seconds:

        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{clear_and_return}{minutes_left:02d}: {seconds_left:02d}')

    if time_left == 0:
        playsound("alarm.mp3")


min = int(input("How many minutes do you want to wait: "))
sec = int(input("How many seconds do you want to wait: "))
total_seconds = min*60 + sec

alarm(total_seconds)
