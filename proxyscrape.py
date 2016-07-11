#!/usr/bin/env python
 
from BeautifulSoup import BeautifulSoup as Soup
import re, urllib
import socket, os

socket.setdefaulttimeout(180)
proxylist = []
sources = 'proxys-sources.txt'
proxies = 'proxies.txt'
# definiendo la variable que va y abre el url para detectar proxys en el archivo
# aqui se le puede agregar mas regex para tenerlo afinado
def scrape_proxies(url):
  global proxylist
  document = urllib.urlopen(line)
  tree = Soup(document.read())
  regex  = re.compile(r'^(\d{3}).(\d{1,3}).(\d{1,3}).(\d{1,3}):(\d{2,4})')
  regex = re.compile('^((([^:]+):([^@]+))@)?((\d{1,3}\.){3}\d{1,3})(:(\d{1,5}))$')
  proxylist = tree.findAll(attrs = {"class":"Apple-style-span", "style": "color: black;"}, text = regex)
  data = proxylist[0]
  for x in data.split('\n'):
    proxylist.append(x)


fp = open(proxies, 'w')
# Esto abre el archivo txt y lo itera para sacar proxys de esas paginas.
with open(sources) as f:
   for line in f:
      scrape_proxies(line)

fp.write("\n".join(proxylist))

#print proxylist[]
os.system("python checkproxies.py")





