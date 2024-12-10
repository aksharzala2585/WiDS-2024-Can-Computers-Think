# imports
from bandits import Bandit
import random
import matplotlib.pyplot as plt
# Include your imports here, if any are used. 


# number of bandits = n
n = 10
# number of iterations = N
N = 1000
bandits = [Bandit(random.random()*4-2) for _ in range(n)]
bandit_mean = []
for bandit in bandits:
    bandit_mean.append(bandit.get_mean())
print(bandit_mean)


bandits[0].pullLever()


def run_greedy():
    # TODO: Implement the greedy algorithm here
    # Return the reward from the bandits in a list
    bandit_rewards = [[] for i in range (n)]
    max_index = 0
    max_rew = -10000
    for i in range(n):
        x = bandits[i].pullLever()
        bandit_rewards[i].append(x)
        if max_rew<x:
            max_rew = x
            max_i = i
    for y in range(N-n):
        bandit_rewards[max_i].append(bandits[max_i].pullLever())
    return bandit_rewards


cumulative_sum = []
#the number of iterations - itr
itr = 1000
for x in range (itr):
    bandit_rewards = run_greedy()
    sum_score = 0
    for bandit in bandit_rewards:
        for y in bandit:
            sum_score+=y
    cumulative_sum.append(sum_score)
plt.hist(cumulative_sum,bins = 100)
plt.title(f"Histogram of rewards over {itr} iterations")
plt.savefig("histogram.png")
plt.show()
sum_score = 0
for score in cumulative_sum:
    sum_score += score
avg = sum_score/itr
print(avg)


optimal_reward= 1000*max(bandit_mean)
print(optimal_reward)
regret = optimal_reward - avg
print(regret)
print(regret /optimal_reward *100 )