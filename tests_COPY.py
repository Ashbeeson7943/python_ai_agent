from functions.get_files_info import get_files_info
import unittest

class TestFunctions(unittest.TestCase):
    
    def test_check_current(self):
        actual_result = get_files_info("calculator", ".")
        for result in actual_result.split("\n")[1:]:
            self.assertTrue(is_valid_entry_format(result))
        print(actual_result)

    def test_check_PKG(self):
        actual_result = get_files_info("calculator", "pkg")
        for result in actual_result.split("\n")[1:]:
            self.assertTrue(is_valid_entry_format(result))
        print(actual_result)

    def test_check_bin(self):
        expected_result = f"Result for '/bin' directory:\n    Error: Cannot list \"/bin\" as it is outside the permitted working directory"
        actual_result = get_files_info("calculator", "/bin")
        self.assertEqual(actual_result, expected_result)
        print(actual_result)

    def test_outside_of_working_directory(self):
        expected_result = f"Result for '../' directory:\n    Error: Cannot list \"../\" as it is outside the permitted working directory"
        actual_result = get_files_info("calculator", "../")
        self.assertEqual(actual_result, expected_result)
        print(actual_result)


# language: python
def is_valid_entry_format(line: str) -> bool:
    # must start with "- "
    if not line.startswith("- "):
        print("not start with: (- )")
        return False

    # split "name: rest"
    if ": " not in line:
        print("No :")
        return False
    name, rest = line[2:].split(": ", 1)
    if not name:  # non-empty filename/dirname
        print("No file name")
        return False

    # expect "file_size=NUMBER bytes, is_dir=BOOL"
    parts = rest.split(", ")
    if len(parts) != 2:
        print("Not enough info")
        return False

    file_size_part, is_dir_part = parts

    if not file_size_part.startswith("file_size=") or not file_size_part.endswith(" bytes"):
        print("File size wrong")
        return False

    # check that the middle is an integer
    num_str = file_size_part[len("file_size="):-len(" bytes")]
    if not num_str.isdigit():
        print("Not valid file size")
        return False

    if not is_dir_part.startswith("is_dir="):
        print("No is_dir")
        return False
    bool_str = is_dir_part[len("is_dir="):]
    if bool_str not in ("True", "False"):
        print("Does not end in true or false")
        return False

    return True


if __name__ == "__main__":
    unittest.main()