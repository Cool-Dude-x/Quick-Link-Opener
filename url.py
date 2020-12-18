import webbrowser
import sys
import subprocess

try:
	keyword = sys.argv[1]
except IndexError:
	exit()

url = dict()

# Add your links here
# url['keyword'] = 'URL'
url['goo'] = 'https://www.google.com'
url['fb'] = 'https://www.facebook.com'
url['duck'] = 'https://duckduckgo.com'
url['bing'] = 'https://www.bing.com'

if url.get(keyword.lower()):
	webbrowser.open_new(url[keyword.lower()])

if keyword == 'edit':
	subprocess.call(sys.argv[0], shell=True)
 