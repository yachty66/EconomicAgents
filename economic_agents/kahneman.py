from open_ai import OpenAI
import matplotlib.pyplot as plt
import numpy as np
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Kahneman:
    def __init__(self, api_key, model):
        openai_api_key: str = None
        self.openai_api_key = openai_api_key
        self.model = OpenAI(key=api_key, model=model)
        self.politics_view = [
            "socialist",
            "leftist",
            "liberal",
            "moderate",
            "liberterian", 
            "conservative",
        ]
        self.store_actions = ["raises the price to", "changes the price to"]
        self.prices = [16, 20, 40, 100]

    def play(self):
        results = {}
        for politics in self.politics_view:
            for store_action in self.store_actions:
                for price in self.prices:
                    prompt = f"""A hardware store has been selling snow shovels for $15. The morning after a large snowstorm, the store {store_action} ${price}. 

                    Please rate this action as:
                    1) Completely Fair 
                    2) Acceptable
                    3) Unfair 
                    4) Very Unfair

                    You are a {politics}.
                    What is your choice [1, 2, 3, or 4]. Its important that you only answer with the number and nothing else:"""
                    solution = self.model.generate(prompt)
                    results[(politics, store_action, price)] = solution
                    print(results)
                    logger.info(f"Prompt: {prompt}")
                    logger.info(f"Model response: {solution}")
        return results

    def create_plot(self, results):
        plot_data = {}
        for (politics, store_action, price), judgment in results.items():
            judgment = int(judgment) - 1  # Convert judgment to zero-based index
            if politics not in plot_data:
                plot_data[politics] = {}
            if price not in plot_data[politics]:
                plot_data[politics][price] = {}
            if store_action not in plot_data[politics][price]:
                plot_data[politics][price][store_action] = [0, 0, 0]
            plot_data[politics][price][store_action][judgment] += 1

        fig, axs = plt.subplots(len(self.politics_view), len(self.prices), figsize=(13, 13))  # Increase figure size
        plt.subplots_adjust(wspace=0.5, hspace=0.5)  # Adjust spacing between subplots
        for i, politics in enumerate(self.politics_view):
            for j, price in enumerate(self.prices):
                ax = axs[i, j]
                width = 0.35
                x = np.arange(3)  # Define x here
                for k, store_action in enumerate(self.store_actions):
                    view_data = [plot_data[politics][price][store_action][l] for l in range(3)]
                    ax.bar(x + k*width/2, view_data, width/2, color=['red', 'grey'][k], label=store_action)
                ax.set_xlabel('Moral Judgments')
                ax.set_ylabel('Count')
                ax.set_title(f'{politics} for price {price}')
                ax.set_xticks(x + width/4)
                ax.set_xticklabels(["Acceptable", "Unfair", "Very Unfair"])  # Set the x-axis labels to the moral judgments
                ax.legend()
        fig.tight_layout()
        plt.savefig('plot.png')  # Save the figure as an image
        plt.show()

    """def __call__(self):
        results = self.play()
        self.create_plot(results)
        return results"""

if __name__ == "__main__":
    game = Kahneman("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", "gpt-3.5-turbo")
    #results = game.play()
    results = {('socialist', 'raises the price to', 16): '3', ('socialist', 'raises the price to', 20): '3', ('socialist', 'raises the price to', 40): '3', ('socialist', 'raises the price to', 100): '3', ('socialist', 'changes the price to', 16): '3', ('socialist', 'changes the price to', 20): '3', ('socialist', 'changes the price to', 40): '3', ('socialist', 'changes the price to', 100): '3', ('leftist', 'raises the price to', 16): '3', ('leftist', 'raises the price to', 20): '3', ('leftist', 'raises the price to', 40): '3', ('leftist', 'raises the price to', 100): '3', ('leftist', 'changes the price to', 16): '3', ('leftist', 'changes the price to', 20): '3', ('leftist', 'changes the price to', 40): '3', ('leftist', 'changes the price to', 100): '3', ('liberal', 'raises the price to', 16): '2', ('liberal', 'raises the price to', 20): '2', ('liberal', 'raises the price to', 40): '3', ('liberal', 'raises the price to', 100): '3', ('liberal', 'changes the price to', 16): '2', ('liberal', 'changes the price to', 20): '2', ('liberal', 'changes the price to', 40): '2', ('liberal', 'changes the price to', 100): '2', ('moderate', 'raises the price to', 16): '2', ('moderate', 'raises the price to', 20): '2', ('moderate', 'raises the price to', 40): '2', ('moderate', 'raises the price to', 100): '2', ('moderate', 'changes the price to', 16): '2', ('moderate', 'changes the price to', 20): '2', ('moderate', 'changes the price to', 40): '2', ('moderate', 'changes the price to', 100): '2', ('liberterian', 'raises the price to', 16): '2', ('liberterian', 'raises the price to', 20): '2', ('liberterian', 'raises the price to', 40): '2', ('liberterian', 'raises the price to', 100): '2', ('liberterian', 'changes the price to', 16): '2', ('liberterian', 'changes the price to', 20): '2', ('liberterian', 'changes the price to', 40): '2', ('liberterian', 'changes the price to', 100): '2', ('conservative', 'raises the price to', 16): '2', ('conservative', 'raises the price to', 20): '2', ('conservative', 'raises the price to', 40): '2', ('conservative', 'raises the price to', 100): '2', ('conservative', 'changes the price to', 16): '2', ('conservative', 'changes the price to', 20): '2', ('conservative', 'changes the price to', 40): '2', ('conservative', 'changes the price to', 100): '2'}
    plot = game.create_plot(results)

