from random import randint as random

def randlist():
  v = []
  sizeOf = random(3, 20)
  for i in range(2, sizeOf):
    v.append(random(0, 1000))

  return v

def insertSort(v):
  for i in range(1, len(v)):
    c = i
    
    while v[c] < v[c-1]:
      if c > 0:
          v[c-1], v[c] = v[c], v[c-1]
          c -= 1
        
      else:
        break
  
  return(v)

print("Digite 1 para escolher os numeros")
print("Digite 2 para numeros aleatorios")
mode = int(input())

if mode == 1:
  v=[]
  n = int(input("Numero de termos: "))
  for i in range (0, n, 1):
    x = int(input())
    v.append(x)
    
  print("Original: {}".format(v))
  print("Ordenada: {}".format(insertSort(v)))

elif mode == 2:
  v = randlist()
  print("Original: {}".format(v))
  print("Ordenada: {}".format(insertSort(v)))
