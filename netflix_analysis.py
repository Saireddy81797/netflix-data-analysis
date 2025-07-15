import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
data = pd.read_csv("netflix1.csv")
print("✅ Data Loaded Successfully!\n")
print(data.head())
print("\n🧾 Columns in CSV:", data.columns.tolist())

# Clean the data
data.drop_duplicates(inplace=True)
data['date_added'] = pd.to_datetime(data['date_added'])
data.dropna(subset=['director', 'country'], inplace=True)

# Add extra columns
data['year'] = data['date_added'].dt.year
data['month'] = data['date_added'].dt.month
data['day'] = data['date_added'].dt.day

# 1. Movies vs TV Shows
sns.countplot(x='type', data=data)
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
input("📊 1/7 - Press ENTER to continue...")

# 2. Top 10 Genres
data['genres'] = data['listed_in'].apply(lambda x: x.split(', '))
all_genres = sum(data['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)

sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()
input("📊 2/7 - Press ENTER to continue...")

# 3. Year-wise Content Added
sns.countplot(x='year', data=data, palette='coolwarm')
plt.title("Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
input("📊 3/7 - Press ENTER to continue...")

# 4. Top 10 Directors
top_directors = data['director'].value_counts().head(10)
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.title("Top 10 Directors")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.show()
input("📊 4/7 - Press ENTER to continue...")

# 5. Word Cloud of Titles
titles = ' '.join(data['title'])
wordcloud = WordCloud(background_color='black', width=800, height=400).generate(titles)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Netflix Titles")
plt.show()
input("📊 5/7 - Press ENTER to continue...")

# 6. Monthly Releases
monthly_movie = data[data['type'] == 'Movie']['month'].value_counts().sort_index()
monthly_show = data[data['type'] == 'TV Show']['month'].value_counts().sort_index()

plt.plot(monthly_movie.index, monthly_movie.values, label='Movies', marker='o')
plt.plot(monthly_show.index, monthly_show.values, label='TV Shows', marker='s')
plt.title("Monthly Releases")
plt.xlabel("Month")
plt.ylabel("Number of Releases")
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.legend()
plt.grid(True)
plt.show()
input("📊 6/7 - Press ENTER to continue...")

# 7. Yearly Releases
yearly_movie = data[data['type'] == 'Movie']['year'].value_counts().sort_index()
yearly_show = data[data['type'] == 'TV Show']['year'].value_counts().sort_index()

plt.plot(yearly_movie.index, yearly_movie.values, label='Movies', marker='o')
plt.plot(yearly_show.index, yearly_show.values, label='TV Shows', marker='s')
plt.title("Yearly Releases")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

print("\n🎉 All Graphs Displayed Successfully!")
input("✅ Done! Press ENTER to close...")
