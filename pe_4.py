
q = range(999,99,-1)

pals = []

for x in q:
  for y in q:
    product = x * y
    if str(product) == str(product)[::-1]:
        pals.append(product)

print max(pals)
