def printList(list:list):
    for elt in list:
        print(elt)


def getData(filename="Question"):
    data = []
    with open(filename, "r") as file:
        temp = []
        for line in file:
            temp.append(line.strip())
            if len(temp) == 5:
                data.append(temp)
                temp = []
    return data





def processData(data):
    dic = {}
    for elt in data:
        question = elt[0].split('?')[0]+'?'
        options = [opt.strip() for opt in elt[1:5]]
        answer = elt[0].split('?')[1].strip()
        dic[question] = {"reponse": answer, "options": options}
    return dic


