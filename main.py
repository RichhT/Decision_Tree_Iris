import sklearn.datasets
import explore_features
import menu
import model_training

new_line="-"*79

iris_data = sklearn.datasets.load_iris()

# 1 is features, 2 is target variable, 3 is keys

print(iris_data.data)

while True:
    choice = menu.menu()

    if choice == 1:
        explore_features.show_features(iris_data)
        proceed = input('Enter to proceed')

    elif choice == 2:
        explore_features.show_target(iris_data)
        proceed = input('Enter to proceed')

    elif choice == 3:
        explore_features.show_keys(iris_data)
        proceed = input('Enter to proceed')

    elif choice == 4:
        model_training.train_model(iris_data)