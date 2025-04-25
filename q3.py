import pandas as pd

asking_prices = pd.Series([10790, 12000, 19000, 15000, 10000])
fair_prices = pd.Series([10500, 11500, 9500, 16000, 12000])

good_deals = asking_prices < fair_prices
good_deal_indices = list(asking_prices[good_deals].index)

print("Good deal indices:", good_deal_indices)