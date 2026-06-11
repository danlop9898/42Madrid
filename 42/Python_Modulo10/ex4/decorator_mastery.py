from typing import Callable, Any
import time
from functools import wraps


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Spell completed in {end - start:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any]
]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any]
]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)

                except Exception:

                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after {max_attempts}"
                            " attempts"
                        )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    attempt = {"count": 0}

    @retry_spell(3)
    def unstable_spell() -> str:
        attempt["count"] += 1
        if attempt["count"] < 3:
            raise Exception("Fail")
        return "Waaaaaaagh spelled!"

    print(unstable_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))

    mage = MageGuild()

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
