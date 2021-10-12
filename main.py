'''
ARMANDS
12.10.21
'''
"""
sakas_vienadi("Liela Lama") -----> True
sakas_vienadi("Maza Lama") ------> False
"""

"""
Noderīgas metodes:

.split()
.lower()
"""
def vienadi(teksts):
  teksts = teksts.lover().split()
  if teksts[1][0]:
    return True
  else:
    return False
print(vienadi(teksts)):
def vienadi(teksts):
  teksts = teksts.lower().split()

  if teksts[0][0] == teksts[1][0]:
    return True
  else:
    return False

print(vienadi("Liela Lama"))
print(vienadi("Maza Lama"))

def vienadi(teksts):
  teksts = teksts.lower().split()

  return teksts[0][0] == teksts[1][0]

print(vienadi("Liela Lama"))
print(vienadi("Maza Lama"))
