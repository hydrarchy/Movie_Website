# Imports fresh_tomatoes and media modules so that classes, methods, and
# functions in those modules can be used in this program.

import fresh_tomatoes
import media

# The following 6 variable assignments create instances of class Movie
# with specific movie information passed in as arguments

heat = media.Movie("Heat",
     "Hunters and their prey--Neil and his professional criminal crew hunt to "
     "score big money targets.",
     "https://upload.wikimedia.org/wikipedia/en/6/6c/Heatposter.jpg",
     "https://www.youtube.com/watch?v=0xbBLJ1WGwQ","12.15.1995")

stay = media.Movie("Stay",
     "Sam Foster (Ewan McGregor), a psychiatrist, has a new patient, Henry "
     "Letham (Ryan Gosling), who claims to be suicidal.",
     "https://upload.wikimedia.org/wikipedia/en/1/1a/Stay_film.jpg",
     "https://www.youtube.com/watch?v=L6GGsl6XUNU","10.21.2005")

crash = media.Movie("Crash",
     "Writer-director Paul Haggis interweaves several connected stories about "
     "race, class, family and gender in Los Angeles in the aftermath of 9/11.",
     "https://upload.wikimedia.org/wikipedia/en/d/d0/Crash_ver2.jpg",
     "https://www.youtube.com/watch?v=durNwe9pL0E","5.6.2005")

no_country_for_old_men = media.Movie("No Country for Old Men",
     "While out hunting, Llewelyn Moss (Josh Brolin) finds the grisly "
     "aftermath of a drug deal.",
     "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_"
     "poster.jpg",
     "https://www.youtube.com/watch?v=38A__WT3-o0","11.9.2007")

american_gangster = media.Movie("American Gangster",
     "Frank Lucas (Denzel Washington) earns his living as a chauffeur to one "
     "of Harlem's leading mobsters.",
     "https://upload.wikimedia.org/wikipedia/en/9/9f/American_Gangster_"
     "poster.jpg", "https://www.youtube.com/watch?v=QOSOYSLDuQE","10.19.2007")

collateral = media.Movie("Collateral",
     "A cab driver realizes his current fare is a hit man that has been having "
     "him drive around from mark to mark until the last witness to a crime is "
     "dead.",
     "https://upload.wikimedia.org/wikipedia/en/4/45/Collateral_%28Movie%29.jpg",
     "https://www.youtube.com/watch?v=9BDx6ZPHV4w","8.6.2004")

# The movies variable is assigned to a list containing all instances of the
# class Movie.

movies = [heat, stay, crash, no_country_for_old_men, american_gangster,
     collateral]

# Calls the open_movies_page method in the fresh_tomatoes module which
# uses the information in each of the instances of the class Movie
# to create an HTML file that displays the movie names, poster art,
# and trailer.

fresh_tomatoes.open_movies_page(movies)


