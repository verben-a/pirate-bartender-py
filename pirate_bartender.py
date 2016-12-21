import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

cocktails = ['The Old Man and the Sea', 'Treasure Island', 'Moby-Dick', 'Twenty Thousand Leagues under the Sea', 'The Odyssey']

answers = {}
name = input ("What is your name?")

for question in questions:
        taste = input (questions[question])
        if taste == 'yes': 
            answers[question] = True 
            # we don't pick anything until the last question
            # then store in that dictionary 'salty': True
        else:
            answers[question] = False
            
print(answers)
        
# Go through the user's answers one by one as a bartender
# if you find that that the user answered yes to a certain category of wine/drink
# then pick an ingredient from that category randomly.
# All the random choices (preferences) for ingredeients are stored in some list 


drink = "Pirate bartender will mix for you the cocktail "
drink_list = [] 
for answer in answers: 
    if answers[answer] == True:
        drink_list.append(random.choice(ingredients[answer]))
print (name + ", " + drink + random.choice(cocktails) + " with " + ", ".join(drink_list) +".")