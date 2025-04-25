import pandas as pd
import datetime

a = pd.to_datetime('2012-01-15')

b = pd.to_datetime('2012-01-15 21:20')


c = pd.to_datetime(datetime.datetime.now())


d = pd.to_datetime('2023-05-01').date()

e = pd.Timestamp.now().date()


f = pd.Timestamp.now().time()


g = datetime.datetime.now().time()

print("a)", a)
print("b)", b)
print("c)", c)
print("d)", d)
print("e)", e)
print("f)", f)
print("g)", g)