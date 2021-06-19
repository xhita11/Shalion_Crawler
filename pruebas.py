import re

llista_preus = [
'$17.99',
'$3.49',
'$14.99',
'$8.49',
'$39.99'
]

for preu in llista_preus:
    currency = (re.sub('[0-9]', '', preu)).replace('.','')
    print(preu, currency)

#cambio local   