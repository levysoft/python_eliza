import random

exit_phrases = [
    "Arrivederci. È stato piacevole parlare con lei",
    "Arrivederci.  È stata una piacevole chiacchierata",
    "Arrivederci.  Non vedo l'ora di un nuovo incontro.",
    "È stato un bell'incontro, vero? Ma il tempo è finito. Arrivederci.",
    "Forse vorresti parlarne di più in un prossimo incontro? Arrivederci.",
]
intro_questions = [
    "Salve sono Eliza, una simulazione di uno psicologo rogeriano. Come va? Mi dica il suo problema.",
    "Salve sono Eliza, per favore, mi dica cosa la turba.",
    "Salve sono Eliza, parliamo un po'.",
]
# choose a random intro question
intro_question = random.choice(intro_questions)
print (intro_question)

input_string = ""
response = ""
quit_commands = ["arrivederci", "addio", "finito", "exit", "quit"]

questions = {
    "Come va oggi?": [
        "bene", "ottimo", "fantastico",
    ],
    "Come hai dormito?": [
        "bene", "male", "abbastanza",
    ],
    "Hai fatto colazione?": [
        "si", "no", "non ancora",
    ],
    "Come ti senti emozionalmente?": [
        "felice", "triste", "arrabbiato", "nervoso", "stressato","bene","male"
    ],
    "Hai qualche progetto per oggi?": [
        "si", "no", "non lo so",
    ],
    "Come ti senti fisicamente?": [
        "bene", "male", "stanco", "affaticato"
    ],
	"Hai fatto qualche attività oggi?": [
		"si", "no", "poca"
	],
	"Hai programmato qualcosa per domani?": [
		"si", "no", "non ancora"
	],
	"Come ti senti fisicamente?": [
		"bene", "male", "stanco", "affaticato"
	],
	"Come ti senti emozionalmente oggi?": [
		"bene", "male", "felice", "triste", "nervoso", "ansioso"
	],
	"Hai fatto qualcosa di divertente oggi?": [
		"si", "no", "non ancora"
	],
	"Hai incontrato qualcuno di interessante oggi?": [
		"si", "no", "non ancora"
	],
	"Hai apprezzato qualcosa di particolare oggi?": [
		"si", "no", "non ancora"
	],
	"Hai imparato qualcosa di nuovo oggi?": [
		"si", "no", "non ancora"
	],
	"Hai fatto qualcosa per gli altri oggi?": [
		"si", "no", "non ancora"
	],
	"Hai fatto qualcosa per te oggi?": [
		"si", "no", "non ancora"
	],
	"Cosa hai fatto ieri sera?": [
		"ho visto un film", "sono stato fuori con gli amici", "ho letto un libro", "non ricordo"
	],
	"Hai programmato qualcosa per domani?": [
		"si", "no", "non ancora"
	],
	"Hai qualche preoccupazione in questo momento?": [
		"si", "no"
	],
	"Hai qualche progetto a lungo termine?": [
		"si", "no", "non lo so"
	],
	"Stai seguendo una dieta o un allenamento?": [
		"si", "no", "sto provando"
	],
	"Hai fatto qualcosa di divertente ultimamente?": [
		"si", "no", "non recentemente"
	],
	"Hai viaggiato ultimamente?": [
		"si", "no", "prossimamente"
	],
	"Hai incontrato qualcuno di interessante ultimamente?": [
		"si", "no", "non recentemente"
	],
}

while True:
    question = random.choice(list(questions.keys()))
    input_string = input(question + " ")
    input_string = input_string.lower()
    if input_string in quit_commands:
        # choose a random exit question
        exit_phrase = random.choice(exit_phrases)
        print(exit_phrase)
        break
    while input_string not in questions[question]:
        input_string = input("Non capisco cosa vuoi dire, potresti ripetere per favore?")
        input_string = input_string.lower()
    question = random.choice(list(questions.keys()))
    input_string = input(question + " ")
    while input_string.lower() not in questions[question]:
        input_string = input("Non capisco cosa vuoi dire, potresti ripetere per favore? ")
    if input_string.lower() in ["bene", "ottimo", "fantastico"]:
        response = "Sono felice di sentirlo!"
    elif input_string.lower() in ["male", "terribilmente", "pessimo"]:
        response = "Mi dispiace sentirlo. Cosa è successo?"
    elif input_string.lower() in ["si", "no", "non ancora"]:
        if input_string.lower() == "si":
            response = "Bene, è importante quello che fai!"
        else:
            response = "D'accordo, puoi farlo in seguito."
    elif input_string.lower() in ["felice", "triste", "arrabbiato", "nervoso", "stressato","bene","male"]:
        if input_string.lower() in ["felice","bene"]:
            response = "Sono felice per te!"
        elif input_string.lower() in ["triste","male"]:
            response = "Mi dispiace sentirlo. Cosa è successo?"
        else:
            response = "Capisco. Parlami un po' di più su come ti senti emozionalmente."
    else:
        response = "Interessante, parlami del tuo progetto."
    print(response)
