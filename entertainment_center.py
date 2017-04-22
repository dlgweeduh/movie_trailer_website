import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                    )

gladiator = media.Movie("Gladiator",
                    "A commander defies a corrupt emperor, becomes a gladiator, and seeks revenge",
                    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                    "https://www.youtube.com/watch?v=IvTT29cavKo"
                    )

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")

the_good_the_bad_the_ugly = media.Movie("The Good the Bad and the Ugly",
                                       "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
                                       "https://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                                       "https://www.youtube.com/watch?v=WCN5JJY_wiA")

forrest_gump = media.Movie("Forrest Gump",
                             "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

#print(toy_story.storyline)
#print(avatar.title)
#avatar.show_trailer()
#gladiator.show_trailer()

movies = [toy_story, avatar, gladiator, fight_club, the_good_the_bad_the_ugly, forrest_gump]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__name__)
print(media.Movie.__doc__)

