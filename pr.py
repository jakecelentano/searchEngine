
import sys
def pageRank():
	
	#pages
	P = []
	#to split the lines
	me = []
	#initial pagerank estimate
	I = []
	#resulting pagerank estimate
	R = []
	#links
	L = []
	Q = []
	#This part works

	lamb = float(sys.argv[1])
	tau = float(sys.argv[2])
	with open("links.srt",'r', encoding='utf8') as f:
		for line in f:
			me = line.split('\t')
			P.append(me[0])
			L.append((me[0].strip('\n'),me[1].strip('\n')))
	f.close()

	I = [(1/len(P))]*len(P)

	qsize = 0
	count = 0
	while (abs(sum(I)-sum(R))) >= tau:
		R = [lamb/len(P)]*len(P)
		
		while count < len(P):
				
			q1 = L[count][1]
			if q1 in P and L[count] in L:
				Q.append(L[count][0])
				qsize+=1
		
			if qsize>0:
				count2 = 0
				while count2 < qsize:
				
					R[count] = R[count] + (1-lamb)*I[count]/qsize
					count2+=1
						
			else:
				
				count3 = 0
				for q in Q:
					if q in P:	
						R[count3] = R[count3] + (1-lamb)*I[count]/abs(len(P))
						count3+=1
						
	
			count+=1
			if count % 1000 == 0:
				print(count)
			
		print("before set")
		I = R
		print("after set")
	return R
					

def main():
	R = pageRank()
	
if __name__ == '__main__':
	main()


