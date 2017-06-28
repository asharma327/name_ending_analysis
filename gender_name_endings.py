import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# URLs with datasets
url_boys = 'https://www.babble.com/pregnancy/1000-most-popular-boy-names/'
url_girls = 'https://www.babble.com/pregnancy/1000-most-popular-girl-names/'


def get_names_from_websites(url):
    # Connect and Scrape all names
    name_list = []
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request_var = requests.get(url, headers=headers)
    page_structure = BeautifulSoup(request_var.text, "lxml")
    names = page_structure.find_all('li', class_='p1')

    for name in names:
        name_list.append(name.get_text())

    return name_list


def get_count_of_ending_letters(names):
    # Return Dictionary with count of all ending letter
    count_of_ending_letters = {}

    for name in names:
        exisiting_letters = count_of_ending_letters.keys()
        ending_letter = name[-1]
        if ending_letter not in exisiting_letters:
            count_of_ending_letters[ending_letter] = 1
        else:
            count_of_ending_letters[ending_letter] += 1

    return count_of_ending_letters


def get_popular_ending_letters(names, how_many_to_plot):
    # Specify the number of popular letters in parameters
    # ex: for Top 10, 'how_many_to_plot = 10'
    temp_dict = dict(names)
    letters = []
    count_of_appearance = []

    for iters in range(how_many_to_plot):
        character = max(temp_dict, key=lambda key: temp_dict[key])
        appearance_count = temp_dict[character]
        letters.append(character)
        count_of_appearance.append(appearance_count)
        del temp_dict[character]

    return letters, count_of_appearance


def plot(names, counts, title, xlabel, ylabel):
    y_pos = np.arange(len(names))
    plt.bar(y_pos, counts, align='center', alpha=0.5)
    plt.xticks(y_pos, names)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)

    plt.show()

boy_names = get_names_from_websites(url_boys)
girl_names = get_names_from_websites(url_girls)

boy_name_counts = get_count_of_ending_letters(boy_names)
girl_name_counts = get_count_of_ending_letters(girl_names)

boy_letters_plot, boy_count_plot = get_popular_ending_letters(boy_name_counts, 10)
girls_letters_plot, girls_count_plot = get_popular_ending_letters(girl_name_counts,10)


'''Run one at a time'''
plot(girls_letters_plot, girls_count_plot, "Most Popular Ending Letters - Girls", '', 'Count')
# plot_to_analyze(boy_letters_plot, boy_count_plot, "Most Popular Ending Letters - Boys", '', 'Count')








