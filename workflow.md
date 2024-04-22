# Workflow
## Branching
The project will be divided into the following semi-independent branches, which will be merged when complete and compatible. The branches will be completed roughly in the listed order:
- stats: This branch covers the character statistics and calculations to change these stats.
  - Set up the data structures for the character
  - Adjust a stat
  - Measure progress towards a stat or skill
- menu: This branch covers the "main menu" of the gameplay loop, where the User allocates points towards their weekly activities.
  - Activity choices
  - UI
  - Current location
  - View character sheet
- intro: This branch covers the intro of the game.
  - Background (starting stats, Dark Souls-style)
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
-
