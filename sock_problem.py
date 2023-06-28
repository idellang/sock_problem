from collections import Counter


def socks_problem_solution(C=None, D=None, K=None):
    # count socks
    clean_socks = Counter(C)
    dirty_socks = Counter(D)
    clean_extra = []

    # find pairs in the clean socks and separate those without pairs

    for sock in clean_socks:
        if clean_socks[sock] % 2 == 1:
            # add to clean_extra
            clean_extra.append(sock)
            # remove from list of clean socks
            clean_socks[sock] -= 1

    clean_extra = Counter(clean_extra)

    # find pairs for clean extra from dirty socks
    for sock in dirty_socks:
        if K > 0 and sock in clean_extra:
            # wash and add to clean extra
            clean_extra[sock] += 1
            dirty_socks[sock] -= 1
            K -= 1

    # wash pair from remaining socks remaining socks
    number_of_washes = K//2
    washed_socks = []

    for sock in dirty_socks:
        # get number of pairs
        number_of_pairs = dirty_socks[sock] // 2
        while number_of_pairs > 0 and number_of_washes > 0:
            # add the sock with the pair
            washed_socks.append(sock)
            washed_socks.append(sock)
            # remove from dirty socks
            dirty_socks[sock] -= 2
            K -= 2

            # reduce number of washes and number of pairs
            number_of_pairs -= 1
            number_of_washes -= 1

    washed_socks = Counter(washed_socks)

    clean_socks.update(clean_extra)
    clean_socks.update(washed_socks)

    total_clean_pairs = sum(v for k, v in clean_socks.items()) // 2
    return total_clean_pairs


if __name__ == "__main__":
    K = 2
    C = [1, 2, 1, 1]
    D = [1, 4, 3, 2, 4]

    solution = socks_problem_solution(C, D, K)
    print(solution)
