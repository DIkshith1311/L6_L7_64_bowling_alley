def format_player_name(name):
    """Format a player name; use 'Unknown' for missing or invalid names."""
    if not isinstance(name, str):
        return "Unknown"

    name = name.strip()
    return name.title()[:10] if name else "Unknown"


def parse_frame(text):
    """Return a roll tuple for valid notation, or None for invalid input."""
    if not isinstance(text, str):
        return None

    text = text.strip().upper()

    if text == "X":
        return 10, 0

    if len(text) != 2 or text[0] not in "0123456789":
        return None

    first = int(text[0])

    if text[1] == "/":
        return first, 10 - first

    if text[1] not in "0123456789":
        return None

    second = int(text[1])

    if first + second > 10:
        return None

    return first, second


def parse_scoreboard(text):
    """Parse valid name:score entries, skipping malformed entries."""
    if not isinstance(text, str):
        return {}

    scores = {}

    for entry in text.split(","):
        if entry.count(":") != 1:
            continue

        name, score_text = entry.split(":")
        name = name.strip()

        if not name:
            continue

        try:
            score = int(score_text.strip())
        except ValueError:
            continue

        if 0 <= score <= 300:
            scores[name] = score

    return scores


def main():
    print("==== Running format_player_name ====")
    value = input("Enter a player name for the scoreboard: ")
    print("Scoreboard name:", format_player_name(value))

    print("\n==== Running parse_frame ====")
    value = input(
        "Enter a frame as X (strike), 7/ (spare) "
        "or two digits (e.g. 45): "
    )
    result = parse_frame(value)

    if result is None:
        print("Invalid frame. Use X, 7/ or two digits totaling at most 10.")
    else:
        print("Pins (first roll, second roll):", result)

    print("\n==== Running parse_scoreboard ====")
    value = input(
        "Enter scores as NAME:SCORE separated by commas "
        "(e.g. Asha:150,Ravi:132): "
    )
    print("Scoreboard:", parse_scoreboard(value))


if __name__ == "__main__":
    main()