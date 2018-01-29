import fresh_tomatoes
import media

# frozen movie = movie title,storyline,poster image,trailer
frozen = media.Movie(
    "Frozen",
    "Story of a fearless princess and rugged iceman to find"
    "her estranged sister",
    "http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
    "http://www.youtube.com/watch?v=TbQm5doF_Uc"
    )
# despicableme2 movie = movie title,storyline,poster image,trailer
despicable_me_two = media.Movie(
    "Despicable Me2",
    "Despicable Me 2 is a 2013 American 3D computer-animated"
    "comedy film and the sequel to"
    "the 2010 animated film Despicable Me",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Despicable_Me_2_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=yM9sKpQOuEw"
    )                            
# homealone movie = movie title,storyline,poster image,trailer
home_alone = media.Movie(
    "Home Alone",
    "An eight-year-old trouble-maker accidentally left home"
    "alone by his family during Christmas",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CK2Btk6Ybm0"
    )
# tangled movie = movie title,storyline,poster image,trailer
tangled = media.Movie(
    "Tangled",
    "Story of Rapunzel with 70 feet of magical golden hair and"
    "most charming bandit Flynn Rider",
    "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ip_0CFKTO9E"
    )
# avatar movie = movie title,storyline,poster image,trailer
avatar = media.Movie(
    "Avatar",
    "A Marine on a alien pianet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )
# toystory movie = movie title,storyline,poster image,trailer
toy_story = media.Movie(
    "Toy Story",
    "Toy Story is a 1995 American computer-animated buddy comedy"
    "adventure film produced by Pixar"
    "Animation Studios for Walt Disney Pictures",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/300px-Toy_Story_logo.svg.png",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )
# Building an array of all the movie instances created
movies = (frozen, despicable_me_two, home_alone, tangled, avatar, toy_story)


# Passing an array 
fresh_tomatoes.open_movies_page(movies)
