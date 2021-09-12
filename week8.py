# Network and HTML

# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode())
# mysock.close()

# Using urllib

# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# Using beautiful soup, tags(links)

# from bs4 import BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
#
# html = urllib.request.urlopen('http://www.google.com').read()
# soup = BeautifulSoup(html,'html.parser')
#
# # Retrieving the tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# Using SSl library on websites that use https

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = 'http://data.pr4e.org'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# Pulling parts of tags
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = 'http://data.pr4e.org'
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

# Exercise 12.1

# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# url = input('Enter a url:')
# host = url.split('/')[2]
#
# mysock.connect((host, 80))
# cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n' #Spaces are important here
# cmd = cmd.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode())
# mysock.close()

# Exercise 12.2

# import socket
# sum = 0
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# url = 'http://data.pr4e.org/romeo.txt'
# host = url.split('/')[2]
#
# mysock.connect((host, 80))
# cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n' #Spaces are important here
# cmd = cmd.encode()
# mysock.send(cmd)
#
# data = mysock.recv(512)
# data = data.decode()
# print(data[:3000])
# print(len(data))
#
# mysock.close()

# Exercise 12.3

# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# for line in fhand:
#     print(line.decode().strip()[:3000])
#     print('Length of text is ' + 'characters')

# Exercise 12.4

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = 'https://docs.python.org/3/library/stdtypes.html#string-methods'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('p')
#
# print(len(tags))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://docs.python.org/3/library/stdtypes.html#string-methods'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the paragraph tags
tags = soup('p')
for tag in tags:
    print(type(tag))
print(len(tags))
