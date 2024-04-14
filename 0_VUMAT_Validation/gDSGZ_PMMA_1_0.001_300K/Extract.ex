# VUMAT ODB Numerical Newton-Raphson with embedded Bisection
#TimeHistory, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=DENSITY, name=density, region=Element CUBIC-1.1 Int Point 1
#TimeHistory, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=SDV1, name=peeq, region=Element CUBIC-1.1 Int Point 1
#TimeHistory, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=MISES, name=mises, region=Element CUBIC-1.1 Int Point 1
#TimeHistory, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=TEMP, name=temp, region=Element CUBIC-1.1 Int Point 1
#TimeHistory, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=DT, name=dt, region=Assembly ASSEMBLY
DataCombine, job=CubicElement-Radial_VUMAT_SNRwBiNUM, value=SDV1, value=MISES, name=peeq, name=mises, region=Element CUBIC-1.1 Int Point 1
