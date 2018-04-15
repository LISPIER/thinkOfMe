import os


def view(pattern=None,
         character=None, sentence=None,
         scene=None, describe=None,
         action=None,
         backGroundMusic=None,backGroundImage=None):
    os.system("clear")
    if pattern == "say":
        print("{character}:{sentence}".format(
            character=character,
            sentence=sentence
        )
        )
    elif pattern == "scene":
        print("{scene}:{describe}".format(
            scene=scene,
            describe=describe
        )
        )
    elif pattern == "action":
        print("{action}".format(
            action=action
        )
        )
    input()
    os.system("clear")