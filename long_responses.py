import random

R_EATING = "I don't like eating anything because I'm not hungry !"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?",
                "yes i have eaten"][
        random.randrange(4)]
    return response