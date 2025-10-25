from pint import UnitRegistry
ur=UnitRegistry()
fuel_consump=30*ur.mile/ur.gallon
fuel_consump.ito(ur.mile/ur.ml)
density_octane=0.74*ur.grams/ur.ml
mm_octane=114.23*ur.grams/ur.moles
#mass of octane per mile
m_octane=density_octane/fuel_consump
print('Amount of octane needed per mile is {}'.format(m_octane))
#convert to moles
n_octane=m_octane/mm_octane
print('Amount of octane need per mile in moles is {}'.format(n_octane))
#Equation tells that 1 mole of octane generates 8 moles of CO2
n_CO2=n_octane*8
mm_CO2=44.01*ur.grams/ur.moles
m_CO2=n_CO2*mm_CO2
print('Amount of CO2 generated per mile driven is {} '.format(m_CO2))



#How much CO2 is generated per mile driven by an electric car

average_tesla=0.367*ur.kilowatt_hour/ur.mile
NG=117*ur.pounds/(1e6*ur.BTU)
elec=10400*ur.BTU/ur.kilowatt_hour

#Mass of CO2 per 1 kilowatt hour
m_CO2=NG*elec
m_CO2.ito(ur.grams/ur.kilowatt_hour)
print('Mass of CO2 per kilowatt hour is {}'.format(m_CO2))

#How much CO2 tesla produces in grams/mile
tesla_CO2=m_CO2*average_tesla*5/4
print(tesla_CO2)