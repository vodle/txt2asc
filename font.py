class metal:
    met_a = [
        "  ___  ",
        " / _ \\ ",
        "/ /_\\ \\",
        "|  _  |",
        "| | | |",
        "\\_| |_/"
        ]
    met_b = [
        "______ ",
        "| ___ \\",
        "| |_/ /",
        "| ___ \\",
        "| |_/ /",
        "\\____/ "
        ]
    met_c = [
        " _____ ",
        "/  __ \\",
        "| /  \\/",
        "| |    ",
        "| \\__/\\",
        " \\____/"
        ]
    met_d = [
        "______ ",
        "|  _  \\",
        "| | | |",
        "| | | |",
        "| |/ / ",
        "|___/  "
        ]
    met_e = [
        " _____ ",
        "|  ___|",
        "| |__  ",
        "|  __| ",
        "| |___ ",
        "\\____/ "
        ]
    met_f = [
        "______ ",
        "|  ___|",
        "| |_   ",
        "|  _|  ",
        "| |    ",
        "\\_|    "
        ]
    met_g = [
        " _____ ",
        "|  __ \\",
        "| |  \\/",
        "| | __ ",
        "| |_\\ \\",
        "\\____/ "
        ]
    met_h = [
        " _   _ ",
        "| | | |",
        "| |_| |",
        "|  _  |",
        "| | | |",
        "\\_| |_/"
        ]
    met_i = [
        " _____ ",
        "|_   _|",
        "  | |  ",
        "  | |  ",
        " _| |_ ",
        " \\___/ " 
        ]
    met_j = [
        "   ___ ",
        "  |_  |",
        "    | |",
        "    | |",
        "/\\__/ /",
        "\\____/ "
    ]
    met_k = [
        " _   __",
        "| | / /",
        "| |/ / ",
        "|    \\ ",
        "| |\\  \\",
        "\\_| \\_/" 
        ]
    met_l = [
        " _     ",
        "| |    ",
        "| |    ",
        "| |    ",
        "| |____",
        "\\_____/" 
        ]
    met_m = [
        "___  ___",
        "|  \\/  |",
        "| .  . |",
        "| |\\/| |",
        "| |  | |",
        "\\_|  |_/" 
        ]
    met_n = [
        " _   _ ",
        "| \\ | |",
        "|  \\| |",
        "| . ` |",
        "| |\\  |",
        "\\_| \\_/" 
        ]
    met_o = [
        " _____ ",
        "|  _  |",
        "| | | |",
        "| | | |",
        "\\ \\_/ /",
        " \\___/ " 
        ]
    met_p = [
        "______ ",
        "| ___ \\",
        "| |_/ /",
        "|  __/ ",
        "| |    ",
        "\\_|    " 
        ]
    met_q = [
        " _____ ",
        "|  _  |",
        "| | | |",
        "| | | |",
        "\\ \\/' /",
        " \\_/\\_\\" 
        ]
    met_r = [
        "______ ",
        "| ___ \\",
        "| |_/ /",
        "|    / ",
        "| |\\ \\ ",
        "\\_| \\_|" 
        ]
    met_s = [
        " _____ ",
        "/  ___|",
        "\\ `--. ",
        " `--. \\",
        "/\\__/ /",
        "\\____/ " 
        ]
    met_t = [
        " _____ ",
        "|_   _|",
        "  | |  ",
        "  | |  ",
        "  | |  ",
        "  \\_/  " 
        ]
    met_v = [
        " _   _ ",
        "| | | |",
        "| | | |",
        "| | | |",
        "\\ \\_/ /",
        " \\___/ " 
        ]
    met_u = [
        " _   _ ",
        "| | | |",
        "| | | |",
        "| | | |",
        "| |_| |",
        " \\___/ "
    ]
    met_w = [
        " _    _ ",
        "| |  | |",
        "| |  | |",
        "| |/\\| |",
        "\\  /\\  /",
        " \\/  \\/ "
    ]
    met_x = [
        "__   __",
        "\\ \\ / /",
        " \\ V / ",
        " /   \\ ",
        "/ /^\\ \\",
        "\\/   \\/" 
        ]
    met_y = [
        "__   __",
        "\\ \\ / /",
        " \\ V / ",
        "  \\ /  ",
        "  | |  ",
        "  \\_/  " 
        ]
    met_z = [
        " ______",
        "|___  /",
        "   / / ",
        "  / /  ",
        "./ /___",
        "\\_____/" 
        ]
    met_prob = [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ]
def call_letter(letter):
    if letter == "a":
        return metal.met_a
    if letter == "b":
        return metal.met_b
    if letter == "c":
        return metal.met_c
    if letter == "d":
        return metal.met_d
    if letter == "e":
        return metal.met_e
    if letter == "f":
        return metal.met_f
    if letter == "g":
        return metal.met_g
    if letter == "h":
        return metal.met_h
    if letter == "i":
        return metal.met_i
    if letter == "j":
        return metal.met_j
    if letter == "k":
        return metal.met_k
    if letter == "l":
        return metal.met_l
    if letter == "n":
        return metal.met_n
    if letter == "m":
        return metal.met_m
    if letter == "o":
        return metal.met_o
    if letter == "p":
        return metal.met_p
    if letter == "q":
        return metal.met_q
    if letter == "r":
        return metal.met_r
    if letter == "s":
        return metal.met_s
    if letter == "t":
        return metal.met_t
    if letter == "v":
        return metal.met_v
    if letter == "u":
        return metal.met_u
    if letter == "w":
        return metal.met_w
    if letter == "x":
        return metal.met_x
    if letter == "y":
        return metal.met_y
    if letter == "z":
        return metal.met_z
    if letter == " " or "":
        return metal.met_prob



