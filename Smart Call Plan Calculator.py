def calculer_cout(duree):
    
    couts_abonnement = [200, 100, 50, 20, 0]
    minutes_gratuites = [float('inf'), 120, 60, 30, 0]
    cout_par_minute = [0, 0.5, 1, 1.5, 2]
    
    couts_mensuels = []
    
    for i in range(5):
        minutes_supplementaires = duree - minutes_gratuites[i]
        if minutes_supplementaires < 0:
            minutes_supplementaires = 0
        cout_total = couts_abonnement[i] + (minutes_supplementaires * cout_par_minute[i])
        couts_mensuels.append(cout_total)
        
    return couts_mensuels


couts = [200, 100, 50, 20, 0] 

while True:
    print("Menu:")
    print("1- Afficher la liste des coûts mensuels par offre")
    print("2- Afficher l'offre la plus avantageuse (coût le plus bas)")
    print("3- Quitter le programme")

    choix = int(input("Choisissez une option: "))
    
    if choix == 1 or choix == 2:
        duree = input("Entrez la durée de communication en minutes: ")
        if duree.isdigit():
            duree = int(duree)
        else:
            print("Invalid input. Please enter a number.") 
        prix = calculer_cout(duree)

    if choix == 1:
        print("le prix a payer pour chaque offer est", prix)

    elif choix == 2:
        min_value = prix[0]
        min_index = 0

        for i in range(1, len(prix)):
            if prix[i] < min_value:
                min_value = prix[i]
                min_index = i

        offre_avantageuse = min_index + 1
        print(f"L'offre la plus avantageuse est l'offre {offre_avantageuse} avec un coût de {min_value} DH")

    elif choix == 3:
        print("Fin du programme.")
        break

    else:
        print("Option invalide, veuillez réessayer.")    