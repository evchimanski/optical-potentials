## EVC Jan 2021
# #Only works for proton induced reactions :: All standard units : MeV, fm.
# see Koning and Delaroche. Nuclear Physics A 713 (2003) 231-310
# May4 : neutron induced reactions added

import numpy as np
import matplotlib.pyplot as plt


def WS(r,R,a):
	return 1./(np.exp((r-R)/a)+1.)



def vn4():
	return 7*10**(-9)

def wn2(Anuc):
	out = 73.55 + 0.0795*Anuc
	return out

def dn2(Anuc):
	out = 0.0180 + 0.003802/(1.+np.exp((Anuc-156)/8.))
	return out

def dn3():
	return 11.5

def vnso1(Anuc):
	return 5.922 + 0.0030*Anuc

def vnso2():
	return 0.0040
	
def wnso1():
	return -3.1
	
def wnso2():
	return 160.





def vq1(Znuc,Anuc,q):
	Nnuc= Anuc-Znuc
	if q == 1 :
		out = 59.30+21.0*(Nnuc-Znuc)/Anuc - 0.024*Anuc
	else :
		out = 59.30-21.0*(Nnuc-Znuc)/Anuc - 0.024*Anuc

	return out

def vq2(Anuc,q):
	if q == 1 :
		out = 0.007067 + 4.23*10**(-6)*Anuc
	else:
		out = 0.007228 - 1.48*10**(-6)*Anuc

	return out

def vq3(Anuc,q):
	if q == 1 :
		out = 1.729*10**(-5) + 1.136*10**(-8)*Anuc
	else :
		out = 1.994*10**(-5) - 2.0*10**(-8)*Anuc

	return out

def vp4():
	return vn4()

def wq1(Anuc,q):
	if q == 1 :
		out = 14.667 + 0.009629*Anuc
	else :
		out = 12.195 + 0.0167*Anuc

	return out

def wp2(Anuc):
	out = wn2(Anuc)
	return out

def dq1(Znuc,Anuc,q):
	Nnuc= Anuc-Znuc
	if q == 1:
		out = 16.0 + 16.0*(Nnuc-Znuc)/Anuc
	else:
		out = 16.0 - 16.0*(Nnuc-Znuc)/Anuc

	return out

def dp2(Anuc):
	out = dn2(Anuc)
	return out

def dp3():
	return dn3()
	
def vpso1(Anuc):
	out=vnso1(Anuc)
	return out

def vpso2(Anuc):
	out=vnso2()
	return out

def wpso1():
	return wnso1()
	
def wpso2():
	return wnso2()
	
def Eqf(Anuc,q):
	if q == 1:
		out=-8.4075 + 0.01378*Anuc
	else:
		out=-11.2814 + 0.02646*Anuc	
	return out

def rC(Anuc):
	out=0.
	out= 1.198+0.697*Anuc**(-2./3)+12.994*Anuc**(-5./3)
	return out
	
def barVC(Znuc,Anuc):
	out=(1.73/rC(Anuc))*Znuc*Anuc**(-1./3)
	return out



#
def rV(Anuc):
	return 1.3039 - 0.4054*Anuc**(-1./3)
	
def aV(Anuc):
	return 0.6778 - 1.487*10**(-4)*Anuc

def rD(Anuc):
	return 1.3424 - 0.01585*Anuc**(1./3)
	
def aD(Anuc):
	return 0.5187 - 5.205*10**(-4)*Anuc

def rSO(Anuc):
	return 1.1854 - 0.647*A**(-1./3)

def aSO(Anuc):
	return 0.59


# strenghts 	
def V_V(E):
	out=0.
	Ediff=E-Eqf(Anuc,q)
	t1 = vq1(Znuc,Anuc,q)*( 1. - vq2(Anuc,q)*Ediff + vq3(Anuc,q)*Ediff**2 - vp4()*Ediff**3 )
	t2 = barVC(Znuc,Anuc)*vq1(Znuc,Anuc,q)*( vq2(Anuc,q) - 2.*vq3(Anuc,q)*Ediff + 3.*vp4()*Ediff**2)
	out=t1+t2
	return out

def W_V(E):
	out=0.
	Ediff=E-Eqf(Anuc,q)
	if abs(Ediff) == 0.:
		out=0.
	else:
		out=wq1(Anuc,q)*((Ediff)**2)/((Ediff)**2 + wp2(Anuc)**2)
		
	return out

def W_D(E):
	out=0.
	Ediff=E-Eqf(Anuc,q)
	if abs(Ediff) == 0.:
		out=0.
	else:
		out=dq1(Znuc,Anuc,q)*((Ediff)**2)/((Ediff)**2 + dp3()**2)*np.exp(-dp2(Anuc)*Ediff)
	return out

def V_SO(E):
	out=0.
	Ediff=E-Eqf(Anuc,q)
	out=vpso1(Anuc)*np.exp(-vpso2()*Ediff)
	return out

def W_SO(E):
	out=0.
	Ediff=E-Eqf(Anuc,q)

	if abs(Ediff) == 0.:
		out=0.
	else:
		out=wpso1()*((Ediff)**2)/((Ediff)**2 + wpso2()**2)
	return out





f1 = open('input.inp', 'r')
n=0
for line in f1:
    p = line.split()
    if n==0 : Znuc=float(p[0]);Anuc=float(p[1])
    if n==1 : E=float(p[0])
    if n==2 : flag_frame=p[0]
    if n==3 : q=float(p[0])
    
    n=n+1
    
f1.close()

#Anuc = 90
#Znuc = 40
#Emu	 = 80.

if flag_frame == 'CM':
	Emu=E
	Elab=Emu/(Anuc/(Anuc+1.0))  # Ei_mu=(A/(A+1.0d0))*Ei
else:
    	Elab=E
    	Emu=Elab*(Anuc/(Anuc+1.0))  # Ei_mu=(A/(A+1.0d0))*Ei


outp=open('output.out','w')
print(" ELAB [MeV]      ECM[MeV]      Znuc    Anuc   ",file=outp)

print(" %8.4f        %8.4f        %i      %i   "%(Elab,Emu,Znuc,Anuc),file=outp)

print("VV         rV    rV*A^(1/3)   aV             -- Volume: REAL",file=outp)
V0=V_V(Emu)
r0=rV(Anuc)
R=r0*Anuc**(1./3)
a0=aV(Anuc)
print("%7.5f  %7.5f  %7.5f  %7.5f"%(V0,r0,R,a0),file=outp)


print("WV         rV    rV*A^(1/3)   aV             -- Volume: Imaginary",file=outp)
W0=W_V(Emu)
print("%7.5f  %7.5f  %7.5f  %7.5f"%(W0,r0,R,a0),file=outp)

print("WD         rD    rD*A^(1/3)   aD      -4aD   -- Surface: Imaginary",file=outp)

a0=aD(Anuc)
m4a0=-4.*a0
r0=rD(Anuc)
R=r0*Anuc**(1./3)

W0=W_D(Emu)
print("%7.5f  %7.5f  %7.5f  %7.5f  %7.5f"%(W0,r0,R,a0,m4a0),file=outp)

if q == 1:
	print("Coulomb:",file=outp)
	print("rC       barVC",file=outp)
	r0 = rC(Anuc)
	Vc = barVC(Znuc,Anuc)
	print("%7.5f  %7.5f"%(r0,Vc),file=outp)

	print("Ef = %7.5f "%Eqf(Anuc,q),file=outp)



print("SO: to be added",file=outp)

outp.close()

