The project begins with the use of web scrapping to obtain from a Colombian newspaper: link, title and body of each news item. This web scrapping was carried out using the **SCRAPY** framework (https://scrapy.org/). (It could be seen inside the Spider folder as ***larepublica.py*** ). As a result, the **quotes.csv** file is obtained, which is placed in the **Data** folder.

In a second stage, the necessary cleanings are carried out and then the **translation from Spanish to English** is applied to the body of each of the news items, importing Translator from **googletrans**.

Finally, the body of each translated news item is tokenized. The final dataframe is saved as a .csv file, called **df.csv**
