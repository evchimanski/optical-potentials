
# User manual:
 - Just modify input.inp and run python get_KD_opt_par.py

 Status :
- Only volume terms for both imaginary and real part are currently implemented


######################################################################################

The KD-optical potential for nucleon–nucleus reactions is usually cast as
$$
\mathcal{U}\left(r,E\right)= -\mathcal{V}_{V}(r,E)-i\mathcal{W}_{V}(r,E)-i\mathcal{W}_{D}(r,E)+\mathcal{V}_{SO}(r,E) \, \vec{l}\cdot \vec{\sigma}  +i\mathcal{W}_{SO}(r,E) \, \vec{l}\cdot \vec{\sigma} + \mathcal{V}_{C}(r) 
$$
where $\mathcal{V}_{V,S}$ and $\mathcal{W}_{V,D,SO}$ are the real and imaginary components of the volume-central ($V$), surface-central ($D$) and spin–orbit ($SO$) potentials, respectively. $E$ is the laboratory energy of the incident particle in MeV. All components are separated in $E$-dependent well depths, $V_{ V}$ , $W_{ V}$ , $W_{ D}$ , $V_{ SO}$ , and $W_{ SO}$ ,

$$
  \mathcal{V}_{V}\left(r,E\right)=V_{V}(E)f(r,R_{V},a_{V}),
$$

$$
  \mathcal{W}_{V}\left(r,E\right)=W_{V}(E)f(r,R_{V},a_{V}),
$$
$$
  \mathcal{W}_{D}\left(r,E\right)=-4a_{D}W_{D}(E)\frac{d}{dr}f(r,R_{D},a_{D}),
$$

$$  
\mathcal{V}_{SO}\left(r,E\right)=V_{SO}(E)\left ( \frac{\hbar c }{m_{\pi}c}\right )^{2} \frac{1}{r}\frac{d}{dr}f(r,R_{SO},a_{SO}),
$$

$$
  \mathcal{W}_{SO}\left(r,E\right)=W_{SO}(E)\left ( \frac{\hbar c }{m_{\pi}c}\right )^{2} \frac{1}{r}\frac{d}{dr}f(r,R_{SO},a_{SO}),
$$

and a radial Wood-Saxon form factor
$$
f \left(r,R_{i},a_{i} \right)=\frac{1}{e^{(r-R_{i})/a_{i}} +1}.
$$
$A$ is the atomic mass number, $R_{i} = r_{i}A^{ 1/3} $ radius and $a_{ i}$ diffuseness parametes. Coulomb potential is as an uniformly charged sphere
where $Z$ is the charge of the target and $z$ the charge of projectile. $R_{ C} = r_{ C} A^{ 1/3}$ the Coulomb radius.

# Reference:
 - For more information see: Koning and Delaroche. Nuclear Physics A 713 (2003) 231-310.
