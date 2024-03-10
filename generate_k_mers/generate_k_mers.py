def generate_k_mers(sequence: str, k: int, start: int = 0, stop: int = 100) -> list:
    k_mer_list = []
    for pos in range(len(sequence))