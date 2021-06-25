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



import numpy as np
import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from pandas import DataFrame

# def neironka():
#     df = pandas.read_csv('/home/user/csv/iq.csv')
#     years_of_education = df['years_of_education'][:, np.newaxis]
#     x_train, x_test, y_train, y_test = train_test_split(
#         years_of_education, df['iq'], test_size=0.4
#     )
#     model = linear_model.LinearRegression()
#     model.fit(x_train, y_train)
#     print('w_1 = ' + str(model.coef_[0]) + ' w_0 = ' + str(model.intercept_))
#     print('iq = ' + str(model.coef_[0]) + ' * experience + ' + str(model.intercept_))
#     y_predicted = model.predict(x_test)
#     score = r2_score(y_test, y_predicted)
#     print('Точность: %s' % score)
#     return

import requests
import json


def curses():
    response = requests.get(
        'https://www.nbrb.by/api/exrates/rates/dynamics/145?startDate=2021-06-16&enddate=2021-06-25'
    )
    data = json.loads(response.text)
    len_days = len(data)
    curse = 0
    for x in range(len_days):
        curse += data[x]['Cur_OfficialRate']
    result = curse / len_days
    return result


print(curses())
