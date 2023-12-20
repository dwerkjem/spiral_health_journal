import argparse

class SignIn:
    def __init__(self,logger, debug, arguments = None, ):
        self.arguments = arguments
        self.logger = logger
        if debug:
            logger.debug ('arguments pre parser: %s', arguments)
        self._parse_args(arguments)

    def help(self):
        print('''
        usage: spiral user [options] [arguments]
              ''')

    def _parse_args(self , arguments):
        logger = self.logger
        logger.info('parsing arguments %s', arguments)