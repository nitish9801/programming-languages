import logging
import random
import concurrent.futures
import threading

SENTINEL = object()


def producer(pipeline):
    """Getting message from network"""
    logging.debug("Inside Producer")
    for index in range(10):
        message = random.randint(1, 101)
        logging.info(f'Producer got message {message}')
        pipeline.set_message(message, "Producer")

    # Send SENTINEL message to tell consumer we are done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """saving message to db"""
    logging.debug("Inside consumer")
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info(f'Consumer storing message {message}')


class Pipeline:
    def __init__(self):
        self.message = 0,
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug(pipeline)
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

    def __str__(self):
        return str(f'Pipeline class {self.message}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    logging.debug(f'{pipeline}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)

