from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import requests
import sys
import os
import urllib2
import codecs


BASE_URL = "http://www.reddit.com" #maybe make this into a prompt
i = 0 #global variable for recursion

filename = raw_input("Enter your filename (do not enter file extension): ")
filename = filename + '.csv'

limit = int(raw_input("Enter the number of pages you want to analyze (MAX 50): "))

path_to_script_dir = os.path.dirname(os.path.abspath("webcrawl.py"))  #create a new file no matter what
#newpath = path_to_script_dir + r'\\' + 'intjpages.csv'  #MAKE PROMPT SO NOT ALWAYS intgpages.csv
newpath = path_to_script_dir + r'\\' + filename
#if not os.path.exists(newpath): os.makedirs(newpath)
outfile = open(filename, 'w')
with open(filename, 'ab') as csvfile:
    
    writer = csv.writer(csvfile, delimiter='\n')              
    writer.writerow(["Links"])  #need to do this so links.py doesn't crash'''


def webcrawler(startingurl):

    agentheader = {'User-Agent': 'Nerd_Destroyer'} #cause reddit wants you to do this and I get better results when I do
    request = urllib2.Request(startingurl,headers=agentheader) #not sure why i need to request then open but i do
    url = urllib2.urlopen(request)       
    soup = BeautifulSoup(url)

    for a in soup.find_all('a', "title may-blank ", href=True): #find every post link on the page via the 'title may-blank ' class
        newsite = str(site)
        if not newsite in a['href']: continue  #prevents non-selfposts from getting in the link list. MAYBE MAKE INTO PROMPT
        found_url = BASE_URL + a['href']

        with open(filename, 'ab') as csvfile:  #write to csvfile, need the 'ab' to append to file without adding space. need to autocreate csvfil

            writer = csv.writer(csvfile, delimiter='\n')
            if isinstance(found_url, str): writer.writerow([found_url])  #there's a problem with non-ascii characters being stored in the csv file, I'm just skipping anything that gives problems here
        
        print found_url  #this prints out all links found, even the ones not stored in csv

    for a in soup.find_all('a', rel="nofollow next", href=True):  #finds the next button via the rel/class thing 'nofollow next'
        next_url = a['href']
        print a['href']  #prints in python shell but doesn't append to csvfile
        global i   #global i so value is define during recursions
        global limit
        i+=1
        if i >= limit: break  #limit the amount of pages it crawls, need to make into PROMPT
        webcrawler(next_url)  #recursion


site = raw_input("Enter subreddit you want to analyze: ")
webcrawler("http://www.reddit.com/r/" + str(site))  #run with starting link. need to make into PROMPT
#"http://www.reddit.com/r/intj"

