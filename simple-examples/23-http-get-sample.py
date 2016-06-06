import urllib2


response = urllib2.urlopen('http://echo.jsontest.com/title/ipsum/content/blah')
#response = urllib2.urlopen('http://hurriyet.com.tr')

print response
print "The URL is : ", response.geturl()
print "get the code : ", response.code
print "The header is : ",response.info
print "The date is : ",response.info()['date'] 
#print "The server is : ",response.info()['server']
print "All data : ",response.read()

#html = response.read()
#print html

# import urlparse

# url = "http://python/org"

# domain = urlparse.urlsplit(url)[1].split(':')[0]
# print "The domain name of the url is: ", domain

# import urllib

# url = 'http://echo.jsontest.com/title/ipsum/content/blah'
# values = { 'productslug': 'bar','qty': 'bar' }
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# result = response.read()
# print result




