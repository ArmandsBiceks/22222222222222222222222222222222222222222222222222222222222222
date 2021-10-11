recepte1 = {"cukurs":2.22, "kaneles":1.53, "aboli":5.22, "udens":0.50}
cenas1 ={'cukurs':2.22, 'kaneles':1.53, 'aboli':5.22, 'udens':0.50}

def izmaksas_receptei(recepte,cenas):

 summa=0
 for sastavdala in recepte:
  daudzums = recepte[sastavdala]
  summa += daudzums* cenas[sastavdala]
 return summa

def izmaksas_kopa(abolu_svars, recepte, cenas):
  izmaksas_kg = izmaksas_receptei(recepte, cenas)
  /recepte["aboli"]

  ievarijuma_izmaksas = abolu_svars* izmaksas_kg
  return ievarijuma_izmaksas
  print(izmaksas_kopa(15.0,recepte1,cenas1))
