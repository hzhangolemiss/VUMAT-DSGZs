# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# **********
# Multi Layers Test Model
# **********

# parallel run
n_cpu = 4
n_domain = n_cpu

# Unit: MPa, mm, s, ton
ydim = 0.4
zdim = 0.4
mesh_size = 0.2
half_mesh = 0.1

#Flayer_dim = 5.0

#AClayer_dim = 0.4
#Mlayer1_dim = 3.0
#Mlayer2_dim = 2.0
#Mlayer3_dim = 8.0

#Blayer_dim = 5.0
Impactor_dim = 5.0
#Foam_dim = 20.0
#Bone_dim = 8.0
FI_gap = 0
BB_gap = 5*mesh_size

v_val = 100000.0

total_time = 4e-05
dt_inc = 5e-09

if_back = False
fixed_back = False

if_bone = True
fixed_bone = True

if if_back == True and if_bone == True:
    exit()

f_out_n = int(0.1*total_time/dt_inc)
f_out_n = max(f_out_n, 1)
h_out_n = int(0.5*total_time/dt_inc)
h_out_n = max(h_out_n, 1)

# **********

# Part - Create Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), point2=(1.6, ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='FLayer', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['FLayer'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(1.6, 0.0), point2=(7.6, ydim)) # 6.0 mm metal Mlayer3
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='MLayer3', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['MLayer3'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(7.6, 0.0), point2=(15.6, ydim)) # 8.0/16.0 mm polymer Mlayer2
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='MLayer2', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['MLayer2'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(15.6, 0.0), point2=(16.2, ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='ACLayer1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['ACLayer1'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(16.2, 0.0), point2=(20.2, ydim)) # 4.0 mm ceramic Mlayer1
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='MLayer1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['MLayer1'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(20.2, 0.0), point2=(20.8, ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='ACLayer2', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['ACLayer2'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(20.8, 0.0), point2=(22.4, ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='BLayer', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['BLayer'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

if if_back == True:
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(22.4, 0.0), point2=(24.0, ydim))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Back', type=DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Back'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']

#mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
#mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(15.0, 0.0), point2=(25.0, ydim))
#mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Foam', type=DEFORMABLE_BODY)
#mdb.models['Model-1'].parts['Foam'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
#del mdb.models['Model-1'].sketches['__profile__']
if if_bone == True:
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(22.4+abs(BB_gap), 0.0), point2=(30.4+abs(BB_gap), ydim))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Bone', type=DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Bone'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0-abs(FI_gap), 0.0), point2=(-abs(Impactor_dim), ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Impactor', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Impactor'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

# abq: * Menu - Tools - Surface - Create
mdb.models['Model-1'].parts['FLayer'].Surface(name='Surf-FLayer-xlo', side1Faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['FLayer'].Surface(name='Surf-FLayer-xhi', side1Faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['BLayer'].Surface(name='Surf-BLayer-xlo', side1Faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['BLayer'].Surface(name='Surf-BLayer-xhi', side1Faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#4 ]', ), ))
if if_back == True:
    mdb.models['Model-1'].parts['Back'].Surface(name='Surf-Back-xlo', side1Faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#1 ]', ), ))
    mdb.models['Model-1'].parts['Back'].Surface(name='Surf-Back-xhi', side1Faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#4 ]', ), ))
#mdb.models['Model-1'].parts['Foam'].Surface(name='Surf-Foam-xlo', side1Faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#1 ]', ), ))
#mdb.models['Model-1'].parts['Foam'].Surface(name='Surf-Foam-xhi', side1Faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#4 ]', ), ))
if if_bone == True:
    mdb.models['Model-1'].parts['Bone'].Surface(name='Surf-Bone-xlo', side1Faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#1 ]', ), ))
    mdb.models['Model-1'].parts['Bone'].Surface(name='Surf-Bone-xhi', side1Faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['Impactor'].Surface(name='Surf-Impactor-xlo', side1Faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['Impactor'].Surface(name='Surf-Impactor-xhi', side1Faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['ACLayer1'].Surface(name='Surf-ACLayer1-xlo', side1Faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['ACLayer1'].Surface(name='Surf-ACLayer1-xhi', side1Faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['MLayer1'].Surface(name='Surf-MLayer1-xlo', side1Faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['MLayer1'].Surface(name='Surf-MLayer1-xhi', side1Faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['ACLayer2'].Surface(name='Surf-ACLayer2-xlo', side1Faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['ACLayer2'].Surface(name='Surf-ACLayer2-xhi', side1Faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['MLayer2'].Surface(name='Surf-MLayer2-xlo', side1Faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['MLayer2'].Surface(name='Surf-MLayer2-xhi', side1Faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['MLayer3'].Surface(name='Surf-MLayer3-xlo', side1Faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['MLayer3'].Surface(name='Surf-MLayer3-xhi', side1Faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#4 ]', ), ))

# abq: * Menu - Tools - Set - Create
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-FLayer-xlo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-FLayer-xhi')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-FLayer-ylo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-FLayer-yhi')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-FLayer-zlo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-FLayer-zhi')
mdb.models['Model-1'].parts['FLayer'].Set(cells=mdb.models['Model-1'].parts['FLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-FLayer')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-BLayer-xlo')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-BLayer-xhi')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-BLayer-ylo')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-BLayer-yhi')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-BLayer-zlo')
mdb.models['Model-1'].parts['BLayer'].Set(faces=mdb.models['Model-1'].parts['BLayer'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-BLayer-zhi')
mdb.models['Model-1'].parts['BLayer'].Set(cells=mdb.models['Model-1'].parts['BLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-BLayer')
if if_back == True:
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-Back-xlo')
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-Back-xhi')
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-Back-ylo')
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-Back-yhi')
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-Back-zlo')
    mdb.models['Model-1'].parts['Back'].Set(faces=mdb.models['Model-1'].parts['Back'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-Back-zhi')
    mdb.models['Model-1'].parts['Back'].Set(cells=mdb.models['Model-1'].parts['Back'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-Back')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-Foam-xlo')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-Foam-xhi')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-Foam-ylo')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-Foam-yhi')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-Foam-zlo')
#mdb.models['Model-1'].parts['Foam'].Set(faces=mdb.models['Model-1'].parts['Foam'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-Foam-zhi')
#mdb.models['Model-1'].parts['Foam'].Set(cells=mdb.models['Model-1'].parts['Foam'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-Foam')
if if_bone == True:
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-Bone-xlo')
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-Bone-xhi')
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-Bone-ylo')
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-Bone-yhi')
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-Bone-zlo')
    mdb.models['Model-1'].parts['Bone'].Set(faces=mdb.models['Model-1'].parts['Bone'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-Bone-zhi')
    mdb.models['Model-1'].parts['Bone'].Set(cells=mdb.models['Model-1'].parts['Bone'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-Bone')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-Impactor-xlo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-Impactor-xhi')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-Impactor-ylo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-Impactor-yhi')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-Impactor-zlo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-Impactor-zhi')
mdb.models['Model-1'].parts['Impactor'].Set(cells=mdb.models['Model-1'].parts['Impactor'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-Impactor')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-ACLayer1-xlo')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-ACLayer1-xhi')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-ACLayer1-ylo')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-ACLayer1-yhi')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-ACLayer1-zlo')
mdb.models['Model-1'].parts['ACLayer1'].Set(faces=mdb.models['Model-1'].parts['ACLayer1'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-ACLayer1-zhi')
mdb.models['Model-1'].parts['ACLayer1'].Set(cells=mdb.models['Model-1'].parts['ACLayer1'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-ACLayer1')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer1-xlo')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-MLayer1-xhi')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-MLayer1-ylo')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-MLayer1-yhi')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-MLayer1-zlo')
mdb.models['Model-1'].parts['MLayer1'].Set(faces=mdb.models['Model-1'].parts['MLayer1'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-MLayer1-zhi')
mdb.models['Model-1'].parts['MLayer1'].Set(cells=mdb.models['Model-1'].parts['MLayer1'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer1')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-ACLayer2-xlo')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-ACLayer2-xhi')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-ACLayer2-ylo')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-ACLayer2-yhi')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-ACLayer2-zlo')
mdb.models['Model-1'].parts['ACLayer2'].Set(faces=mdb.models['Model-1'].parts['ACLayer2'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-ACLayer2-zhi')
mdb.models['Model-1'].parts['ACLayer2'].Set(cells=mdb.models['Model-1'].parts['ACLayer2'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-ACLayer2')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer2-xlo')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-MLayer2-xhi')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-MLayer2-ylo')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-MLayer2-yhi')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-MLayer2-zlo')
mdb.models['Model-1'].parts['MLayer2'].Set(faces=mdb.models['Model-1'].parts['MLayer2'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-MLayer2-zhi')
mdb.models['Model-1'].parts['MLayer2'].Set(cells=mdb.models['Model-1'].parts['MLayer2'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer2')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer3-xlo')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-MLayer3-xhi')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-MLayer3-ylo')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-MLayer3-yhi')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-MLayer3-zlo')
mdb.models['Model-1'].parts['MLayer3'].Set(faces=mdb.models['Model-1'].parts['MLayer3'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-MLayer3-zhi')
mdb.models['Model-1'].parts['MLayer3'].Set(cells=mdb.models['Model-1'].parts['MLayer3'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-MLayer3')

# abq: Module - Property - Create Material
mdb.models['Model-1'].Material(name='JCS-OFHCCu')
mdb.models['Model-1'].materials['JCS-OFHCCu'].Density(table=((8.96e-09, ), )) # c0 ~= 2200 m/s; Z = 1.97e+07
mdb.models['Model-1'].materials['JCS-OFHCCu'].SpecificHeat(table=((383000000.0, ), ))
mdb.models['Model-1'].materials['JCS-OFHCCu'].Elastic(table=((44700.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['JCS-OFHCCu'].Plastic(hardening=JOHNSON_COOK,scaleStress=None, table=((90.0, 292.0, 0.310, 1.09, 1356.0, 298.0), ))
mdb.models['Model-1'].materials['JCS-OFHCCu'].plastic.RateDependent(table=((0.025, 1.0), ), type=JOHNSON_COOK)
mdb.models['Model-1'].materials['JCS-OFHCCu'].Eos(table=((3933000.0, 1.49, 2.00), ), type=USUP)
mdb.models['Model-1'].materials['JCS-OFHCCu'].plastic.setValues(scaleStress=None)

mdb.models['Model-1'].Material(name='JCS-Al6061')
mdb.models['Model-1'].materials['JCS-Al6061'].Density(table=((2.70e-09, ), )) # c0 ~= 5000 m/s; Z = 1.35e+07
mdb.models['Model-1'].materials['JCS-Al6061'].SpecificHeat(table=((896000000.0, ), ))
mdb.models['Model-1'].materials['JCS-Al6061'].Elastic(table=((25900.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['JCS-Al6061'].Plastic(hardening=JOHNSON_COOK,scaleStress=None, table=((290.0, 204.0, 0.350, 1.34, 858.0, 298.0), ))
mdb.models['Model-1'].materials['JCS-Al6061'].plastic.RateDependent(table=((0.011, 1.0), ), type=JOHNSON_COOK)
mdb.models['Model-1'].materials['JCS-Al6061'].Eos(table=((5350000.0, 1.34, 2.0), ), type=USUP)
mdb.models['Model-1'].materials['JCS-Al6061'].plastic.setValues(scaleStress=None)

mdb.models['Model-1'].Material(name='JCS-Steel4340')
mdb.models['Model-1'].materials['JCS-Steel4340'].Density(table=((7.83e-09, ), )) # c0 ~= 5000 m/s; Z = 3.91e+07
mdb.models['Model-1'].materials['JCS-Steel4340'].SpecificHeat(table=((477000000.0, ), ))
mdb.models['Model-1'].materials['JCS-Steel4340'].Elastic(table=((77500.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['JCS-Steel4340'].Plastic(hardening=JOHNSON_COOK,scaleStress=None, table=((792.0, 510.0, 0.26, 1.03, 1793.0, 298.0), ))
mdb.models['Model-1'].materials['JCS-Steel4340'].plastic.RateDependent(table=((0.014, 1.0), ), type=JOHNSON_COOK)
mdb.models['Model-1'].materials['JCS-Steel4340'].Eos(table=((4578000.0, 1.33, 1.67), ), type=USUP)
mdb.models['Model-1'].materials['JCS-Steel4340'].plastic.setValues(scaleStress=None)





mdb.models['Model-1'].Material(name='gDSGZ-PA12')
mdb.models['Model-1'].materials['gDSGZ-PA12'].Density(table=((1.015e-09, ), ))
mdb.models['Model-1'].materials['gDSGZ-PA12'].SpecificHeat(table=((1185000000.0, ), ))
mdb.models['Model-1'].materials['gDSGZ-PA12'].Depvar(n=7)
mdb.models['Model-1'].materials['gDSGZ-PA12'].UserMaterial(mechanicalConstants=(1935.0, 0.39,
                                                                                3.083, 0.0, 0.415, 2.687, 3.0, 200.0, 870.0, 6.6, 0.01,
                                                                                0.9, 1.015e-09, 1185000000.0, 0.0))

# Ref.DOI: 10.1016/j.polymertesting.2015.12.010
mdb.models['Model-1'].Material(name='gDSGZ-PCABS')
mdb.models['Model-1'].materials['gDSGZ-PCABS'].Density(table=((1.15e-09, ), ))
mdb.models['Model-1'].materials['gDSGZ-PCABS'].SpecificHeat(table=((1500000000.0, ), ))
mdb.models['Model-1'].materials['gDSGZ-PCABS'].Depvar(n=7)
mdb.models['Model-1'].materials['gDSGZ-PCABS'].UserMaterial(mechanicalConstants=(3000.0, 0.30,
                                                                                 35.81, 0.0, -1.324, 1.984, 0.0379, 3.58, 232.2, 22.26, 0.0854,
                                                                                 0.9, 1.15e-09, 1500000000.0, 0.0))

# Ref.DOI: 10.1007/s12206-015-0922-3
mdb.models['Model-1'].Material(name='mDSGZ-PC2015H')
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].Density(table=((1.15e-09, ), ))
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].SpecificHeat(table=((1500000000.0, ), ))
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].Depvar(n=7)
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].UserMaterial(mechanicalConstants=(2100.0, 0.38,
                                                                                   8.97, 1.127, -0.161, 1.35, 0.007, 100, 465, 65, 0.093,
                                                                                   0.9, 1.15e-09, 1500000000.0, 0.0))

# Ref.DOI: 10.1007/s12206-015-0922-3
mdb.models['Model-1'].Material(name='mDSGZ-PMMA2015H')
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].Density(table=((1.2e-09, ), ))
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].SpecificHeat(table=((1466000000.0, ), ))
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].Depvar(n=7)
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].UserMaterial(mechanicalConstants=(3200.0, 0.38,
                                                                                     2.7, 1.582, -0.760, 2.443, 0.03, 20, 800, 18, 0.138,
                                                                                     0.9, 1.2e-09, 1500000000.0, 0.0))

# Ref.DOI: 10.1007/s00170-009-2335-x
mdb.models['Model-1'].Material(name='MR-PUR')
mdb.models['Model-1'].materials['MR-PUR'].Density(table=((1.07e-09, ), ))
mdb.models['Model-1'].materials['MR-PUR'].Hyperelastic(materialType=ISOTROPIC, table=((77.69, -37.66, 2.51e-04), ), testData=OFF, type=MOONEY_RIVLIN, volumetricResponse=VOLUMETRIC_DATA)
#mdb.models['Model-1'].materials['MR-PUR'].Hyperelastic(materialType=ISOTROPIC, table=((224.2, -152.26, 8.34e-06), ), testData=OFF, type=MOONEY_RIVLIN, volumetricResponse=VOLUMETRIC_DATA)

mdb.models['Model-1'].Material(name='ABQ_JH2-SiC')
mdb.models['Model-1'].materials['ABQ_JH2-SiC'].Density(table=((3.215e-09, ), ))
mdb.models['Model-1'].materials['ABQ_JH2-SiC'].SpecificHeat(table=((750000000.0, ), ))
mdb.models['Model-1'].materials['ABQ_JH2-SiC'].Depvar(n=8, deleteVar=8)
mdb.models['Model-1'].materials['ABQ_JH2-SiC'].UserMaterial(mechanicalConstants=(3.215e-09, 193000.0, 0.96, 0.65, 0.35, 1.0, 0.009,
                                                                                 1.0, 750.0, 1.23795, 0.1319127, 11700.0, 5130.0, 1.0, 0.48, 0.48, 1.2, 0.0,
                                                                                 0.2, 0.0, 220000.0, 361000.0, 0.0))

# Ref.DOI: 10.1016/j.matdes.2010.05.002
mdb.models['Model-1'].Material(name='EoS-Bone')
mdb.models['Model-1'].materials['EoS-Bone'].Density(table=((1.412e-09, ), ))
mdb.models['Model-1'].materials['EoS-Bone'].SpecificHeat(table=((1260000000.0, ), ))
mdb.models['Model-1'].materials['EoS-Bone'].Elastic(table=((2664.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['EoS-Bone'].Eos(table=((1850000.0, 0.94, 0.0), ), type=USUP)

# abq: Module - Property - Create Section & Assign Section
mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-Steel4340', name='Section-Flayer', thickness=None)
mdb.models['Model-1'].parts['FLayer'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['FLayer'].sets['Set-FLayer'],
                                                        sectionName='Section-Flayer', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-Steel4340', name='Section-Blayer', thickness=None)
mdb.models['Model-1'].parts['BLayer'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['BLayer'].sets['Set-BLayer'],
                                                        sectionName='Section-Blayer', thicknessAssignment=FROM_SECTION)
if if_back == True:
    mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-Steel4340', name='Section-Back', thickness=None)
    mdb.models['Model-1'].parts['Back'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                            region=mdb.models['Model-1'].parts['Back'].sets['Set-Back'],
                                                            sectionName='Section-Back', thicknessAssignment=FROM_SECTION)
#mdb.models['Model-1'].HomogeneousSolidSection(material='HF-PU', name='Section-Foam', thickness=None)
#mdb.models['Model-1'].parts['Foam'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
#                                                        region=mdb.models['Model-1'].parts['Foam'].sets['Set-Foam'],
#                                                        sectionName='Section-Foam', thicknessAssignment=FROM_SECTION)
if if_bone == True:
    mdb.models['Model-1'].HomogeneousSolidSection(material='EoS-Bone', name='Section-Bone', thickness=None)
    mdb.models['Model-1'].parts['Bone'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                            region=mdb.models['Model-1'].parts['Bone'].sets['Set-Bone'],
                                                            sectionName='Section-Bone', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-OFHCCu', name='Section-Impactor', thickness=None)
mdb.models['Model-1'].parts['Impactor'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['Impactor'].sets['Set-Impactor'],
                                                        sectionName='Section-Impactor', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='MR-PUR', name='Section-ACLayer1', thickness=None)
mdb.models['Model-1'].parts['ACLayer1'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['ACLayer1'].sets['Set-ACLayer1'],
                                                        sectionName='Section-ACLayer1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='ABQ_JH2-SiC', name='Section-MLayer1', thickness=None)
mdb.models['Model-1'].parts['MLayer1'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['MLayer1'].sets['Set-MLayer1'],
                                                        sectionName='Section-MLayer1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='MR-PUR', name='Section-ACLayer2', thickness=None)
mdb.models['Model-1'].parts['ACLayer2'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['ACLayer2'].sets['Set-ACLayer2'],
                                                        sectionName='Section-ACLayer2', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='mDSGZ-PC2015H', name='Section-MLayer2', thickness=None)
mdb.models['Model-1'].parts['MLayer2'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['MLayer2'].sets['Set-MLayer2'],
                                                        sectionName='Section-MLayer2', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-Al6061', name='Section-MLayer3', thickness=None)
mdb.models['Model-1'].parts['MLayer3'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['MLayer3'].sets['Set-MLayer3'],
                                                        sectionName='Section-MLayer3', thicknessAssignment=FROM_SECTION)

# Module - Assembly - Create Instance
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='FLayer-Inst', part=mdb.models['Model-1'].parts['FLayer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='BLayer-Inst', part=mdb.models['Model-1'].parts['BLayer'])
if if_back == True:
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Back-Inst', part=mdb.models['Model-1'].parts['Back'])
#mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Foam-Inst', part=mdb.models['Model-1'].parts['Foam'])
if if_bone == True:
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Bone-Inst', part=mdb.models['Model-1'].parts['Bone'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Impactor-Inst', part=mdb.models['Model-1'].parts['Impactor'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='ACLayer1-Inst', part=mdb.models['Model-1'].parts['ACLayer1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='MLayer1-Inst', part=mdb.models['Model-1'].parts['MLayer1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='ACLayer2-Inst', part=mdb.models['Model-1'].parts['ACLayer2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='MLayer2-Inst', part=mdb.models['Model-1'].parts['MLayer2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='MLayer3-Inst', part=mdb.models['Model-1'].parts['MLayer3'])

# Module - Step - Create Step {Adiabatic, No thermal conduction, mechanical only}
#mdb.models['Model-1'].TempDisplacementDynamicsStep(improvedDtMethod=ON, name='Step-1', previous='Initial', timePeriod=0.00001)
mdb.models['Model-1'].ExplicitDynamicsStep(adiabatic=ON, improvedDtMethod=ON, name='Step-1', previous='Initial', timeIncrementationMethod=FIXED_USER_DEFINED_INC,
                                           timePeriod=total_time, userDefinedInc=dt_inc)

# Module - Step - Create Field Output
mdb.models['Model-1'].FieldOutputRequest(createStepName='Step-1', name='F-Output-1', numIntervals=f_out_n,
                                         variables=('ERV', 'LE', 'PE', 'PEEQ', 'S', 'SDV', 'TEMP', 'V', 'U'))

# Module - Step - Create History Output
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-1', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['FLayer-Inst'].sets['Set-FLayer'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-2', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['BLayer-Inst'].sets['Set-BLayer'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
if if_back == True:
    mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-3', numIntervals=h_out_n,
                                            rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['Back-Inst'].sets['Set-Back'], sectionPoints=DEFAULT,
                                            variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
#mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-3', numIntervals=h_out_n,
#                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['Foam-Inst'].sets['Set-Foam'], sectionPoints=DEFAULT,
#                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
if if_bone == True:
    mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-4', numIntervals=h_out_n,
                                            rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['Bone-Inst'].sets['Set-Bone'], sectionPoints=DEFAULT,
                                            variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-5', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['Impactor-Inst'].sets['Set-Impactor'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-6', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['ACLayer1-Inst'].sets['Set-ACLayer1'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-7', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['MLayer1-Inst'].sets['Set-MLayer1'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-8', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['ACLayer2-Inst'].sets['Set-ACLayer2'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-9', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['MLayer2-Inst'].sets['Set-MLayer2'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name='H-Output-10', numIntervals=h_out_n,
                                           rebar=EXCLUDE, region=mdb.models['Model-1'].rootAssembly.allInstances['MLayer3-Inst'].sets['Set-MLayer3'], sectionPoints=DEFAULT,
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'PEEQ', 'S11', 'S22', 'SDV', 'TEMP', 'V1', 'U1'))

# Module - Interaction - Create Constraint
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].surfaces['Surf-FLayer-xhi'],
                          name='Constraint-Tie-FLayerMLayer3', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].surfaces['Surf-MLayer3-xlo'],
                          thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].surfaces['Surf-MLayer3-xhi'],
                          name='Constraint-Tie-MLayer3MLayer2', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].surfaces['Surf-MLayer2-xlo'],
                          thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].surfaces['Surf-MLayer2-xhi'],
                          name='Constraint-Tie-MLayer2ACLayer1', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].surfaces['Surf-ACLayer1-xlo'],
                          thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].surfaces['Surf-ACLayer1-xhi'],
                          name='Constraint-Tie-ACLayer1MLayer1', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].surfaces['Surf-MLayer1-xlo'],
                          thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].surfaces['Surf-MLayer1-xhi'],
                          name='Constraint-Tie-MLayer1ACLayer2', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].surfaces['Surf-ACLayer2-xlo'],
                          thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON,
                          master=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].surfaces['Surf-ACLayer2-xhi'],
                          name='Constraint-Tie-ACLayer2BLayer', positionToleranceMethod=COMPUTED,
                          slave=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].surfaces['Surf-BLayer-xlo'],
                          thickness=ON, tieRotations=ON)
#mdb.models['Model-1'].Tie(adjust=ON,
#                          master=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].surfaces['Surf-BLayer-xhi'],
#                          name='Constraint-Tie-BLayerFoam', positionToleranceMethod=COMPUTED,
#                          slave=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].surfaces['Surf-Foam-xlo'],
#                          thickness=ON, tieRotations=ON)
#mdb.models['Model-1'].Tie(adjust=ON,
#                          master=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].surfaces['Surf-Foam-xhi'],
#                          name='Constraint-Tie-FoamBone', positionToleranceMethod=COMPUTED,
#                          slave=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].surfaces['Surf-Bone-xlo'],
#                          thickness=ON, tieRotations=ON)

# Module - Interaction - Create Interaction Property & Create Interaction
mdb.models['Model-1'].ContactProperty('IntProp-C-FLayerImpactor')
mdb.models['Model-1'].interactionProperties['IntProp-C-FLayerImpactor'].TangentialBehavior(formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-C-FLayerImpactor'].NormalBehavior(allowSeparation=ON,constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
mdb.models['Model-1'].SurfaceToSurfaceContactExp(clearanceRegion=None, createStepName='Step-1', datumAxis=None, initialClearance=OMIT, interactionProperty='IntProp-C-FLayerImpactor',
                                                 master= mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].surfaces['Surf-FLayer-xlo'],
                                                 mechanicalConstraint=KINEMATIC, name='Int-STSC-FLayerImpactor',
                                                 slave=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].surfaces['Surf-Impactor-xhi'],
                                                 sliding=FINITE)
#mdb.models['Model-1'].ContactExp(createStepName='Initial', name='Int-GC-FLayerImpactor')
#mdb.models['Model-1'].interactions['Int-GC-FLayerImpactor'].includedPairs.setValuesInStep(
#    addPairs=((mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].surfaces['Surf-Impactor-xhi'],
#               mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].surfaces['Surf-FLayer-xlo']), ),
#               stepName='Initial', useAllstar=OFF)
#mdb.models['Model-1'].interactions['Int-GC-FLayerImpactor'].contactPropertyAssignments.appendInStep(
#    assignments=((GLOBAL, SELF, 'IntProp-C-FLayerImpactor'), ), stepName='Initial')
if if_back == True:
    mdb.models['Model-1'].ContactProperty('IntProp-C-BackBLayer')
    mdb.models['Model-1'].interactionProperties['IntProp-C-BackBLayer'].TangentialBehavior(formulation=FRICTIONLESS)
    mdb.models['Model-1'].interactionProperties['IntProp-C-BackBLayer'].NormalBehavior(allowSeparation=ON,constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(clearanceRegion=None, createStepName='Step-1', datumAxis=None, initialClearance=OMIT, interactionProperty='IntProp-C-BackBLayer',
                                                    master= mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].surfaces['Surf-Back-xlo'],
                                                    mechanicalConstraint=KINEMATIC, name='Int-STSC-BackBLayer',
                                                    slave=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].surfaces['Surf-BLayer-xhi'],
                                                    sliding=FINITE)
if if_bone == True:
    mdb.models['Model-1'].ContactProperty('IntProp-C-BoneBLayer')
    mdb.models['Model-1'].interactionProperties['IntProp-C-BoneBLayer'].TangentialBehavior(formulation=FRICTIONLESS)
    mdb.models['Model-1'].interactionProperties['IntProp-C-BoneBLayer'].NormalBehavior(allowSeparation=ON,constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(clearanceRegion=None, createStepName='Step-1', datumAxis=None, initialClearance=OMIT, interactionProperty='IntProp-C-BoneBLayer',
                                                    master= mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].surfaces['Surf-Bone-xlo'],
                                                    mechanicalConstraint=KINEMATIC, name='Int-STSC-BoneBLayer',
                                                    slave=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].surfaces['Surf-BLayer-xhi'],
                                                    sliding=FINITE)

# Module - Load - Create Boundary Condition
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-FLayer-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-FLayer-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-FLayer-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-FLayer-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-BLayer-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].sets['Set-BLayer-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-BLayer-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].sets['Set-BLayer-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-BLayer-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].sets['Set-BLayer-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-BLayer-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].sets['Set-BLayer-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
if if_back == True:
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Back-ylo',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back-ylo'],
                                        u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Back-yhi',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back-yhi'],
                                        u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Back-zlo',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back-zlo'],
                                        u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Back-zhi',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back-zhi'],
                                        u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Foam-ylo',
#                                     region=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].sets['Set-Foam-ylo'],
#                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Foam-yhi',
#                                     region=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].sets['Set-Foam-yhi'],
#                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Foam-zlo',
#                                     region=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].sets['Set-Foam-zlo'],
#                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Foam-zhi',
#                                     region=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].sets['Set-Foam-zhi'],
#                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
if if_bone == True:
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Bone-ylo',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone-ylo'],
                                        u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Bone-yhi',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone-yhi'],
                                        u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Bone-zlo',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone-zlo'],
                                        u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Bone-zhi',
                                        region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone-zhi'],
                                        u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Impactor-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Impactor-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Impactor-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Impactor-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer1-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].sets['Set-ACLayer1-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer1-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].sets['Set-ACLayer1-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer1-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].sets['Set-ACLayer1-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer1-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].sets['Set-ACLayer1-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer1-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].sets['Set-MLayer1-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer1-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].sets['Set-MLayer1-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer1-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].sets['Set-MLayer1-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer1-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].sets['Set-MLayer1-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer2-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].sets['Set-ACLayer2-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer2-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].sets['Set-ACLayer2-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer2-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].sets['Set-ACLayer2-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-ACLayer2-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].sets['Set-ACLayer2-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer2-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].sets['Set-MLayer2-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer2-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].sets['Set-MLayer2-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer2-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].sets['Set-MLayer2-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer2-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].sets['Set-MLayer2-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer3-ylo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].sets['Set-MLayer3-ylo'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer3-yhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].sets['Set-MLayer3-yhi'],
                                     u1=UNSET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer3-zlo',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].sets['Set-MLayer3-zlo'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-MLayer3-zhi',
                                     region=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].sets['Set-MLayer3-zhi'],
                                     u1=UNSET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)

if if_back == True:
    if fixed_back == True:
        mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Back-xhi',
                                            region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back-xhi'],
                                            u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)

if if_bone == True:
    if fixed_bone == True:
        mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Bone-xhi',
                                            region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone-xhi'],
                                            u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)

# abq: Module - Load - Create Predefined Field
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-FLayer', region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-BLayer', region=mdb.models['Model-1'].rootAssembly.instances['BLayer-Inst'].sets['Set-BLayer'])
if if_back == True:
    mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                    name='Predefined Field-Temp-Back', region=mdb.models['Model-1'].rootAssembly.instances['Back-Inst'].sets['Set-Back'])
#mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
#                                  name='Predefined Field-Temp-Foam', region=mdb.models['Model-1'].rootAssembly.instances['Foam-Inst'].sets['Set-Foam'])
if if_bone == True:
    mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                    name='Predefined Field-Temp-Bone', region=mdb.models['Model-1'].rootAssembly.instances['Bone-Inst'].sets['Set-Bone'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-Impactor', region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-ACLayer1', region=mdb.models['Model-1'].rootAssembly.instances['ACLayer1-Inst'].sets['Set-ACLayer1'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-MLayer1', region=mdb.models['Model-1'].rootAssembly.instances['MLayer1-Inst'].sets['Set-MLayer1'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-ACLayer2', region=mdb.models['Model-1'].rootAssembly.instances['ACLayer2-Inst'].sets['Set-ACLayer2'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-MLayer2', region=mdb.models['Model-1'].rootAssembly.instances['MLayer2-Inst'].sets['Set-MLayer2'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-MLayer3', region=mdb.models['Model-1'].rootAssembly.instances['MLayer3-Inst'].sets['Set-MLayer3'])

mdb.models['Model-1'].Velocity(distributionType=MAGNITUDE, field='', name='Predefined Field-Vel-Impactor', omega=0.0,
                               region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor'],
                               velocity1=v_val, velocity2=0.0, velocity3=0.0)

# abq: Module - Mesh - Seed Part & Mesh Part
mdb.models['Model-1'].parts['FLayer'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['FLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['FLayer'].edges.getSequenceFromMask(('[#800 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['FLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['FLayer'].edges.getSequenceFromMask(('[#40 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['FLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['FLayer'].edges.getSequenceFromMask(('[#10 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['FLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['FLayer'].edges.getSequenceFromMask(('[#400 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['FLayer'].generateMesh()
mdb.models['Model-1'].parts['FLayer'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['FLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['BLayer'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['BLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['BLayer'].edges.getSequenceFromMask(('[#800 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['BLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['BLayer'].edges.getSequenceFromMask(('[#40 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['BLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['BLayer'].edges.getSequenceFromMask(('[#10 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['BLayer'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['BLayer'].edges.getSequenceFromMask(('[#400 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['BLayer'].generateMesh()
mdb.models['Model-1'].parts['BLayer'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['BLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
if if_back == True:
    mdb.models['Model-1'].parts['Back'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
    mdb.models['Model-1'].parts['Back'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['Back'].edges.getSequenceFromMask(('[#800 ]', ), ), size=half_mesh)
    mdb.models['Model-1'].parts['Back'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['Back'].edges.getSequenceFromMask(('[#40 ]', ), ), size=half_mesh)
    mdb.models['Model-1'].parts['Back'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['Back'].edges.getSequenceFromMask(('[#10 ]', ), ), size=half_mesh)
    mdb.models['Model-1'].parts['Back'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['Back'].edges.getSequenceFromMask(('[#400 ]', ), ), size=half_mesh)
    mdb.models['Model-1'].parts['Back'].generateMesh()
    mdb.models['Model-1'].parts['Back'].setElementType(
        elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                            hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
                ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
                ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
        regions=(mdb.models['Model-1'].parts['Back'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
#mdb.models['Model-1'].parts['Foam'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
#mdb.models['Model-1'].parts['Foam'].generateMesh()
#mdb.models['Model-1'].parts['Foam'].setElementType(
#    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
#                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
#               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
#               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
#    regions=(mdb.models['Model-1'].parts['Foam'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
if if_bone == True:
    mdb.models['Model-1'].parts['Bone'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
    mdb.models['Model-1'].parts['Bone'].generateMesh()
    mdb.models['Model-1'].parts['Bone'].setElementType(
        elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                            hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
                ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
                ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
        regions=(mdb.models['Model-1'].parts['Bone'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['Impactor'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['Impactor'].generateMesh()
mdb.models['Model-1'].parts['Impactor'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['Impactor'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['ACLayer1'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['ACLayer1'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer1'].edges.getSequenceFromMask(('[#800 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer1'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer1'].edges.getSequenceFromMask(('[#40 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer1'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer1'].edges.getSequenceFromMask(('[#10 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer1'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer1'].edges.getSequenceFromMask(('[#400 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer1'].generateMesh()
mdb.models['Model-1'].parts['ACLayer1'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['ACLayer1'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['MLayer1'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['MLayer1'].generateMesh()
mdb.models['Model-1'].parts['MLayer1'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['MLayer1'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['ACLayer2'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['ACLayer2'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer2'].edges.getSequenceFromMask(('[#800 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer2'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer2'].edges.getSequenceFromMask(('[#40 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer2'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer2'].edges.getSequenceFromMask(('[#10 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer2'].seedEdgeBySize(constraint=FINER, edges=mdb.models['Model-1'].parts['ACLayer2'].edges.getSequenceFromMask(('[#400 ]', ), ), size=half_mesh)
mdb.models['Model-1'].parts['ACLayer2'].generateMesh()
mdb.models['Model-1'].parts['ACLayer2'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['ACLayer2'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['MLayer2'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['MLayer2'].generateMesh()
mdb.models['Model-1'].parts['MLayer2'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['MLayer2'].cells.getSequenceFromMask(('[#1 ]', ), ), ))
mdb.models['Model-1'].parts['MLayer3'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['MLayer3'].generateMesh()
mdb.models['Model-1'].parts['MLayer3'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['MLayer3'].cells.getSequenceFromMask(('[#1 ]', ), ), ))

#mdb.models['Model-1'].parts['FLayer'].deleteMesh()
#mdb.models['Model-1'].parts['MLayer1'].deleteMesh()
#mdb.models['Model-1'].parts['BLayer'].deleteMesh()
#mdb.models['Model-1'].parts['Impactor'].deleteMesh()

# abq: * Menu - Model - Edit Attributes
mdb.models['Model-1'].setValues(absoluteZero=0.0)

# user: regenerate the assembly in Abaqus/CAE
mdb.models['Model-1'].rootAssembly.regenerate()

# abq: Module - Job - Create Job
mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
        explicitPrecision=DOUBLE_PLUS_PACK, historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE,
        model='Model-1', modelPrint=OFF, multiprocessingMode=THREADS, name='Job-1',
        nodalOutputPrecision=FULL, numCpus=n_cpu, numDomains=n_domain, parallelizationMethodExplicit=DOMAIN,
        queue=None, resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='../../../VUMAT/VUMAT-mDSGZ-SNRwBiNUM.f',
        waitHours=0, waitMinutes=0)

# user: submit the job in Abaqus/CAE
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

# user: save the model database in Abaqus/CAE
mdb.saveAs(pathName='CompShock.cae')
