from pint import UnitRegistry
import sympy as sym
ur=UnitRegistry()
# m_flowrate=5000*ur.pounds/ur.hour #flow rate of milk
# sym.var(['M1', 'M2', 'M3', 'M4', 'M5'])
# M1=5000
# M5=32.2034
# eqns=[sym.Eq(M1,M2+M3+M4+M5), sym.Eq(0.0385*M1,0.0325*M2+0.010*M3+0*M4+1*M5), sym.Eq(0.0885*M1, 0.0825*M2+0.010*M3+1*M4+0*M5)]
# solution=sym.solve(eqns)
# print(solution)
# #Price
# price_M2=solution[M2]*0.2148
# price_M4=solution[M4]*1.98
# price_M5=M5*1.77
# total_price=price_M2+price_M4+price_M5
# print(total_price, 'Dollars/hour')
# price_M1=total_price/M1
# print(price_M1, 'dollars/pound')


#Figure out max revenue by graphing
M1, M2, M3, M4, M5=sym.var(['M1', 'M2', 'M3', 'M4', 'M5'])
eqns=[sym.Eq(M1,M2+M3+M4+M5), sym.Eq(0.0385*M1,0.0325*M2+0.001*M3+0*M4+1*M5), sym.Eq(0.0885*M1, 0.0825*M2+0.0825*M3+1*M4+0*M5),sym.Eq(M1,5000)]
solution=sym.solve(eqns)
print(solution)
# Find values for M5
# m2_plot=sym.plot(solution[M2], (M5,0,200))
# #plots M2=5951.131-31.6406*M5 for M5 (xvalues from 0 to 200)
# m3_plot=sym.plot(solution[M3], (M5, 0, 2000))
# m4_plot=sym.plot(solution[M4], (M5, 0, 200))
print('The values of M5 are:',sym.solve(solution[M2]),sym.solve(solution[M3]),sym.solve(solution[M4]))
# sym.solve() solves for M5 in the equation of M2, M3, and M4
M5_min=sym.solve(solution[M3])[0] #32.2033
M5_max=sym.solve(solution[M2])[0] #187.737
#ignore negative because can't have negative mass flow rate

#Revenue
#Find the Highest price the processor 
#can pay for raw milk 
#and generate positive cash flow

Revenue=0.2148*(solution[M2])+0.1601*(solution[M3])+1.95*(solution[M4])+1.77*M5
print(Revenue) #in dollars/hour
Revenue_plot=sym.plot(Revenue, (M5, M5_min, M5_max))
#plots Revenue plot from minimum of M5 to maximum of M5
#We are trying to find the maximum price of the processor
#for raw milk so that it can still generate positive cash flow
#Cash flow=Revenue-Cost (Cost is the price for rawmilk)
#we want to Maximize Revenue in this case and set to Cash Flow to 0
#so use M5_Max
max_revenue=Revenue.subs(M5, M5_max)
print('Maximum Revenue is:',max_revenue, 'dollars')
#max cost
max_cost=max_revenue/5000
print('Maximum Raw Milk Cost is:', max_cost, 'dollars')

opt=[sym.Eq(M5, M5_max)]
new_solution=sym.solve(eqns+opt)
for i in new_solution.keys():
    print('{}:{} lb/hour'.format(i, new_solution[i].round(2)))









#.subs method in Sympy
# experiment=solution[M4].subs(M5, 5) #this substitutes M5 with 5 in the equation for M4
# print(experiment)
