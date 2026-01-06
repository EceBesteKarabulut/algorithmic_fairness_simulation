## Algorithmic Fairness Simulation
This project explores how different task allocation algorithms affect fairness and inequality in a team based system.
This simulation models a group of agents who improve their skills as they complete tasks. Over time, the way tasks are assigned can significantly influence both performance and fairness.
---

## Algorithms Implemented
### 1. Greedy Assignment
Always assigns tasks to the agent with the highest current skill. This strategy maximizes short-term efficiency but leads to extreme task concentration and inequality.

### 2. Balanced Assignment (Exploration-Based)
Introduces randomness into task assignment ny occasionally selecting a random agent instead of the best-performing one. 
This changes which agent becomes dominant but does not eliminate inequality.

### 3. Opportunity-Aware Assignment
Prioritizes agents who have completed fewer tasks.

This approach significantly reduces task concentration and ensures a more equitable distribution of opportunities.

---

## Key Findings
-Greedy strategies amplify small initial advantages.

-Random exploration alone is insufficient to ensure fairness.

-Opportunity-aware rules lead to more balanced outcomes.
---

## How To Run
```bash
python simulation.py
``` 

## Experimental Results
The simulation was run with 6 agents and 100 tasks.

### Greedy Assignment
One agent received almost all tasks, while others received few or none, demonstrating extreme task concentration.

### Balanced Assignment (Exploration-Based)
Increasing the exploration rate changed which agent became dominant,but task inequality persisted across different runs.

### Opportunity-Aware Assignment
Tasks were distributed much more evenly across agents, with no single agent dominating the workload.



