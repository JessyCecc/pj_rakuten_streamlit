def dataframe_percent_of_missing(df, colname):
    total_len = df.shape[0]
    total_missing = df[df[colname].isna()].count()[0]
    percent_brut = 1 - (total_len - total_missing) / total_len
    percent = round(percent_brut * 100, 2)
    return percent, percent_brut
