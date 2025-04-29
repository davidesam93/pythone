
import urllib.request                       # Importa la libreria per fare richieste HTTP
url = "https://lacordataescursionismo.it/"  # URL del sito web da scaricare
risultato = urllib.request.urlopen(url)     # Apre la connessione e scarica il contenuto
theBytes = risultato.read()                 # Legge i byte della risposta
text = theBytes.decode()                    # Converte i byte in stringa (HTML)

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

lista=dir(bs4.element.Tag)
for met in lista:
  if not met.startswith("_"):               # Filtra i metodi privati
    print(met)                              # Stampa i metodi pubblici della classe Tag                       




def naviga3(tag, indent=""):
    print(indent + tag.name.upper())                # Stampa il nome del tag con indentazione
    if tag.name == "a":                             # Se il tag è un link <a>
        print(indent + "  href:", tag.get("href"))  # Stampa il valore dell'attributo href

    for stag in tag.contents:                       # Per ogni figlio del tag
        if isinstance(stag, bs4.element.Tag):       # Se è un altro tag HTML
            naviga3(stag, indent + "  ")            # Chiamata ricorsiva

def naviga4(tag):               
    if tag.name.upper == "A":                  # Se il tag è un link <a>                     
        print(tag["href"])                     # Stampa il valore dell'attributo href            
    for stag in tag.contents:                  # Per ogni figlio del tag     
        if type(stag) == bs4.element.Tag:      # Se è un altro tag HTML
            naviga4(stag)                      # Chiamata ricorsiva


visited = []


def crawl ( url, prof, visited) :                               # Funzione per il crawling di un sito web
    if prof == 0 :                                              # Se la profondità è zero
       return                                                   # Esci dalla funzione
    response = urllib.request.urlopen(url)                      # Apre la connessione e scarica il contenuto
    doc = bs4.BeautifulSoup(response)                           # Crea un oggetto BeautifulSoup che rappresenta l'HTML
    for link in doc.find_all("a") :                             # Trova tutti i tag <a> (link)
       href = link["href"]                                      # Ottiene l'attributo href del link
       if href [0:4] == "http" and href not in visited  :       # Se è un link assoluto e non è già stato visitato
          visited.append(href)                                  # Aggiunge il link alla lista dei visitati
          crawl(href,visited)                                   # Chiamata ricorsiva per il link trovato



def crawl ( url,visited) :                                      # Funzione per il crawling di un sito web
    response = urllib.request.urlopen(url)                      # Apre la connessione e scarica il contenuto
    doc = bs4.BeautifulSoup(response)                           # Crea un oggetto BeautifulSoup che rappresenta l'HTML
    print (f" Sto visitando il percorso {url}")                 # Stampa il percorso corrente

    try:                                                        # Sezione try per gestire eventuali errori
        for link in doc.find_all("a") :                         # Trova tutti i tag <a> (link)
            href = link["href"]                                 # Ottiene l'attributo href del link
        if href [0:4] == "http" and href not in visited  :      # Se è un link assoluto e non è già stato visitato
          visited.append(href)                                  # Aggiunge il link alla lista dei visitati
          crawl(href,visited)                                   # Chiamata ricorsiva per il link trovato
    except:                                                     # Se si verifica un errore                                
        return                                                  # Esci dalla funzione