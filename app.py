# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns

# Setting page options for the Shiny app
ui.page_opts(title="Tes Shiny App", fillable=True)

# Creating sidebar with input options
with ui.sidebar():
    ui.input_slider("number_of_bins", "Number of Bins", 1, 100, 50)
    ui.input_select(
        "species",
        "Which species would you like to render?",
        ["setosa", "versicolor", "virginica"],
    )

# Plotting histogram with random data
@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_points: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.number_of_bins(), density=True, color="indigo")

# Plotting scatterplot using seaborn with the iris dataset
@render.plot(alt="Sepal Length vs. Sepal Width")
def draw_scatterplot():
    iris = sns.load_dataset("iris")  # Loading iris dataset from seaborn
    iris = iris[iris['species'] == input.species()]
    sns.scatterplot(
        data=iris,
        x='sepal_length',
        y='sepal_width',
        hue='species',  # Color points blue
        palette='Set1'  # Optional: use a different color palette
    )
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("Sepal Length vs. Sepal Width")
