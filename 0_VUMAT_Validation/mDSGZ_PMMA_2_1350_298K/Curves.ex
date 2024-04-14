# Global parameters
Parameters, xscale=0.01, xname=$Elongation\ along\ loading\ direction\ (mm)$, marksnumber=15, title=One Cubic Element Radial Test (compression at 50\%), crop=True

# Density curve
#Plot_Density, yname=$Density\ \rho\ (ton/mm^3)$, legendlocate=topright, removename=-density, CubicElement-Radial_VUMAT_SNRwBiNUM_density.plot

# Plastic strain curve
#Plot_PlasticStrain, yname=$Equivalent\ plastic\ strain\ \overline{\varepsilon}^{pl}$, legendlocate=bottomright, removename=-peeq, CubicElement-Radial_VUMAT_SNRwBiNUM_le22.plot

# von Mises curve
#Plot_VonMises, yname=$von\ Mises\ stress\ \overline{\sigma}\ (MPa)$, legendlocate=bottomright, removename=-mises, CubicElement-Radial_VUMAT_SNRwBiNUM_mises.plot

# Temperature curve
#Plot_Temperature, yname=$Temperature\ (K)$, legendlocate=bottomright, removename=-temp, CubicElement-Radial_VUMAT_SNRwBiNUM_temp.plot

# Timestep curve
#Plot_TimeStep, yname=$TimeStep\ increment\ \Delta t\ (s)$, legendlocate=topright, removename=-dt, CubicElement-Radial_VUMAT_SNRwBiNUM_dt.plot

# Combine curve for plastic strain vs von Mises
Plot_Combination, xscale=1, xname=$Equivalent\ plastic\ strain\ \overline{\varepsilon}^{pl}$, yname=$von\ Mises\ stress\ \overline{\sigma}\ (MPa)$, legendlocate=bottomright, removename=-peeq_mises, CubicElement-Radial_VUMAT_SNRwBiNUM_peeq_mises.plot
