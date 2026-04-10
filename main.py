


def filter_lines(input_file: str, output_file: str, keyword: str) -> None:
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {input_file} не знайдено")

    filtered = [line for line in lines if keyword in line]

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(filtered)
    except IOError as e:
        raise IOError(f"Помилка запису у файл {output_file}: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Використання: python filter_lines.py <вхідний.txt> <вихідний.txt> <ключове_слово>")
        sys.exit(1)
    try:
        filter_lines(sys.argv[1], sys.argv[2], sys.argv[3])
        print(f"Готово. Відфільтровані рядки збережено у {sys.argv[2]}")
    except Exception as e:
        print(f"Помилка: {e}")
        sys.exit(1)