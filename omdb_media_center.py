import urllib	#used to open URL
import media2	#defines classes
import omdb_fresh_tomatoes 	#used to generate HTML
import json 	#used to convert json to dictionary

# Set a list of movies to display using IMDB IDs:
target_movie_list = ("tt2084970", "tt0074860", "tt2562232")

# Create a dictionary of YouTube URL's for the movie trailer for each movie in target_movie_list:
trailers = {"tt2084970":"https://www.youtube.com/watch?v=S5CjKEFb-sM",
            "tt0074860":"https://www.youtube.com/watch?v=OK26KtN99R4",
            "tt2562232": "https://www.youtube.com/watch?v=8jAfBd3g6bA"}
# >>> need an error routine to check if a youtube video is included

# Read JSON from OMDB for each movie.  Convert each json set to a dictionary and save to a list:
omdb_dict_list = []

for movie in target_movie_list:
    
    omdb_open_as_json = urllib.urlopen("http://www.omdbapi.com/?i=" + movie + "&plot=short&r=json")
    omdb_json = omdb_open_as_json.read()
    omdb_dict = json.loads(omdb_json)
    omdb_dict_list.append(omdb_dict)

    omdb_open_as_json.close()
	
# For each movie in the dictionary list extract relavent data from omdb_dict_list and trailers
# and store to a list of class instances for Fresh_Tomatoes:
final_movie_list = []

for target_dict in omdb_dict_list:
    m = media2.Movie()
    m.title = target_dict["Title"]
    m.storyline = target_dict["Plot"]
    m.poster_image_url = target_dict["Poster"]
    m.genre = target_dict["Genre"]
    m.duration = target_dict["Runtime"]
    m.rating = target_dict["Rated"]
    m.year = target_dict["Year"]
	#Trailer is pulled from the trailer list using the string version of the unicode imdbID:
    m.trailer_youtube_url = trailers[str(target_dict["imdbID"])]
	#append each instance to a list:
    final_movie_list.append(m)

#Call fresh_tomatoes to display a webbrower page listing all the movies:
omdb_fresh_tomatoes.open_movies_page(final_movie_list)
