
def madlib():
    adj1 = input("Adjective: ")
    noun1 = input("Abstract noun: ")
    verb1 = input("Verb (present tense): ")
    noun2 = input("Noun: ")
    adj2 = input("Adjective: ")
    verb2 = input("Verb ending in -ing: ")
    noun3 = input("Abstract noun: ")

    madlib = f"""
    In the {adj1} journey of life, we often search for {noun1}.
    We {verb1} forward, not knowing what the {noun2} holds for us.
    Every choice feels {adj2}, yet we keep {verb2},
    because without uncertainty, there is no {noun3}.
    """

    print(madlib)

    
