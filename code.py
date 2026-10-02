# practice-work4
# Практическая работа №4
# Minimax и Alpha–Beta: сравнение порядка обхода дерева

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
}

payoffs = {
    "H": 2,
    "I": 8,
    "J": 6,
    "K": 4,
    "L": 1,
    "M": 5,
    "N": 9,
    "O": 3,
}


def is_terminal(state):
    return state in payoffs


def utility(state):
    return payoffs[state]


def successors(state, reverse=False):
    if reverse:
        return tree[state][::-1]
    return tree[state]


def minimax(state, maximizing, counter, reverse=False):
    # Считаем каждый вызов, включая терминальные узлы.
    counter[0] += 1

    if is_terminal(state):
        return utility(state)

    values = [
        minimax(child, not maximizing, counter, reverse)
        for child in successors(state, reverse)
    ]

    return max(values) if maximizing else min(values)


def alphabeta(
    state, alpha, beta, maximizing, counter, reverse=False
):
    counter[0] += 1

    if is_terminal(state):
        return utility(state)

    value = float("-inf") if maximizing else float("inf")

    for child in successors(state, reverse):
        child_value = alphabeta(
            child,
            alpha,
            beta,
            not maximizing,
            counter,
            reverse,
        )

        if maximizing:
            value = max(value, child_value)
            alpha = max(alpha, value)
        else:
            value = min(value, child_value)
            beta = min(beta, value)

        if alpha >= beta:
            break

    return value


def main():
    for reverse in (False, True):
        minimax_counter = [0]
        alphabeta_counter = [0]

        minimax_value = minimax(
            "A", True, minimax_counter, reverse
        )

        alphabeta_value = alphabeta(
            "A",
            float("-inf"),
            float("inf"),
            True,
            alphabeta_counter,
            reverse,
        )

        direction = "Справа налево" if reverse else "Слева направо"

        print(f"\nОбход: {direction}")
        print(
            f"Minimax: значение = {minimax_value}, "
            f"вызовов = {minimax_counter[0]}"
        )
        print(
            f"Alpha–Beta: значение = {alphabeta_value}, "
            f"вызовов = {alphabeta_counter[0]}"
        )
        print(
            "Пропущено узлов:",
            minimax_counter[0] - alphabeta_counter[0],
        )

        assert minimax_value == alphabeta_value


if __name__ == "__main__":
    main()
