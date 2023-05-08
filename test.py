from main import solution
import unittest


class TestSolution(unittest.TestCase):
    def test_case_0(self):
        references = [1, 2, 3, 5, 4, 2]
        expected = ("ABC*A-", 5)
        self.assertEqual(solution(references), expected)

    def test_case_1(self):
        references = [1, 2, 3, 2, 4, 3, 2, 1]
        expected = ("ABC-A--B", 5)
        self.assertEqual(solution(references), expected)

    def test_case_2(self):
        references = [1, 2, 3, 3, 4, 5, 2, 1]
        expected = ("ABC-ABC*", 7)
        self.assertEqual(solution(references), expected)

    def test_case_3(self):
        references = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        expected = ("ABC*AB-CA", 8)
        self.assertEqual(solution(references), expected)

    def test_case_4(self):
        references = [-5, 2, 5, 3, 2, 1, -3]
        expected = ("AB-C-A-", 4)
        self.assertEqual(solution(references), expected)

    def test_case_5(self):
        references = [1, 2, 3, 4, 1, 5, 1, 3, 6, 3]
        expected = ("ABC*-B--CB", 7)
        self.assertEqual(solution(references), expected)