# Øving 7 - Oppgave 6c
# Håkon Ødegård Løvdal

import reverse_string

def palindrom(string):
        if string == reverse_string.reverse_string(string):
                return True
        else:
                return False

print(palindrom('abbo'))
