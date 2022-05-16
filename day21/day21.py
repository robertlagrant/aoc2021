from raw_input import p1_start, p2_start


def play_game(track_length=10, die_sides=100, score_limit=1000):
    p1_pos = p1_start
    p2_pos = p2_start
    p1_score = 0
    p2_score = 0
    p1_turn = True
    die_roll_count = 0
    die = 0
    while max(p1_score, p2_score) < score_limit:
        die_roll_1 = (die + 1) % die_sides
        die_roll_2 = (die_roll_1 + 1) % die_sides
        die_roll_3 = (die_roll_2 + 1) % die_sides
        die = die_roll_3
        die_roll_count += 3

        if p1_turn:
            p1_pos = (p1_pos + die_roll_1 + die_roll_2 + die_roll_3) % track_length
            p1_score += track_length if p1_pos == 0 else p1_pos
        else:
            p2_pos = (p2_pos + die_roll_1 + die_roll_2 + die_roll_3) % track_length
            p2_score += track_length if p2_pos == 0 else p2_pos

        p1_turn = not p1_turn

    return min(p1_score, p2_score) * die_roll_count


print(f"Part 1: {play_game()}")

