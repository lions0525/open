import pandas as pd

dataframe=pd.read_csv('2019_kbo_for_kaggle_v2.csv')

year2015=dataframe[dataframe['year']==2015]
year2016=dataframe[dataframe['year']==2016]
year2017=dataframe[dataframe['year']==2017]
year2018=dataframe[dataframe['year']==2018]

s2015H=year2015.sort_values(by='H', ascending=False)
s2015avg=year2015.sort_values(by='avg', ascending=False)
s2015HR=year2015.sort_values(by='HR', ascending=False)
s2015OBP=year2015.sort_values(by='OBP', ascending=False)

s2016H=year2016.sort_values(by='H', ascending=False)
s2016avg=year2016.sort_values(by='avg', ascending=False)
s2016HR=year2016.sort_values(by='HR', ascending=False)
s2016OBP=year2016.sort_values(by='OBP', ascending=False)

s2017H=year2017.sort_values(by='H', ascending=False)
s2017avg=year2017.sort_values(by='avg', ascending=False)
s2017HR=year2017.sort_values(by='HR', ascending=False)
s2017OBP=year2017.sort_values(by='OBP', ascending=False)

s2018H=year2018.sort_values(by='H', ascending=False)
s2018avg=year2018.sort_values(by='avg', ascending=False)
s2018HR=year2018.sort_values(by='HR', ascending=False)
s2018OBP=year2018.sort_values(by='OBP', ascending=False)



#2-1,2015
print("2015년 안타 TOP 10")
print(s2015H['batter_name'].head(10))
print()

print("2015년 타율 TOP 10")
print(s2015avg['batter_name'].head(10))
print()

print("2015년 홈런 TOP 10")
print(s2015HR['batter_name'].head(10))
print()

print("2015년 출루율 TOP 10")
print(s2015OBP['batter_name'].head(10))
print()

#2-1,2016
print("2016년 안타 TOP 10")
print(s2016H['batter_name'].head(10))
print()

print("2016년 타율 TOP 10")
print(s2016avg['batter_name'].head(10))
print()

print("2016년 홈런 TOP 10")
print(s2016HR['batter_name'].head(10))
print()

print("2016년 출루율 TOP 10")
print(s2016OBP['batter_name'].head(10))
print()

#2-1,2017
print("2017년 안타 TOP 10")
print(s2017H['batter_name'].head(10))
print()

print("2017년 타율 TOP 10")
print(s2017avg['batter_name'].head(10))
print()

print("2017년 홈런 TOP 10")
print(s2017HR['batter_name'].head(10))
print()

print("2017년 출루율 TOP 10")
print(s2017OBP['batter_name'].head(10))
print()

#2-1,2018
print("2018년 안타 TOP 10")
print(s2018H['batter_name'].head(10))
print()

print("2018년 타율 TOP 10")
print(s2018avg['batter_name'].head(10))
print()

print("2018년 홈런 TOP 10")
print(s2018HR['batter_name'].head(10))
print()

print("2018년 출루율 TOP 10")
print(s2018OBP['batter_name'].head(10))
print()


p1=year2018.loc[dataframe['cp']=='포수']
p2=year2018.loc[dataframe['cp']=='1루수']
p3=year2018.loc[dataframe['cp']=='2루수']
p4=year2018.loc[dataframe['cp']=='3루수']
p5=year2018.loc[dataframe['cp']=='유격수']
p6=year2018.loc[dataframe['cp']=='좌익수']
p7=year2018.loc[dataframe['cp']=='중견수']
p8=year2018.loc[dataframe['cp']=='우익수']


p1s=p1.sort_values(by='war',ascending=False).head(1)
p2s=p2.sort_values(by='war',ascending=False).head(1)
p3s=p3.sort_values(by='war',ascending=False).head(1)
p4s=p4.sort_values(by='war',ascending=False).head(1)
p5s=p5.sort_values(by='war',ascending=False).head(1)
p6s=p6.sort_values(by='war',ascending=False).head(1)
p7s=p7.sort_values(by='war',ascending=False).head(1)
p8s=p8.sort_values(by='war',ascending=False).head(1)

#2-2 포수 top 1
print("2018 포수 top1")
print(p1s['batter_name'])
print()

#2-2 1루수 top 1
print("2018 1루수 top1")
print(p2s['batter_name'])
print()

#2-2 2루수 top 1
print("2018 2루수 top1")
print(p3s['batter_name'])
print()


#2-2 3루수 top 1
print("2018 3루수 top1")
print(p4s['batter_name'])
print()


#2-2 유격수 top 1
print("2018 유격수 top1")
print(p5s['batter_name'])
print()


#2-2 좌익수 top 1
print("2018 좌익수 top1")
print(p6s['batter_name'])
print()


#2-2 중견수 top 1
print("2018 중견수 top1")
print(p7s['batter_name'])
print()


#2-2 우익수 top 1
print("2018 우익수 top1")
print(p8s['batter_name'])
print()


cordata=dataframe[['R','H','HR','RBI','SB','war','avg','OBP','SLG']].corrwith(dataframe['salary'])

print("salary와 관련도가 가장 높은 것은")
print(cordata.idxmax()+" : "+str(cordata.max()))



