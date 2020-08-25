from threading import Thread
import time
from helpers.antibot import ip_limit

class Global():
    def __init__(self):
        pass

glob = Global()

##defining all the globals
glob.reuploaded_levels = 0 #levels reuploaded per 24h

def daily_glob_reset_thread():
    """Thread that resets specific glob values."""
    while True:
        glob.reuploaded_levels = 0
        ip_limit.ips = {}
        time.sleep(86400)

#start  thread
Thread(target=daily_glob_reset_thread).start()
