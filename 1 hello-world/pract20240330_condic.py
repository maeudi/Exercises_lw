# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:17:40 2024

@author: maeud
"""

#8 a 12 OPEN y 14 a 18 es OPEN
#si la hora esta entre los horarios OPEN
#CASO contrario es CLOSED
hora = 10
if (8<= hora<=11) or (14<=hora<=17):
    print('el comercio esta abierto')
else:
    print('el comercio esta cerrado')