def check_substring(main_string: str):
    i = 0
    match_counter = 0
    while i < len(main_string) - 2:
        if main_string[i:i + 3] == "010" or main_string[i:i + 3] == "101":
            match_counter += 1
            i += 3
        else:
            i += 1
    return match_counter
