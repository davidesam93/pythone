
import urllib.request                       # Importa la libreria per fare richieste HTTP
url = "https://lacordataescursionismo.it/"  # URL del sito web da scaricare
risultato = urllib.request.urlopen(url)     # Apre la connessione e scarica il contenuto
theBytes = risultato.read()                 # Legge i byte della risposta
text = theBytes.decode()                    # Converte i byte in stringa (HTML)

import bs4                                  # Importa BeautifulSoup per lavorare con l'HTML
doc = bs4.BeautifulSoup(text)               # Crea un oggetto BeautifulSoup che rappresenta l'HTML

doc.title.string = "NUOVO TITOLO DEL SITO"  # ✅ Modifica il contenuto del <title>

print(doc.prettify())                       # Stampa l’HTML ben formattato con il nuovo <title>


"""
lista=dir(bs4.element.Tag)
for met in lista:
  if not met.startswith("_"):               # Filtra i metodi privati
    print(met)                              # Stampa i metodi pubblici della classe Tag   
"""                    

def naviga3(tag):               
    if tag.name.upper == "A":                             # Se il tag è un link <a>
        print(tag.get("href"))                      # Stampa il valore dell'attributo href
    for stag in tag.contents:                       # Per ogni figlio del tag
        if type(stag) == bs4.element.Tag:
            naviga3(stag)                             # Chiamata ricorsiva

naviga3(doc)                                        # Avvia la navigazione a partire dalla radice

def naviga4(tag):               
    if tag.name.upper == "A":                             
        print(tag["href"])                      
    for stag in tag.contents:                       
        if type(stag) == bs4.element.Tag:
            naviga4(stag)                             
