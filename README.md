# game-demo
Final Project for SE4Sci-S2024 course

## Concept
This project details the process for making game using concepts learned in class. The game is about the training of a hero. Users play as the aspiring hero and make decisions, talk to people, go on training quests, and encounter events that will shape who they become. These characteristics are represented as stats -- much as you might see in a typical role-playing game -- that are raised (or lowered) as decisions are made and events occur.

## Objective
Creating a game is well beyond the scope of this project. Too many components and too few members are involved to accomplish such a feat. Instead, this report will detail the game concept, design goals, backend work, and everything involved in setting up this game for an easier future. There will also be a short demo provided for an example of how testing will occur, what branch conventions will be used, and how object-oriented design.

The objective would be met if parts of a game were cohesively stitched together from a variety of different parts. This would put to the test operating out of the terminal (UNIX), best practices, version control, (feature) branching, pytest, pre-commit, GitHub Actions, continuous integration, sphinx (documentation), and object-oriented design.

## Overview
The player chooses a background -- orphan, farmer, or noble -- and is brought under the tutelage of a mentor -- an enterprising mercenary, a cunning scholar, or a nature-loving monk.

The character travels with the mentor, learning about the world as they go. There are opportunities for exploration (*OUT OF SCOPE*), combat (*OUT OF SCOPE*), dialogue with interesting characters, and honing their skills.

Eventually, a story emerges from their training, and the journey ends with the inciting incident typical of the hero's journey.

Sometimes events will directly impact the character stats, sometimes certain dialogue options will unlock future outcomes, sometimes the dialogue is just interesting, sometimes a non-playable character will say something useful about the world that you can use later on.

## Content
The game was be built using Python and operates out of the terminal. This archaic approach is used to focus on learning design principles, but this game could be expanded to operate out of a game engine.

Much of the game itself is programmed through a great deal of if-else and try-catch blocks. This is a sample of the much more extensive and complex blocks that will be needed for branching into different paths of dialogue and sub-events. Each “scenario” may be broken into a class (or function and sub-functions), which walk through the story of the main character. With the amount of dialogue present, this game could quickly spiral out of control. 

### Breaking up Functions
This spiraling was quickly caught in the design process during create_character(), a method called in the Character constructor. Itself already a lengthy extension to the constructor, it once contained an entire algorithm for changing the character stats in a way specific to character creation. This was found to be far beyond the reach of the method. Instead, the entire system was generalized and moved into a method called update_stats(), which acts as a sort of "setter" function for character attributes and skills. It increases or decreases any stat based on User input, up to the minimum or maximum allowed by the game. When all the special statements and "User-proofing" was implemented, the method proved extensive in its own right.

These challenges encountered are only a microcosm to the project as a whole. Vigilance is required to keep a program organized and functional. Big functions need to be broken up into their smallest divisible chunks. Not only does this make the code easier to read, it also makes the program more functional and robust for the future.

### Improvement
The method of personal improvement in the game is determined using the same algorithm used by Anki flashcard software (which is open-source). It is based on a grading scheme that determines the easiness factor with which a task was completed, emphasizing or de-emphasizing future tasks in response.

## Process
1. Setup (Git(Hub), branching, big picture ideas)
2. Game design (high-level game mechanics, gameplay loop, story idea)
3. Project design (goals, planned feature branches)
4. Draft work (rough draft/pseudo-code)
5. See CHANGELOG section.

## CHANGELOG
Below are the current contributions to the project, divided into versions in order of release. Branch version are organized by:
- X.0.0 (major release milestone)
- 0.X.0 (branch release)
- 0.0.X (features/changes/fixes within a branch)

### v0.0.7
- Reorganized files
- Fixed sphinx documentation
- Minor fixes

### v0.0.6
- Updated docstrings
- Added update_stat()
- Moved create_character() functionality to update_stat()
- Fixed: can now add skill points to languages
- Changed create_character
  - Displays all languages
- Added tests

### v0.0.5
- Added NPC subclass
  - __init__()
- Changes to Character
  - If name and background given in constructor args, skip create_character() and use default values
  - __str__() now formatted to look like proper character sheet
- Added supermemo()
- Finished create_character()
- Added report.md

### v0.0.4
- Added methods for Character
  - create_character() (WIP)
  - __str__()

### v0.0.3
- Added noxfile.py
- Added pyproject.toml
- Added ci.yaml
- Added tests/test_character.py with dummy method for debugging
- Added .gitignore

### v0.0.2
- Added sphinx documentation support
  - Added docs/conf.py
  - Added docs/index.rst
  - Added docs/make.bat
  - Added docs/Makefile

### v0.0.1
- Added character.py
- Added CHANGELOG.py

## Todo
Features can be endlessly added to a game. Rather than discuss the features that could be added (see Branches section below), what follows is a list of backend support that could realistically be produced for the game:
- More test cases
- Pre-made terminal input commands to test character creation
- Proper GitHub Actions (fix relative/local imports)
- Framework for creating events/scenarios
- Look for continual keyboard input detection for commands like "View Character" from User.
  - Alternatively, create a GUI with buttons

## Branches
The project will be divided into the following semi-independent branches, which will be merged when complete and compatible. The branches will be completed roughly in the listed order:
- stats: This branch covers the character statistics and calculations to change these stats.
  - Set up the data structures for the character (DONE)
  - Adjust a stat (DONE)
  - Measure progress towards a stat or skill (DONE)
- menu: This branch covers the "main menu" of the gameplay loop, where the User allocates points towards their weekly activities.
  - Activity choices
  - UI
  - Current location
  - View character sheet (DONE)
- intro: This branch covers the intro of the game.
  - Background (starting stats, Dark Souls-style) (DONE)
  - Mentor choice
  - Dialogue & story
- event-generator: This branch covers the events and when they occur
  - Event types
  - Accumulating probability per event/scenario type (modified by player skills and stats, e.g. characters with high persuasion skills are more likely to get persuastion-oriented events)
  - Events (*LIMITED SCOPE*)
- story: This branch covers the storyline of the game, which consists of period "story events" that progress the plot of the game and send the timeline significantly forward.
- events: This branch covers the events/scenarios of the game. *Given the scope of the project, this may only be addressed in a limited capacity.*
  - Decision trees
  - Opponent statistics
  - Combat system (relevant combat skills + situation skill + rand(1-4) vs. opponent values)
  - Fallout-style dialogue trees
- expansion:
  - Mass combat system