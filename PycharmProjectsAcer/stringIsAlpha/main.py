spam = '12tupple is not yours to use, 17Minute ride from Home is preety far away'
alphaLet = ''
for i in spam:
  if not i.isalpha() :
     alphaLet = alphaLet +i
  else:
      break
print(alphaLet)