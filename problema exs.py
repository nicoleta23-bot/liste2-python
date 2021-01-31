#Fiind date doua liste scrise deja in editor, rezolvati cerintele urmatoare:
#prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
#ani=[14,23,15,14,12,41,39]
#a)Considerand ca fiecare persoana are asociata varsta pe acelasi indice, afisati precum mai jos:
#Mihai are varsta de 14 ani.
#George are varsta de 23 de ani.
#...
#b)Adaugati in liste la final, corespunzator, datele: Andreea, 34 si Ioan, 23. Afisati ambele liste apoi.
#c)Stergeti datele din ambele liste despre Ana(atentie la indici).
#d)Afisati primele trei elemente din lista prenume.
#e)Afisati lista prenume de la dreapta la stanga.
#f)Afisati elementele cu indicii 2 si 4, apoi de la 0 la 5 din ambele liste. 

with open("input.txt","r") as f:
    a=f.readline()
    b=f.readline()
    prenume=a.split()
    varsta=b.split()
    for i in range(0,len(prenume)):
        print(prenume[i],"are varsta de",varsta[i],"ani.")
    prenume.extend(["Andreea","Ioan"])
    varsta.extend([34,23])
    print(prenume,varsta,sep="\n")
    varsta.pop(prenume.index("Ana"))
    prenume.remove("Ana")
    print(prenume[0:3])
    print(prenume[::-1])
    print(prenume[2],varsta[2])
    print(prenume[4],varsta[4])
    print(prenume[:5],varsta[:5])