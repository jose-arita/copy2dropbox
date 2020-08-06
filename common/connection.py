from common import settings
import sys

import dropbox
from dropbox.exceptions import AuthError, BadInputError

from common.logger import get_logger

log = get_logger()


def get_connection():

    with dropbox.Dropbox(settings.DROPBOX_TOKEN) as dbx:

        try:
            log.debug('connecting to Dropbox...')
            dbx.users_get_current_account()
        except (AuthError, BadInputError):
            log.error('invalid Token')
            sys.exit(1)
        log.debug('successfully connection')

        return dbx
