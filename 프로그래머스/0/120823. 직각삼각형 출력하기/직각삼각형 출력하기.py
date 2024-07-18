n = int(input())

def generate_star_pattern(n):
    return "\n".join("*" * i for i in range(1, n+1, 1))

print(generate_star_pattern(n))