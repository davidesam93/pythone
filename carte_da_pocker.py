#identificare i caratteri Unicode che rappresentano i 4 semi del pocker (cuori,quadri,fiori,picche) nella variante solo bordo.
#create una stringa con i quattro semi . # .. U+1F0B1	 cuori U+1F0C1	quadri U+1F0D1 fiori U+2664 picche , b"U+1F0C1",b"U+1F0D1",b"U+2664"]

solo_bytes = b"\xe2\x99\xa1\xe2\x99\xa2\xe2\x99\xa7\xe2\x99\xa4"
stringa= solo_bytes.decode()
print (stringa)