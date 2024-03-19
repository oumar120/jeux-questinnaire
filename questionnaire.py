import json
import jsonpickle
class Question:
    def __init__(self,titre:str,reponseList:(),bReponse:str):
        self.titre = titre
        self.reponseList = reponseList
        self.bReponse = bReponse

    def poserQuestion(self):
        print(self.titre)
        for i in range(0, len(self.reponseList)):
            print(f"{i + 1}.{self.reponseList[i]}")
        reponse = self.demanderReponse()
        if self.reponseList[reponse - 1] == self.bReponse:
            print("Bonne réponse!")
            return True
        else:
            print("mauvaise réponse!")
            return False

    def demanderReponse(self):
        min = 1
        max = len(self.reponseList)
        reponse = input(f"Donnez votre réponse entre {min} et {max}: ")
        try:
            reponse = int(reponse)
            if min <= reponse <= max:
                return reponse
            print(f"vous devez saisir un chiffre compris entre {min} et {max}")

        except:
            print("vous devez saisir un chiffre valide")
        return self.demanderReponse()
class Questionnaire:
    def __init__(self,titre,questions:[]):
        self.titre = titre
        self.questions = questions

    def lancerQuestionnaire(self):
        score = 0
        for question in self.questions:
            question = Question(question["titre"],question["reponseList"],question["bReponse"])
            if Question.poserQuestion(question):
                score += 1
        print(f"votre score est de: {score}/{len(self.questions)}")

    def creerQuestionnaire():
        i = 1
        questions = []
        titre = input("Donner le titre du questionnaire ou entrer pour quitter:`\n")
        if titre != "":
            while True:
                reponsePossible = ()
                bonneReponse = ""
                titreQuestion = input(f"Donnez le titre de la question {i} ou entrer pour quitter:\n")
                if titreQuestion != "":
                    while len(reponsePossible) < 2 or reponsePossible[0] == "":
                        reponsePossible = input("Donner les réponses possibles (minimum 2 séparé par des virgules): ")
                        reponsePossible = tuple(reponsePossible.split(","))
                    while bonneReponse not in reponsePossible:
                        bonneReponse = input("Donnez la bonne réponse parmis les réponses possibles: ")
                    question = Question(titreQuestion, reponsePossible, bonneReponse)
                    questions.append(question)
                    i += 1
                else:
                    if len(questions) > 1:
                        questionnaire = Questionnaire(titre, questions)
                        questionnaire.saveQuestionnaire()
                        print("questionnaire crée avec succès")
                        return

                    else:
                        print("un questionnaire doit avoir minimum 2 questions pour etre valide")
                        return
        else:
            return


    def saveQuestionnaire(self):
       questionnaire_str = jsonpickle.encode(self,unpicklable=False)
       f = open("questionnaire.txt","a")
       f.write(questionnaire_str+"\n")
       f.close()
    def getQuestionnaire():
        questionnaires = []
        f = open("questionnaire.txt","r")
        for jsonObject in f:
            questionnaire = jsonpickle.decode(jsonObject)
            questionnaires.append(questionnaire)
        f.close()
        return questionnaires
    def listerQuestionnaire():
        questionnaires = Questionnaire.getQuestionnaire()
        if questionnaires:
            for i in range(0,len(questionnaires)):
                print(f"{i+1}.{questionnaires[i]["titre"]}")
            return True
        else:
            return False






