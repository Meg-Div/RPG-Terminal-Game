# RPG Game

import random
import time


class Hero:
    def __init__(self):
        """ Creates a hero """
        self._hat_dict = {
            "Cowboy hat": ["rope","horse", "hay bale", "spur", "cow"],
            "Sun hat": ["picnic table", "flower", "iced tea", "apple pie", "ants"],
            "Top hat": ["rabbit", "white glove", "pocket watch", "cane", "scarf"],
            "Party hat": ["birthday cake", "gift bag", "bottle of champagne", "a numbered candle", "bottle of wine"]
        }
        self._police_dict = {
            -10: "The police do not seem impacted.",
            -20: "The police look bored.",
            10: "The police look scared!",
            20: "The police look terrified!"
        }
        self._health = 40
        self._hero_hat_dict = {}

    def get_hat_dict(self):
        """ returns hat_dict """
        return self._hat_dict

    def del_hat_dict(self, hat):
        """ deletes a hat from the hat_dict """
        del self._hat_dict[hat]

    def get_police_dict(self):
        """ returns police_dict """
        return self._police_dict

    def get_health(self):
        """ returns health """
        return self._health

    def update_health(self, amount):
        """ updates the hero's health """
        self._health += amount
        return self._health

    def get_hero_hat_dict(self):
        """ returns hero_hat_dict """
        return self._hero_hat_dict

    def add_to_hat_dict(self, hat, hat_items):
        """ adds hat to hero_hat_dict """
        self._hero_hat_dict[hat] = hat_items

    def del_hero_hat_dict(self, hat):
        """ deletes a hat from hero_hat_dict """
        del self._hero_hat_dict[hat]

    def del_hero_hat_dict_item(self, hat, hat_items):
        """ deletes an item from hero_hat_dict's hats """
        self._hero_hat_dict[hat].remove(hat_items)

        hats = list(self._hero_hat_dict.keys())
        items = list(self.get_hero_hat_dict().values())

        # changes the hat if no items left
        if len(items[0]) == 0 and len(hats) == 2:
            print(f"Your {hats[0]} disappears!")
            print(f"You put on your second hat and now wear your {hats[1]}!\n")
            self.del_hero_hat_dict(hats[0])
            return "hat changed"

        # ends the game if no hats left
        if len(items[0]) == 0 and len(hats) == 1:
            time.sleep(3)
            print("Oh no!")
            print("Your current hat disappeared and you have no more hats!")
            time.sleep(3)
            print("You try to run but the police tackle you and haul you away to jail.")
            #time.sleep(3)
            print("Hope you have a good attorney!\n")
            return "game over"

        return True


class Actions(Hero):
    """ the actions of the game """
    def __init__(self):
        # inherits from Hero
        super().__init__()

    def welcome(self, new_hero):
        """ welcomes the hero and sets the stage with dialogue """
        health = new_hero.get_health()
        print("\nWelcome Hero!")
        time.sleep(3)
        print(f"""
        You are being chased by the police for a crime you didn't commit.
        You duck into a store to hide but you've been running so long 
        your health is at: {health} / 100
        """)
        time.sleep(6)
        print("""
        The shopkeep sees you attempting to hide and offers to sell you a magic hat.
        You are exhausted and stare at him as he puts a hat on,
        only to take it off to pull something out of it.
        """)
        time.sleep(7)
        print("""
        Your eyes widen.
        "How much?" You ask and you have just enough cash to purchase two.
        He tells you that you can only wear one hat at a time...
        """)
        time.sleep(6)

    def choose_hats(self, new_hero):
        """ prompts the hero to choose their hats """
        hat_dict = new_hero.get_hat_dict()
        hats_list = list(hat_dict.keys())

        # user prompted to choose hats
        print("\nChoose your first hat to use Hero!")
        choice = int(new_hero.hat_options(new_hero))
        first_hat = hats_list[choice - 1]

        print(f"\nYou chose: {first_hat}\n")
        first_hat_items = hat_dict[first_hat]

        # hat added to hero's dict, and removed from original hat_dict
        new_hero.add_to_hat_dict(first_hat, first_hat_items)
        new_hero.del_hat_dict(first_hat)

        hat_dict = new_hero.get_hat_dict()
        hats_list = list(hat_dict.keys())

        print("\nChoose your second hat to use Hero!")
        choice = int(new_hero.hat_options(new_hero))
        second_hat = hats_list[choice - 1]

        print(f"\nYou chose: {second_hat}\n")
        second_hat_items = hat_dict[second_hat]

        # hat added to hero's dict, and removed from original hat_dict
        new_hero.add_to_hat_dict(second_hat,second_hat_items)
        new_hero.del_hat_dict(second_hat)

        # current hero's hats
        hero_hat_list = list(new_hero.get_hero_hat_dict().keys())

        print(f"\nYou put on the {hero_hat_list[0]} and pocket the {hero_hat_list[1]}.\n")
        print("\nNo sooner do you hand him the money and take the two hats,\nwhen the police bust into the store.\n")

    def hat_options(self, new_hero):
        """ gives the hero their hat options """
        hat_dict = new_hero.get_hat_dict()

        # runs through hat list to give user options
        for i, (key, value) in enumerate(hat_dict.items()):
            print(f"{i+1}: {key}")
        response = input(f"\nYour choice: ")

        # checking for input bounds
        if (response.isnumeric() is False) or (int(response) < 1 or int(response) > len(list(hat_dict.keys()))):
            print("\nPlease choose a hat listed:")
            return self.hat_options(new_hero)

        return response

    def reach_in_hat(self, new_hero):
        """ the hero reaches in the hat for an item """
        hero_dict = new_hero.get_hero_hat_dict()
        hats = list(hero_dict.keys())
        items = list(hero_dict.values())

        # shuffle the possible items for the hat
        random.shuffle(items[0])

        # checks bounds
        if items:
            item = items[0][0]
        else:
            return True

        # chooses item from hat
        time.sleep(3)
        print(f"Pulling off the {hats[0]} you reach inside and pull out a ...")
        time.sleep(3)
        print(f"{item}!")

        # prompts user to choose whether to eat or use item as distraction
        response = new_hero.choose_action(item)

        # changes health based on random shuffle of health possible updates
        if response == "1":
            result = new_hero.eat_item(item, new_hero)
        else:
            result = new_hero.use_distraction(item, new_hero)

        # checks health and ends game if too low
        if result != "game over":
            return new_hero.reach_in_hat(new_hero)
        else:
            return True

    def choose_action(self, item):
        """ prompts the hero to choose an action for the item """
        time.sleep(3)
        print(f"""Would you like to: 
        1) Eat the {item} to attempt to increase your health 
        2) Use the {item} to attempt to get away from the police
        """)
        action = input("Your choice:")
        # if the entry is not a number or out of bounds
        if (action.isnumeric() is False) or (int(action) < 1 or int(action) > 2):
            print("\nPlease choose 1 or 2:")
            return self.choose_action(item)

        return action

    def health_check(self, new_hero, change, item):
        """ checks the health of the player and if game should end """
        hero_dict = new_hero.get_hero_hat_dict()
        hats = list(hero_dict.keys())
        result = None
        new_hero.update_health(change)
        health = new_hero.get_health()

        # checks health bounds
        if health < 100 and health > 0:
            print(f"\nYour health is now at: {health} / 100\n")
            #time.sleep(3)
            result = new_hero.del_hero_hat_dict_item(hats[0], item)

        if result == "game over":
            print("Game Over")
            return "game over"

        if health > 90:
            print("You're now finally strong enough to get away!")
            #time.sleep(3)
            print("You race out the side door and the cops are left in your dust!\n")
            return "game over"

        if health < 10:
            print("You're no longer strong enough to get away!")
            #time.sleep(3)
            print("The police tackle you and haul you away to jail.")
            #time.sleep(3)
            print("Hope you have a good attorney!\n")
            return "game over"

    def eat_item(self, item, new_hero):
        """ dialogue for if the hero eats the item """
        police_dict = new_hero.get_police_dict()
        change_list = list(police_dict.keys())

        # chooses random health update
        random.shuffle(change_list)
        change = change_list[0]

        print(f"\nYou put your hat back on and eat the {item}.")
        time.sleep(3)

        # dialogue based on health change
        if int(change) > 0:
            print(f"The {item} has given you strength!")

        else:
            print(f"But the {item} has poisoned you!")

        result = new_hero.health_check(new_hero, change, item)

        return result

    def use_distraction(self, item, new_hero):
        """ dialogue for if the hero uses the item as a distraction """
        police_dict = new_hero.get_police_dict()
        change_list = list(police_dict.keys())

        # chooses random health update
        random.shuffle(change_list)
        change = change_list[0]
        response = police_dict[change]

        # dialogue based on health change
        print(f"\nYou put your hat back on and use your {item} as a distraction,")
        print(f"{response}")

        result = new_hero.health_check(new_hero, change, item)
        return result

    def run_game(self, new_hero):
        """ creates and runs the new game """
        new_hero.welcome(new_hero)
        new_hero.choose_hats(new_hero)
        new_hero.reach_in_hat(new_hero)

if __name__ == '__main__':
    new_hero = Actions()
    new_hero.run_game(new_hero)
