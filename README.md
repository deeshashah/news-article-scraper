# News Article Scraper 

TL;DR - This code uses  [newsapi.org](newsapi.org) to get news article URL and then scrape news content from various sources, and returns the JSON response of the scraped data.  

Many of the APIs that I came across provided only the headlines and urls of the news articles. None of them provided the content of that news article. The content of news may be required to apply various Machine Learning and Natural Language Processing techniques to improve the functionality of news websites. 

Thus in this project I have used the newsapi provided by [newsapi.org](newsapi.org)

The json data provided by this api is in the following manner

```python
{
	'articles': [
			{
				'author': 'Fleet Street Fox',
				'description': 'The alternative coalition of lexical chaos would see us all tweeting about Ed Balls',
				'publishedAt': '2017-04-28T12:35:03Z',
				'title': 'A strong, stable leader needs strength, stability and a stable, strong message',
				'url': 'http://www.mirror.co.uk/news/uk-news/strong-stable-leadership-needs-3-10314956',
				'urlToImage': 'http://i4.mirror.co.uk/incoming/article10314310.ece/ALTERNATES/s1200/fleet-may.jpg'
			},
		       {
				'author': 'Voice of the Mirror',
				'description': "The Tories' cruel \xa33bn cuts plan has left the education system teetering on the brink of collapse, according to unions",
				'publishedAt': '2017-04-27T21:40:43Z',
				'title': "Voice of the Mirror: May's grim propaganda exposed by destruction of schools",
				'url': 'http://www.mirror.co.uk/news/politics/voice-mirror-theresa-mays-grim-10311950',
				'urlToImage': 'http://i3.mirror.co.uk/incoming/article10311108.ece/ALTERNATES/s1200/PROD-Britains-Prime-Minister-Theresa-May-ges.jpg'
			},
			.
			.
			.
		   ]
}
```

I have written a custom scraper code to scrape the data from the above URL and then after processing, following JSON is returned.

Data After Processing :
```python
{
	'articles': {
			'article_0': {
						'data': "Thank you for that totally unstaged round of applause to this snap general election column which is the only one you will find that can provide the strength and stability to enable Britain to safely chart the uncertain waters of praying for the sweet release of death. That strength and stability doesn't sort itself out: the person in charge of this column must provide the steady hand on the linguistic tiller in a manner which is not just strong, but also stable, in order to avoid the rocky shoals which .... (so on)",
                            			'image': 'http://i4.mirror.co.uk/incoming/article10314310.ece/ALTERNATES/s1200/fleet-may.jpg',
                            			'title': 'A strong, stable leader needs strength, stability and a stable, strong message'
					},
              		'article_1': {
					'data': "The destruction of good and excellent schools exposes the grim reality behind Theresa May and her Tory propaganda.Who would you believe? More than 500 heads who signed a protest letter... or a politician prepared to say anything to con people into voting Tory?The price of May\u2019s \xa33billion education cuts will be paid by the children of working and middle class families in thousands of ... (so on)",
                            		'image': 'http://i3.mirror.co.uk/incoming/article10311108.ece/ALTERNATES/s1200/PROD-Britains-Prime-Minister-Theresa-May-ges.jpg',
                            		'title': "Voice of the Mirror: May's grim propaganda exposed by destruction of schools"
				   },
              	
                            .
                            .
                            .
                            .
                            so on..
              }
}
```

### Steps to Execute the code

- Simply run `fetchApiData.py`. And the dictionary is being created with the above formatted JSON data. Its a basic python script.
- Also I have made an API in Django which can be hosted on a server and given above formatted JSON when requested. [Check it out here] (some link).

Note that - Current code scrapes articles from the source "Mirror". Many other news sites can be scraped. If you want to contribute the scraping code for other sources, add it in the code in the "scraping" package to support more sources.
