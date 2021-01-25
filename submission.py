import plotly.express as px
import numpy as np



countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]


colors = ["blue", "green", "red", "yellow"]


def build_graph(path):
    graph = np.zeros((len(countries), len(countries)))
    with open(path) as f:
        next(f)
        i = -1
        for line in f.read().splitlines():
            i += 1

            country_list = line.split(",")

            for item in countries:
                if item in country_list:
                    graph[i][countries.index(item)] = 1


    return graph


def is_safe(color_index, country_index, graph, country_colors):
    for neighboor_index in range(len(countries)):
        if graph[country_index][neighboor_index] == 1 \
                and countries[neighboor_index] in country_colors \
                and colors[color_index] == country_colors[countries[neighboor_index]]:
            return False
    return True


def graph_coloring(country_index, graph, country_colors):
    for color_index, value in enumerate(colors):
        if is_safe(color_index, country_index, graph, country_colors):
            country_colors[countries[country_index]] = colors[color_index]
            return



# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    graph = build_graph("data.csv")
    country_colors = dict()
    for country_index in range(len(countries)):
        graph_coloring(country_index, graph, country_colors)
    print(country_colors)
    plot_choropleth(colormap=country_colors)

    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    #plot_choropleth(colormap=colormap_test)
