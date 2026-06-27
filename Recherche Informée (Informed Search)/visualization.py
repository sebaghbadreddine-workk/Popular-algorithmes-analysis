import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_bar_comparison(stats_df):
    """ 1. Bar Plot: Compares averages for Time, Memory, and Path Length """
    metrics = ['Time', 'Memory', 'Path Length']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    axes = axes.flatten()
   
    for i, metric in enumerate(metrics):
        sns.barplot(x='Algorithm', y=metric, hue='Algorithm', legend=False, data=stats_df, ax=axes[i], palette='magma', errorbar=None)
        axes[i].set_title(f'Average {metric}')
        axes[i].set_ylabel(metric)

    plt.tight_layout()
    plt.show()

def plot_box_plots(stats_df):
    """ 2. Box Plot: Visualizes the distribution of Time, Path Length, and Memory results """
    metrics = ['Time', 'Path Length', 'Memory']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    axes = axes.flatten()
   
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Algorithm', y=metric, hue='Algorithm', legend=False, data=stats_df, ax=axes[i], palette='Set3')
        axes[i].set_title(f'{metric} Distribution')

    plt.tight_layout()
    plt.show()

def plot_pie_charts(stats_df):
    """ 3. Pie Charts: Shows the proportional consumption for each metric """
    metrics = ['Time', 'Path Length', 'Memory']
    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    
    avg_data = stats_df.groupby('Algorithm')[metrics].mean()
    colors = sns.color_palette('Set2')
    
    for i, metric in enumerate(metrics):
        axes[i].pie(avg_data[metric], labels=avg_data.index, autopct='%1.1f%%', 
                    startangle=140, colors=colors)
        axes[i].set_title(f'Proportion of {metric}')

    plt.tight_layout()
    plt.show()

def plot_line_metrics(stats_df):
    """ 4. Line Plot: Analyzes performance stability (Time) across multiple runs """
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=stats_df.index % 20, y='Time', hue='Algorithm', data=stats_df, marker='o')
    plt.title('Algorithm Performance Stability (Time per Run)')
    plt.xlabel('Run Number')
    plt.ylabel('Execution Time')
    plt.legend(title='Algorithm')
    plt.show()

def visualize_maze_solution(maze, path, title="Maze Path"):
    """ 5. Visualizer: Displays the maze grid and the identified solution path """
    grid = np.array(maze.grid)
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='binary')
    
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color='red', linewidth=2, label='Path Found')
    
    plt.scatter(maze.start[1], maze.start[0], color='green', s=100, label='Start', zorder=5)
    plt.scatter(maze.goal[1], maze.goal[0], color='blue', s=100, label='Goal', zorder=5)
    plt.title(title)
    plt.legend()
    plt.show()