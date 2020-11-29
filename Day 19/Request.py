
import webbrowser  # web browser module to open websites
import requests

url = 'https://www.google.com'
response = requests.get(url)
print(f'Response returned: {response.status_code}, {response.reason}')
print(response.text)

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.google.com',
    'https://ysquaresolutions.com'
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
