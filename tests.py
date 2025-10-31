from functions.get_files_info import get_files_info
import unittest

class TestFunctions(unittest.TestCase):
    
    def test_check_current(self):
        expected_result = f"Result for current directory:\n - main.py: file_size=719 bytes, is_dir=False\n - tests.py: file_size=1331 bytes, is_dir=False\n - pkg: file_size=44 bytes, is_dir=True"
        actual_result = get_files_info("calculator", ".")
        self.assertEqual(actual_result, expected_result)
    
    def test_check_PKG(self):
        expected_result = f"Result for 'pkg' directory:\n - calculator.py: file_size=1721 bytes, is_dir=False\n - render.py: file_size=376 bytes, is_dir=False"
        actual_result = get_files_info("calculator", "pkg")
        self.assertEqual(actual_result, expected_result)

    def test_check_bin(self):
        expected_result = f"Result for '/bin' directory:\n    Error: Cannot list \"/bin\" as it is outside the permitted working directory"
        actual_result = get_files_info("calculator", "/bin")
        self.assertEqual(actual_result, expected_result)

    def test_outside_of_working_directory(self):
        expected_result = f"Result for '../' directory:\n    Error: Cannot list \"../\" as it is outside the permitted working directory"
        actual_result = get_files_info("calculator", "../")
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()