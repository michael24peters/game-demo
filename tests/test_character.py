## USE FOR LOCAL IMPORTS AS NEEDED ##
# importing sys
# import sys

# adding Folder_2/subfolder to the system path
# sys.path.insert(0, "/Users/Michael/Documents/game-demo/char")
## ##

from char import Character, NPC


def test_create_init():
    test = Character(name="Test", background="orphan")

    assert test.name == "Test"
    assert test.background == "orphan"
    assert test.attr == {
        "STR": 6.0,
        "INT": 6.0,
        "WIS": 6.0,
        "DEX": 6.0,
        "CON": 6.0,
        "CHA": 6.0,
    }
    assert test.skills == {
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


def test_update_stats():
    test = Character(name="Test", background="orphan")

    test.update_stat(*["STR", 2])
    assert test.attr["STR"] == 8
    test.update_stat("combat", 0.15)
    assert test.skills["combat"] == 0.15
    test.update_stat("northern", 0.5)
    assert test.skills["languages"]["northern"] == 0.5
    test.update_stat("southern", 2)
    assert test.skills["languages"]["southern"] == 2


def test_NPC():
    mentor = NPC("Anaheim", background="mentor")

    assert mentor.name == "Anaheim"
    assert mentor.background == "mentor"
