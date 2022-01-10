# This project is currently in dormant state and has no scheduled roadmap for its completion

# Sports Betting Arbitrage

## Concept
Arbitrage sports betting consists of a summing the inverse of the payouts for every outcome of an event
This is referred to as the total implied probability
If the TIP is less than 1 this represents an arbitrage opportunity

## Execution
The execution of this strategy is more work to set up if automation is the goal

You need:
### 1. A model of the outcome of the sport
 - most basic:
    - wins, draws, losses
 - Works as long as the model encompasses all possible outcomes

### 2. A means to obtain the odds and place the bets
 - If API available, use it.
    - Different API client for each betting site. (most of the work is here)
 - Else use computer vision to read the website

### 3. Performance and logging output
 - Can be taken as far as needed
    - text files or graphical front end

The solution proposed would differentiate on the basis of speed, execution and diligence.
Given algorithmic execution it would not require supervision and could therefore be running at all times