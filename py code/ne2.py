import sched
import schedule
import time
from schedule import every,repeat,run_pending


@repeat(every(2).seconds)

#if you use decorators you can use run_pending isted of schedule.run_pending

def job():
    print('do job')
    
schedule.every(3).seconds.do(job).tag('daily-work')
schedule.every().minute.at(':20').do(job)
schedule.every().monday.at('20:30').do(job)
#to cancel an specific job
schedule.cancel_job(job)
#to cancel all jobs
schedule.clear()
#to get the jobs with an specific tag (.tag(!))
daily = schedule.get_jobs('daily-work')
#to stop all jobs with an specific tag 
schedule.clear('daily-work')
#to set an start time for a schedule (schedule will run after the said time!)
schedule.every().hours.until('2023-02-02 18:30').tag('daily work')



while True:
    schedule.run_pending()
    time.sleep(1)
    
    