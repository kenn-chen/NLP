import pickle
f2=open("/home/kawamoto/kawamoto/NLP/n-gram/01_2.dict","rb")
dict2 = pickle.load(f2)
for k, v in dict2.items():
    print ("%d %s %s" %(v, k[0].decode('utf-8','ignore'), k[1].decode('utf-8','ignore')))
 
