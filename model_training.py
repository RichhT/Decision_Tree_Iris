from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics

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
    new_section()
    print("Data successfully split into training and test sets.")
    proceed=("Training model on training dataset.\nEnter to proceed.")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    proceed = input("Model successfully trained.\nEnter to proceed")
    tree_display = tree.plot_tree(clf)
    output = input(("Would you like to see a visual representation of the decision tree?\nY/N: "))
    if output.lower() == 'y':
        show_tree(clf)
    input("Enter to continue.")
    print("Decision tree making predictions...")
    input("Enter to proceed.")
    y_pred = clf.predict(X_test)
    input("Predictions made. Evaluating predictions...")
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Model evaluation complete.\nModel accuracy:{accuracy}")
    output = input("Would you like to see a confusion matrix? ")
    if output.lower() == 'y':
        display_cm(y_test, y_pred)





def show_tree(model):
    tree_display = tree.plot_tree(model)
    plt.show()
    output = ("Enter to proceed")

def display_cm(y_test, y_pred):
    confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
    cm_display.plot()
    plt.show()
    output = ("Enter to proceed")



