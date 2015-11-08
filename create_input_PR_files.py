import snap

graphFile = './Edge_List_Users_Amazon_Instant_Video.txt'
graph = snap.LoadEdgeList(snap.PUNGraph, graphFile, 0, 1, '\t')
# print graph.GetEdges()

wtData = {}
with open(graphFile,'r') as f:
	for line in f.xreadlines():
		data = line.split()
		k = ( int(data[0]), int(data[1]) )
		v = float(data[2])
		wtData[k] = v

filename = './out/Edge_List_Users_Amazon_Instant_Video.tree'

outFilePrefix = './UnanalyzedClusters/cluster'
# outFilePrefix = './input_PR/cluster'
N = 400

def writeToFile(fname, NIdV, idx):
	subG = snap.GetSubGraph(graph, NIdV)
	string = ''
	if idx==1:
		print subG.GetEdges()
	for edge in subG.Edges():
		n1 = edge.GetSrcNId()
		n2 = edge.GetDstNId()
		v = wtData[(n1,n2)] if (n1,n2) in wtData else wtData[(n2,n1)]
		string += '%d\t%d\t%0.4f\n' %(n1, n2, v)
	with open(fname, 'w') as f:
		f.write(string)
	# if idx==399:
	# 	print len(NIdV), '\t', subG.GetNodes(), '\t', subG.GetEdges()
	# snap.SaveEdgeList(subG, fname)
	# FOut = snap.TFOut(fname)
	# subG.Save(FOut)
	# FOut.Flush()
	# if idx==N:
	# print subG.GetNodes()
	# print subG.GetEdges()
	# print snap.CntDegNodes(subG, 0)

with open(filename, 'r') as inputFile:
	idx = 1
	# toWrite = ''
	NIdV = snap.TIntV()
	minVal = 1000000
	outFile = outFilePrefix+str(idx)
	for line in inputFile.readlines():
		if line[0] == '#':
			continue
		if idx > N:
			continue
		colon = line.split(':',1)
		clusterNum = int(colon[0])
		nodeId = int(colon[1].split()[-1])
		if clusterNum > idx:
			# with open(outFile,'w') as f:
			# 	f.write(toWrite)
			outFile = outFilePrefix+str(idx)
			writeToFile(outFile, NIdV, idx)
			# if minVal > len(NIdV):
			# 	minVal = len(NIdV)
			# 	print idx, '\t', minVal
			NIdV = snap.TIntV()
			idx += 1
			# toWrite = ''
		if idx > N:
			break
		# toWrite += nodeId+'\n'
		NIdV.Add(nodeId)
