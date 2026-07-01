from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)

    print("\n=== Password Analysis ===")
    print(f"Password: {password}")
    print(f"Strength Score: {result['score']}/4")
    print(f"Estimated Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")

    if result['feedback']['warning']:
        print("Warning:", result['feedback']['warning'])

    for suggestion in result['feedback']['suggestions']:
        print("Suggestion:", suggestion)
