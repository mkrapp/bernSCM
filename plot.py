import matplotlib.pyplot as plt
import pandas as pd
import sys

fnm = sys.argv[1]

col_names = ["glob_temp_dev", "RF_tot", "RF_CO2", "RF_nonCO2", "RF_budget", "ocean_heat_uptake", "co2_atm", "co2_seasurf", "atm_CO2_change", "fossil_CO2_em", "budget_C_uptake", "ocean_C_uptake", "land_C_uptake", "NPP", "RH", "LandC", "dDIC", "fdeep"]
df = pd.read_table(fnm,comment='#',header=None,index_col=0,delim_whitespace=True, names=col_names)
df.index.name = 'time'
df.plot(subplots=True, layout=(6, 3), figsize=(6, 6), sharex=True)
plt.show()
