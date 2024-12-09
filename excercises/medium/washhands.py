def hand_washing_duration(N, nM):
    total_washes = N * nM * 30
    total_seconds = total_washes * 21
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes} minutes and {seconds} seconds"



print(hand_washing_duration(8,7))

    