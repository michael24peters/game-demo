import math

# TODO: NPC subclass that generates NPC from declaration
# TODO: calculate changes in stats and skills, set by Anki-style algorithm. Leave it to later systems to select which system was triggered.


class Character:
    """
    Creates a Character with a set of characteristics and attributes that define them.
    The Character class also contains the functionality needed to view, update, and use these statistics.

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
    update_stat(stat):
        Increases or decreases Character stat by inputted amount.
    supermemo(q, n, EF, I):
        Track progression through spaced repitiion
    """

    def __init__(self, name="", background=""):
        self.attr = {
            "STR": 6.0,
            "INT": 6.0,
            "WIS": 6.0,
            "DEX": 6.0,
            "CON": 6.0,
            "CHA": 6.0,
        }

        self.skills = {
            "combat": 0,
            "social": 0,
            "athletics": 0,
            "history": 0,
            "herbalism": 0,
            "medicine": 0,
            "religion_sol": 0,
            "religion_deivos": 0,
            "languages": {
                "central": 1,
                "northern": 0,
                "eastern": 0,
                "southern": 0,
                "western": 0,
            },
        }

        self.hidden_skills = {
            "secret_history": 0,
            "metaphysics": 0,
            "sorcery": 0,
            "mental_resistance": 0,
        }

        self.background = background
        self.name = name
        if self.name == "" or background not in ["orphan", "farmer", "noble"]:
            self.create_character()

    def create_character(self):
        """Creates a character within the game.

        The Character class constructor sets the default characteristics of the Character, plus the User
        chosen background. create_character() completes this process by giving a series of user-inputted
        choices for stat adjustments, allocating skills points, and so on.
        """

        default_attr = {
            "STR": 6.0,
            "INT": 6.0,
            "WIS": 6.0,
            "DEX": 6.0,
            "CON": 6.0,
            "CHA": 6.0,
        }
        default_skills = {
            "combat": 0,
            "social": 0,
            "athletics": 0,
            "history": 0,
            "herbalism": 0,
            "medicine": 0,
            "religion_sol": 0,
            "religion_deivos": 0,
            "languages": {
                "central": 1,
                "northern": 0,
                "eastern": 0,
                "southern": 0,
                "western": 0,
            },
        }

        points = 25

        # ====Background====
        while True:
            if self.background in ["orphan", "farmer", "noble"] != "":
                break
            background = input("What is your background? Orphan, farmer, or noble? ")
            if background in ["orphan", "Orphan", "o", "O"]:
                self.background = "orphan"
            elif background in ["farmer", "Farmer", "f", "F"]:
                self.background = "farmer"
            elif background in ["noble", "Noble", "n", "N"]:
                self.background = "noble"

            print("Invalid background.", end=" ")

        # ====Stats====
        print(f"You have {points} points to create your character.")
        print(
            "You may use these points to increase your six attributes or starting skills."
        )
        print("Below is your character sheet. Use it as a reference.")

        show = True
        while True:
            if show:  # Character sheet + prompt + points
                print(self)
                print(
                    "Enter the attribute or skill you which to increase, followed by the amount you"
                )
                print(
                    "wish to increase or decrease the score by, e.g. 'STR +2', 'history +1', 'INT -1'."
                )
                print(
                    "Note that the range for attributes is 6 to 15 and for skills 0 to 3."
                )
                print(f"Points remaining: {points}")

            stat = input().split(
                " "
            )  # user must input STAT, a single space, then the value
            stat[1] = int(stat[1])

            show = self.update_stat(*stat)
            if show:
                points -= stat[1]
            else:
                print("Invalid input. Try again.")

            if points == 0:
                flag = input("Finished? (Y/N/Restart) ")
                if flag in {"Y", "y", "yes", "Yes", "YES"}:
                    break
                # Restart character creation
                if flag in {"Restart", "restart", "r", "R"}:
                    self.attr = default_attr
                    self.skills = default_skills
                    points = 25

        # ====Name====
        flag = False
        self.name = input("Finally, What is your name? ")
        while True:
            flag = input(f"Your name is {self.name}. Confirm? (Y/N) ")
            if flag in {"Y", "y", "yes", "Yes", "YES"}:
                break
            self.name = input("What is your name? ")

    def update_stat(self, stat, x):
        """
        Increases or decreases Character stat[0] value by an amount equal to stat[1].

        Parameters
        ----------
        stat : str
            Character stat name
        x : float
            Amount to change stat

        Returns
        -------
        bool
            Successful change of stat (True) or not (False)

        Examples
        --------
        >>> update_stat(['STR', 2]) # Increases STR attr by 2
        >>> update_stat('combat', .15) # Increases combat skill by .15
        """
        done = True
        # Attribute
        if len(stat) == 3:
            try:
                if 6.0 <= self.attr[stat.upper()] + x <= 18.0:
                    self.attr[stat.upper()] += x
                else:
                    done = False
            except:
                done = False
        # Skill
        else:
            try:
                if stat in self.skills["languages"]:
                    if 0.0 <= self.skills["languages"][stat.lower()] + x <= 6.0:
                        self.skills["languages"][stat.lower()] += x
                    else:
                        done = False
                else:
                    if 0.0 <= self.skills[stat.lower()] + x <= 6.0:
                        self.skills[stat.lower()] += x
                    else:
                        done = False
            except:
                done = False
        return done

    def __str__(self):
        """
        Returns str output of Character object.
        """
        # Formatting
        str = "\n+----------------------+\n"
        # Name
        str += f"| Name: {self.name}\n"
        # Background
        str += f"| Background: {self.background}\n| \n"
        # Attributes
        for key, val in self.attr.items():
            # Always output floor of attributes to user.
            str += f"| {key} {math.floor(val)}\n"
        str += "| \n"
        # Skills
        for (
            key,
            val,
        ) in self.skills.items():
            if key != "languages":
                str += f"| {key} {val}\n"
        # Languages
        str += "| langauges:\n"
        for key, val in self.skills["languages"].items():
            str += f"|   {key} {val}\n"
        # Formatting
        str += "+----------------------+\n"
        return str

    def supermemo(self, q, n, EF, I):
        """
        supermemo() uses the SuperMemo2 algorithm to track progression through spaced repitition [1].
        It takes in the previous progress of the item to learn and updates the values based on the
        grade of the learner.

        Parameters
        ----------
        q : int
            User grade ranging from 1-5:
            5 - perfect response
            4 - correct response after a hesitation
            3 - correct response recalled with serious difficulty
            2 - incorrect response; where the correct one seemed easy to recall
            1 - incorrect response; the correct one remembered
            0 - complete blackout.
        n : int
            Repitition number
        EF : float
            Easiness factor
        I : int
            Interval number

        Returns
        -------
        int
            Updated value of repitition number, n
        float
            Updated value of easiness factor, EF
        int
            Updated value of interval, I

        References
        ----------
        [1] "SuperMemo2", https://www.supermemo.com/en/blog/application-of-a-computer-to-improve-the-results-obtained-in-working-with-the-supermemo-method

        Examples
        --------
        >>> supermemo(q=5, n=0, EF=1.3, I=0) # New card answered perfectly
        >>> (n=0, EF=1.4, I=1)
        >>> supermemo(4, 2, 1.5, 8) # Encountered card answered with a grade of 4
        >>> (n=3, EF=1.5, I=12)
        """

        if q >= 3:  # Correct response
            if n == 0:
                I = 1
            elif n == 1:
                I = 6
            else:
                I = round(I * EF)
            n += 1
        else:  # Incorrect response
            n = 0
            I = 1

        EF = round(EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)), 2)
        if EF < 1.3:
            EF = 1.3

        return (n, EF, I)


class NPC(Character):
    def __init__(
        self,
        name,
        background=None,
        attr=None,
        skills=None,
        hidden_skills=None,
    ):
        if hidden_skills is None:
            hidden_skills = {
                "secret_history": 0,
                "metaphysics": 0,
                "sorcery": 0,
                "mental_resistance": 0,
            }
        if skills is None:
            skills = {
                "combat": 0,
                "social": 0,
                "athletics": 0,
                "history": 0,
                "herbalism": 0,
                "medicine": 0,
                "religion, sol": 0,
                "religion, deivos": 0,
                "languages": {
                    "central": 1,
                    "northern": 0,
                    "eastern": 0,
                    "southern": 0,
                    "western": 0,
                },
            }
        if attr is None:
            attr = {
                "STR": 6.0,
                "INT": 6.0,
                "WIS": 6.0,
                "DEX": 6.0,
                "CON": 6.0,
                "CHA": 6.0,
            }
        self.name = name
        self.background = background
        self.attr = attr
        self.skills = skills
        self.hidden_skills = hidden_skills
