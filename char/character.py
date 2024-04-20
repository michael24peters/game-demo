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

    def __init__(self, background, name):

        self.stats = {}

        self.skills = {
            'combat': 0,
            'social': 0,
            'athletics': 0,
            'history': 0,
            'herbalism': 0,
            'medicine': 0,
            'religion_sol': 0,
            'religion_deivos': 0,
            'languages': {'Northern': 0, 'Eastern': 0, 'Southern': 0, 'Western': 0, 'Central': 0}
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
#        if self.background=="orphan":
