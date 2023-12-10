# Purpose: entry point for spiral HTJ 'health tracking journal'
# see README.md for more details
# Author: @dwerkjem (Derek R Neilson)'
# License: (see documentation/LICENSE.md for more details)
# Version: 0.1.0
# DO NOT EDIT ANYTHING ABOVE THIS LINE
import argparse
import sys
import logging
import os
import modules.user as user

parser = argparse.ArgumentParser(description="entry point for spiral HTJ 'health tracking journal'")
parser.add_argument('-v', '--version', action='version', version=' 0.1.0')
parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
parser.add_argument('-V', '--verbosity', type=int, default=1, help='increase output verbosity (max 3, min 0)')
parser.add_argument('-u', '--user', type=str, help='user arguments see `help user` for more details')

red = '\033[91m' # error
yellow = '\033[93m' # warning
green = '\033[92m' # info
blue = '\033[94m' # debug
white = '\033[0m' # rest of text
colors = [red, yellow, green, blue, white]
# add logging default to error and format to timestamp: filename  levelname: message ! for errors and warnings only
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(filename)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__) # get logger for this file
# add color to logging levels
logging.addLevelName(logging.ERROR, red + logging.getLevelName(logging.ERROR) + white)
logging.addLevelName(logging.WARNING, yellow + logging.getLevelName(logging.WARNING) + white)
logging.addLevelName(logging.INFO, green + logging.getLevelName(logging.INFO) + white)
logging.addLevelName(logging.DEBUG, blue + logging.getLevelName(logging.DEBUG) + white)

def set_verbosity(verbosity):
    log.debug('setting verbosity level to %s', verbosity)
    if verbosity == 0:
        log.setLevel(logging.ERROR)
        log.info('verbosity level set to 0, only errors will be shown')
    elif verbosity == 1:
        log.setLevel(logging.WARNING)
        log.info('verbosity level set to 1, errors and warnings will be shown')
    elif verbosity == 2:
        log.setLevel(logging.INFO)
        log.info('verbosity level set to 2, errors, warnings, and info will be shown')
    elif verbosity == 3:
        log.setLevel(logging.DEBUG)
        log.info('verbosity level set to 3, errors, warnings, info, and debug will be shown')
    else:
        log.error('invalid verbosity level: %s', verbosity)
        return False
    log.debug('verbosity level set to %s', verbosity)
    return True

def parse_args():
    args = parser.parse_args()
    set_verbosity(args.verbosity)
    log.debug('args: %s', args)
    if args.debug:
        log.info('debug mode enabled extra debug actions will be performed')
    return True

def start():
    log.debug('starting spiral HTJ')
    if parse_args():
        log.debug('args parsed successfully')

    else:
        log.error('failed to parse args')
        sys.exit(1)
    log.debug('spiral HTJ started successfully')
    return True

if __name__ == '__main__':
    if start():
        log.info('spiral HTJ exited successfully and gracefully')
        log.debug("starting user module")
        user.SignIn(
            logger=log,
            debug=parser.parse_args().debug,
            arguments=parser.parse_args().user
        )
        log.debug("user module exited")
    sys.exit(0)