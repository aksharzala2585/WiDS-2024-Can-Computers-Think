# imports
from bandits import Bandit
import random
import matplotlib.pyplot as plt
import numpy as np
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
print(f'{regret*100/optimal_reward} %')


def run_epsilon_greedy(epsilon):
    # TODO: Implement the epsilon greedy algorithm here
    # Return the reward from the bandits in a list
    bandit_rewards = [[] for i in range (n)]
    for x in range(N):
        i = random.random()
        if i < epsilon:
            bandit_num = random.randint(0,n-1)
            bandit_rewards[bandit_num].append(bandits[bandit_num].pullLever())
        else:
            max_index=0
            max_val = -10000
            for j in range(n):
                if len(bandit_rewards[j]):
                    mean_val = sum(bandit_rewards[j])/len(bandit_rewards[j])
                else:
                    mean_val = 0
                if mean_val>max_val:
                    max_val = mean_val
                    max_index = j
            bandit_num = max_index
            bandit_rewards[bandit_num].append(bandits[bandit_num].pullLever())
            
    return bandit_rewards


cumulative_sum = []
#the number of iterations - itr
itr = 1000
for x in range (itr):
    bandit_rewards = run_epsilon_greedy(0.1)
    sum_score = 0
    for bandit in bandit_rewards:
        for y in bandit:
            sum_score+=y
    cumulative_sum.append(sum_score)
plt.hist(cumulative_sum,bins = 100)
plt.title(f"Histogram of rewards over {itr} iterations")
plt.show()
sum_score = 0
for score in cumulative_sum:
    sum_score += score
avg_epsilon = sum_score/itr
print(avg_epsilon)


regret_epsilon = optimal_reward - avg_epsilon
print(regret_epsilon)
print(f'{regret_epsilon*100/optimal_reward} %')

epsilon_values= [i/100 for i in range(100)]
cumulative_epsilon_sum = []
for val in epsilon_values:
    cumulative_sum = []
    for x in range (1):
        bandit_rewards = run_epsilon_greedy(val)
        sum_score = 0
        for bandit in bandit_rewards:
            for y in bandit:
                sum_score+=y
        cumulative_sum.append(sum_score)
    cumulative_sum_score = 0
    for score in cumulative_sum:
        cumulative_sum_score += score
    avg_epsilon = cumulative_sum_score/10
    cumulative_epsilon_sum.append(avg_epsilon)
plt.plot(epsilon_values, cumulative_epsilon_sum)
plt.xlabel("Epsilon Value")
plt.ylabel("Cumulative Reward")
plt.title("Cumulative Average Reward vs. Number of Iterations")
plt.grid()
plt.show()
print(f'The reward is maximum at the value of epsilon {np.argmax(cumulative_epsilon_sum)/100}')