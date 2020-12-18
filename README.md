## Betrayals for the win 

### Abstract

While the paper focused on the linguistic harbingers of betrayal, we would like to study the effectiveness of betrayal, as a strategy in the Diplomacy online game. Does betraying your allies improve your odds of winning? To conduct our analysis, we will use a new dataset corresponding to an MySQL database including more than 21’000 games. Using the same definition of relationships as the the original paper, we will detect players that betrayed their allies and how many times they did so during a game. We will also study how being betrayed influences the behavior of the victim during the rest of the game. Our project will therefore take the analysis one step further than the paper by looking at what happens after the betrayal, while our paper focused on what happened before. Even though the dataset comes from an online strategy game, we believe that the uncovered patterns could provide interesting insights on the impact of betrayal in real-life relationships.

### Research Questions 

- What’s the probability of winning if you betray your allies? How does it change depending on the number of allies betrayed? 
- What’s the probability of winning if you have been betrayed?
- ~~How many players did a winner betray on average?~~
- ~~Do victims tend to become more aggressive towards all the other players after a betrayal?~~
- ~~Do victims tend to overreact against their betrayer after the betrayal?~~
- Can a classifier be trained to predict a betrayal based onorders ? 

The questions are in order of importance. The number of answered questions will depend on the time left. The striked through questions were the ones not longer relevant after our preliminary analysis. 

### Proposed dataset 

We have found one very rich dataset about the Diplomacy game: **[DiplomacyBoardGame - dataset by maxstrange | data.world](https://data.world/maxstrange/diplomacyboardgame)** - it's a SQL dataset consisting of 5 tables :
- `games`, with 21197 records
- `players`, with 150668 records
- `turns`, representating mostly events within seasons, with 1'005'01 records
- `units`, representating armies within the game, with 1'205'180 records
- `orders`, representating military decisions made by players, with 13'039'412 records

A first analysis of the dataset revealed that our proposed study is feasible. As showed in the notebook that is present in this repository, it was possible to identify for one game the **acts of friendships** and the **acts of hostility** that plays a central role in the first paper we had studied. Hence, it will be possible to define 'friends' and when a betrayal happens.

*Note about the format of the dataset*: the dataset is provided as a .sql file, which could be opened using 'mysql'. There is a python script called 'read_sql_file.py' which transforms this dataset into '.pickle' object, so that we can work with pandas and not with SQL request. 

### Methods

**Data collection**:  all tables can be linked to one another with several identifier variables such as `game_id` or `unit_id`, thus it is possible to reconstruct from all the events of a game who is wining and what relationships exist between the 7 different players.

**Data analysis**: In order to detect all betrayals in a game, each player's orders will be analyzed to find friendships between players and their (potential) downfall. Friendships and betrayals will be defined like in the paper on “ linguistic harbingers of betrayal’, i.e. “we focus on relationships that contain at least two consecutive and reciprocated acts of friendships that span at least three seasons in game time.”  A player is defined as a winner of the game if the variable “won” for the game (identified with its ‘game_id’) is equal to 1. In term of the rules, it's often the case when this player controls 18 '' 

**Matching player**:  match players with similar actions and starting locations (probably using a propensity score) to see how a betrayal has affected the player (more aggressive orders, e.g. ‘destroy, ‘move’ troops to the enemy’s territory, or betrayals)

### Proposed timeline

**Week 12** - downloading and extracting features from SQL database dump / formatting to use panda tools on the dataset, identify betrayals and match victims to non-victims <br>
**Week 13** - data analysis (process the data and plot the figures required to answer our research questions)<br>
**Week 14** - report (figures & analysis), prepare the data story and the video (script, film, edit)

### Organization within the team

- ~~Arthur will handle the downloading and the formatting of the dataset in week 1.~~
- ~~The code will be regularly posted on the github in order for each student to work on each part without disturbing the rest of the team.~~
- ~~Arthur will work on finding the betrayals in each game using the same criteria as in the first paper.~~
- ~~In week 2, the key insights will be defined by the whole team and the report will be built on the insights.~~
- ~~In week 3, writing the report (especially Diane and Taavet), video and data story writing~~

- Arthur : data wrangling and processing, coming up with the algorithm and coding it
- Diane : writing the datastory, ploting graphs and proofreading the notebook
- Taavet : writing the report, ploting graphs and proofreading the datastory

