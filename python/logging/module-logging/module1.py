import logging
import module2


logger = logging.getLogger(__name__)
print(logger.name)
logger.setLevel(logging.INFO)

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating instance of module class')
a = module2.ModuleClass()
logger.info('created an instance of module class')
logger.info('calling module do_something ')
a.do_something()
logger.info('calling some function')
module2.some_function()
logger.info('done with some function')
