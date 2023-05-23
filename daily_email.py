import schedule
import time
import subprocess

def job():
	subprocess.call(['python', 'full_send.py'])

schedule.every().day.at("13:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)