"""
#TEST RABIN
from economic_agents import CharnessRabin

charness_rabin = CharnessRabin(api_key="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", model="gpt-3.5-turbo", personality=1, image_path="random/file", logging=True)
results = charness_rabin.play()
charness_rabin.create_plot(results)
"""

"""
#TEST HORTON
from economic_agents import Horton
#def __init__(self, api_key, model, image_path, logging):
horton = Horton(api_key="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", model="gpt-3.5-turbo", image_path="random/horton", logging=True)
results = horton.play()
horton.create_plot(results)
"""

"""
#TEST Kahneman
from economic_agents import Kahneman

kahneman = Kahneman(api_key="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", model="gpt-3.5-turbo", image_path="results/kahneman", logging=True)
results = kahneman.play()
kahneman.create_plot(results)
"""

#TEST ZECKAUSER
from economic_agents import Zeckhauser

zeckhauser = Zeckhauser(api_key="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", model="gpt-3.5-turbo", image_path="results/zeckhauser", logging=True)
results = zeckhauser.play()
zeckhauser.create_plot(results)