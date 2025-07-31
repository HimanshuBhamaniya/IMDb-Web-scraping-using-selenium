from bs4 import BeautifulSoup
import os
import pandas as pd


d = {'Title': [], 'Year': [], 'Duration':[], 'Rating': [], 'Score': [], 'Link': []}

for file in os.listdir('data'):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find('h3')
        full_title = t.get_text().strip()
    # Split at the first period and take the second part
        Title = full_title.split('.', 1)[1].strip()

        metadata_div = soup.find('div', class_='sc-86fea7d1-7')
        metadata_items = metadata_div.find_all('span', class_='sc-86fea7d1-8')

        Year = metadata_items[0].get_text().strip() if len(metadata_items) > 0 else ''
        Duration = metadata_items[1].get_text().strip() if len(metadata_items) > 1 else ''
        Rating = metadata_items[2].get_text().strip() if len(metadata_items) > 2 else ''
        
        s = soup.find('span', class_= 'ipc-rating-star--rating')
        Score = s.get_text()

        l = soup.find('a', class_='ipc-title-link-wrapper')
        Link =f"https://www.imdb.com{l['href']}"

        
        d['Title'].append(Title)
        d['Year'].append(Year)
        d['Rating'].append(Rating)
        d['Duration'].append(Duration)
        d['Score'].append(Score)
        d['Link'].append(Link)
    except Exception as e:
        print(e)    
    
df = pd.DataFrame(d)
df.to_csv("imdb_top250_movies.csv")
       
# success_count = 0
# failures = []

# for file in os.listdir('data'):
#     try:
#         with open(f"data/{file}", encoding='utf-8') as f:
#             html_doc = f.read()
#         soup = BeautifulSoup(html_doc, 'html.parser')

#         # Title
#         t = soup.find('h3')
#         if not t:
#             raise ValueError("Missing <h3> tag")
#         full_title = t.get_text().strip()
#         title = full_title.split('.', 1)[1].strip()

#         # Metadata
#         metadata_div = soup.find('div', class_='sc-86fea7d1-7')
#         if not metadata_div:
#             raise ValueError("Missing metadata div")
#         metadata_items = metadata_div.find_all('span', class_='sc-86fea7d1-8')
#         year = metadata_items[0].get_text().strip() if len(metadata_items) > 0 else ''
#         duration = metadata_items[1].get_text().strip() if len(metadata_items) > 1 else ''
#         rating = metadata_items[2].get_text().strip() if len(metadata_items) > 2 else ''

#         # Score
#         s = soup.find('span', class_='ipc-rating-star--rating')
#         score = s.get_text().strip() if s else ''

#         # Link
#         l = soup.find('a', class_='ipc-title-link-wrapper')
#         link = f"https://www.imdb.com{l.get('href')}" if l and l.get('href') else ''

#         # Append to dictionary
#         d['title'].append(title)
#         d['year'].append(year)
#         d['duration'].append(duration)
#         d['rating'].append(rating)
#         d['score'].append(score)
#         d['link'].append(link)

#         success_count += 1
#         print(title, year, rating, duration, score, link)

#     except Exception as e:
#         failures.append((file, str(e)))

# print(f"\n✅ Successfully parsed {success_count} movies.")
# print(f"❌ Failed to parse {len(failures)} files.")
# if failures:
#     print("\n🔍 Sample failures:")
#     for f, err in failures[:5]:
#         print(f"{f}: {err}")
