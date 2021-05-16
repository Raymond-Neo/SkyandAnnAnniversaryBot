import requests
joke_bool = False
joke_punchline = ''
joke_setup = ''

def get_joke(boolean):
    if boolean is True:
        global joke_bool, joke_setup, joke_punchline
        resp = requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
        print(resp.json())
        joke_setup = resp.json()['setup']
        joke_punchline = resp.json()['punchline']
        joke_bool = False

def conversation_responses(input_text):
    global joke_bool, joke_setup, joke_punchline
    get_joke(True)
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup", "yo", "good morning", "good afternoon", "baby"):
        return "Hows your day?????????"
    elif user_message in ("good", "happy", "great", "wonderful", "okay", "ok"):
        return "Thats nice! Want to hear a joke?"

    elif user_message in ("bad", "sad", "not good", "horrible"):
        return "Whats wrong? Do you want to hear a joke?"

    elif user_message in ("sure", "okay", "okie", "ok", "yes"):
        return "You HAHAHAAHAHA\n just kidding, is my joke funny?\n please type \"your joke is funny\" to end the joke"

    elif user_message in ("no", "nope", "dw", "nah"):
        return f"You still have to hear the joke: \"{joke_setup}\"\n{joke_punchline}\nyou are now in a loop of jokes," + \
        "please type \"your joke is funny\" to end the loop"

    elif user_message in ("your joke is funny"):
        return f"Thanks, heres another joke: \"{joke_setup}\"\n{joke_punchline}HAHAHAHA\n" + \
        "Okay you can end the joke by typing " + \
        "\"Walk down memry lane\""

    elif user_message in ("walk down memry lane"):
        return "Sike! you can't even spell memory.\nOkay jokes aside, please enter /memories to continue(for real tho)"

    else:
        return "Error message: AHFJDKAFNFKLJFLAFJLAS It means you need to learn english."
