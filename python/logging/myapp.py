import logging
import mylib

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
print(logger.level)

def main():
    logging.basicConfig(filename='example.log',
                        format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                        level=logging.INFO)
    logging.info('Hello world')
    mylib.do_something()


if __name__ == '__main__':
    main()