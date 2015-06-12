import media
import fresh_tomatoes

# create 6 six movie instances
ocean_heaven = media.Movie("Ocean Heaven",
                           "Explores the subject of parental love and autism in kids.",
                           "http://ia.media-imdb.com/images/M/MV5BMjMyNDk5ODgxM15BMl5BanBnXkFtZTgwODQ4NjI2MDE@._V1__SX1853_SY843_.jpg",
                           "https://www.youtube.com/watch?v=EJemRXBaO80")

the_raid = media.Movie("The Raid",
                        "A S.W.A.T. team becomes trapped in a tenement run by a ruthless mobster and his army of killers and thugs.",
                       "http://ia.media-imdb.com/images/M/MV5BMTgxODQyNTY0MV5BMl5BanBnXkFtZTcwMjMwMjU0Nw@@._V1__SX1853_SY843_.jpg",
                       "https://www.youtube.com/watch?v=PkULMOFpuCo")

taken = media.Movie("Taken",
                    "A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.",
                    "http://ia.media-imdb.com/images/M/MV5BMTM4NzQ0OTYyOF5BMl5BanBnXkFtZTcwMDkyNjQyMg@@._V1__SX1853_SY843_.jpg",
                    "https://www.youtube.com/watch?v=kZ02_Uzf7So")

secret = media.Movie("Secret",
                     "Ye Xiang Lun, a talented piano player is a new student at the prestigious Tamkang School. On his first day, he meets Lu Xiao Yu, a pretty girl playing a mysterious piece of music.",
                     "http://ia.media-imdb.com/images/M/MV5BOTg4MzA3MjQ4NF5BMl5BanBnXkFtZTgwMjQ5MTA2MDE@._V1__SX1853_SY843_.jpg",
                     "https://www.youtube.com/watch?v=5hkZsgPO8h4")

dragon = media.Movie("How to train your dragon",
                     "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.",
                     "http://ia.media-imdb.com/images/M/MV5BMjA5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1__SX1853_SY843_.jpg",
                     "https://www.youtube.com/watch?v=oKiYuIsPxYk")

titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind, but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1__SX1853_SY843_.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

movies = [ocean_heaven, the_raid, taken, secret, dragon, titanic]
# method open_movies_page takes in list of movies and display them with html file
fresh_tomatoes.open_movies_page(movies)
