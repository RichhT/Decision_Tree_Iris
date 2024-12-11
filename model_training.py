from sklearn import tree
from sklearn.model_selection import train_test_split

def new_section():
    new_line = "-" * 79
    print(new_line)
    print('\n')

def train_model(iris_data):
    new_section()
    proceed = input("Please press enter to begin model training...")
    new_section()
    print("Creating train test split...")
    proceed = input("Enter to proceed")
    X_train, X_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], test_size=0.30, random_state=8)
    print("Data successfully split into training and test sets.")
    new_section()
    proceed=("Training model on training dataset.\nEnter to proceed.")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)



