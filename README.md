# Scraping Project

## Process

For this project, I scraped information from the Billboard Year-End Hot 100 singles from [2010](https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2010) to [2015](https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2015) from Wkikipedia.

I thought this information might be useful for analyzing recent music trends, so I collected song titles, artists, genres, producers, labels, and writers. The information could be used to make several comparisons, for example: which artists and genres are most popular; who produces the most popular music; and which artists write their own songs.

First I had to create a list of links to follow, which I did with `getTableLinks()`. I looped through the years after that to construct the complete paths.

Then I built several functions(`getTitle()`, `getArtist()`, etc.)  to get each item in the tables. This was hard because Wikipedia doesn't give IDs or classes for the items in the song page tables, so I had to figure out ways to reach the information. With help from [this StackOverflow response](http://stackoverflow.com/questions/18227209/how-can-i-get-the-first-and-third-td-from-a-table-with-beautifulsoup), I made a list of the table items with `get_tr_list()` because I didn't want to write "`bsObj.find("table", {"class":"infobox vevent"}).find_all("tr")`" in each function. That allowed me to reach some information by simply jumping to whateever number in the list I was looking for, although it didn't work as well as I had hoped.

Finally I wrote a function to add the items to a CSV file.

## Problems

I thought I was so smart, navigating to each item by its order number (ex. "`titles = tr_list**[0]**.find("th", {"class":"summary"})`"), until I realized that the tables often skip rows. Some tables had a row for "Recorded," but plenty didn't, which threw off my whole system. The only option I could think of was to somehow jump to the `<tr>` containing the word I was looking for (ex. Genre, Label) and navigate from there to the next `<td>` containing the information I needed. Before I spiraled too far into despair, I found [this wonderful StackOverflow response](http://stackoverflow.com/questions/33744798/using-python-and-beautifulsoup-to-find-certain-table-cell-value-then-print-the), which told me exactly how to do that.

I also kept running into errors that broke my program several times. I didn't realize how inconsistent Wikipedia's song pages would be. So I added Try/Excepts to almost every function.

## What changed

Originally, I had planned to run this program starting in 1951, the first year of Billboard singles avaialble, but that would have taken too long. That would be easy to change, though  — just change 2010 to 1951.

I also added more items to scrape from the individual song pages — originally, I was not going to scrape label, producer or writer.
And I decided to scrape artist and song title from the individual pages instead of the main page to make the output easier to format.
