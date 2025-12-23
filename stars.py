"""Simple script to print ten stars in a row."""

STAR_COUNT = 10


def build_stars(count: int = STAR_COUNT) -> str:
    """Return a string containing `count` star characters."""
    if count < 0:
        raise ValueError("count must be non-negative")
    return "*" * count


def main() -> None:
    print(build_stars())


if __name__ == "__main__":
    main()
