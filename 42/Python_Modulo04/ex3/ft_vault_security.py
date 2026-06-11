def secure_archive(
    filename: str,
    mode: str = "read",
    content: str | None = None
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename, "r") as f:
                data = f.read()
            return True, data

        elif mode == "write":
            with open(filename, "w") as f:
                f.write(content if content is not None else "")
            return True, "Content successfully written to file"

        else:
            return False, "Invalid mode"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result = secure_archive("new_file.txt", "write", "Test content")
    print(result)


if __name__ == "__main__":
    main()
