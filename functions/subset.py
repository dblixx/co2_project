def transpose_df(df):
    """
    Return the transpose of the given DataFrame from kaya co2 data.

    """
    # Create the list of years
    year_range = [i for i in range(1971, 2019)]
    
    # Transpose the dataframe
    df_trans = df[year_range].T
    
    return df_trans

def specify_df_T(df, name, factors):
    """
    Get the transposed dataframe of the given one specific region/country and factors.

    Parameters
    ----------
    df : DataFrame
        The dataset to select from.
    name : str
        The name of the specified region/country.
    factors : list
        List of specified factors.

    Returns
    -------
    specific_df_T : DataFrame
        The specified transposed dataframe.

    """
    # Select a subset of dataframe by given name and factors
    specific_df = df[(df['Name']==name)&(df['Factor'].isin(factors))]
    
    # Transpose the dataframe to make it easy to query
    specific_df_T = transpose_df(specific_df)
    
    # Rename the columns
    specific_df_T.columns=factors
    
    return specific_df_T.dropna(axis=0)
    