def array_of_names(dict):
    names = []
    for word in persons:
        names.append(f"{word.capitalize()} {dict[word].capitalize()}")
    print(names)
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))