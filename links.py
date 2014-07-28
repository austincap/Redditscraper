from bs4 import BeautifulSoup
import urllib2, urllib
import csv
import requests
import sys
import os
import codecs

filename = raw_input("Please enter the filename (no extension): ")
newfilename = filename + '.csv'


with open(newfilename, 'rb') as csvfile:
    pagereader = csv.reader(open(newfilename,"rb"))  #read from csvfile, maybe make prompt so more flexible than intjpages
    i=0
    for row in pagereader:
        if "http://" in row[0]:  #checks to make sure it's not a title cell
            print row
            
            agentheader = {'User-Agent': 'Nerd_Destroyer'}  #access page with header and turn into soup

            newurl = row[0].decode('string_escape')
            request = urllib2.Request(newurl,headers=agentheader)  #each row is a list with one value
            url = urllib2.urlopen(request)       
            soup = BeautifulSoup(url)
            
            for div in soup.findAll('div', {"class" : "side"}):  #take out sidebar junk
                div.extract()
            for div in soup.findAll('div', {"class" : "wiki"}):  #take out privacy philosophy stuff
                div.extract()
            body = soup.find_all("div", { "class" : "md" })  #find all post and comment data

            name = "page" + str(i) + ".html"  #create newfile name
            path_to_script_dir = os.path.dirname(os.path.abspath("links.py"))
            newpath = path_to_script_dir + r'\\' + filename  #create folder name
            if not os.path.exists(newpath): os.makedirs(newpath)  #checks if folder exists
            outfile = open(path_to_script_dir + r'\\' + filename + r'\\' + name, 'w')  #create new file
            body=str(body)  #write to file
            outfile.write(body)
            outfile.close()
            i+=1
        else:
            print row
            

