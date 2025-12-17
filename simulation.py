# Algorithmic Fairness Simulation
#This project compares three task allocation strategies:
# 1. Greedy assignment
# 2. Exploration-based balanced assignment
# 3. Opportunity-aware assignment
#
#The goal is to study how different algorithms affect fairness and task
#and task concentration over time.


import random 

class TeamMember: 
    def __init__(self, skill, learning_rate):
        self.skill = skill
        self.learning_rate = learning_rate
        self.tasks_done = 0

    def complete_task(self):
        self.tasks_done += 1
        self.skill += self.learning_rate
      
def create_team():
    team = []   
    for _ in range (6):
        skill = random.uniform(1.0, 3.0)
        learning_rate = random.uniform(0.05, 0.15)
        team.append(TeamMember(skill, learning_rate))
    return team

def greedy_assignment(team, tasks):
    for _ in range(tasks):
        best_member = max(team, key=lambda m: m.skill)   
        best_member.complete_task()

def balanced_assignment(team, tasks, explore_prob=0.6):
    for _ in range(tasks):
        if random.random() < explore_prob:
            chosen = random.choice(team)
        else:
            chosen = max(team, key=lambda m: m.skill)
        chosen.complete_task() 

def opportunity_aware_assignment(team, tasks):
    for _ in range(tasks):
        chosen = min(team, key=lambda m: m.tasks_done)
        chosen.complete_task()                   

def main():
    team = create_team()
    opportunity_aware_assignment(team, 100)   

    for i, member in enumerate(team):
        print(i, member.tasks_done, round(member.skill, 2))       

        
if __name__ == "__main__":
    main()




