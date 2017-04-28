# News Article Scraper 

Many of the APIs that I came across provided only the headlines and urls of the news articles. None of them provided the content of that news article. The content of news may be required to apply various Machine Learning and Natural Language Processing techniques to improve the functionality of news websites. 

Thus in this project I have used the newsapi provided by newsapi.org[newsapi.org] 
The json data provided by this api is in the following manner
```python
{'articles': [{'author': 'Fleet Street Fox',
                'description': 'The alternative coalition of lexical chaos would see us all tweeting about Ed Balls',
                'publishedAt': '2017-04-28T12:35:03Z',
                'title': 'A strong, stable leader needs strength, stability and a stable, strong message',
                'url': 'http://www.mirror.co.uk/news/uk-news/strong-stable-leadership-needs-3-10314956',
                'urlToImage': 'http://i4.mirror.co.uk/incoming/article10314310.ece/ALTERNATES/s1200/fleet-may.jpg'},
               {'author': 'Voice of the Mirror',
                'description': "The Tories' cruel \xa33bn cuts plan has left the education system teetering on the brink of collapse, according to unions",
                'publishedAt': '2017-04-27T21:40:43Z',
                'title': "Voice of the Mirror: May's grim propaganda exposed by destruction of schools",
                'url': 'http://www.mirror.co.uk/news/politics/voice-mirror-theresa-mays-grim-10311950',
                'urlToImage': 'http://i3.mirror.co.uk/incoming/article10311108.ece/ALTERNATES/s1200/PROD-Britains-Prime-Minister-Theresa-May-ges.jpg'},
               {'author': 'Ian Hyland',
                'description': "In sitcom Bucket, Miriam plays a terminally ill seventysomething mum, who is trying to establish a connection with her daughter - and it's something of a hidden gem",
                'publishedAt': '2017-04-27T19:24:46Z',
                'title': 'Miriam Margolyes dials down but her Bucket list has plenty of life',
                'url': 'http://www.mirror.co.uk/tv/tv-news/miriam-margolyes-dials-down-barmy-10310445',
                'urlToImage': 'http://i3.mirror.co.uk/incoming/article10310706.ece/ALTERNATES/s1200/Bucket.jpg'},
               {'author': 'Fiona Phillips',
                'description': 'Of COURSE black lives matter. It should be a given. White lives matter. Humanity matters',
                'publishedAt': '2017-04-28T15:22:05Z',
                'title': 'All lives matter - no matter what the coloure colour',
                'url': 'http://www.mirror.co.uk/news/uk-news/lives-matter-no-matter-what-10316850',
                'urlToImage': 'http://i3.mirror.co.uk/incoming/article10316508.ece/ALTERNATES/s1200/Fatal-shooting-of-Mark-Duggan-sparks-riots-in-Tottenham-north-London.jpg'},
 'sortBy': 'top',
 'source': 'mirror',
 'status': 'ok'}
```

