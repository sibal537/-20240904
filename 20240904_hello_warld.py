# -*- coding: utf-8 -*-
"""20240904 hello warld

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uCfNPbr6uQzFa4k4vGYdiKSk_hY7KdQk
"""

# prompt:  print ( "hello" )

print("hello")

# prompt: pocket = [   '정윤'  ,   '재상'   ,  '재원'   ]
# if  '정윤'  in pocket: print( "류재상 10년" )

pocket = [   '정윤'  ,   '재상'   ,  '재원'   ]
if  '정윤'  in pocket:
  print( "류재상 10년" )

import pylab as py

x_deg = py.arange(-180, 180+1, )
x_rad = py.deg2rad(x_deg)
y = py.sin(x_rad)

py.plot(x_deg, y)

py.xlabel('x_deg')
py.ylabel('sin(x)')
py.grid(true)

