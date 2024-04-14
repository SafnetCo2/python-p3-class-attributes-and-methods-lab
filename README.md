## Song Class

The Song class represents individual songs and provides methods to manage information about them, such as the song name, artist, and genre. It also includes functionality to keep track of the total number of songs created, unique genres, and unique artists.

# Overview

The `Song` class is a fundamental component for managing song data in applications that deal with music libraries, playlists, or any other song-related functionality. It encapsulates key attributes and methods to create, access, and manage song objects.

# Features

- Create new song instances with song name, artist, and genre.
- Access attributes of song instances, including name, artist, and genre.
- Keep track of the total number of songs created.
- Maintain lists of unique genres and artists.
- Track the count of songs for each genre and artist.

# Usage
# Creating a Song
# Creating song instances
song1 = Song("Thriller", "Michael Jackson", "Pop")
song2 = Song("Single Ladies", "Beyoncé", "R&B")

# Displaying song attributes
print(song1.name, song1.artist, song1.genre)
print(song2.name, song2.artist, song2.genre)

# Displaying class attributes
print("Total songs created:", Song.count)
print("Unique genres:", Song.genres)
print("Unique artists:", Song.artists)

# Contributing
Comments, feedback, and suggestions for improvement are welcome! Feel free to open an issue or submit a pull request.

# Support
If you encounter any issues or have questions about the Song class code, please open an issue in the repository or contact the author via 
Email: josephine.nzioka1@student.moringaschool

# License
This project is licensed under the [MIT License] https://opensource.org/licenses/MIT- see the LICENSE file for details.

# Acknowledgments
Special thanks to Technical Mentor Ian of Moringa School for inspiring me to learn python programming skills.
