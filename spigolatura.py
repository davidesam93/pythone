
import urllib.request                       # Importa la libreria per fare richieste HTTP
url = "https://lacordataescursionismo.it/" # URL del sito web da scaricare
risultato = urllib.request.urlopen(url)    # Apre la connessione e scarica il contenuto
theBytes = risultato.read()                # Legge i byte della risposta
text = theBytes.decode()                   # Converte i byte in stringa (HTML)

import bs4                                  # Importa BeautifulSoup per lavorare con l'HTML
doc = bs4.BeautifulSoup(text)               # Crea un oggetto BeautifulSoup che rappresenta l'HTML

doc.title.string = "NUOVO TITOLO DEL SITO"  # ✅ Modifica il contenuto del <title>

print(doc.prettify())                       # Stampa l’HTML ben formattato con il nuovo <title>

def naviga2(tag, indent):                   # Funzione ricorsiva per navigare nei tag HTML
    print(indent + tag.name.upper())        # Stampa il nome del tag con indentazione
    for stag in tag.contents:               # Cicla tra i contenuti (figli) del tag
        if type(stag) == bs4.element.Tag:   # Se è un altro tag HTML (non testo o spazi)
            naviga2(stag, indent + "  ")    # Richiama la funzione per quel figlio, aumentando l'indentazione

naviga2(doc, "")                            # Avvia la navigazione a partire dalla radice
