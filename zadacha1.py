import pandas
import zagruzka

def collectData():
    return zagruzka.main()

def collectDataTest():
    d1 = {'s1': [100, 120, 140, 170]}
    d1['s2'] = [120, 110, 145, 165]
    d1['s3'] = [160, 145, 140, 150]
    d1['s4'] = [185, 170, 175, 190]
    dt = pandas.DataFrame(d1, index=['A1','A2','A3','A4'])
    return dt

def LaplasFunc(df, p):
    tempSeries = df.sum(axis=1) * p
    return f'{tempSeries.idxmax()} : {tempSeries.max()}'


def Minimax(df):
    tempSeries = df.max(axis=1)
    return f'{tempSeries.idxmin()} : {tempSeries.min()}'

def minus(s, temp):
    return s - temp


def Sevidg(df):
    localMin = df.max()
    tempDf = df.copy()
    tempDf = - tempDf.sub(localMin)
    temp = tempDf.iterrows()
    tempSeriesNames = [next(temp)[0] for i in range(len(tempDf))]
    temp = tempDf.iterrows()
    tempSeries = [next(temp)[1].max() for i in range(len(tempDf-1))]
    tempSeries = pandas.Series(tempSeries, tempSeriesNames)
    result = f'{tempSeries.idxmin()} : {tempSeries.min()}'
    return result


def Gurvits(df, alfa = 0.25):
    tempDf = df.copy()
    tempDf['min'] = df.min(axis = 1)
    tempDf['max'] = df.max(axis= 1)
    tempMin = tempDf.iterrows()
    tempDf['result'] = 0
    tempDf['result'] = tempDf['result'].add(tempDf['max'] * alfa)
    tempDf['result'] = tempDf['result'].add(tempDf['min'] * (1-alfa))
    tempSeries = tempDf['result']
    result = f'{tempSeries.idxmax()} : {tempSeries.max()}'
    return result


def Maximax(df):
    tempSeries = df.max(axis = 1)
    return f'{tempSeries.idxmax()} : {tempSeries.max()}'


def Valda(df):
    tempSeries = df.min(axis = 1)
    return f'{tempSeries.idxmax()} : {tempSeries.max()}'


def RandomKrit(df):
    sumAll = df.sum().sum()
    qSeries = df.sum(axis = 1) / sumAll
    tempSeries = df.max(axis = 1) * qSeries
    return f'{tempSeries.idxmax()} : {tempSeries.max()}'

def main():
    data = collectDataTest()
    print(data)
    resultMaximax = Maximax(data)
    print('resultMaximax\n', resultMaximax)
    resultLaplas = LaplasFunc(data, 1 / len(data.columns))
    print('resultLaplas\n', resultLaplas)
    resultValda = Valda(data)
    print('resultValda\n', resultValda)
    resultSevidg = Sevidg(data)
    print('resultSevidg\n', resultSevidg)
    resultGurvits = Gurvits(data)
    print('resultGurvits\n', resultGurvits)
    resultRandomKrit = RandomKrit(data)
    print('resultRandomKrit\n', resultRandomKrit)


main()