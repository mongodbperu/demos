#! /usr/bin/python
# -*- coding: UTF-8-*-

__author__ = 'carlucho'

import hashlib
import datetime

from random import randint
"""
from libs.encriptacion import *
get_identificador()
"""
def get_identificador():
    fecha_id     = datetime.datetime.now()
    encriptacion = hashlib.sha224(str(fecha_id)).hexdigest()
    return "%s%s"%(str(encriptacion),randint(1,113399))

