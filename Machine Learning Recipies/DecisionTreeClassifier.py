training_data=[ ['Green',3,'Apple'],
                ['Yellow',3,'Apple'],
                ['Red',1,'Grape'],
                ['Red',1,'Grape'],
                ['Yellow',3,'Lemon']
               ]

def unique_vals(data,col):
    return set(row[col] for row in data)

def class_count(data):

    count= {}

    for row in data:
        label= row[-1]

        if label not in count:
            count[label]=0

        count[label]+=1

    return count

def isNumeric(value):
    return isinstance(value,int) or isinstance(value,float)

class Question():
    def __init__(self,col,value):
        self.col=col
        self.value=value

    def match(self,example):
        if(isNumeric(self.value)):
            return example[self.col]>=self.value
        return example[self.col] == self.value


def partition(data,question):
    true_rows, false_rows= [], []

    for row in data:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)

    return true_rows, false_rows


def gini(data):

    impurity=1

    count= class_count(data)
    for label in count:
        prb= count[label]/(float)(len(data))
        impurity-=prb**2

    return impurity

def infoGain(current_uncertainity, true_rows, false_rows):
    p= (len(true_rows)/(float)(len(true_rows)+len(false_rows)))

    return current_uncertainity- p*gini(true_rows)- (1-p)*gini(false_rows)


def findBestSplit(data):

    best_gain=0
    best_Question= None

    current_uncertainity= gini(data)

    length= len(data[0])

    for col in range(length):

        values= unique_vals(data,col)

        for val in values:

            q= Question(col,val)

            true_rows, false_rows= partition(data,q)

            if((len(true_rows)==0)or(len(false_rows)==0)):
                continue

            current_gain= infoGain(current_uncertainity,true_rows,false_rows)

            if(current_gain>=best_gain):
                best_gain=current_gain
                best_Question=q


    return best_gain,best_Question

class Leaf():

    def __init__(self,data):
        self.prediction=class_count(data)

class DecisionNode():

    def __init__(self,question,true_branch,false_brance):
        self.true_branch=true_branch
        self.false_branch= false_brance
        self.question= question


def build_tree(data):

    gain, question= findBestSplit(data)

    if(gain==0):
        return Leaf(data)

    true_rows, false_rows= partition(data,question)

    true_branch= build_tree(true_rows)
    false_branch= build_tree(false_rows)

    return DecisionNode(question,true_branch,false_branch)


def classify(node, example):

    if isinstance(node,Leaf):
        return node.prediction

    if(node.question.match(example)):
        return classify(node.true_branch,example)
    else:
        return classify(node.false_branch, example)

def printLeaf(counts):

    total= sum(counts.values()) * 1.0
    probs={}

    for lbl in counts:
        probs[lbl] = str(int(counts[lbl]/total*100))+"%"

    print(probs)

if __name__ == '__main__':
    my_tree= build_tree(training_data)
    printLeaf(classify(my_tree,training_data[1]))



