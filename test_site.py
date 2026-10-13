
from pathlib import Path
import unittest

PROJECT_DIR = Path(__file__).resolve().parent


class WebsiteTests(unittest.TestCase):

    def setUp(self):
        self.html = (PROJECT_DIR / "index.html").read_text(
            encoding="utf-8"
        )

    def test_page_has_correct_title(self):
        self.assertIn(
            "<title>CloudDeploy | CI/CD Portfolio</title>",
            self.html
        )

    def test_page_links_stylesheet(self):
        self.assertIn('href="styles.css"', self.html)

    def test_page_has_main_heading(self):
        self.assertIn("From code to cloud.", self.html)


if __name__ == "__main__":
    unittest.main()
