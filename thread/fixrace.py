import logging
import concurrent.futures
import threading
import time


class FakeDatabase:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    def get_value(self):
        return self._value

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self._value
            local_copy += 1
            time.sleep(0.1)
            self._value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")
    database = FakeDatabase()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info(f'Testing update: End value is {database.get_value()}')