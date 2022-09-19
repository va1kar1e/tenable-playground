# coding: utf-8
# Author: Siwanont Sittinam

import os
from dotenv import load_dotenv
load_dotenv()


class TenableAuthentication:
    def getHostname(self):
        HOSTNAME = os.getenv("TENABLE_HOSTNAME")

        return HOSTNAME

    def getRequestHeader(self):
        TENABLE_ACCESSKEY = os.getenv("TENABLE_ACCESSKEY")
        TENABLE_SECRETKEY = os.getenv("TENABLE_SECRETKEY")

        return {
            'x-apikey': 'accesskey=' + str(TENABLE_ACCESSKEY) + '; secretkey=' + str(TENABLE_SECRETKEY) + ';'
        }
