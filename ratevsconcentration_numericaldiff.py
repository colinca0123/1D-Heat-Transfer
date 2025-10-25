#File Reading
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#rate of reaction is in form -ra=kCa^n*Cb^m
#answer k is 2,n is 2, m is 1
df=pd.read_excel('C:/Users\colin\Downloads\Morepythoncoding\Conc vs time data_Lec19.xlsx')
#by default this reads the first sheet of the excel file
#if you want it to read the second sheet or so on 
#add 'Sheet2' after the path file followed by a comma
#converts the excel to matrix, so df is now a matrix
t=np.array(df['t']) #stores the values of time 
Ca=np.array(df['Ca'])#stores the values of Ca
Cb=np.array(df['Cb']) #stores the value of Cb

#the reason why we want to store it as numpy is so we can do mathmatical operations easy on the matrix 
#for example Ca*2 will return the value of each element in Ca multiplied by 2

#Numerical Differentiation for finding the rate of reaction
dt=t[1]-t[0] #delta t is 0.1
dtinv=1/dt #division makes code run long to make it efficient we can multiply
#derivatives
#first point: can't do central difference because the point behind 0 is -0.1 for time. 
ra=[(Ca[1]-Ca[0])*dtinv] #this is for the first point so we must do foward difference method
for i in range(1,len(Ca)-1):
    ra.append((Ca[i+1]-Ca[i-1])*0.5*dtinv) #reduces number of division operations for more efficient programming
#Ca[i+1] so we can get the next time index which is 0.1 away
ra.append((Ca[-1]-Ca[-2])*dtinv) #backward difference method
#ra gives instantnous rate of change of the cocentration of a at each time interval
ra=-1*np.array(ra) #-ra

#now we have the rate of A we can evaluate the constants n, m, 
#our rate of reaction is in the form -ra=kCa^n*Cb^m
#take ln of both sides
#we find that the b parameter vecotr contains B0, B1, B2 which correspons to ln(k), n, and m respectivley.
#Y corresponds to ln(-ra)
y=np.log(ra) #in numpy np.log(x) is the natural log ln(x)
#y is len(ra)X1
x1=np.log(Ca)
x2=np.log(Cb)
const=np.ones(len(Ca))
#X matrix
x=np.column_stack((const,x1,x2)) #stacks 1-D arrays as columns into a 2-D aary
#so now this is a matrix len(t)X3
# xr=np.row_stack((const, x1, x2)) #this makes a 1-D array of (N,) turn into (1,N)
#so const, x1, x2, all have 1D array of (len(t),) so row stack makes it (1,len(t))
#so it merges all the const, x1, and x2 so will be 3Xlen(t)

#To find b(The paramater vector) 
#b=(xt*x)^-1*xT*y
#Transposing and multiplying matrix 
xt=np.transpose(x) #now this is 3Xlen(t)
#Matrix Multiplication
xtx=np.dot(xt,x)
#size 3 by 3
#Taking Inverse of a Matrix
xtxi=np.linalg.inv(xtx)
xty=np.dot(xt,y) #matrix multiplication of xt and y
#xt has size 3Xlen(t) and y has len(t) by 1 
#so xty has size 3 by 1

#Solving for b
b=np.dot(xtxi, xty) #this is a 3 by 1
#this gives answer to k,n, and m
k=np.exp(b[0])
n=b[1]
m=b[2]
print('The parameters of k, n, and m are', k, n, m)

#Parity plot, plot between predicted variable and actual plot and comparing it to y=x

bt=np.column_stack(b) #this is now 1 by 3

ypre=np.dot(bt, xt) #y is now 1 by len(t)

ypret=np.transpose(ypre) #now this is len(t) by 1

# plt.scatter(y, ypret, label='Predicted')
# plt.plot(y, y, label='Actual')
# plt.title('Parity Plot')
# plt.show()




#Coupled ODE for Ca and Cb
#delta t is 0.1 denoted dt
# Ca0=[Ca[0]] #[1]
# Cb0=[Cb[0]]#[0.5]
# t0=[t[0]]#[0]
# tf=0.5
# while t0[-1]<tf: 
#     dca=-k*Ca0[-1]**n*Cb0[-1]**m #number
#     dcb=-k*Ca0[-1]**n*Cb0[-1]**m #number
#     Ca0.append(Ca0[-1]+dt*dca) #new Ca0 value is 1+0.1*-1.13178
#     #Ca0 list is now [1,0.8868,
#     Cb0.append(Cb0[-1]+dt*dcb)
#     t0.append(t0[-1]+dt)
    
# plt.scatter(t0,Ca0, label='Predicted')
# plt.plot(t[:6],Ca[:6], label='Actual')
# plt.title('Predicted Rate of Change for Concentration of A')
# plt.show()

# plt.scatter(t0, Cb0, label='Predicted')
# plt.plot(t[:6], Cb[:6], label='Actual')
# plt.title('Predicted Rate of Change for Concentration of B ')
# plt.show()

#This is the less efficient way because I am storing Ca0 and Cb0 as a matrix 
#How to make it more efficient 
Ca0=[1]
Cb0=[0.5]
t0=[0]
tf=0.5
while t0[-1]<tf:
    y=np.array([Ca0[-1], Cb0[-1]])
    f=np.array([-k*y[0]**n*y[1]**m, -k*y[0]**n*y[1]**m])
    y_next=y+dt*f #gets the next y value
    Ca0.append(y_next[0])
    Cb0.append(y_next[1])
    t0.append(t0[-1]+dt)
    print(y_next)

plt.scatter(t0, Ca0, label='Predicted')
plt.plot(t[:6], Ca[:6], label='Actual') #access index 0 to 5 
plt.title('Predicted concentration of A over time')
plt.xlabel('Time')
plt.grid(True)
plt.show()

plt.scatter(t0, Cb0, label='Predicted')
plt.plot(t[:6], Cb[:6], label='Actual')
plt.title('Predicted Concnetration of B over time')
plt.xlabel('Time')
plt.grid(True)
plt.show()

# f=np.array[]
