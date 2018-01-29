# Movie Trailers Website #
This is a project to build the movie trailers website which lists all the movies you want to display in a single page and plays the trailer in a small window  when you click on it without taking you to a different page.

## Requirements ##
Download Phyton Programming language for the program to work.
The following are the links for downloading
?    Phyton for Windows 32 bit
?   Python for windows 64bit
?   Python for Mac
Click on the appropriate link according to your system configuration and follow the steps to download the python programming language.

## Specifications ##
Below are the three files that are needed for the program to work.
? media.py
? entertainment.py
? fresh_tomatoes.py(The fresh_tomatoes.py is the file with html, CSS and Javascript code required to run in the webrowser.It is provided in the folder media trailers.It needs to be stored in the same folder where all your python files were located.
All of the exact program files are located in the zip folder media trailers.

## Getting Started and Creating New File ##
After the installation has been done click on the Windows icon on your keyboard and look for recently added files. Then click on IDLE(Python GUI) to start your new program.
A page with python 2.7.9 shell opens.You will see something like this.
Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 Now click on File and select New File and then click Save As and save it  with a file name media.py extention and write your program code and save it.
Repeat the same steps for entertainment.py file as well.


Step 1:write the code in blue in media.py file
```
import webbrowser

class Movie():
    '''This Docstring explains the constructor method,inputs and outputs'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''This Docstring explains about the show_trailer function'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
After you are done make sure you save it.

Step 2: write the code in blue in entertainment.py file

import fresh_tomatoes
import media

# frozen movie = movie title,storyline,poster image,trailer
frozen = media.Movie(
    "Frozen",
    "Story of a fearless princess and rugged iceman to find"
    "her estranged sister",
    "http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
    "http://www.youtube.com/watch?v=TbQm5doF_Uc"
    
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
```

Then save it.
Also make sure to save the fresh_tomatoes.py file in the same folder where all your python files were located.This is a supporting which consists of all the styling required for the web page to work.

## Running the Program ##
Follow these steps to run the program. 
Make sure you downloaded the python programming language as specified above in the requirements and install it before you download the file.
1.Download the Zip File and UnZip in a folder
2.Open the IDLE(python GUI) file.
3.From the IDLE open entertainment.py file and click run Run Module F5 button.
4.It takes you to the page what you are looking for.
