import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from skfuzzy import control as ctrl
# degiskenlerin tanımı
# * uzaklik değerleri [0, 10] m cinsinden bu aralıkta.
# *Hiz değerleri [0, 10] m/s cinsinden bu aralıkta.
# * Fren kuvveti değerleri [0, 24] N cinsinden bu aralıkta.

uzaklik= np.arange(0, 11, 1)
hiz = np.arange(0, 11, 1)
Fren_Kuvvet = np.arange(0, 25, 1)
#bulanık mantık üye fonksiyonlarının tanımı
Uzaklik_Cok_yakin = fuzz.trimf(uzaklik, [0, 0, 4])
Uzaklik_yakin = fuzz.trapmf(uzaklik, [2, 4, 6, 8])
Uzaklik_uzak = fuzz.trimf(uzaklik, [6, 10, 10])
####################################################
hiz_cok_yavas = fuzz.trapmf(hiz, [0, 0, 1, 2])
hiz_yavas = fuzz.trapmf(hiz, [1, 2, 3, 4])
hiz_op = fuzz.trapmf(hiz, [3, 4, 5, 6])
hiz_hizli = fuzz.trapmf(hiz, [5, 6, 7, 8])
hiz_cok_hizli = fuzz.trapmf(hiz, [7, 8, 10,10])
####################################################
Fren_cok_azalt = fuzz.trimf(Fren_Kuvvet, [0, 4, 8])
Fren_biraz_azalt = fuzz.trimf(Fren_Kuvvet, [4, 8, 12])
Tepki_yok = fuzz.trimf(Fren_Kuvvet, [8, 12, 16])
Fren_biraz_arttir = fuzz.trimf(Fren_Kuvvet, [12, 16, 20])
Fren_cok_arttir = fuzz.trimf(Fren_Kuvvet, [16, 20, 24])

# üyelik fonksiyonlarının ve degerlerin gorselleştirilmesi grafikle

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 10))
ax0.plot(uzaklik, Uzaklik_Cok_yakin, 'b', linewidth=1.5, label='Cok Yakin')
ax0.plot(uzaklik, Uzaklik_yakin, 'g', linewidth=1.5, label='Yakin')
ax0.plot(uzaklik, Uzaklik_uzak, 'r', linewidth=1.5, label='Uzak')
ax0.set_title('Araclar_Arasi_Uzaklik')
ax0.legend()
ax1.plot(hiz, hiz_cok_yavas, 'b', linewidth=1.5, label='Cok Yavas')
ax1.plot(hiz, hiz_yavas, 'y', linewidth=1.5, label='Yavas')
ax1.plot(hiz, hiz_op, 'g', linewidth=1.5, label='Optimum')
ax1.plot(hiz, hiz_hizli, 'r', linewidth=1.5, label='Hizli')
ax1.plot(hiz, hiz_cok_hizli, 'k', linewidth=1.5, label='Cok Hizli')
ax1.set_title('Hiz')
ax1.legend()
ax2.plot(Fren_Kuvvet, Fren_biraz_azalt, 'b', linewidth=1.5, label='Biraz Azalt')
ax2.plot(Fren_Kuvvet, Fren_cok_azalt, 'y', linewidth=1.5, label='Cok-Azalt')
ax2.plot(Fren_Kuvvet, Tepki_yok, 'g', linewidth=1.5, label='Tepki Yok')
ax2.plot(Fren_Kuvvet, Fren_biraz_arttir, 'r', linewidth=1.5, label='Biraz Arttir')
ax2.plot(Fren_Kuvvet, Fren_cok_arttir, 'k', linewidth=1.5, label='Cok Arttir')
ax2.set_title('Fren_Kuvvet_Miktari')
ax2.legend()

# üst ve sağ eksenler için
for ax in (ax0, ax1, ax2):
 ax.spines['top'].set_visible(False)
 ax.spines['right'].set_visible(False)
 ax.get_xaxis().tick_bottom()
 ax.get_yaxis().tick_left()
plt.tight_layout()
plt.show() # giriş üyelerinin göstermek icin 
#uzaklik=np.arange(0, 11, 1)
uzaklik = ctrl.Antecedent(uzaklik, 'uzaklik')
hiz = ctrl.Antecedent(hiz, 'hiz')
Fren_Kuvvet = ctrl.Consequent(Fren_Kuvvet,'Fren_Kuvvet')
###################################################

# bulanık mantık üye fonk tanımı

uzaklik['Cok_yakin'] = fuzz.trimf(uzaklik.universe, [0, 0, 4])
uzaklik['yakin'] = fuzz.trapmf(uzaklik.universe, [2, 4, 6, 8])
uzaklik['uzak'] = fuzz.trimf(uzaklik.universe, [6, 10, 10])
#uzaklik.view()
####################################################
hiz['cok_yavas'] = fuzz.trapmf(hiz.universe, [0, 0, 1, 2])
hiz['yavas'] = fuzz.trapmf(hiz.universe, [1, 2, 3, 4])
hiz['op'] = fuzz.trapmf(hiz.universe, [3, 4, 5, 6])
hiz['hizli'] = fuzz.trapmf(hiz.universe, [5, 6, 7, 8])
hiz['cok_hizli'] = fuzz.trapmf(hiz.universe, [7, 8, 10,10])
#hiz.view()
####################################################
Fren_Kuvvet['CAZ'] = fuzz.trimf(Fren_Kuvvet.universe, [0, 4, 8])
Fren_Kuvvet['BAZ'] = fuzz.trimf(Fren_Kuvvet.universe, [4, 8, 12])
Fren_Kuvvet['TY'] = fuzz.trimf(Fren_Kuvvet.universe, [8, 12, 16])
Fren_Kuvvet['BART'] = fuzz.trimf(Fren_Kuvvet.universe, [12, 16, 20])
Fren_Kuvvet['CART'] = fuzz.trapmf(Fren_Kuvvet.universe, [16, 20, 24, 24])
#Fren_Kuvvet.view()

# fonk ve değerlerin görselleştirilmesi

#uzaklik.view()

rule1 = ctrl.Rule(uzaklik ['Cok_yakin'] , Fren_Kuvvet['CART'])
rule2 = ctrl.Rule(uzaklik ['yakin'] & hiz['cok_hizli'] , Fren_Kuvvet['BART'])
rule3 = ctrl.Rule(uzaklik ['yakin'] & hiz['op'] , Fren_Kuvvet['BART'])
rule4 = ctrl.Rule(uzaklik['uzak'] & hiz['op'] , Fren_Kuvvet['TY'])
rule5 = ctrl.Rule(uzaklik['uzak'] & hiz['yavas'] , Fren_Kuvvet['BAZ'])
rule6 = ctrl.Rule(uzaklik['uzak'] & hiz['cok_yavas'] , Fren_Kuvvet['CAZ'])
fren_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
frenleme = ctrl.ControlSystemSimulation(fren_ctrl)
# API ve antecetend ile girdileri control sisteme atma
# aynı anda biecok girdi icin .inputs(dict_of_data)
frenleme.input['uzaklik'] =3
frenleme.input['hiz'] = 8

# sayıların crunchlanması
frenleme.compute()
print (frenleme.output['Fren_Kuvvet'])
Fren_Kuvvet.view(sim=frenleme)

""""""
sim = ctrl.ControlSystemSimulation(fren_ctrl, flush_after_run=24 * 24 + 1)
# bu dogrular ile simulasyon yapa
upsampled = np.linspace(0, 10, 25)
x, y = np.meshgrid(upsampled, upsampled)
z = np.zeros_like(x)


for i in range(10):
 for j in range(10):
  sim.input['uzaklik'] = x[i, j]
  sim.input['hiz'] = y[i, j]
  sim.compute()
 z[i, j] = sim.output['Fren_Kuvvet']
# 3d sonuc alma
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 3d çizim için 
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
linewidth=0.4, antialiased=True)
cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)
ax.view_init(10, 20)
plt.show()

