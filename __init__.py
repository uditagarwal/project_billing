# -*- coding: utf-8 -*-
"""
    __init__

    Initilize project_billing

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool

from .billing import *
from .timeline import *

def register():
    Pool.register(
        Resource,
        TopProject,
        Timeline,
        module='projectbilling', type_='model',
    )