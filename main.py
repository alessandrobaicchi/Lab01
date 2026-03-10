import random
from domanda import Domanda

# list[Domanda] è un type hint che serve a dire a PyCharm che lista contiene oggetti Domanda e
# così posso usare la dot notation con gli oggetti di tipo Domanda
lista_domande: list[Domanda] = []

# ---------------------------------------------------------
# LETTURA DELLE DOMANDA DAL FILE domande.txt
# ---------------------------------------------------------

with open("domande.txt", "r", encoding="utf-8") as f:
    riga = f.readline()
    conta_righe = 0
    lista_righe_temp = []

    while riga:     # Continua finché la riga non è vuota
        riga = riga.strip()
        # strip() "pulisce la riga", cioè rimuove spazi indesiderati

        if not riga: # Se la riga è vuota. Nota: in Python "" è considerato FALSE
            riga = f.readline()
            # Il continue "salta tutto il resto del ciclo e lo ricomincia dall'inizio"
            continue

        # Creo "il blocco domanda: domanda + risposte"
        lista_righe_temp.append(riga)
        conta_righe = conta_righe + 1

        if conta_righe == 6:
            # Ci sono 6 righe --> creo l'oggetto Domanda
            testo, livello, corretta, e1, e2, e3 = lista_righe_temp
            # Creo un pacchetto di 6 variabili a cui assegno le 6 righe appena lette. Poi, uso questo
            # pacchetto per creare la domanda.
            domanda = Domanda(testo, livello, corretta, e1, e2, e3)
            lista_domande.append(domanda)

            # Resetto per la prossima domanda
            lista_righe_temp.clear()
            conta_righe = 0

        riga = f.readline()



# ---------------------------------------------------------
# CREO UN DIZIONARIO CON LE DOMANDE DIVISE PER LIVELLO
# ---------------------------------------------------------

# Creo un DIZIONARIO vuoto
# dict[int, list[Domanda]] è un type hint -> la chiave del dizionario è il livello (int)
# e il valore del dizionario è una lista di oggetti Domanda
domande_per_livello: dict[int, list[Domanda]] = {}
# Scorro tutte le domande
for d in lista_domande:
    # Per ogni domanda prendo il suo livello
    livello = d.livello_difficolta
    # Se il livello non c'è ancora nel dizionario -> lo creo
    if livello not in domande_per_livello:
        # Creo una nuova voce nel dizionario con chiave = livello e
        # valore = lista (momentaneamente) vuota
        domande_per_livello[livello] = []
    # Aggiungo la domanda nella lista nel livello corretto
    domande_per_livello[livello].append(d)
# Ora calcolo il livello massimo
livello_massimo = max(domande_per_livello.keys())



# ---------------------------------------------------------
# CREO UNA PARTITA
# ---------------------------------------------------------
livello_corrente = 0
punteggio = 0

print("\n--- INZIO PARTITA ---\n")

while livello_corrente <= livello_massimo:
    # Prendo le domande del livello corrente
    lista_livello_corrente = domande_per_livello[livello_corrente]

    # Estraggo una domanda casuale da lista_livello_corrente
    domanda_fatta: Domanda = random.choice(lista_livello_corrente)
    # Per far capire a PyCharm il tipo di domanda_fatta serve anche il type hint.

    # Della domanda_fatta mischio le risposte (è una lista di stringhe)
    risposte = domanda_fatta.get_risposte_mescolate()

    # Stampo la domanda di domanda_fatta
    print(f"\nLivello {livello_corrente} - {domanda_fatta.testo}")

    # Stampo le risposte di domanda_fatta
    for i, r in enumerate(risposte):
        print(f"{i+1} {r}")

    # Chiedo al giocatore la sua risposta
    risposta_utente = int(input("Inserisci la tua risposta: "))

    # Verifico la risposta del giocatore
    if risposte[risposta_utente-1] == domanda_fatta.risposta_corretta:
        print("Risposta corretta!")
        punteggio += 1
        livello_corrente += 1
    else:
        print(f"Risposta sbagliata! La risposta corretta è {domanda_fatta.risposta_corretta}")
        break

print("\n--- GAME OVER ---\n")
print(f"Hai totalizzato {punteggio} punti!")


# ---------------------------------------------------------
# LISTA CON I PUNTEGGI
# ---------------------------------------------------------
nickname = input("Inserisci tua nickname: ")

# 1) Leggo i punteggi esistenti in punti.txt
lista_punteggi = []     # Lista vuota

try:    # Provo ad aprire punti.txt in lettura
    with open("punteggio.txt", "r", encoding="utf-8") as f:
        for riga in f:      # Per ogni riga
            riga = riga.strip()     # Tolgo gli "spazi"
            if not riga:        # Se la riga è vuota "salta al prossimo giro del ciclo for"
                continue
            nome, punti = riga.split()  # Divido nome e punti
            lista_punteggi.append((nome, int(punti)))   # Aggiungo a lista_punteggi
except FileNotFoundError:
    pass    # Se il file non esiste ignora l'errore

# 2) Aggiungo il NUOVO punteggio a lista_punteggi
lista_punteggi.append((nickname, punteggio))

# 3) Ordina il punteggio in modo decrescente
lista_punteggi.sort(key=lambda x: x[1], reverse=True)
# LAMBDA è una FUNZIONE ANONIMA, cioè una funzione senza nome. In pratica, sto dicendo a Python di ordinare
# lista_punteggi usando questa funzione anonima. Tale funzione anonima prende il secondo elemento della tupla.
# Quindi: x[0] = nome, x[1] = punteggio,
# Ad esempio: "Luca", 5

# 4) Riscrivo il file punti.txt
with open("punti.txt", "w", encoding="utf-8") as f:
    for nome, punti in lista_punteggi:
        f.write(f"{nome} {punti}\n")

print("Punteggio salvato correttamente!")

