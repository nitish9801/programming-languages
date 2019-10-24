import logging


module_logger = logging.getLogger('__main__.'+__name__)
module_logger.setLevel(logging.INFO)

print(module_logger.name)


class ModuleClass:
    def __init__(self):
        self.logger = logging.getLogger('__main__.'+__name__+'.ModuleClass')
        print(self.logger.name)
        self.logger.info('creating instance of module class')

    def do_something(self):
        self.logger.info('doing something')


def some_function():
    module_logger.info('received a call to "some function"')
