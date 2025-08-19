from stem import Signal
from stem.control import Controller
import time

def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print("[TOR] New IP requested.")
            time.sleep(5)
    except Exception as e:
        print("[TOR] IP change failed:", e)