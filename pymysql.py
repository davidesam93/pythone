import pymysql
conn = pymysql.connect(host="localhost", port=3306,
                       user="root", passwd ="root", db = "italy")
cur = conn.cursor()

queries = ["DELETE FROM regione",
           "INSERT INTO regione (nome) VALUES ('Marche')",
           "INSERT INTO regione (nome) VALUES ('Emilia Romagna') "]

idx = int(input(f"Passami un valore minore di {len(queries)}:"))
print (f" Sto eseguendo la query: {queries[idx]}...")

n_righe = cur.execute(queries[idx])

conn.commit()