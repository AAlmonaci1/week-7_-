#while loop = execute somme code WHILE some conditions remain true

# name = input("Enter your name")
# while name == "":   #Repeats
#     print("You did not entabier your name")
#     name = input("Enter your name:")
# print(f"Hello {name}")

# #Infinite loops are bad
# #Iteration = loop           iterate = looping over something
# while name == "" :
#     print("You did not enter your name")
# print(f"Hello {name}")

# age = int(input("Enter your age"))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age"))

# print(f"You are {age} years old")

#HOW YOU CAN ESCAPE LOOP
# food = input("Enter a food your like (q to quit)")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food your like (q to quit)")

# print("bye")

#While logical operators
# num = input("Enter a number between 1 and 10")

# while num < 1 or num > 10:
#     print("number is not valid")
#     num = input("Enter a number between 1 and 10")

# print(f"Your number is {num}")

# for loops= execute a block f code a fixed number of times.
#you don't iterate over a range, string, sequence, etc

# for x in reversed(range(1, 11, 2)): #counts by 2
#     print(x)

# print("HAPPY NEW YEAR")

# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

#CONTINUE(skips over)
# for x in range(1, 21):
#     if x == 13 or x== 15 or x== 20:
#         continue
#     else:
#         print(x)

#BREAK(stops)
# for x in range(1, 21):
#     if x == 13 or x== 15 or x== 20:
#         break
#     else:
#         print(x)





#create a list of horror movie characters
horror_characters = ["Freddy Krueger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky"]
#Iterate through the list and print each chracter
# for character in horror_characters:
#     if character == "Jason Voorhees":
#         continue
#    print(character)

# if character == "Michael Myers":
#     character = "Dracula"
#    print(character)

# if character == "Chucky":
#     character = "Anabelle"
#   print(character)


#crete a list of famous horror mocies or your
#favorite horror movies
# iterate through th list and if a certain movie is dound
#is your least favorite movie, break out the loop
#print out rest of the movies
# next replace one of the movies with a movie that you like

horror_movies = ["Smile", "The Nun", "Terrifier 3", "Anabelle"]

for movie in horror_movies:
    if movie == "The Nun":
        continue
    print(movie)

for movie in horror_movies:
    if movie == "Smile":
        movie == "Chucky"
    print(movie)
