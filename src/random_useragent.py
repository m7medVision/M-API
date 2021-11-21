# open user-agents.txt and return a random user-agent
import random
import requests
def random_useragent():
    f =  requests.get('https://gist.githubusercontent.com/majhcc/4ff967b2f15d01feb0e496eef1db4458/raw/bbed5c3cf42e49643c445d395148c0ea5e06c0f0/user-agent.list').text
    user_agents = f.split('\n')
    return user_agents[random.randint(0, len(user_agents) - 1)]

# print(random_useragent())