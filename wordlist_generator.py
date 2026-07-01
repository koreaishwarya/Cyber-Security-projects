def generate_wordlist(name, pet, birthyear):

    words = []

    base_words = [name, pet]

    years = [
        birthyear,
        "2024",
        "2025",
        "2026"
    ]

    symbols = [
        "@",
        "#",
        "!",
        "$"
    ]

    for word in base_words:

        words.append(word)
        words.append(word.lower())
        words.append(word.upper())
        words.append(word.capitalize())

        # Leetspeak
        leet = word.replace("a", "@").replace("o", "0").replace("i", "1")
        words.append(leet)

        for year in years:
            words.append(word + year)

            for symbol in symbols:
                words.append(word + symbol + year)

    return list(set(words))
