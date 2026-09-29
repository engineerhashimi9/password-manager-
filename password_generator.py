import random


def generate():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = (
        [random.choice(letters) for i in range(random.randint(8, 10))]
        + [random.choice(symbols) for j in range(random.randint(2, 4))]
        + [random.choice(numbers) for k in range(random.randint(2, 4))]
    )

    random.shuffle(password_list)

    password = "".join(password_list)
    clipboard.copy(password)
    genbtn["text"] = "copied to clipboard"
    genbtn["bg"] = "red"
    pasen.delete(0, "end")
    pasen.insert("end", password)
    # -----------------------------------#
