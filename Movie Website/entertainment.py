import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A boy & his toys that comes to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

avengers = media.Movie("Avengers Infinity War",
                       "All marvel heroes come together",
                       "https://images-na.ssl-images-amazon.com/images/I/A1t8xCe9jwL._SY679_.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
                       )

titanic = media.Movie("Titanic",
                      "A drowning ship",
                      "https://images-na.ssl-images-amazon.com/images/I/51tOG0zzUgL.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
                      )

lord_rings = media.Movie("Lord of the rings",
                          "A ring to get super natural power",
                          "https://j.b5z.net/i/u/6127364/i/lord_of_the_rings_49_ezr2.jpg",
                          "https://www.youtube.com/watch?v=V75dMMIW2B4"
                          )

three_hundred = media.Movie("Three Hundred",
                            "A battle of 300 soldier to become free",
                            "https://imgc.allpostersimages.com/img/posters/300-movie-leonidas-spartans-tonight-we-dine-in-hell_u-L-F578WZ0.jpg?src=gp&w=300&h=375",
                            "https://www.youtube.com/watch?v=UrIbxk7idYA"
                            )
    


movies = [toy_story, avatar, avengers, titanic, lord_rings, three_hundred]
fresh_tomatoes.open_movies_page(movies)

#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#print(avengers.storyline)
#avengers.show_trailer()
#three_hundred.show_trailer()


