import logging
import threading
import time


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    # i = 3232323434
    # while i:
    #     i**i
    #     i -= 1

    logging.info(f'Thread {name}: finished')


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info(f'Main: Before creating main thread')
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info(f'Main: Before running thread')
    x.start()
    logging.info(f'Main: wait for thread to finish')
    x.join()
    logging.info(f'Main: All done')
