"""Simple statistics for hobby sessions."""


def total_minutes(sessions):
    """Return the total duration of all sessions in minutes."""
    return sum(sessions)


def average_minutes(sessions):
    """Return the average session duration, or 0.0 for an empty list."""
    if not sessions:
        return 0.0
    return total_minutes(sessions) / len(sessions)


def main():
    """Print statistics for a sample week."""
    week = [30, 45, 60, 20]
    print(f"Total: {total_minutes(week)} min")
    print(f"Average: {average_minutes(week):.1f} min")


if __name__ == "__main__":
    main()
