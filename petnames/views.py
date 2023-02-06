import openai
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request, result=''):
    if request.method == "POST":
        animal = request.POST["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="three names for a " + animal,
            temperature=0.6,
        )
        return redirect(reverse("index", kwargs={"result": response.choices[0].text}))

    return render(request, "index.html", {'result': result})


def _generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
