import math

def createDiamand(largeur):
  diamond = "\n"

  if largeur % 2 == 0 : 
    largeur += 1

  start = math.ceil(largeur / 2)
  end = math.ceil(largeur / 2)

  # partie haute du carreau

  for i in range(1, math.ceil(largeur / 2) + 1 ) :

    for j in range(1,largeur +1 ) :
      if j >= start and j <= end  :
        diamond += "x"
      else:
        diamond += "."

    diamond += "\n"
    start -= 1
    end += 1
  
  # partie basse du carreau
  start = 2
  end = largeur - 1 
  for i in range(1, math.floor(largeur / 2) + 1):

    for j in range(1,largeur+1) :
      if j >= start and j <= end :
        diamond += "x"
      else:
        diamond += "."
    diamond += "\n"
    start += 1
    end -= 1

  print(diamond)


createDiamand(12) 