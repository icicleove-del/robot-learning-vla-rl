"""纯 Python 标准库测试，无下载、无训练、无外部依赖。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from robot_learning.action_queue import ToyActionQueue


class ToyActionQueueTests(unittest.TestCase):
    def test_chunk_order(self):
        q = ToyActionQueue()
        q.replace_chunk([0.1, 0.2, 0.3])
        self.assertEqual(len(q), 3)
        self.assertAlmostEqual(q.next_action(), 0.1)
        self.assertAlmostEqual(q.next_action(), 0.2)
        self.assertAlmostEqual(q.next_action(), 0.3)
        self.assertEqual(len(q), 0)

    def test_replan_replaces_old_chunk(self):
        q = ToyActionQueue()
        q.replace_chunk([1, 2, 3])
        q.next_action()
        q.replace_chunk([9, 10])
        self.assertEqual(q.next_action(), 9)
        self.assertEqual(q.next_action(), 10)

    def test_empty_chunk_raises(self):
        q = ToyActionQueue()
        with self.assertRaises(IndexError):
            q.next_action()


if __name__ == "__main__":
    unittest.main()
