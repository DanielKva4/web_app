import numpy as np
import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import requests
import json
from datetime import date, timedelta
import statistics


# def shame():
#     return 'Твоя функция не пашет дружок'
#
#
# def calk(a, b):
#     if a > 5:
#         c = a + b
#         return c
#     else:
#         return shame()


def linear_regression():
    df = pandas.read_csv('D:/Учеба/Базы/iq.csv')  # Для Linux /home/user/csv/iq.csv
    years_of_education = df['years_of_education'][:, np.newaxis]
    x_train, x_test, y_train, y_test = train_test_split(
        years_of_education, df['iq'], test_size=0.4
    )
    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    print('w_1 = ' + str(model.coef_[0]) + ' w_0 = ' + str(model.intercept_))
    print('iq = ' + str(model.coef_[0]) + ' * experience + ' + str(model.intercept_))
    y_predicted = model.predict(x_test)
    score = r2_score(y_test, y_predicted)
    print('Точность: %s' % score)
    return



def curses():
    link = 'https://www.nbrb.by/api/exrates/rates/dynamics/145?startDate=' + str(date.today() - timedelta(days=7)) + '&enddate=' + str(date.today())
    response = requests.get(
        link
    )
    data = json.loads(response.text)
    len_days = len(data)
    curse = []
    for x in range(len_days):
        curse.append(data[x]['Cur_OfficialRate'])
    result = statistics.mean(curse)
    result = float('{:.4f}'.format(result))   # round - округляет
    return result


print(curses())
