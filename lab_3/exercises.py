import collections


def letter_count(phrase):
    counters = collections.defaultdict(int)
    for letter in phrase.lower():
        count = counters.get(letter, 0)
        counters[letter] = count + 1
    return counters


capitals = {
    'Timis': 'Timisoara',
    'Bihor': 'Oradea',
    'Arad': 'Arad',
    'Hunedoara': 'Deva',
    'Caras-Severin': 'Resita',
}

def judet(city):
    reverse_capitals = {
        county: city
        for city, county in capitals.items()
    }
    return reverse_capitals[city]

judet('Deva')