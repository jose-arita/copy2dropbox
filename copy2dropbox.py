#!/usr/bin/env python
from common.connection import get_connection
from common import settings, logger

import sys
import os


from dropbox.files import WriteMode
from dropbox.exceptions import ApiError


def copy():
    logger.debug('files upload started')
    for d,  dirs, files in os.walk(settings.LOCAL_DIR):
        for file in files:
            file_path = os.path.join(d, file)
            str_path = str(file_path)
            str_path = settings.DROPBOX_DIR + \
                str_path[len(settings.LOCAL_DIR):]

            with open(file_path, 'rb') as f:
                try:
                    logger.debug('uploading:{}'.format(str_path))
                    dbx.files_upload(f.read(), str_path,
                                     mode=WriteMode('overwrite'))
                    logger.debug('success uploaded:{}'.format(str_path))
                except ApiError as err:
                    if (
                        err.error.is_path() and
                        err.error.get_path().reason.is_insufficient_space()
                    ):
                        sys.exit(1)
                        logger.error('Cannot upload, insufficient space.')
                    elif err.user_message_text:
                        logger.error(err.user_message_text)
                        sys.exit(1)
                    else:
                        logger.error(err)
                        sys.exit(1)
    logger.debug('files upload finished')


if __name__ == '__main__':
    logger = logger.get_logger()
    logger.debug('started program')
    dbx = get_connection()
    copy()
    dbx.close()
    logger.debug('connection closed and finished program')
