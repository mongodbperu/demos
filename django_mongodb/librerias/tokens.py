# -*- coding: utf-8 -*-

__author__ = 'carlucho'

import hashlib
import datetime

from random import randint


def get_identificador():
    fecha_id = datetime.datetime.now()
    encriptacion = hashlib.sha224(str(fecha_id)).hexdigest()
    return "%s%s" % (str(encriptacion), randint(1, 113399))
