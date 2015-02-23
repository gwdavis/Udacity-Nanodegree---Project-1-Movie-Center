# OMDB Media Center

OMDB Media Center is a short Python routine that requests movie data from omdbapi.com and youtube.com and displays tiles in html in a webbrowser using a modified verstion of fresh_tomatoes_py.

Movies can be hardcoded into omdb_media)_center.py using IMDB ID codes in variable: target_movie_list.  It will also be necessary to add trailer youtube links in the dictionary variable: trailers.

The routine imports:
*urllib to access and read omdbapi.com
*json to convert the json form omdbapi to a dictionary (not sure if this is necessary but handling a dictionary is easier for me than json)
*media2  to define the movie class used by omdb_fresh_tomatoes
*omdb_fresh_tomatoes, a modified version of fresh_tomatoes to dispay the movie instances in a webbrower.