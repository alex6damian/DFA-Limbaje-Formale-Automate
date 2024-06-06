import dfa_checker
import cs112_passer

c=cs112_passer.load_file("dfa2.cfg") # citirea fisierului

s=cs112_passer.get_section_list(c) # extragerea sectiunilor

stari=cs112_passer.get_section_content(s, "States") # extragerea starilor

transitions=cs112_passer.get_section_content(s,"Transitions") # extragerea tranzitiilor

curent=cs112_passer.get_section_content(s,'S') # extragerea starii curente

curent=curent[0] # extragerea starii curente

final=cs112_passer.get_section_content(s, 'F') # extragerea starilor finale

string=input() # citirea stringului

for s in string: # parcurgerea stringului
    pasi=0
    for t in transitions: # parcurgerea tranzitiilor
        pasi=pasi+1
        if t[0] == curent and s==t[1]: # verificare daca tranzitia este posibila
            curent=t[2] # schimbarea starii curente
            break # iesire din for
    if pasi==len(transitions): # verific daca elementul pe care sunt in string nu se gaseste in tranzitii
        curent='error'

if curent in final: # verificare daca starea curenta este finala
    print("Acceptat")  # afisare acceptat
else: # altfel
    print("Respins") # afisare respins