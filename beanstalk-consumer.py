from pystalk import BeanstalkClient

TUBE_NAME = "MAIN_TUBE"

client = BeanstalkClient('localhost', 11300)

client.watch(TUBE_NAME)

while True:
    for job in client.reserve_iter():
        try:
            print(job)
        except Exception:
            client.release_job(job.job_id)
            raise
        client.delete_job(job.job_id)

