import pandas
import datetime
import numpy


def to_datetime(s):
    return datetime.datetime.strptime(s, "%Y.%m.%d")


def read(filepath):
    result = pandas.read_csv(filepath)
    normalIzm = result['Изм. %']
    for elem in normalIzm.index:
        normalIzm[elem] = (str(normalIzm[elem])).replace('%', '')
        normalIzm[elem] = (str(normalIzm[elem])).replace(',', '.')
        normalIzm[elem] = float(normalIzm[elem])
    dates = result['Дата']
    for i in dates.index:
        dates[i] = datetime.datetime.strptime(dates[i], "%d.%m.%Y")
    result = pandas.concat([result['Дата'].rename('Data'), normalIzm.rename('Pts')], axis=1)
    return result


def get_mean(df : pandas.DataFrame):
    month = 12
    tempCount = 0
    tempMean = 0
    result = {}
    for i in df.index:
        if month == df['Data'].values[i].month:
            tempCount += 1
            tempMean += df['Pts'].values[i]
        else:
            result[f"{df['Data'].values[i-1].year}.{df['Data'].values[i-1].month}"] = tempMean/ tempCount
            tempMean = df['Pts'].values[i]
            tempCount = 1
            month = df['Data'].values[i].month
    result[f"{df['Data'].values[len(df.index) -1].year}.{df['Data'].values[len(df.index) -1].month}"] = tempMean / tempCount
    return result


def main():
    nestleDf = read('Nestle.csv')
    nestleMeans = get_mean(nestleDf)
    #print(nestleMeans)
    LIndtDf = read('LIndt.csv')
    LIndtMeans = get_mean(LIndtDf)
    #print(LIndtMeans)
    HSYDf = read('HSY.csv')
    HSYMeans = get_mean(HSYDf)
    #print(HSYMeans)
    resultDf = pandas.DataFrame([nestleMeans, LIndtMeans, HSYMeans], index=['Nestle', 'LIndt', 'HSY'])
    return resultDf


main()
