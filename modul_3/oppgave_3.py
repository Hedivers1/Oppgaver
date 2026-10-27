brus = 24.90
smørbrød = 45 
banan = 8.50

total = brus + smørbrød + banan
print("Totalpris:", total)

total_med_moms = total * 1.25
print("Totalpris med moms:", total_med_moms)

pris_per_person = total_med_moms / 4
print("Pris per person:", pris_per_person)

prisforskjell = smørbrød - banan
print("Prisforskjell:", prisforskjell)

##Reflekter og noter:

# Smørbrød er et heltall, brus er et desimaltall. Hva slags datatype ble svaret da du la dem sammen?
# Svaret ble et desimaltall, fordi når man legger sammen et heltall og et desimaltall, blir resultatet et desimaltall.

# Hva ble datatypen da du delte på fire? Ble du overrasket?
# Datatypen ble et desimaltall, fordi når man deler et tall på et annet tall, blir resultatet et desimaltall. Jeg ble ikke overrasket.

# Hvorfor er det en fordel å bruke variabler i stedet for å skrive tallene på nytt hver gang? Tenk på hva som skjer hvis prisen på brus endrer seg.
# Det er en fordel å bruke variabler fordi det gjør koden mer lesbar og enklere å vedlikeholde. Hvis prisen på brus endrer seg, trenger man bare å endre verdien i variabelen, og alle beregninger som bruker den variabelen vil automatisk oppdatere seg. 
# Dette sparer tid og reduserer risikoen for feil.
