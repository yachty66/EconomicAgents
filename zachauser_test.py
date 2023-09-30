prommpt = """The National Highway Safety Commission is deciding how to allocate its budget between two safety research programs: 
i) improving automobile safety (bumpers, body, gas tank configurations, seatbelts) and 
ii) improving the safety of interstate highways (guard rails, grading, highway interchanges, and implementing selective reduced speed limits)."""


"""The National Highway Safety Commission is deciding how to allocate its budget between two safety research programs: i) improving automobile safety (bumpers, body, gas tank configurations, seatbelts) and ii) improving the safety of inter-state highways (guard rails, grading, highway interchanges, and implementing selectively reduced speed limits).

They are considering the following options:

a) Allocate 70% to auto safety and 30% to highway safety
b) Allocate 40% to auto safety and 60% to highway safety
c) Allocate 30% to auto safety and 70% to highway safety
d) Allocate 50% to auto safety and 50% to highway safety

Your own views: You believe that a balanced approach is best, with equal funding to both auto safety and highway safety.

Please choose your most preferred option in light of your views. its important that you only respond with one letter a, b, c, d:"""




if heads:
    option1, option2 = "car", "highway"
else:
    option1, option2 = "highway", "car"
options = [
    f"{option1} safety is the most important thing.",
    f"{option1} safety is a terrible waste of money; we should only fund {option2} safety.",
    f"{option1} safety is all that matters. We should not fund {option2} safety.",
    f"{option1} safety and {option2} safety are equally important",
    f"{option1} safety is slightly more important thatn {option2} safety",
    f"I don't really care about {option1} safety or {option2} safety"
]

views = "You believe that a balanced approach is best, with equal funding to both auto safety and highway safety."
options = {
    'a': (70, 30),
    'b': (40, 60),
    'c': (30, 70),
    'd': (50, 50)
}

prompt = f"""The National Highway Safety Commission is deciding how to allocate its budget between two safety research programs: 
i) improving automobile safety (bumpers, body, gas tank configurations, seatbelts) and 
ii) improving the safety of interstate highways (guard rails, grading, highway interchanges, and implementing selective reduced speed limits).

They are considering the following options:

a) Allocate {70}% to auto safety and {30}% to highway safety
b) Allocate {40}% to auto safety and {60}% to highway safety
c) Allocate {30}% to auto safety and {70}% to highway safety
d) Allocate {50}% to auto safety and {50}% to highway safety

Your own views: {views}

Please choose your most preferred option in light of your views a, b, c or d:"""




#mistralai/-demo-mistral-7b-instruct-v0.1