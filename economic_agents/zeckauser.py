from open_ai import OpenAI
import matplotlib.pyplot as plt
import numpy as np
import logging 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Zeckauser:
    def __init__(self, api_key, model, image_path):
        self.model = OpenAI(key=api_key, model=model)
        self.image_path = image_path
        self.views = [
            'car safety is the most important thing.',
            'car safety is a terrible waste of money; we should only fund highway safety.',
            'car safety is all that matters. We should not fund highway safety.',
            'car safety and highway safety are equally important',
            'car safety is slightly more important than highway safety',
            "I don't really care about car safety or highway safety",
            'highway safety is the most important thing.',
            'highway safety is a terrible waste of money; we should only fund car safety.',
            'highway safety is all that matters. We should not fund car safety.',
            'highway safety and car safety are equally important',
            'highway safety is slightly more important than car safety',
            "I don't really care about highway safety or car safety"
        ]
        self.status_quo = [30, 50, 60, 70, " "]
        self.options = ['a', 'b', 'c', 'd']

    def play(self):
        generate_status_quo = [
            "The current budget allocation is 30% to auto safety and 70% to highway safety.",
            "The current budget allocation is 50% to auto safety and 50% to highway safety.", 
            "The current budget allocation is 60% to auto safety and 40% to highway safety.",
            "The current budget allocation is 70% to auto safety and 30% to highway safety.",
            " "
        ]
        results = {}
        for element in generate_status_quo:
            for view in self.views:
                prompt = f"""The National Highway Safety Commission is deciding how to allocate its budget between two safety research programs: 

                i) improving automobile safety (bumpers, body, gas tank configurations, seatbelts) and 
                ii) improving the safety of interstate highways (guard rails, grading, highway interchanges, and implementing selective reduced speed limits).

                {element}

                They are considering the following options:

                a) Allocate 70% to auto safety and 30% to highway safety
                b) Allocate 40% to auto safety and 60% to highway safety
                c) Allocate 30% to auto safety and 70% to highway safety
                d) Allocate 50% to auto safety and 50% to highway safety

                Your own views: {view}

                Please choose your most preferred option in light of your views a, b, c or d. Its important that you respond only with one letter!:"""
                solution = self.model.generate(prompt)
                results[(view, element)] = solution
                logger.info(f"Prompt: {prompt}")
                logger.info(f"Model response: {solution}")
            return results

    def create_plot(self, df, views):
        views = ["30% auto \n framed as Status Quo", "50% \n auto framed as Status Quo", "60% \n auto framed as Status Quo", "70% \n auto framed as Status Quo", "Neutral framing"]
        choices = ["30% car, 70% hwy", "50% car, 50% hwy", "60% car, 40% hwy", "70% car, 30% hwy"]
        fig, axs = plt.subplots(1, 5, figsize=(18, 3.5), sharey=True)
        for i, ax in enumerate(axs):
            ax.plot(df[df['View'] == views[i]]['Response'])
            ax.set_title(views[i])
            ax.set_xticks(range(len(choices)))  # Set x-ticks to the range of the number of choices
            ax.set_xticklabels(choices, rotation='vertical')  # Set x-tick labels and rotate them
        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.show()
    """heads = ["30% auto framed as Status Quo", "50% auto framed as Status Quo", "60% auto framed as Status Quo", "70% auto framed as Status Quo", "Neutral framing"]
    df = pd.DataFrame([(view, response) for view, response in self.results.items()], columns=['View', 'Response'])
    views = df['View'].unique()
    fig, axs = plt.subplots(1, len(views), figsize=(15, 3), sharey=True)

    for i, ax in enumerate(axs):
        ax.plot(df[df['View'] == views[i]]['Response'])
        ax.set_title(views[i])

    plt.show()"""

if __name__ == "__main__":
    #api_key, model, image_path
    zeckauser = Zeckauser("sk-", "gpt-3.5-turbo", "test_plot")
    results={('car', 'highway', 'car safety is the most important thing.'): 'd', ('car', 'highway', 'car safety is a terrible waste of money; we should only fund highway safety.'): 'b', ('car', 'highway', 'car safety is all that matters. We should not fund highway safety.'): 'd', ('car', 'highway', 'car safety and highway safety are equally important'): 'd', ('car', 'highway', 'car safety is slightly more important thatn highway safety'): 'b', ('car', 'highway', "I don't really care about car safety or highway safety"): 'As', ('highway', 'car', 'highway safety is the most important thing.'): 'c', ('highway', 'car', 'highway safety is a terrible waste of money; we should only fund car safety.'): 'd', ('highway', 'car', 'highway safety is all that matters. We should not fund car safety.'): 'c', ('highway', 'car', 'highway safety and car safety are equally important'): 'd', ('highway', 'car', 'highway safety is slightly more important thatn car safety'): 'c', ('highway', 'car', "I don't really care about highway safety or car safety"): 'd'}
    views = ['view1', 'view2', 'view3', 'view4', 'view5']
    data = {
        'View': np.repeat(views, 20),  # Repeat each view 20 times
        'Response': np.random.rand(100)  # 100 random numbers
    }

    df = pd.DataFrame(data)  # Create DataFrame from synthetic data
    zeckauser.create_plot(df, views)
    #zeckauser.create_plot(results)
    #zeckauser.play()
