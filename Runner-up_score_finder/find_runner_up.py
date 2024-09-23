def find_runner_up(scores):
    """
    This function takes a list of scores as input and returns the runner-up score.

    Args:
        scores (list): A list of scores

    Returns:
        int: The runner-up score
    """
    # Check if the input list is empty
    if not scores:
        return None

    # Remove duplicates by converting the list to a set
    unique_scores = set(scores)

    # Check if there is only one unique score
    if len(unique_scores) == 1:
        return None

    # Sort the unique scores in descending order
    sorted_scores = sorted(unique_scores, reverse=True)

    # Return the second highest score (runner-up)
    return sorted_scores[1]

# Example usage:
scores = [10, 20, 30, 20, 10, 40, 30, 20]
runner_up = find_runner_up(scores)
print("Runner-up score:", runner_up)