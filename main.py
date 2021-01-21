import urllib.request

def get_url(url):

	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

def parse_game_ids(mystr):
	GAME_IDS=[]
	id_pos=mystr.find("/p/")
	id_length=17
	while id_pos!=-1:
		id_pos=mystr.find("/p/")
		GAME_IDS.append(mystr[id_pos+6:id_pos+id_length])
		mystr=mystr[id_pos+2:]

	GAME_IDS=set(GAME_IDS[:-1])

	return list(GAME_IDS)
def get_pgn(game_id):
	return get_url("https://www.playok.com/p/?g="+str(game_id)+".txt")

def get_game_ids(url):
	txt=get_url(url)
	ids=parse_game_ids(txt)
	return ids
def list_to_txt(filename,ids):
	with open(filename, 'w') as file_handler:
	    for i in ids:
	        file_handler.write("{}\n".format(i))
	print("Done")
ids = open("PGNS2.txt", "r")
with open('PGNS3.txt','w') as file_handler:
	for i,line in enumerate(ids):
		print(i,line)
		if line[0:6]=='[Event':
			file_handler.write('\n\n'+line)
		elif line[0:3]=='1. ':
			file_handler.write('\n'+line)
		else:
			file_handler.write(line)



# PGNS=""
# for c,i in enumerate(ids):
# 	print(c)
# 	PGNS+=get_pgn(i[:-1])
# 	#print(PGNS)
# 	break

# new=PGNS.strip(PGNS[11:13])
# print("bb:",PGNS[11:13])
# print(new)
# # with open('test.txt', 'w') as file_handler:
# # 	file_handler.write(PGNS)


