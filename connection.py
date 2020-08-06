import sys
import settings

import dropbox
from dropbox.exceptions import AuthError, BadInputError

from utils.logger import get_logger

log = get_logger()


def get_connection():

    with dropbox.Dropbox(settings.DROPBOX_TOKEN) as dbx:

        # Check that the access token is valid
        try:
            dbx.users_get_current_account()
        except (AuthError, BadInputError):
            log.error('Invalid Token')
            sys.exit(1)
        log.debug('successfully connection')
        return dbx
