# Imports the built-in function webbrowser for use in
# the show_trailer method inside class Movie

import webbrowser

class Movie():
     '''
     Groups together movie information into a class so that 
     multiple instances can be created.
     '''
     def __init__(self, movie_title, movie_storyline, poster_image,
          trailer_youtube, release_date):
          '''
          Inits Movie class by assigning class variable to the args
          passed in when the __init__ method is called.
          '''
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_youtube
          self.release_date = release_date

     def show_trailer(self):
          '''
          Opens url in class variable self.trailer_youtube_url in a webbrowser
          '''
          webbrowser.open(self.trailer_youtube_url)