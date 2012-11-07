import sys
import urllib2
from collections import defaultdict
from bs4 import BeautifulSoup

hackerTable = defaultdict(int)

def getMembers(url):
  text = urllib2.urlopen(url).read();
  soup = BeautifulSoup(text);
  memberList = []

  data = soup.findAll('ul',attrs={'class':'members-list'});
  for div in data:
    links = div.findAll('li')
    for link in links:
		  memberList.append("https://github.com" + str(link.a['href']))
	
  return memberList

def getFollowings(url):
	text = urllib2.urlopen(url).read();
	soup = BeautifulSoup(text);

	friendList = []
	data = soup.findAll('ul',attrs={'class':'members'});
	if len(data) > 0:
		for div in data:
			links = div.findAll('li')
  		if len(links) > 0:
  			for link in links:
  				friendList.append(link.a['href'])
  				hackerTable[link.a['href']] += 1
  				print 'Link that goes into hashtable: ' + link.a['href']
		  	 
				print 'Member: ' + str(link.a['href'])
  
  
	return friendList

def getAllFollowings(url):
	i,totalFollowers = 1, []
	followerList = getFollowings(url + '/following?page=' + str(i))
	
	while(len(followerList) != 0):
		print "followerList: " + str(len(followerList))
		i += 1
		followerList = getFollowings(url + '/following?page=' + str(i))
	
	return

def crawlWithDepth(depth, hackersToCrawl, topHackerCount):
	if depth > 0:
		for i in xrange(len(hackersToCrawl)):
			#given List of People Retrieve all of their followings.
			#Insert them to hash and increase their rank by 1 in each occurence
			print 'Hacker Name: ' + hackersToCrawl[i]
			getAllFollowings(hackersToCrawl[i])
		
		topHackers, counter = [], 0
			
			#sort the hacker hash and choose N best hackers among the others
		sortedHackerHash = sorted(hackerTable, key=hackerTable.get, reverse=False)
			
		for hacker in sortedHackerHash:
			if counter >= topHackerCount:
				break
			topHackers.append('https://www.github.com' + hacker)
			counter += 1
		
		print 'My Top Hackers: ' + str(topHackers)
		
		if len(topHackers) < 1: # If you end up getting no hackers at all
			return hackersToCrawl #return the previous full list
		
		hackerTable.clear() #clear the hash for the new hackers
		return crawlWithDepth(depth - 1, topHackers, topHackerCount)
	else:
		return str(hackersToCrawl)
		
#default settings

url = "https://github.com/vmware?tab=members"; 
topHackerCount = 2
depth = 3

#end of default settings

if (len(sys.argv) > 1):
	url = sys.argv[1] + '?tab=members'

if (len(sys.argv) > 2):
	depth = int(sys.argv[2])

if (len(sys.argv) > 3):
	topHackerCount = sys.argv[3]


employeeList = getMembers(url)
hackers =  crawlWithDepth(depth, employeeList, topHackerCount)
print 'Hackers you should take a look: ' + str(hackers)