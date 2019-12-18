import urllib.request
webUrl  = urllib.request.urlopen(input('Enter the website you wanna open: '))

print ("result code: " + str(webUrl.getcode()))

data = webUrl.read()
print (data)