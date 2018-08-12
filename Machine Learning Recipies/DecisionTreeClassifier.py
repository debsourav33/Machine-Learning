header= ['color','size','label']


def class_counts(data):
    counts = {}

    for row in data:
        lbl = row[-1]
        if lbl not in counts:
            counts[lbl] = 0
        counts[lbl] += 1

    return counts


def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)


class Question:
    def __init__(self, col, value):
        self.col = col
        self.value = value

    def match(self,x):
        if(is_numeric(self.value)):
            return x[self.col]>=self.value
        else:
            return x[self.col]==self.value

    def __repr__(self):
        if(is_numeric(self.value)):
            condition=">="
        else:
            condition="=="

        return "Is %s %s %s?" % (header[self.col],condition,self.value)


def partition(data, question):
    true_rows, false_rows= [],[]

    for row in data:
        if(question.match(row)):
            true_rows.append(row)
        else:
            false_rows.append(row)


    return true_rows, false_rows


def gini(data):

    impurity= 1
    counts= class_counts(data)
    length= len(data)

    for lbl in counts:
        prb= counts[lbl]/length
        impurity-=prb**2

    return impurity

def info_gain(data,true_rows,false_rows):

    p= len(true_rows)/float(len(data))
    return gini(data)- p*gini(true_rows)- (1-p)*gini(false_rows)


def find_best_split(data):
    best_question= None
    best_gain= 0

    n_features= len(training_data[0])-1

    for col in range(n_features):
        values= set(x[col] for x in data)

        for val in values:
            q= Question(col,val)

            true_rows, false_rows= partition(data,q)

            if len(true_rows)==0 or len(false_rows)==0:
                continue

            gain= info_gain(data,true_rows,false_rows)
            if gain>best_gain:
                best_gain=gain
                best_question=q

    return best_gain, best_question

class Leaf:
    def __init__(self,data):
        self.prediction= class_counts(data)

class decision_node:
    def __init__(self,true_branch,false_branch,question):
        self.true_branch= true_branch
        self.false_branch= false_branch
        self.question= question


def build_tree(data):

    gain, question= find_best_split(data)

    if(gain==0):
        return Leaf(data)

    true_rows, false_rows= partition(data,question)

    true_branch= build_tree(true_rows)
    false_branch= build_tree(false_rows)

    return decision_node(true_branch,false_branch,question)


def print_tree(node,spacing=" "):
    """The world's most elegant tree printing function"""

    if(isinstance(node,Leaf)):
        print(spacing+"Prediction:",node.prediction)
        return

    print(spacing+str(node.question))

    print(spacing+'-->True')
    print_tree(node.true_branch,spacing+"  ")

    print(spacing+'-->false')
    print_tree(node.false_branch,spacing+"  ")

def print_accuracy(counts):
    length=0
    for lbl in counts:
        length+=counts[lbl]

    for lbl in counts:
        print("%s= %.2f%%" %(lbl,counts[lbl]*100/length))

def traverse(node,x):
    if isinstance(node,Leaf):
        print_accuracy(node.prediction)
        return

    if(node.question.match(x)):
        traverse(node.true_branch,x)
    else:
        traverse(node.false_branch,x)

def predict(root,data):
    prediction=[]
    cnt=1

    for x in data:
        print("\nPrediction accuracy for data #%d:"%(cnt))
        cnt+=1
        traverse(root,x)

    return prediction

if __name__ == '__main__':
    training_data = [['Green', 3, 'Apple'],
                     ['Yellow', 3, 'Apple'],
                     ['Red', 1, 'Grape'],
                     ['Red', 1, 'Grape'],
                     ['Yellow', 3, 'Lemon']
                     # ['Green', 4, 'Apple'],
                     # ['Red', 4, 'Mango'],
                     # ['Blue', 1, 'Berry'],
                     # ['Yellow', 2, 'Lemon']
                     ]

    root= build_tree(training_data)
    #print_tree(root)
    test=[['Yellow',3],['Red',3]]
    predict(root,test)








