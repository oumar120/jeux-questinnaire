import questionnaire
while True:
        print("--------------------------QUESTIONNAIRE----------------------------------")
        print("""              Menu
              1. Créer Questionnaire
              2. Lancer Questionnaire
              3. Lister les Questionnaires
              4. Quitter
        """)
        try:
            reponse = int(input("Veuiller choisir une option entre 1,2,3 ou 4: "))
            if reponse < 1 or reponse > 4:
                print("vous dever faire un choix entre 1,2 3 ou 4")
        except:
            print("vous devez choisir un nombre valide")
        else:
            match reponse:
                case 1:
                    questionnaire.Questionnaire.creerQuestionnaire()
                case 2:
                     if not questionnaire.Questionnaire.listerQuestionnaire():
                         print("Vous n'avez pas de questionaire, veuiller en créer un")
                     else:
                         questionnaires = questionnaire.Questionnaire.getQuestionnaire()
                         while True:
                             try:
                                 numero = int(input("veuiller choisir le numéro du questionnaire à lancer: "))
                             except:
                                 print("vous devez choisir un nombre")
                             else:
                                 if numero > len(questionnaires):
                                     print("vous devez saisir un numéro valide")
                                 else:
                                     titreQuestionnaire = questionnaires[numero-1]["titre"]
                                     questionQuestionnaire = questionnaires[numero-1]["questions"]
                                     questionnaire = questionnaire.Questionnaire(titreQuestionnaire,questionQuestionnaire)
                                     questionnaire.lancerQuestionnaire()
                                     break
                case 3:
                    if not questionnaire.Questionnaire.getQuestionnaire():
                        print("vous n'avez pas de questionnaire pour le moment,Veuiller en créer une\n")
                    else:
                        questionnaire.Questionnaire.listerQuestionnaire()
                case 4:
                    exit()

