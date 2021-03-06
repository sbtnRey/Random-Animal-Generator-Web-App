from flask import Flask, render_template
import webbrowser
import random
import wikipedia
import collections

app = Flask(__name__)

@app.route("/")
def template_test():
    animal, sumAn = web()
    #print (animal)
    #my_string = sumAn
    return render_template('template.html', my_sum=sumAn, my_animal=animal)


# Function to output wikipedia info on the animal and search it on google images.
def web():

    # Call random animal funciton and set to animal
    animal = randomAnimal()

    # Set 'wikiAnimal' to the wikipedia page of the random animal
    wikiAnimal = wikipedia.page(animal)

    # 'wikiAnimal.content' for the entire wiki info, .summary just
    # for a short summary of the animal

    #print (wikiAnimal.summary)
    sumAn = (wikiAnimal.summary)

    # Split the random animal name into species and genus
    genus,species = animal.split(" ")

    # Set the url to the google image search with the values being the species and genus of the random animal
    url = 'https://www.google.com/search?q=' + genus + '+' + species + '+&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi6l_u-kY_RAhVS52MKHSKZDXYQ_AUICCgB&biw=982&bih=680'

    # Open URL in a new tab, if browser window is open. Otherwise open in new window for default browser
    webbrowser.open_new_tab(url)

    #Point = collections.namedtuple('Point', ['animal', 'sumAn'])
    #return Point
    #return (animal + sumAn)
    return (animal, sumAn)

# Function that chooses a random animal from a list then prints and returns it
def randomAnimal():

    # List of animals with there species and genus
    #animalList = [ ]
    with open("animals.txt") as f:
        animalList = list(f)

    # Utilization of the random function on the above list of animals and the
    # parsing of single quotes and the comma
    randAnimal = random.choice(animalList)[1:-3]


    # Simply prints the random animal
    #print(randAnimal + '\n')

    return randAnimal




if __name__ == "__main__":
    app.run()
