import webbrowser

class Movie():
    """
    A movie object containing variety of movie's information

    Attributes:
        title: A string movie's title
        storyline: A string movie's plot
        poster_image_url = A string movie's poster image url
        trailer_youtube_url = A string movie's trailer url
    """
    def __init__(self, movie_title, storyline, poster_image_url, trailer_youtube_url):
        """Inits Movie class with movie_title, storyline, poster_image_url and trailer_youtube_url."""
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open trailer url to display a movie's trailer."""
        webbrowser.open(self.trailer_youtube_url)
    
