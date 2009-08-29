#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management import call_command


settings.configure(
    INSTALLED_APPS=('autoslug',),
    DATABASE_ENGINE='sqlite3'
)

if __name__ == "__main__":
    call_command('test', 'autoslug')
