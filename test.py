from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    X = df[iris.feature_names]
    y = df['species']

    X_train, X_test, y_train, y_test = split_data(X,y)

    model = train_model(X_train, X_test, y_train, y_test)


    eval_model(model, X_test, y_test)


def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_model(X_train, X_test, y_train, y_test):

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    return clf

def eval_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model´s  accuracy: {accuracy:.2f}')


if __name__ == "__main__":

    main()