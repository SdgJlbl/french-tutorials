def choisir_label(distances_triees, k):
    plus_proches_voisins = distances_triees[:k]
    count_R = 0
    count_L = 0
    for voisin in plus_proches_voisins:
        if voisin['label'] == 'R':
            count_R += 1
        if voisin['label'] == 'L': 
            # à compléter
            count_L += 1
    if count_R > count_L:
        return 'R'
    else:
        return 'L'
