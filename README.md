# Spotify-SuperGenre

### **1. Data Collection**
   - There are two files for Data Collection: **"get_data.py"** and **"get_sample.py"**
   - **"get_sample.py"** collects track and genre information from a small playlist I created to check if the code works properly 
   - **"get_data.py"** is the actual code that creates the dataset I will be using to generate "Super-genres"

### **2. Dataset Information**
   - Dataset consists of **9964 songs** (fetched from the playlist called _"Biggest Playlist With All The Best Songs"_)
   - Features collected are _**genre, name, album, artist, release date, duration (ms), popularity, acousticness,  danceability, energy, key, mode, instrumentalness, liveness, loudnness, speechiness, valence, tempo, and time signature**_

### **3. Super-Genre Creation**

- Super-genre will be created using **K-Means Clustering**
   - In total of **1019 genres** in the dataset will be sub-grouped based on the euclidean distance of feature vectors
   - Optimal number of clusters (**12**) is chosen by the **elbow method**
   - **Word Cloud** and **Feature Analysis** will be done to name the 12 clusters (=super-genres)
