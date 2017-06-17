import pandas
from collections import Counter

# calculating number of males and females
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(str(data.get('Sex').value_counts()['male']) + ' ' + str(data.get('Sex').value_counts()['female']))

# calculating percentage of survived people at Titanic
survived = data.get('Survived').value_counts()[1]
all = data.get('Survived').value_counts().sum()
print("%.4f" % (survived / all))

# calculating percentage of first class at Titanic
first_class = data.get('Pclass').value_counts()[1]
all = data.get('Pclass').value_counts().dropna().sum()
print("%.4f" % (first_class / all))

# calculating mean and median
ages = data.get('Age')
print("%.2f" % ages.mean(axis=0), "%.2f" % ages.median(axis=0), sep=' ')

# calculating pearson correlation between SibSp and Parch columns
print(data.corr(method='pearson')['SibSp']['Parch'])

# computation of most popular female name
women_names = data.where(data.get('Sex') == 'female').get('Name').dropna()
first_names = []
for name in women_names:
    # selecting first name from full name
    bracket = name.find('(')
    if bracket != -1:
        first_name = name[bracket + 1:name.find(' ', bracket + 1)]
    else:
        dot = name.find('.')
        first_name = name[dot+2:name.find(' ', dot + 2)]
    first_names.append(first_name)
print(Counter(first_names).most_common(1)[0][0])
