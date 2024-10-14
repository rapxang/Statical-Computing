import pandas as pd
data = {
        'Name': ["Kunga", "Rapxang", "Anis"],
        'Age': [25, 26, 27],

        }
df = pd.DataFrame(data)
print(df)
print(df.loc[0])