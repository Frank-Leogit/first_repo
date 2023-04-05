
from utility.formule import somma_due_numeri as s
from utility.formule import area_quadrato as aq
from utility.formule import area_triangolo as at
from utility.formule import perimetro_quadrato as pq
from utility.formule import perimetro_triangolo as pt
from utility.formule import cubo
from utility.classes import Persona
from utility.classes import Cubo
from utility.classes import Math
import numpy as np
import pandas as pd
from tabulate import tabulate as tab
# i = True
# while i:
#     scelta = int(input("Dimmi cosa vuoi calcolare:\n1 Area qudrato\n2 Area Triangolo\n3 Perimetro Triangolo\n4 Perimetro quadrato\n0 Esci\n"))
#     if scelta==1:
#             print(aq())
#     elif scelta==2:
#             print(at())
#     elif scelta==3:
#             print(pt())
#     elif scelta==4:
#             print(pq())
#     elif scelta==5:
#             print(pq())
#     elif scelta==0:
#            break
#     else:
#             print("Scelta non valida")
#     i = input("Vuoi continuare?(y/n)").lower().strip()=='y'
    
# _, volume = cubo(3)
# print(f"La superficie è: {superficie}")
# print(f"La volume è: {volume}")
gianfranco = Persona('Gianfranco',28)
print(gianfranco.nome)
print(gianfranco.eta)
gianfranco2 = Persona('Gianfranco',28)
print(gianfranco == gianfranco2)
print(gianfranco)
print(gianfranco2)
print(gianfranco.nome == gianfranco2.nome)
dado = Cubo()
print(f"superficie faccia:{dado.sup_faccia()} superficie:{dado.superficie()} area:{dado.volume()}   {dado.triple(3)}")
# rizzo = Math()
# print(rizzo.mean())
np.random.seed(667)
mydata = np.random.randint(0,101,(4,3))
print(mydata)
df = pd.DataFrame(mydata, index=['CA','NY','AZ','TX'],columns=['jan','feb','mar'])
print(tab(df,headers='keys', tablefmt='psql'))
df.info()
#!wget
df = pd.read_csv('Spotify_Youtube.csv')
print(tab(df,headers='keys', tablefmt='psql'))
