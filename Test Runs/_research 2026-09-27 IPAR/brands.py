import glob,re
B=['Burberry','Lanvin','Paul Smith','S.T. Dupont','Van Cleef','Montblanc','Boucheron','Jimmy Choo','Balmain','Repetto','Karl Lagerfeld','Rochas','Coach','Dunhill','Agent Provocateur','Oscar de la Renta','Abercrombie','Hollister','Anna Sui','Bebe','Betsey Johnson','Nickelodeon','Gap','Banana Republic','Brooks Brothers','Shanghai Tang','Guess','GUESS','Graff','MCM','Kate Spade','Moncler','Emanuel Ungaro','Ferragamo','Donna Karan','Lacoste','Roberto Cavalli','French Connection','Off-White','Goutal','Longchamp','Nautica','David Beckham','Divabox','Intimate','Tristar','Aziza','Diane von','Tommy','Lulu','Jordache','Mauboussin','Swiss Army','Victorinox','Ben Sherman','Cavalli']
fs=sorted(glob.glob('filings/*_10-K_*.txt'))
print('brand'.ljust(20)+' '.join(f[8:12] for f in fs))
T={f:open(f,encoding='utf-8',errors='ignore').read() for f in fs}
for b in B:
    print(b[:19].ljust(20)+' '.join(('  x ' if b in T[f] else '  . ') for f in fs))
