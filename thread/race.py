import logging
import concurrent.futures
import threading
import time


class FakeDatabase:
    def __init__(self):
        self._value = 0

    def get_value(self):
        return self._value

    def update(self, name):
        logging.info(f'Thread {name}: starting update')
        # Creating local copy of value in function to make it thread safe
        local_copy = self._value
        local_copy += 1
        logging.info(f'Thread {name}: Going to sleep')
        time.sleep(0.1)
        self._value = local_copy
        logging.info(f'Thread {name}: finished')
        

if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    database = FakeDatabase()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info(f'Testing update: End value is {database.get_value()}')