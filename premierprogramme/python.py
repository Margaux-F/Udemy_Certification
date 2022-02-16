def f1(n):
  if n > 5:
    return
  ligne = ""
  for i in range(n):
    ligne += "#"
  print(ligne)
  f1(n+1)
 
f1(1)