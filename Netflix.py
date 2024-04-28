import pandas as pd
import matplotlib.pyplot as plt

# Read the file & create a Dataframe
net = pd.read_csv('Netflix.csv')

# To show top-5 records of the dataset?
print(net.head())

# To show bottom-5 records of the dataset?
print(net.tail())

# To show the No. of Rows and Columns?
print(net.shape)

# To show indexes, columns, data-types of each column, memory at once?
print(net.index)             # for Index
print(net.columns)           # for Columns
print(net.dtypes)            # for data-types of each column
print(net.memory_usage())    # for memory at once

# Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
print(net[net.duplicated()])           # Find duplicate data
net.drop_duplicates(inplace=True)      # Remove duplicate data into to dataframe

# Is there any Null Value present in any column ?
print(net.isnull().sum())

# For 'House of Cards', what is the Show Id and Who is the Director of this show ?
print(net[net.Title=='House of Cards'].loc[:,['Show_Id','Director']])

# In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.
net['Date_N'] = pd.to_datetime(net['Release_Date'],format='mixed')     # Create a new column "Date_N" and convert into datetime formate.
net['Year'] = net.Date_N.dt.year       # Extract the year from the Date_N' column and store these year values in a new column named 'Year'.
net.Year.value_counts().plot(kind='bar')
plt.grid()

# How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
net.Category.value_counts().plot(kind='bar')
plt.show()

# Show all the Movies that were released in year 2016?
print(net[(net.Category=='Movie') & (net.Year==2016)])

# Show only the Titles of all TV Shows that were released in India only?
print(net[(net.Category=='TV Show') & (net.Country=='India')].loc[:,['Title']])

# Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
print(net['Director'].value_counts().head(10))

# Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom" ?
print(net[(net.Category=='Movie') & (net.Type=='Comedies') | (net.Country=='United Kingdom')])

# In how many movies/shows, Tom Cruise was cast ?
print([net.Cast.str.contains('Tom Cruise',na=False)])

# What are the different Ratings defined by Netflix ?
print(net.Rating.unique())

# How many Movies got the 'TV-14' rating, in Canada ?
print(net[(net.Category=='Movie') & (net.Rating=='TV-14') & (net.Country=='Canada')].shape)

# How many TV Show got the 'R' rating, after year 2018 ?
print(net[(net.Category=='TV Show') & (net.Rating=='R') & (net.Year>2018)].shape)

# What is the maximum duration of a Movie/Show on Netflix ?
net[['Minutes','Unit']] = net['Duration'].str.split(' ',expand=True)
net = net.astype({'Minutes':'int'})
print(net.Minutes.max())

# Which individual country has the Highest No. of TV Shows ?
tvshow = net[net.Category=='TV Show']
print(tvshow.Country.value_counts().head(1))

# How can we sort the dataset by Year ?
print(net.sort_values(by='Year',ascending=False))

# Find all the instances where : Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV' ?
net[(net.Category=='Movie') & (net.Type=='Dramas') | (net.Category=='TV Show') & (net.Type=="Kids' TV")]
