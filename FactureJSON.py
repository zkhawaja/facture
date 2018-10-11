import json

def JSON(fichier):
    dict = {}
    dict2 = {}
    listkey = []
    key = 5
    listdict = []
    with open('fichierJSON.txt','a') as file:
        with open(fichier,'r') as f:
            i = 0
            for line in f:
                if i ==0:
                    liste1 = line.split(';')
                    for j in range(6):
                        dict[liste1[j]] = ''
                        listkey.append(liste1[j])
                    dict[liste1[5]] = []
                    for j in range(5,9):
                        dict2[liste1[j]] = ''
                        listkey.append(liste1[j])
                    dict[liste1[5]].append(dict2)
                    i +=1
                    #file.write(json.dumps(dict))
                else:
                    liste1 = line.split(';')
                    for j in range(5):
                        dict[listkey[j]] = liste1[j]

                    for j in range(5,len(liste1),4):
                        if liste1[j] == '':
                            break
                        for k in range(j-1,j+4):
                            if "\n" in liste1[k]:
                                dict2[listkey[key]]= liste1[k].split('\n')[0]
                            else:
                                dict2[listkey[key]]= liste1[k]
                            key +=1
                        key = 5
                        listdict.append(dict2)
                    dict[listkey[5]] = listdict
                    file.write(json.dumps(dict)+"\n")
                    listdict.clear()

JSON(r'C:\Users\Fitec\Desktop\python\exo\data.csv')