from collections import defaultdict, Counter


def product_addition_order_stats(carts):
    """
    carts: list of ShoppingCart objects
    For each product, determine the product most commonly added before it.
    """

    pair_counts = defaultdict(Counter)

    for cart in carts:
        # Go through items in the order they were added
        for i in range(1, len(cart.items)):
            prev_item = cart.items[i - 1].id
            current_item = cart.items[i].id
            pair_counts[current_item][prev_item] += 1

    results = {}

    for product_id, counter in pair_counts.items():
        most_common_prev, count = counter.most_common(1)[0]
        results[product_id] = {
            "added_after": most_common_prev,
            "occurrences": count,
        }

    return results
