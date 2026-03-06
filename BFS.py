# تعريف الرسم البياني (Graphe)
graphe = {
    '1' : ['2','3','4'],
    '2' : ['4', '5','7'],
    '3' : ['4'],
    '4' : ['1','8'],
    '5' : ['6','7'],
    '6' : ['5'],
    '7' : ['2','6','8'],
    '8' : ['7']
}

visite = [] # قائمة العقد التي تمت زيارتها
file = []   # تهيئة الطابور (file d'attente)

def bfs(visite, graphe, noeud): # وظيفة BFS
    visite.append(noeud)
    file.append(noeud)
    
    while file: # حلقة لزيارة كل عقدة في الطابور
        m = file.pop(0)
        print(m)
        
        for voisin in graphe[m]:
            if voisin not in visite:
                visite.append(voisin)
                file.append(voisin)

# تنفيذ خوارزمية BFS
print("Les noeuds visités selon l'algorithme BFS -Breadth-First Search-")
bfs(visite, graphe, '1')