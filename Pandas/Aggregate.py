df.set_index('Data', inplace=True)

df2=df.groupby([df.Serial,df.index.month,df.index.day]).sum()

df3=df2.reset_index(level=['Serial'])
