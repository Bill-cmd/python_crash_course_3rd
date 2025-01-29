favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'bILL': [],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    
    if len(languages) == 1:
        print( f"\n{name.title()}'s favorite language is: {languages[0].title()}")
    elif len(languages) < 1:
        print(f"\n{name.title()} has no favorite languages.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
