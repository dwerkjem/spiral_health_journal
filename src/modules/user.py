import argparse

class SignIn:
    def __init__(self,logger, debug, arguments = None, ):
        self.arguments = arguments
        self.logger = logger
        if debug:
            logger.debug ('arguments pre parser: %s', arguments)
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='Sign in to the HTJ system.',
            usage=' -u <arguments>')
        parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
        parser.add_argument('-n', '--name', type=str, help='name of user')
        parser.add_argument('-p', '--password', type=str, help='password of user if not provided will be blank and unencrypted')
        parser.add_argument('-a', '--add-user', action='store_true', help='add user to system')
        parser.add_argument('-d', '--delete-user', action='string', help='delete user from system')
        parser.add_argument('-l', '--list-users', action='store_true', help='list all users in system')
        parser.add_argument('-e', '--edit-user', action='store_true', help='edit user in system')
        parser.add_argument('-s', '--sign-in', action='store_true', help='sign in user')
        parser.add_argument('-o', '--sign-out', action='store_true', help='sign out user')
        parser.add_argument('-c', '--change-password', action='store_true', help='change password of user')
        parser.add_argument('-r', '--reset-password', action='store_true', help='reset password of user')
