from background_task import background
import os

@background(schedule=60)
def refresh_db():
    print("starting db refresh process ")
    os.system("python insert_scripts/run_insert_data.py > db_refresh_log.txt")
    print("db process ended....")
