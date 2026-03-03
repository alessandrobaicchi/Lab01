import random

from domanda import Domanda

f = open("domande.txt", "r")

riga = f.readline()
conta_righe = 0
lista_righe_temp = []
# list[Domanda] è un type hint che serve a dire a PyCharm che lista contiene oggetti Domanda e
# così posso usare la dot notation con gli oggetti di tipo Domanda
lista_domande: list[Domanda] = []

while riga != "":
    riga = riga.strip()
    # strip() "pulisce la riga", cioè rimuove spazi indesiderati

    if (riga == ""):
        riga = f.readline()
        # Il continue "salta tutto il resto del ciclo e lo ricomincia dall'inizio"
        continue

    lista_righe_temp.append(riga)
    conta_righe = conta_righe + 1

    if(conta_righe == 6):
        # Ci sono 6 righe --> creo l'oggetto Domanda
        domanda = Domanda(lista_righe_temp[0], lista_righe_temp[1], lista_righe_temp[2], lista_righe_temp[3],
                          lista_righe_temp[4], lista_righe_temp[5])
        lista_domande.append(domanda)

        # Resetto per la prossima domanda
        lista_righe_temp.clear()
        conta_righe = 0

    riga = f.readline()

f.close()

# for d_Temp in lista_domande:
#     print(d_Temp)
#
# risposte = domanda.get_risposte_mescolate()
# #print(risposte)
# for r in risposte:
#     print(r)

# Creo una lista filtrata con le domande di un certo livello di difficoltà
lista_domande_livello: list[Domanda] = []
for d in lista_domande:
    if (d.livello_difficolta == 0):
       lista_domande_livello.append(d)

# for d in lista_domande_livello:
#     print(d)

# Estraggo dalla lista filtrata lista_domande_livello una domanda
domanda_fatta: Domanda = random.choice(lista_domande_livello)
# Per far capire a PyCharm che tipo è domanda_fatta serve anche il type hint sulla variabile estratta, oltre ad
# averlo fatto su lista_domande_livello

# Di quella domanda mischio le risposte (è una lista di stringhe)
risposte = domanda_fatta.get_risposte_mescolate()
print(domanda_fatta.testo)
for i, r in enumerate(risposte):
    print(f"{i+1} {r}")

risposta_utente = int(input("Inserisci la tua risposta: "))
if risposte[risposta_utente-1] == domanda_fatta.risposta_corretta:
    print("Risposta corretta!")
else:
    print("Risposta sbagliata!")
