import matplotlib.pyplot as plt
import math
import os
import logging
import sys, getopt;
#path="C:\Users\Xuan Thanh\Desktop\sisron\domain.txt"

def readFileToList(file_path):
    """
    Read data from a file .txt
    File contains malicious domains
    """
    if not os.path.isfile(file_path):
        logging.debug("File %s not found", file_path)
        return []
    else:
        with open(file_path)as f:
            content=f.readlines()
            #you may also want to remove whitespace like '\n' at end of each line
            content=[x.strip() for x in content]
            return content

def checkDuplicate(rawList):
    """
    remove same value in array
    """
    newList=[]
    for item in rawList:
        if item not in newList:
            newList.append(item)
    return newList
	
def Number(newList,rawList):
    """
    get number of same value in array
    """
    result=dict()
    for item in newList:
        result[item]=int(rawList.count(item))
    return result
	
def getTopLevelDomain(rawList): #get to Top Level Domain 
    """
    get Top Level Domain of domains
    """
    listDomain=[]
    for item in rawList:
        TDL=item.split('.')[1]
        if TDL not in listDomain:
            listDomain.append(TDL)
    return listDomain

def probability(listOfYou,newList):
    block=dict() 
    for item in listOfYou:
        block[item]=newList.count(item)/float(len(newList))*100 #%
    return block
	
def entropy(string):
    """Calculates the Shannon entropy of a string"""
    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    return entropy
	
def drawBarwithProbability(listOfYou,rawList):
    dictOfYou=probability(listOfYou,rawList)
    x=list(dictOfYou.keys())
    x_sort=sorted(x,reverse=False)
    y_sort=[value for (key, value) in sorted(dictOfYou.items(), reverse=False)]
    idArray=range(len(dictOfYou))
    #print(x)
    #print(y)
    #print(idArray)
    plt.bar(idArray,y_sort,align='center')
    plt.xticks(idArray,x_sort,fontsize=20)
    #plt.ylim(0,100)
    plt.yticks(fontsize=20)
    plt.ylabel('%',fontsize=20)
    plt.title('Probability of characters')
    #for x, y in zip(idArray, y):
       # plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom', fontsize='8')
    plt.show()	
def drawBarwithNumber(listOfYou,rawList):
    x=list(Number(listOfYou,rawList).keys())
    y=list(Number(listOfYou,rawList).values())
    idArray=range(len(Number(listOfYou,rawList)))
	#print(x)
    #print(y)
    #print(idArray)
    plt.bar(idArray,y,align='center')
    plt.xticks(idArray,x)
   # plt.ylim(0, int(y[0]) + 0.01)
    plt.show()

def checkRule(rawList,newList):
    list_SLD=[] #list of second domain
    len_domain=[]
    #print list of second domain:
    print("Second domain: ")
    for item in rawList:
        string=item.split('.')[0]
        length=len(string)
        len_domain.append(length)
        if string not in list_SLD:
            list_SLD.append(string)
    print(list_SLD)
    #print length of second domain generateds
    print("Do dai ten mien duoc sinh ra la: "+str(sorted(checkDuplicate(len_domain),reverse=False))+" bytes")
    """
    Calculating entropy of SLD
    """
    entropy_list=dict()
    for item in list_SLD:
        entropy_list[item]=entropy(item)
    print("Entropy cua SLD: ")    
    print(entropy_list)
    value_entropy=list(entropy_list.values())
    print("Entropy max: "+ str(max(value_entropy)))
    print("Entropy min: "+ str(min(value_entropy)))	
    print("Quy luat cu phap la:")
    ch=[]
    for i in list_SLD:
        ch= ch+list(i)
    ch2=checkDuplicate(ch)
    print("Tong so cac ky tu sinh ra second domain: "+str(len(ch2)) +" ky tu")
    print("cac ky tu sinh ra so lan: "+str(len(ch))+ " lan")
    print("So luong cac ky tu: ")
    print(Number(ch2,ch))
    print("Tan suat: ")
    print(probability(ch2,ch))
	#draw bar for character
    drawBarwithProbability(ch2,ch)
    #drawBarwithNumber(ch2,ch)


def main(argv):
    inputfile=''
    outputfile=''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('analysis log.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print('analysis log.py -i <inputfile> -o <outputfile>')
        sys.exit()
      elif opt in ("-i", "--ifile"):
        inputfile = arg
      elif opt in ("-o", "--ofile"):
        outputfile = arg
        
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)
    path =inputfile
    sys.stdout=open(outputfile,'a')
    rawList=readFileToList(path)
    newList= checkDuplicate(rawList)
    print("****************************************")
    print("File phan tich: "+ inputfile)
    print("Tong so queries la: "+ str(len(rawList)))
    print("Danh sach domain: \n")
    print(newList)
    print("\nSo luong domain sinh ra:"+str(len(newList)))
    print("TLD: "+ str(getTopLevelDomain(rawList)))
	#so luong cac ten mien khac nhau
    print(Number(newList,rawList))
	#xac suat
    print(probability(newList, rawList))
    checkRule(rawList,newList)
	
    
if __name__ == "__main__":
   main(sys.argv[1:])
    
    
