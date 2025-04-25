import pandas as pd

df = pd.DataFrame({
    'Shyam': [True, True, True, True, False],
    'Ravi': [True, False, False, True, False]
})

df['party'] = df['Shyam'] & df['Ravi']

days_til_party = [None] * len(df)

next_party_day = None
for i in reversed(range(len(df))):
    if df.loc[i, 'party']:
        next_party_day = i
        days_til_party[i] = 0
    elif next_party_day is not None:
        days_til_party[i] = next_party_day - i
    else:
        days_til_party[i] = None

df['days_til_party'] = days_til_party
print(df)