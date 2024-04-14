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
# Single Layer Test Model
# **********

# parallel run
n_cpu = 4
n_domain = n_cpu

# Unit: MPa, mm, s, ton
ydim = 0.4
zdim = 0.4
mesh_size = 0.2

Flayer_dim = 10.0
Impactor_dim = 5.0
#FI_gap = 2*mesh_size
FI_gap = 0.0

v_val = 50000.0

total_time = 2e-05
dt_inc = 5e-09

f_out_n = int(0.1*total_time/dt_inc)
f_out_n = max(f_out_n, 1)
h_out_n = int(0.1*total_time/dt_inc)
h_out_n = max(h_out_n, 1)

# **********

# Part - Create Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), point2=(abs(Flayer_dim), ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='FLayer', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['FLayer'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0-abs(FI_gap), 0.0), point2=(-abs(Impactor_dim), ydim))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Impactor', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Impactor'].BaseSolidExtrude(depth=zdim, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

# abq: * Menu - Tools - Surface - Create
mdb.models['Model-1'].parts['FLayer'].Surface(name='Surf-FLayer-xlo', side1Faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['FLayer'].Surface(name='Surf-FLayer-xhi', side1Faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#4 ]', ), ))
mdb.models['Model-1'].parts['Impactor'].Surface(name='Surf-Impactor-xlo', side1Faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
mdb.models['Model-1'].parts['Impactor'].Surface(name='Surf-Impactor-xhi', side1Faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#4 ]', ), ))

# abq: * Menu - Tools - Set - Create
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-FLayer-xlo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-FLayer-xhi')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-FLayer-ylo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-FLayer-yhi')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-FLayer-zlo')
mdb.models['Model-1'].parts['FLayer'].Set(faces=mdb.models['Model-1'].parts['FLayer'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-FLayer-zhi')
mdb.models['Model-1'].parts['FLayer'].Set(cells=mdb.models['Model-1'].parts['FLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-FLayer')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-Impactor-xlo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#4 ]', ), ), name='Set-Impactor-xhi')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#8 ]', ), ), name='Set-Impactor-ylo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Set-Impactor-yhi')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#20 ]', ), ), name='Set-Impactor-zlo')
mdb.models['Model-1'].parts['Impactor'].Set(faces=mdb.models['Model-1'].parts['Impactor'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-Impactor-zhi')
mdb.models['Model-1'].parts['Impactor'].Set(cells=mdb.models['Model-1'].parts['Impactor'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-Impactor')

# abq: Module - Property - Create Material
mdb.models['Model-1'].Material(name='JCS-OFHCCu')
mdb.models['Model-1'].materials['JCS-OFHCCu'].Density(table=((8.96e-09, ), ))
mdb.models['Model-1'].materials['JCS-OFHCCu'].SpecificHeat(table=((383000000.0, ), ))
mdb.models['Model-1'].materials['JCS-OFHCCu'].Elastic(table=((44700.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['JCS-OFHCCu'].Plastic(hardening=JOHNSON_COOK,scaleStress=None, table=((90.0, 292.0, 0.310, 1.09, 1356.0, 298.0), ))
mdb.models['Model-1'].materials['JCS-OFHCCu'].plastic.RateDependent(table=((0.025, 1.0), ), type=JOHNSON_COOK)
mdb.models['Model-1'].materials['JCS-OFHCCu'].Eos(table=((3933000.0, 1.49, 2.00), ), type=USUP)
mdb.models['Model-1'].materials['JCS-OFHCCu'].plastic.setValues(scaleStress=None)

mdb.models['Model-1'].Material(name='JCS-Al6061')
mdb.models['Model-1'].materials['JCS-Al6061'].Density(table=((2.70e-09, ), ))
mdb.models['Model-1'].materials['JCS-Al6061'].SpecificHeat(table=((896000000.0, ), ))
mdb.models['Model-1'].materials['JCS-Al6061'].Elastic(table=((25900.0, ), ), type=SHEAR)
mdb.models['Model-1'].materials['JCS-Al6061'].Plastic(hardening=JOHNSON_COOK,scaleStress=None, table=((290.0, 204.0, 0.350, 1.34, 858.0, 298.0), ))
mdb.models['Model-1'].materials['JCS-Al6061'].plastic.RateDependent(table=((0.011, 1.0), ), type=JOHNSON_COOK)
mdb.models['Model-1'].materials['JCS-Al6061'].Eos(table=((5350000.0, 1.34, 2.0), ), type=USUP)
mdb.models['Model-1'].materials['JCS-Al6061'].plastic.setValues(scaleStress=None)

mdb.models['Model-1'].Material(name='JCS-Steel4340')
mdb.models['Model-1'].materials['JCS-Steel4340'].Density(table=((7.83e-09, ), ))
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
mdb.models['Model-1'].Material(name='mDSGZ-PMMA2015H')
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].Density(table=((1.2e-09, ), ))
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].SpecificHeat(table=((1466000000.0, ), ))
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].Depvar(n=7)
mdb.models['Model-1'].materials['mDSGZ-PMMA2015H'].UserMaterial(mechanicalConstants=(3200.0, 0.38,
                                                                                     2.7, 1.582, -0.760, 2.443, 0.03, 20, 800, 18, 0.138,
                                                                                     0.9, 1.2e-09, 1500000000.0, 0.0))

# Ref.DOI: 10.1007/s12206-015-0922-3
mdb.models['Model-1'].Material(name='mDSGZ-PC2015H')
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].Density(table=((1.15e-09, ), ))
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].SpecificHeat(table=((1500000000.0, ), ))
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].Depvar(n=7)
mdb.models['Model-1'].materials['mDSGZ-PC2015H'].UserMaterial(mechanicalConstants=(2100.0, 0.38,
                                                                                   8.97, 1.127, -0.161, 1.35, 0.007, 100, 465, 65, 0.093,
                                                                                   0.9, 1.15e-09, 1500000000.0, 0.0))

#mdb.models['Model-1'].Material(name='HF-PU')
#mdb.models['Model-1'].materials['HF-PU'].Density(table=((3.4e-11, ), ))
#mdb.models['Model-1'].materials['HF-PU'].Hyperfoam(n=3, poisson=None, table=((0.99, 29.78, 0.0008454, -2.48, 0.0138, -0.0088, 0.0, 0.0, 0.0), ))
#mdb.models['Model-1'].materials['HF-PU'].MullinsEffect(table=((1.5001, 0.002, 0.9), ))

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
mdb.models['Model-1'].HomogeneousSolidSection(material='ABQ_JH2-SiC', name='Section-Flayer', thickness=None)
mdb.models['Model-1'].parts['FLayer'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['FLayer'].sets['Set-FLayer'],
                                                        sectionName='Section-Flayer', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(material='JCS-OFHCCu', name='Section-Impactor', thickness=None)
mdb.models['Model-1'].parts['Impactor'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE,
                                                        region=mdb.models['Model-1'].parts['Impactor'].sets['Set-Impactor'],
                                                        sectionName='Section-Impactor', thicknessAssignment=FROM_SECTION)

# Module - Assembly - Create Instance
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='FLayer-Inst', part=mdb.models['Model-1'].parts['FLayer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Impactor-Inst', part=mdb.models['Model-1'].parts['Impactor'])

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
                                           variables=('ERV', 'DENSITY', 'LE11', 'MISES', 'S11', 'S22', 'SDV', 'TEMP', 'V1'))

# Module - Interaction - Create Interaction Property & Create Interaction
mdb.models['Model-1'].ContactProperty('IntProp-C-FLayerImpactor')
mdb.models['Model-1'].interactionProperties['IntProp-C-FLayerImpactor'].TangentialBehavior(formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-C-FLayerImpactor'].NormalBehavior(allowSeparation=ON,constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
mdb.models['Model-1'].SurfaceToSurfaceContactExp(clearanceRegion=None, createStepName='Step-1', datumAxis=None, initialClearance=OMIT, interactionProperty='IntProp-C-FLayerImpactor',
                                                 master= mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].surfaces['Surf-FLayer-xlo'],
                                                 mechanicalConstraint=KINEMATIC, name='Int-STSC-FLayerImpactor',
                                                 slave=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].surfaces['Surf-Impactor-xhi'],
                                                 sliding=FINITE)
#smdb.models['Model-1'].ContactExp(createStepName='Initial', name='Int-GC-FLayerImpactor')
#smdb.models['Model-1'].interactions['Int-GC-FLayerImpactor'].includedPairs.setValuesInStep(
#s    addPairs=((mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].surfaces['Surf-Impactor-xhi'],
#s               mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].surfaces['Surf-FLayer-xlo']), ),
#s               stepName='Initial', useAllstar=OFF)
#smdb.models['Model-1'].interactions['Int-GC-FLayerImpactor'].contactPropertyAssignments.appendInStep(
#s    assignments=((GLOBAL, SELF, 'IntProp-C-FLayerImpactor'), ), stepName='Initial')


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

# abq: Module - Load - Create Predefined  Field
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-FLayer', region=mdb.models['Model-1'].rootAssembly.instances['FLayer-Inst'].sets['Set-FLayer'])
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(298.0, ),
                                  name='Predefined Field-Temp-Impactor', region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor'])

mdb.models['Model-1'].Velocity(distributionType=MAGNITUDE, field='', name='Predefined Field-Vel-Impactor', omega=0.0,
                               region=mdb.models['Model-1'].rootAssembly.instances['Impactor-Inst'].sets['Set-Impactor'],
                               velocity1=v_val, velocity2=0.0, velocity3=0.0)

# abq: Module - Mesh - Seed Part & Mesh Part
mdb.models['Model-1'].parts['FLayer'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['FLayer'].generateMesh()
mdb.models['Model-1'].parts['FLayer'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['FLayer'].cells.getSequenceFromMask(('[#1 ]', ), ), ))

mdb.models['Model-1'].parts['Impactor'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['Impactor'].generateMesh()
mdb.models['Model-1'].parts['Impactor'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN,
                        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON),
               ElemType(elemCode=C3D6, elemLibrary=EXPLICIT),
               ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)),
    regions=(mdb.models['Model-1'].parts['Impactor'].cells.getSequenceFromMask(('[#1 ]', ), ), ))

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
        queue=None, resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='../../../VUMAT/VUMAT-gDSGZ-SNRwBiNUM.f',
        waitHours=0, waitMinutes=0)

# user: submit the job in Abaqus/CAE
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

# user: save the model database in Abaqus/CAE
mdb.saveAs(pathName='CompShock.cae')
