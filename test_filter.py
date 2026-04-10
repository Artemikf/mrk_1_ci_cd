import pytest
from main import filter_lines

@pytest.fixture
def sample_files(tmp_path):
    """Фікстура створює тимчасовий вхідний файл з вмістом."""
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "filtered.txt"
    return input_file, output_file

@pytest.mark.parametrize("content, keyword, expected_lines", [
    (["hello world\n", "python is great\n", "hello again\n"], "hello", ["hello world\n", "hello again\n"]),
    (["line one\n", "line two\n", "third line\n"], "two", ["line two\n"]),
    (["no match\n", "nothing here\n"], "xyz", []),
    (["Case Sensitive\n", "case sensitive\n"], "Case", ["Case Sensitive\n"]),
    ([], "any", []),
])
def test_filter_lines(sample_files, content, keyword, expected_lines):
    input_file, output_file = sample_files
    # Записуємо тестовий вміст у вхідний файл
    input_file.write_text("".join(content), encoding='utf-8')

    filter_lines(str(input_file), str(output_file), keyword)

    result = output_file.read_text(encoding='utf-8')
    assert result == "".join(expected_lines)

def test_file_not_found():
    """Перевірка реакції на відсутній вхідний файл."""
    with pytest.raises(FileNotFoundError):
        filter_lines("nonexistent.txt", "out.txt", "test")