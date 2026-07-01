from password_analyzer import analyze_password
from wordlist_generator import generate_wordlist

password = input("Enter password to analyze: ")

analyze_password(password)

print("\n=== Custom Wordlist Generator ===")

name = input("Name: ")
pet = input("Pet Name: ")
birthyear = input("Birth Year: ")

wordlist = generate_wordlist(
    name,
    pet,
    birthyear
)

with open("generated_wordlist.txt", "w") as file:
    for word in wordlist:
        file.write(word + "\n")

print(f"\nGenerated {len(wordlist)} words.")
print("Saved as generated_wordlist.txt")
