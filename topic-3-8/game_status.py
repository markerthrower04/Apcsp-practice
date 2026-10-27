"""Game Status: refactor render_status without changing its behavior."""
def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def make_bar(value, maximum):
    filled = value * 10 // maximum
    bar = "["
    for position in range(10):
        if position < filled:
            bar += "#"
        else:
            bar += "-"
    return bar + "]"


def make_meter_line(label, value, maximum):
    shown_value = clamp(value, 0, maximum)
    bar = make_bar(shown_value, maximum)
    return label + "  " + bar + " " + str(shown_value) + "/" + str(maximum)


def format_time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    text = str(minutes) + ":"
    if remainder < 10:
        text += "0"
    return text + str(remainder)


def total_score(scores):
    total = 0
    for score in scores:
        total += score
    return total


def highest_score(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest


def count_strong_scores(scores):
    count = 0
    for score in scores:
        if score >= 80:
            count += 1
    return count


def choose_level(total):
    if total < 100:
        return "Rookie"
    if total < 250:
        return "Skilled"
    return "Expert"


def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.

    health_line = make_meter_line("Health", health, 100)
    energy_line = make_meter_line("Energy", energy, 60)

    elapsed_text = format_time(elapsed_seconds)
    best_text = format_time(best_seconds)

   
    total = total_score(scores)
    highest = highest_score(scores)
    strong_count = count_strong_scores(scores)
    level = choose_level(total)

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\n" + health_line
    report = report + "\n" + energy_line
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))
