# ODB for single layer model

# -- Velocity --
#TimeHistory, job=Job-1, value=V1,      name=v1_n2,      region=Node FLAYER-INST.230
TimeHistory, job=Job-1, value=V1,      name=v1_n1,      region=Node FLAYER-INST.5

# -- Density --
#TimeHistory, job=Job-1, value=DENSITY, name=density_e2, region=Element FLAYER-INST.104 Int Point 1

# -- Stress --
#TimeHistory, job=Job-1, value=S11,     name=s11_e3,     region=Element FLAYER-INST.188 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e3,     region=Element FLAYER-INST.188 Int Point 1
TimeHistory, job=Job-1, value=S11,     name=s11_e2,     region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2,     region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e1,     region=Element FLAYER-INST.24 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e1,     region=Element FLAYER-INST.24 Int Point 1

# -- Log Strain --
#TimeHistory, job=Job-1, value=LE11,     name=le11_e3,   region=Element FLAYER-INST.104 Int Point 1
TimeHistory, job=Job-1, value=LE11,     name=le11_e2,   region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e1,   region=Element FLAYER-INST.104 Int Point 1

# -- von Mises Stress --
#TimeHistory, job=Job-1, value=MISES,   name=mises_e3,   region=Element FLAYER-INST.104 Int Point 1
TimeHistory, job=Job-1, value=MISES,   name=mises_e2,   region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=MISES,   name=mises_e1,   region=Element FLAYER-INST.104 Int Point 1

# -- Plastic Strain --
#TimeHistory, job=Job-1, value=SDV1,    name=peeq_e3,    region=Element FLAYER-INST.188 Int Point 1
TimeHistory, job=Job-1, value=SDV1,    name=peeq_e2,    region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=SDV1,    name=peeq_e1,    region=Element FLAYER-INST.24 Int Point 1

# -- Plastic Strain Rate --
#TimeHistory, job=Job-1, value=SDV2,    name=dotpeeq_e3, region=Element FLAYER-INST.188 Int Point 1
#TimeHistory, job=Job-1, value=SDV2,    name=dotpeeq_e2, region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=SDV2,    name=dotpeeq_e1, region=Element FLAYER-INST.24 Int Point 1

# -- Volumetric Strain Rate --
#TimeHistory, job=Job-1, value=ERV,     name=erv_e3,     region=Element FLAYER-INST.188 Int Point 1
TimeHistory, job=Job-1, value=ERV,     name=erv_e2,     region=Element FLAYER-INST.104 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e1,     region=Element FLAYER-INST.24 Int Point 1

# -- von Mises Stress vs. Plastic Strain --
#DataCombine, job=Job-1, value=SDV1, value=MISES, name=peeq, name=mises, region=Element FLAYER-INST.104 Int Point 1
