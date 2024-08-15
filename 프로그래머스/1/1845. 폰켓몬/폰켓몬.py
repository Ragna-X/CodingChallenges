def solution(nums):
    unique_pokemon_count = len(set(nums))
    max_pokemon_count = len(nums) // 2
    return min(unique_pokemon_count, max_pokemon_count)