####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'r', 'p', 's', 'l', or 'k'
####

team_name = 'Match'
strategy_name = 'Match'
strategy_description = 'Try to match their history'
    
def move(my_history, their_history, my_score, their_score):
    
    '''
                            O   P   P   O   N   E   N   T
    ||----------||----------||----------||----------||----------||----------||
    ||          || Rock     || Paper    || Scissors || Lizard   || spock    ||
    ||----------||----------||----------||----------||----------||----------||   
    || Rock     ||    0 pts || -100 pts ||  100 pts ||  100 pts || -100 pts ||
  Y ||----------||----------||----------||----------||----------||----------||
    || Paper    ||  100 pts ||    0 pts || -100 pts || -100 pts ||  100 pts ||                                                    
  O ||----------||----------||----------||----------||----------||----------||
    || Scissors || -100 pts ||  100 pts ||    0 pts ||  100 pts || -100 pts ||                                         
  U ||----------||----------||----------||----------||----------||----------|| 
    || Lizard   || -100 pts ||  100 pts || -100 pts ||    0 pts ||  100 pts ||                               
    ||----------||----------||----------||----------||----------||----------||
    || spock    ||  100 pts || -100 pts ||  100 pts || -100 pts ||    0 pts ||              
    ||----------||----------||----------||----------||----------||----------||

    Rock = 'r'
    Paper = 'p'
    Scissors = 's'
    Lizard = 'l'
    spock = 'k'      
    '''
    '''Make my move based on the history with this player.
    
    history: a string with one letter (r, p, s, l, or k) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns a 'r', 'p', 's', 'l', or 'k' for Rock, Paper, Scissors, Lizard, Spock
    '''
    
    # Looks back at their history and makes a decision based on that.
    
    if len(my_history)==0: # It's the first round: LIZARD
        return 'l'
    else:
        # If there was a previous round just like the last one,
        # do whatever they did in the round that followed it
        
        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        # Look at rounds before that one
    for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and (prior_round_them == recent_round_them):
                return their_history[round]
               # No match found
            if my_history[-1]=='r' and their_history[-1]=='p':
                return 's' # if the last round they played paper and I played rock then next round play scissors
            else:
                return 'k' # Otherwise SPOCK.