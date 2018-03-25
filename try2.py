import urllib
import datetime
import urllib.request
import datetime
import urllib
import pandas as pd

now_time = datetime.datetime.now()
for i in range(1, 28):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean".format(
        i)
    vhi_url = urllib.request.urlopen(url)
    out = open("vhi_id_{} {}.csv".format(i, now_time.strftime('%Y %m %d')), 'wb')
    out.write(vhi_url.read())
    out.close()
print("VHI is downloaded...")

df = pd.read_csv('vhi_id_1 2017 04 02.csv', index_col=False, header=1, skipfooter=1, engine='python',
                 names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'], delimiter='\,\s+|\s+|\,')

print(df.head())


def max(df, year):
    df_year = df[df.year == year]
    maximum = df_year['VHI'].max()
    print(maximum)


def min(df, year):
    df_year = df[df.year == year]
    minimum = df_year['VHI'].min()
    print(minimum)


def extr(df):
    print(df[df.VHI < 15])


max(df, 1981)
min(df, 1981)
extr(df)
