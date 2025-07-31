# 🎬 IMDb Top 250 movies Web Scraper

This project demonstrates how to extract movie details from IMDb's Top 250 chart using **Selenium** and **BeautifulSoup**. 
The scraped data is processed and stored in a structured **CSV file** for further analysis.

## 🛠 Setup

Before running the project, set up a Python virtual environment and install dependencies:

#pip install selenium pandas numpy beautifulsoup4

Project Structure

o  main.py: Uses Selenium to extract raw HTML of top 250 movie entries and saves each in a separate file inside the 
   data/ folder.

o  collect.py: Parses saved HTML files to extract movie metadata (Title, Year, Duration, Rating, Score, Link) and compiles 
   the information into a CSV file imdb_top250_movies.csv.

Features

o  Extracts:

   o  🎬 Title
   o  🗓 Year of release
   o  ⏱ Duration
   o  📛 Content rating
   o  ⭐ IMDb score
   o  🔗 Direct link to the movie page
  
o  Saves HTML snapshots for offline inspection

o  Robust error handling for parser failures

Output

The final result is stored in:
 
 imdb_top250_movies.csv



 

