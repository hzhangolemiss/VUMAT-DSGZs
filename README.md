# VUMAT-DSGZs
Data for a research article published in MDPI

Zhang, H.; Rajendran, A.M.; Shukla, M.K.; Nouranian, S.; Al-Ostaz, A.; Larson, S.; Jiang, S. Simulation of the Dynamic Responses of Layered Polymer Composites under Plate Impact Using the DSGZ Model. J. Compos. Sci. 2024, 8, 159. https://doi.org/10.3390/jcs8050159

All *.py scripts are compatible with Abaqus 2021 version. For Abaqus 2022 and later versions, some auguments in several functions need to be modified. For example, in the "Interaction" module, "master" and "slave" in the "Create Constraints" and "Create Interaction Properties and Create Interactions" items should be changed to "main" and "secondary" respectively.
