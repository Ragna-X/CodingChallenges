def solution(babbling):
    count = 0
    valid_sounds = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        temp_babble = babble
        for sound in valid_sounds:
            temp_babble = temp_babble.replace(sound, "-", 1)
            
        if not temp_babble.replace("-", ""):
            count += 1

    return count