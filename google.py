import urllib.request
import urllib.parse
import simplejson

q = urllib.parse.urlencode({'q' : 'windows mac'})

url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' %(q)
print(url)
search = urllib.request.urlopen(url)
print(search)

