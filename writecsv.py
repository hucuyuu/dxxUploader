import pandas as pd


def write_true(studentid,dxxNumber):
        df = pd.read_csv('1904_count.csv', dtype=object)
        for i in range(0, df.shape[0]):
                if df['id'][i] == studentid:
                        df[dxxNumber][i] = '1'

        df.to_csv('1904_count.csv', index=False, encoding='UTF-8')


def count_value(dxxNumber):
        df = pd.read_csv('1904_count.csv', dtype=object)
        sum = 0
        for i in range(0, df.shape[0]):
                if df[dxxNumber][i] == '1':
                        sum = sum + 1
        return sum

