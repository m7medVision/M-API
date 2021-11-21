# open user-agents.txt and return a random user-agent
import random
def random_useragent():
    with open(r'src\files\user-agent.txt', 'r') as f:
        user_agents = f.read().split('\n')
    return user_agents[random.randint(0, len(user_agents) - 1)]