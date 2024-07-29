def solution(spell, dic):
    sorted_spell = sorted(spell)
    return 1 if any(sorted(string) == sorted_spell for string in dic) else 2