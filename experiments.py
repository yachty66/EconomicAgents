scenarios = dict({
    "Berk29": ((400, 400), (750, 400)),
    "Barc2": ((400, 400), (750, 375)),
    "Berk23": ((800, 200), (0, 0)),
    "Barc8": ((300, 600), (700, 500)),
    "Berk15": ((200, 700), (600, 600)),
    "Berk26":((0, 800), (400, 400))
    })

def play():
    #store results left/right
    results = {}
    #iter over all scenarios and send requests to openai
    for scenario, allocations in scenarios.items():
        left_a, left_b = allocations[0]
        right_a, right_b = allocations[1]
        print(scenario)
        print(left_a)
        print(left_b)
        print(right_a)
        print(right_b)
        break





play()