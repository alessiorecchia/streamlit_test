import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("500_rows.csv")
df['minmax_norm_ratings'] = 1 + (df['avg_rating'] - df['avg_rating'].min()) / (df['avg_rating'].max() - df['avg_rating'].min()) * 9
df['mean_norm_ratings'] = (1 + (df['avg_rating'] - df['avg_rating'].mean()) / (df['avg_rating'].max() - df['avg_rating'].min())) * 4.5 +1


def plot_norm(not_norm_series, norm_series, norm_type: str, bins_ = 20, not_norm_color='#e67e4d', norm_color='#e67eff', edgecolor_='black'):
    
    # defining some useful variables
    norm_min = round(norm_series.min(), 2)
    norm_max = round(norm_series.max(), 2)

    
    # Set the number of subplots and the fig dimensions
    fig, ax = plt.subplots(1, 2, figsize = (15,7))

    # defining the not-normilized graph
    ax[0].hist(not_norm_series, bins=bins_, color=not_norm_color, histtype='bar', edgecolor=edgecolor_)
    ax[0].set_title("Not normalized")
    ax[0].set_xlabel('Ratings')
    ax[0].set_ylabel('Frequency')

    # defining the normilized graph
    ax[1].hist(norm_series, bins=bins_, color=norm_color, histtype='bar', edgecolor=edgecolor_)
    ax[1].set_title(norm_type)
    ax[1].set_xlabel(f'Ratings (normalized {norm_min} to {norm_max})')
    ax[1].set_ylabel('Frequency')

    # Set the ticks for x axis in normalized graph, according to the data range
    plt.sca(ax[1])
    plt.xticks(np.arange(norm_min, norm_max + 1, 1))

    return fig

def plot_compared_norms(first_norm, second_norm, first_norm_type: str, second_norm_type: str, \
    bins_ = 20, first_norm_color='blue',second_norm_color='darkorange', edgecolor_='white'):
    min_range = round(np.array([first_norm.min(), second_norm.min()]).min(), 2)
    max_range = round(np.array([first_norm.max(), second_norm.max()]).max(), 2)


    # Set the fig dimensions
    fig, graph = plt.subplots(figsize = (15, 8))
    
    # defining the normilized graph
    graph.hist(first_norm, bins = bins_, alpha = 0.7, color=first_norm_color, edgecolor = edgecolor_, label = first_norm_type)
    graph.hist(second_norm, bins = bins_, alpha = 0.7, color=second_norm_color, edgecolor = edgecolor_, label = second_norm_type)
    graph.set_title(f'Comparison between {first_norm_type} and {second_norm_type}')
    graph.legend()
    
    # Set the range of the ticks in x axis, according to data range
    graph.set_xlabel(f'Range between min: {min_range} and max: {max_range}')

    return fig

def app():

    st.title("The Plot")
    st.subheader("Visualization with Matplotlib")

    # Examples
    fig1 = plot_norm(df.avg_rating, df.minmax_norm_ratings, norm_type='Min-Max normalization')
    fig2 = plot_norm(df.avg_rating, df.mean_norm_ratings, norm_type='Mean normalization')
    fig3 = plot_compared_norms(df.minmax_norm_ratings, df.mean_norm_ratings, first_norm_type = 'Min-Max normalization', second_norm_type='Mean normalization')

    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
