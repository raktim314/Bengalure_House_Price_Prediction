
#!/usr/bin/python3
#!/usr/lib/matplotlib

import matplotlib.pyplot as plt


def plot_norm_bar(df, title, figsize=(12,7)):
    """plot bar graph of the categorical variables 
    of the dataset with parcentage
    """
    fig, ax = plt.subplots(ncols=1, figsize=figsize)
    fig.suptitle(title)
    cat_value_counts = df.fillna('missing').value_counts(normalize=True)
    sns.barplot(y = cat_value_counts.index, x= cat_value_counts.values*100)
    ax.set(xlabel= 'percentage', ylabel=str(df.name))
    
    plt.plot()

    return