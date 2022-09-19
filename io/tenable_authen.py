# coding: utf-8
# Author: Siwanont Sittinam

import os
from dotenv import load_dotenv
load_dotenv()


class TenableAuthentication:
    def getCredential(self):
        TENABLE_ACCESSKEY = os.getenv("TIO_ACCESS_KEY")
        TENABLE_SECRETKEY = os.getenv("TIO_SECRET_KEY")

        return {
            'TENABLE_ACCESSKEY': str(TENABLE_ACCESSKEY),
            'TENABLE_SECRETKEY': str(TENABLE_SECRETKEY)
        }
