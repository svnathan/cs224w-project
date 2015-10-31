import sys
import gzip
import snap
import time

yearlist = []
countlist = []

def parseIterator(path):
	g = gzip.open(path, 'r')
	for l in g:
		yield eval(l)

def parseReviews(path):
	# Adding nodes to GUsers
	global combinedNodeId
	usersNodeId = 0
	for review in parseIterator(path):
		# Adding nodes to GUsers
		year = review['reviewTime'].split()
		if year not in yearlist:
			yearlist.append(year)
			countlist.append(1)
		else:
			index = yearlist.index(year)
			countlist[index] += 1

	for i in range(0, len(yearlist)):
		print str(yearlist[i]) + " - " + str(countlist[i])

		
		
def main(argv):
	item = 'Automotive'

	# Parsing Reviews
	parseReviews('reviews_' + item + '.json.gz')
	

if __name__ == '__main__':
	start_time = time.time()
	main(sys.argv)
	print 'Execution time is ' + str(time.time() - start_time) + ' seconds'