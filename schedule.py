movies = {"Die Hard": "9pm",
          "John Wick" : "8pm",
          "Iron Man" : "7pm",
          "Galaxy of the Guardians" : "6pm"}
print("Movies showing: ")
for key in movies:
    print(key)
movie_choice = input("Select a movie to see showtime:\n")

showtime = movies.get(movie_choice)
if showtime:
    print(showtime)
else:
    print("That movie isn't playing")