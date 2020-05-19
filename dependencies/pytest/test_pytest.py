import pytest

class TestPyTest:

    def test_version(self):
        self.assertEqual(pytest.__version__, '5.4.1')


if __name__ == '__main__':
    TestPyTest().test_version()