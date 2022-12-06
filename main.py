import os
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from PIL import Image
from PIL import ImageDraw
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image as PImage
from subprocess import check_call


def clean_dataset(data):
    assert isinstance(data, pd.DataFrame), "df needs to be a pd.DataFrame"
    data.dropna(inplace=True)
    indices_to_keep = ~data.isin([np.nan, np.inf, -np.inf]).any(1)


def find_cat(data, max_count_unique=5):
    for name in data.columns:
        s = ''
        s += name
        if type(data[name][0]) == str:
            s += ' is string, '
        if data[name].nunique() <= max_count_unique:
            s += ' few unique'
        if s != name:
            print(s, data[name].unique())


# replacing categorical variables
def encoding_cat(data, max_count_unique=5, msg=True):
    for name in data.columns:
        if type(data[name][0]) == str and data[name].nunique() <= max_count_unique:
            le = LabelEncoder()
            le.fit(data[name])
            data[name] = le.transform(data[name])
    if msg:
        print('Encoding done!')


if __name__ == '__main__':
    for dirname, _, filenames in os.walk('/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
    SEED = 15
    train = pd.read_csv('input/train.csv')
    test = pd.read_csv('input/test.csv')
    train.head()
    clean_dataset(train)
    find_cat(train)
    encoding_cat(train)
    train.info()
    train.Class = train.Class.replace({0: 3})
    # Correcting Class variable in accordance with the meaning Eco -> Eco Plus -> Business
    train['Arrival Delay in Minutes'].astype('int')
    y = train.satisfaction
    X = train.drop(['Unnamed: 0', 'id', 'satisfaction'], axis=1)
    X.head()
    train.Class = train.Class.replace({0: 3})
    # Correcting Class variable in accordance with the meaning Eco -> Eco Plus -> Business
    train['Arrival Delay in Minutes'].astype('int')
    y = train.satisfaction
    X = train.drop(['Unnamed: 0', 'id', 'satisfaction'], axis=1)
    X.head()
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    decision_tree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=100, random_state=SEED)
    decision_tree.fit(X_train, y_train)
    DecisionTreeClassifier(criterion='entropy', max_depth=100, random_state=15)
    with open("tree1.dot", 'w') as f:
        f = export_graphviz(decision_tree, out_file=f, max_depth=4,#4
                            impurity=True, feature_names=X_train.columns,
                            rounded=True, filled=True)
    check_call(['dot', '-Tpng', 'tree1.dot', '-o', 'tree.png'])
    img = Image.open("tree.png")
    draw = ImageDraw.Draw(img)
    img.save('sample-out.png')
    PImage("sample-out.png")
    decision_tree.score(X_val, y_val)
