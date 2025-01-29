cities = {
    'Beijing': {
        'country': 'China',
        'population': 21_710_000,
        'fact': 'Beijing is the capital of China.',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13_515_271,
        'fact': 'Tokyo is the capital of Japan.',
    },
    'New York': {
        'country': 'USA',
        'population': 8_336_817,
        'fact': 'New York is the largest city in the USA.',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\tCountry: {country}, Population: {population}, Fact: {fact}")
    