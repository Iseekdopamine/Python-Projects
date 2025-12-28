def madlib():
    

    adj1 = input("Adjective describing an inner state: ")
    noun1 = input("Spiritual concept (e.g., soul, spirit, awareness): ")
    verb1 = input("Verb (present tense): ")
    place1 = input("A peaceful place: ")
    adj2 = input("Adjective describing emotion: ")
    noun2 = input("Abstract noun: ")
    verb2 = input("Verb ending in -ing: ")
    time = input("Time of day: ")
    adj3 = input("Adjective: ")
    verb3 = input("Verb (present tense): ")
    noun3 = input("Abstract noun: ")
    noun4 = input("Spiritual value (e.g., peace, truth, unity): ")

    madlib = f"""
    In the {adj1} stillness of the {time}, the {noun1} begins to {verb1}.
    Surrounded by the quiet presence of the {place1}, we feel {adj2},
    as thoughts of {noun2} slowly dissolve.

    We move forward gently, {verb2} with each breath,
    learning that the path does not demand certainty,
    only attention.

    As the world feels {adj3}, the heart chooses to {verb3},
    not in resistance, but in trust.
    Through every moment of doubt and wonder,
    we discover that true {noun3} is found not in answers,
    but in the practice of presence.

    And so, step by step, we return to {noun4}.
    """

    print(madlib)
