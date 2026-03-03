import random

class Domanda:

    # COSTRUTTORE
    def __init__(self, testo: str, livello_difficolta: int, risposta_corretta: str,
                 risposta_errata1: str, risposta_errata2: str, risposta_errata3: str):
        # Con livello_difficolta: int sto solo dicendo all’IDE e ai lettori del codice
        # “questo dovrebbe essere un intero”, ma Python non lo verifica né lo converte.
        # Python è un linguaggio dinamico: accetta qualsiasi valore e controlla i tipi solo quando li usi.
        # Java invece è statico: se il costruttore richiede un , il compilatore non ti permette di passare una stringa.
        # Il controllo avviene prima dell’esecuzione.

        self.testo = testo
        # Impongo che livello_difficolta sia un intero, sennò è resta una stringa.
        self.livello_difficolta = int(livello_difficolta)
        self.risposta_corretta = risposta_corretta
        # Creo una lista di risposte_errate
        self.risposte_errate = [risposta_errata1, risposta_errata2, risposta_errata3]


    # Stampa dell'oggetto
    def __str__(self):
        return (
            f"Domanda: {self.testo}\n"
            f"Difficoltà: {self.livello_difficolta}\n"
            f"Corretta: {self.risposta_corretta}\n"
            f"Errate: {self.risposte_errate}\n"
        )


    def get_risposte_mescolate(self):
            # Creo una nuova lista di 4 elementi concatenando tutte le risposte
            risposte = [self.risposta_corretta] + self.risposte_errate[:]
            # nuova lista = lista (1 elemento) + lista (3 elementi) COPIA di quella originale

            # Mischio gli elementi della lista risposte
            random.shuffle(risposte)
            # shuffle() -> operazione IN PLACE = MODIFICARE L'OGGETTO ORIGINALE, infatti
            # shuffle() non restituisce nulla, perché lavora in place

            # Ritorno la lista mischiata risposte
            return risposte