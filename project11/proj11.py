##################################################################
#  CSE 231 Project 11
#  Creates a virtual dog or cat based on user input
#  The user can feed, drink, shower, sleep, and play with the pet
#  The pets can see the status of the cat or dog
####################################################################

from cse231_random import randint
from edible import *
import edible

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]


# Main class of Pet
class Pet(object):
    # Initializes the following attributes to initial values
    def __init__(self, name='fluffy', species='dog', gender='male', color='white'):
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []

        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')

    # Gets the time_pass_by
    def _time_pass_by(self, t=1):
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    # Returns the hunger value of the pet
    def get_hunger_level(self):
        return self._hunger

    # Returns the thirst value of the pet
    def get_thirst_level(self):
        return self._thirst

    # Returns the energy value of the pet
    def get_energy_level(self):
        return self._energy

    # Makes the pet drink
    def drink(self, liquid):
        # If liquid is an instance of tuple of self.drinkable items
        if isinstance(liquid, tuple(self._drinkable_items)):
            # Gets the quantity of liquid
            liquid_quantity = liquid.get_quantity()
            # Calls the time_pass_by()
            self._time_pass_by()
            # Subtracts the liquid_quantity from thirst
            self._thirst -= liquid_quantity
            # If thirst is greater than or equal to 10, thirst is 10
            if self._thirst >= MAX:
                self._thirst = 10
            # Elif thirst is less than or equal to 0, thirst is 0
            elif self._thirst <= MIN:
                self._thirst = 0
        # Else liquid is not drinkable
        else:
            print("Not drinkable")

        # Calls update_status and reply_to_master
        self._update_status()
        self._reply_to_master('drink')

    # Feeds the pet
    def feed(self, food):
        # insert docstring
        if isinstance(food, tuple(self._edible_items)):
            # Stores food quantity in edible food
            edible_food = food.get_quantity()
            # Calls time pass by
            self._time_pass_by()
            # Subtracts food quantity from hunger
            self._hunger -= edible_food
            # If hunger is greater than or equal to 10, hunger is 10
            if self._hunger >= MAX:
                self._hunger = 10
            # Elif hunger is less than or equal to 0, hunger is 0
            elif self._hunger <= MIN:
                self._hunger = 0
        else:
            print("Not eatable")

        # Calls update_status and reply_to_master
        self._update_status()
        self._reply_to_master('feed')

    # Showers the pet
    def shower(self):
        # Calls time_pass_by with a default of 4
        self._time_pass_by(4)
        # Subtracts 4 from smell
        self._smell -= 4
        # Subtracts 4 from loneliness
        self._loneliness -= 4
        # If smell is greater than or equal to 10, smell is 10
        if self._smell >= MAX:
            self._smell = 10
        # Elif smell is less than or equal to 0, smell is 0
        elif self._smell <= MIN:
            self._smell = 0
        # If loneliness is greater than or equal to 10, loneliness is 10
        if self._loneliness >= MAX:
            self._loneliness = 10
        # Elif loneliness is less than or equal to 0, loneliness is 0
        elif self._loneliness <= MIN:
            self._loneliness = 0

        # Calls update_status and reply_to_master
        self._reply_to_master('shower')
        self._update_status()

    # Makes the pet sleep
    def sleep(self):
        # Calls time_pass_by with a default of 7
        self._time_pass_by(7)
        # Adds 7 to energy
        self._energy += 7
        # If energy is greater than or equal to 10, energy is 10
        if self._energy >= MAX:
            self._energy = 10
        # Elif energy is less than or equal to 0, energy is 0
        elif self._energy <= MIN:
            self._energy = 0

        # Calls update_status and reply_to_master
        self._update_status()
        self._reply_to_master('sleep')

    # Plays with the pet
    def play_with(self):
        # Calls time_pass_by with a default of 4
        self._time_pass_by(4)
        # Adds 4 to smell
        self._smell += 4
        # Subtracts 4 from loneliness
        self._loneliness -= 4
        # Subtracts 4 from energy
        self._energy -= 4
        # If smell is greater than or equal to 10, smell is 10
        if self._smell >= MAX:
            self._smell = 10
        # Elif smell is less than or equal to 0, smell is 0
        elif self._smell <= MIN:
            self._smell = 0
        # If loneliness is greater than or equal to 10, loneliness is 10
        if self._loneliness >= MAX:
            self._loneliness = 10
        # Elif loneliness is less than or equal to 0, loneliness is 0
        elif self._loneliness <= MIN:
            self._loneliness = 0
        # If energy is greater than or equal to 10, energy is 10
        if self._energy >= MAX:
            self._energy = 10
        # Elif energy is less than or equal to 0, energy is 0
        elif self._energy <= MIN:
            self._energy = 0

        # Calls update_status and reply_to_master
        self._update_status()
        self._reply_to_master('play')

    # Replies the master with the following sentences
    def _reply_to_master(self, event='newborn'):
        # insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(à¹‘>â—¡<à¹‘)"
        faces['feed'] = "(à¹‘Â´Ú¡`à¹‘)"
        faces['drink'] = "(à¹‘Â´Ú¡`à¹‘)"
        faces['play'] = "(à¸…^Ï‰^à¸…)"
        faces['sleep'] = "à­§(à¹‘â€¢Ì€âŒ„â€¢Ìà¹‘)à«­âœ§"
        faces['shower'] = "( â€¢Ì€ .Ì« â€¢Ì )âœ§"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event]) + ": " + talks[event]
        print(s)

    # Prints out the status of the pet
    def show_status(self):
        print("{:<12s}: [{:<20s}]".format("Energy","#"*2*int(round(self._energy))) + "{:5.2f}/{:2d}".format(self._energy,10))
        print("{:<12s}: [{:<20s}]".format("Hunger", "#"*2*int(round(self._hunger))) + "{:5.2f}/{:2d}".format(self._hunger, 10))
        print("{:<12s}: [{:<20s}]".format("Loneliness","#"*2*int(round(self._loneliness))) + "{:5.2f}/{:2d}".format(self._loneliness, 10))
        print("{:<12s}: [{:<20s}]".format("Smell", "#"*2*int(round(self._smell))) + "{:5.2f}/{:2d}".format(self._smell, 10))
        print("{:<12s}: [{:<20s}]".format("Thirst", "#"*2*int(round(self._thirst))) + "{:5.2f}/{:2d}".format(self._thirst, 10))

    # Updates the status of the pet
    def _update_status(self):
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(à¹‘>â—¡<à¹‘)"
        faces['hunger'] = "(ï½¡>ï¹<ï½¡)"
        faces['thirst'] = "(ï½¡>ï¹<ï½¡)"
        faces['energy'] = "(ï½žï¹ƒï½ž)~zZ"
        faces['loneliness'] = "(à¹‘oÌ´Ì¶Ì·Ì¥á·…ï¹oÌ´Ì¶Ì·Ì¥á·…à¹‘)"
        faces['smell'] = "(à¹‘oÌ´Ì¶Ì·Ì¥á·…ï¹oÌ´Ì¶Ì·Ì¥á·…à¹‘)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

# Cat is the subclass of Pet
class Cat(Pet):
    def __init__(self, name='fluffy', gender='male', color='white'):
        # Initializes the pet to cat
        Pet.__init__(self, name, 'cat', gender, color)
        self._edible_items = cat_edible_items
        self._drinkable_items = cat_drinkable_items

# Dog is the subclass of the Pet
class Dog(Pet):
    # Initializes the pet to dog
    def __init__(self, name='fluffy', gender='male', color='white'):
        Pet.__init__(self, name,'dog', gender, color)
        self._edible_items = dog_edible_items
        self._drinkable_items = dog_drinkable_items


def main():
    # Prints welcome
    print("Welcome to this virtual pet game!")

    # Command0 is true
    command0 = True
    # While command0 is true
    while command0:
        # Prompt0 provides instructions for user and splits it
        prompt0 = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
        prompt0 = input(prompt0).split(" ")
        # If the prompt0 is not empty
        if prompt0 != (['']):
            # If the prompt0[0] is dog, then subclass Dog() is called, and exits loop
            if (prompt0[0] == 'dog'):
                p1 = Dog(prompt0[1],prompt0[2],prompt0[3])
                command0 = False
            # If the prompt0[0] is cat, then subclass Cat() is called, and exits loop
            elif (prompt0[0] == 'cat'):
                p1 = Cat(prompt0[1],prompt0[2], prompt0[3])
                command0 = False
            # Else the loop runs again
            else:
                command0 = True
        # If user hits enter, then it defaults to Dog(), and exists the loop
        else:
            p1 = Dog()
            command0 = False

    # Prints the intro
    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    # While command is True then it runs
    command = True
    while command:
        # Prints instructions
        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
        # If prompt is q then exits the loop
        if prompt.lower() == 'q':
            command = False
        else:
            # If prompt is feed then the following runs
            if prompt == "feed":
                z = True
                #While z is true
                while z:
                    # Feed_quantity is the how much food should be feed
                    feed_quantity = input("How much food ? 1 - 10 scale: ")
                    # If feed_quantity is a digit
                    if feed_quantity.isdigit():
                        # If feed_quantity is between 0 and 10 then it runs
                        if (int(feed_quantity) > 0) and (int(feed_quantity) < 10):
                            # Z is false to end te infinte loop
                            z =False
                            # If the pets hunger level is greater than 0
                            if p1.get_hunger_level() > 0:
                                # If the pet is dog or default pet
                                if (prompt0[0] == "dog") or (prompt0 == ([''])):
                                    # Dogfood is called and the quantity is inputted
                                    food = edible.DogFood(int(feed_quantity))
                                    # Pet is fed
                                    p1.feed(food)
                                # If the pet is cat
                                elif prompt0[0] == "cat":
                                    # Catfood is called and the pet is fed
                                    food = edible.CatFood(int(feed_quantity))
                                    p1.feed(food)
                            # If the pet hunger is 0 then the following is printed
                            else:
                                print("Your pet is satisfied, no desire for sustenance now.")
                        # If the feed_quantity is not a digit or not between 0-10, this is printed
                        else:
                            print("Invalid input.")
                    else:
                        print("Invalid input.")
            # If prompt is drink then the following runs and the structure is similar to feed
            elif prompt == "drink":
                z = True
                while z:
                    drink_quantity = input("How much drink ? 1 - 10 scale: ")
                    if drink_quantity.isdigit():
                        if (int(drink_quantity) > 0) and (int(drink_quantity) < 10):
                            z = False
                            if p1.get_thirst_level() > 0:
                                water = edible.Water(int(drink_quantity))
                                p1.drink(water)
                            else:
                                print("Your pet is satisfied, no desire for sustenance now.")
                        else:
                            print("Invalid input.")
                    else:
                        print("Invalid input.")
            elif prompt == "shower":
                p1.shower()
            # If prompt is sleep then sleep() is called
            elif prompt == "sleep":
                p1.sleep()
            # If prompt is play then play_with() is called
            elif prompt == "play":
                p1.play_with()
            # If prompt is status then show_status() is called
            elif prompt == "status":
                p1.show_status()
            # If prompt is q exits loop
            elif prompt.lower() == "q":
                command = False
            else:
                print("Invalid command.")
    # Prints bye
    print("Bye ~")


if __name__ == "__main__":
    main()