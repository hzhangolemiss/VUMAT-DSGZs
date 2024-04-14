# -- Global parameters --
Parameters, xscale=1e6, xname=$Time\ (\mu s)$, marksnumber=1, title=CompShock.py, crop=True

# -- Velocity curve --
Plot_Velocity, yscale=1e-3, yname=$Velocity\ (m/s)$, legendlocate=topleft, Job-1_v1_n2_Bo.plot

# -- Displacement --
Plot_Displacement, yscale=1, yname=$Displacement\ (mm)$, legendlocate=topleft, Job-1_u1_n3_Fr.plot, Job-1_u1_n1_Ip.plot

# -- Density curve --
#Plot_Density, yname=$Density\ \rho\ (ton/mm^3)$, legendlocate=topright, Job-1_density_e2.plot

# -- Stress curve --
Plot_Stress, yscale=1, yname=$Stress\ \sigma_{ii}\ (MPa)$, legendlocate=bottomright, Job-1_s11_e2_Bo.plot

# -- Log Strain curve --
#Plot_LogStrain, yscale=1, yname=$Log\ Strain\ \epsilon_{11}\ (MPa)$, legendlocate=bottomright, Job-1_le11_e2.plot

# -- von Mises curve --
#Plot_VonMises, yscale=1, yname=$von\ Mises\ Stress\ \overline{\sigma}\ (MPa)$, legendlocate=bottomright, Job-1_mises_e2.plot

# -- Plastic Strain curve --
#Plot_PlasticStrain, yname=$Equivalent\ Plastic\ Strain\ \overline{\varepsilon}^{pl}$, legendlocate=bottomright, Job-1_peeq_e2.plot

# -- Plastic Strain Rate curve --
#Plot_PlasticStrainRate, yscale=1, yname=$Equivalent\ Plastic\ Strain\ Rate\ (/s)$, legendlocate=topleft, Job-1_dotpeeq_e2.plot

# -- Volumetric Strain Rate curve --
#Plot_VolumetricStrainRate, yscale=1, yname=$Volumetric\ Strain\ Rate\ (/s)$, legendlocate=topleft, Job-1_erv_e3.plot, Job-1_erv_e2.plot, Job-1_erv_e1.plot

# -- Combine curve for von Mises Stress vs. Plastic Strain
#Plot_Combination, xscale=1, xname=$Equivalent\ Plastic\ Strain\ \overline{\varepsilon}^{pl}$, yscale=1, yname=$von\ Mises\ Stress\ \overline{\sigma}\ (MPa)$, legendlocate=bottomright, Job-1_peeq_mises.plot
