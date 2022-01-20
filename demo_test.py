# create a collection of news/articles having the keys as
# id,title,date,description and type
# Apply operations to search based on id or category or type

# news_articles = list()
# print(len(news_articles))
news_articles = [{'id': 123, 'title': 'Happy new year', 'date': '01-01-2022',
                  'description': 'It is 2022 for KLU'},
                {'id': 124,'title': 'RRR', 'date': '07-01-20',
                 'description': 'It is releasing'},
                 {'id': 125,'title': 'KLU', 'date': '01-03-2022',
                  'description': 'It is opening again'},
                 {'id': 126,'title': 'cricket', 'date': '12-01-2022',
                  'description': 'IPL starts again'},
                 {'id': 127,'title': 'COVID-19', 'date': '15-02-2022',
                  'description': 'Cases increasing again'}
                 ]
article = {'id': [123, 124, 125, 135, 137], 'title': {}, 'date': []}
print(type(article))
# print(type(news_articles), len(news_articles))
for na in news_articles:
    if na.get('id') == 123:
        print(na.get('type'))
        print(na.get('date'))
        print(na.get('title'))



