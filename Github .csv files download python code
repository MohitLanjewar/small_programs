import requests
url = 'https://raw.githubusercontent.com/codebasics/py/master/pandas/1_intro/nyc_weather.csv'
res = requests.get(url, allow_redirects=True)
with open('nyc_weather.csv','wb') as file:
    file.write(res.content)
