films = ["Star Wars", "Lord of the Rings", "Shawshank Redemption", "God father"]

for films in films:
    print ("%s" % films)

add = input("Please enter a film: ")
if add not in films:
    films.append(add)