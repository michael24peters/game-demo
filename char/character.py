import math

class Character:
    """
    Creates a Character with a set of characteristics and attributes that define them. 
    The Character class also contains the functionality needed to view, update, and use these statistics.

    ...

    Attributes
    ----------
    stats : dict
        Six defining attributes of the Character
    hp : int
        Hit Points (HP), which represents Player health and defense in combat.
    skills : dict
        Skills the User can progress through play
    hidden_skills : dict
        Skills the User cannot see until unlocked/revealed
    background : string
        Character background prior to game start
    name : str
        Name of Character

    Methods
    -------
    create_character():
        Generates main character (hero) from User input.
    """

    def __init__(self, background):

        self.stats = {
            'STR': 6.0, 
            'INT': 6.0, 
            'WIS': 6.0, 
            'DEX': 6.0, 
            'CON': 6.0, 
            'CHA': 6.0
        }

        self.skills = {
            'combat': 0,
            'social': 0,
            'athletics': 0,
            'history': 0,
            'herbalism': 0,
            'medicine': 0,
            'religion, sol': 0,
            'religion, deivos': 0,
            'languages': {'central': 1, 'northern': 0, 'eastern': 0, 'southern': 0, 'western': 0}
        }

        self.hidden_skills = {
            'secret_history': 0,
            'metaphysics': 0,
            'sorcery': 0,
            'mental_resistance': 0
        }
        
        if background=="orphan" or "Orphan" or "o" or "O": self.background = "orphan"
        elif background=="farmer" or "Farmer" or "f" or "F": self.background = "farmer"
        elif background=="noble" or "Noble" or "n" or "N": self.background = "noble"
        else: raise Exception("Not a valid background.")
        self.background = background

        self.name = ""

        self.create_character()

    def create_character(self):
        """Creates a character within the game.

        The Character class constructor sets the default characteristics of the Character, plus the User
        chosen background. create_character() completes this process by giving a series of user-inputted
        choices for stat adjustments, allocating skills points, and so on.
        """

        stats = {'STR': 6.0, 'INT': 6.0, 'WIS': 6.0, 'DEX': 6.0, 'CON': 6.0, 'CHA': 6.0}
        points = 25

        print(f"You have {points} points to create your character. You may use these points to increase your six attributes or starting skills.")
        print(f"Enter the attribute or skill you which to increase, followed by the amount you wish to increase or decrease the score by. Note that attributes cannot fall below 6.")
        print(self)

        # User input name
        flag = False
        self.name = input("Finally, What is your name? ")
        while True:
            flag = input(f"Your name is {self.name}. Confirm? (Y/N) ")
            if flag in {"Y","y","yes","Yes","YES"}: break
            self.name = input("What is your name? ")

    def __str__(self):
        """
        Returns str output of Character object.
        """
        # Name
        str = f"Name: {self.name}\n"
        # Background
        str += f"Background: {self.background}\n\n"
        # Attributes
        for key, val in self.stats.items():
            # Always output floor of attributes to user.
            str += f"{key} {math.floor(val)}\n"
        str+="\n"
        # Skills
        for key, val, in self.skills.items():
            if key!="languages": str += f"{key} {val}\n"
        # Languages
        str += "langauges:\n"
        for key, val in self.skills['languages'].items():
            if(val>0): str += f"  {key} {val}\n"
        return str


hero = Character("orphan")
