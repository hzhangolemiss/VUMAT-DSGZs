# ODB for single layer model

# -- Velocity --
#TimeHistory, job=Job-1, value=V1,      name=v1_n2_Fr,      region=Node FLAYER-INST.77
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_Fr,      region=Node FLAYER-INST.5
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_M1,      region=Node MLAYER1-INST.5
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_M2,      region=Node MLAYER2-INST.5
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_M3,      region=Node MLAYER3-INST.5
#TimeHistory, job=Job-1, value=V1,      name=v1_n2_Bs,      region=Node BLAYER-INST.77
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_Bs,      region=Node BLAYER-INST.5
#TimeHistory, job=Job-1, value=V1,      name=v1_n1_Ip,      region=Node IMPACTOR-INST.5
TimeHistory, job=Job-1, value=V1,      name=v1_n2_Bo,      region=Node BONE-INST.185

# -- Displacement --
TimeHistory, job=Job-1, value=U1,      name=u1_n3_Fr,      region=Node FLAYER-INST.149
TimeHistory, job=Job-1, value=U1,      name=u1_n1_Ip,      region=Node IMPACTOR-INST.5

# -- Density --
#TimeHistory, job=Job-1, value=DENSITY, name=density_e2, region=Element FLAYER-INST.104 Int Point 1

# -- Stress --
#TimeHistory, job=Job-1, value=S11,     name=s11_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e3_Bo,     region=Element BONE-INST.124 Int Point 1
TimeHistory, job=Job-1, value=S11,     name=s11_e2_Bo,     region=Element BONE-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=S11,     name=s11_e1_Bo,     region=Element BONE-INST.44 Int Point 1

#TimeHistory, job=Job-1, value=S22,     name=s22_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e3_Bo,     region=Element BONE-INST.124 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e2_Bo,     region=Element BONE-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=S22,     name=s22_e1_Bo,     region=Element BONE-INST.44 Int Point 1

# -- Log Strain --
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e3_Bo,     region=Element BONE-INST.124 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e2_Bo,     region=Element BONE-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=LE11,     name=le11_e1_Bo,     region=Element BONE-INST.44 Int Point 1

# -- von Mises Stress --
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e3_Bo,     region=Element BONE-INST.124 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e2_Bo,     region=Element BONE-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=MISES,     name=mises_e1_Bo,     region=Element BONE-INST.44 Int Point 1

# -- Plastic Strain --
#TimeHistory, job=Job-1, value=PEEQ,     name=peeq_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=SDV1,     name=peeq_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=SDV1,     name=peeq_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=SDV1,     name=peeq_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=SDV1,     name=peeq_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=PEEQ,     name=peeq_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=PEEQ,     name=peeq_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=PEEQ,     name=peeq_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1

# -- Plastic Strain Rate --
#TimeHistory, job=Job-1, value=SDV2,     name=dotpeeq_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=SDV2,     name=dotpeeq_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=SDV2,     name=dotpeeq_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=SDV2,     name=dotpeeq_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1

# -- Volumetric Strain Rate --
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_Fr,     region=Element FLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_M1,     region=Element MLAYER1-INST.44 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e1_M1,     region=Element MLAYER1-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_M2,     region=Element MLAYER2-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e1_M2,     region=Element MLAYER2-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_M3,     region=Element MLAYER3-INST.64 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e1_M3,     region=Element MLAYER3-INST.4 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_Bs,     region=Element BLAYER-INST.36 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e3_Bo,     region=Element BONE-INST.124 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e2_Bo,     region=Element BONE-INST.84 Int Point 1
#TimeHistory, job=Job-1, value=ERV,     name=erv_e1_Bo,     region=Element BONE-INST.44 Int Point 1

# -- von Mises Stress vs. Plastic Strain --
#DataCombine, job=Job-1, value=SDV1, value=MISES, name=peeq, name=mises, region=Element FLAYER-INST.104 Int Point 1
