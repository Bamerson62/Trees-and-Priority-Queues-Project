import unittest
from triage import TriageSystem

class TestTriageSystem(unittest.TestCase):
    def setUp(self):
        self.t = TriageSystem()

    def test_add_and_process_order(self):
        self.t.AddPatient("A", 3)
        self.t.AddPatient("B", 5)
        self.t.AddPatient("C", 5)
        first = self.t.ProcessNext()
        self.assertEqual(first, ("B", 5))
        second = self.t.ProcessNext()
        self.assertEqual(second, ("C", 5))
        third = self.t.ProcessNext()
        self.assertEqual(third, ("A", 3))

    def test_peek_and_size(self):
        self.assertTrue(self.t.IsEmpty())
        self.t.AddPatient("X", 2)
        self.assertFalse(self.t.IsEmpty())
        self.assertEqual(self.t.Size(), 1)
        self.assertEqual(self.t.PeekNext(), ("X", 2))
        self.assertEqual(self.t.Size(), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.t.AddPatient("", 3)
        with self.assertRaises(ValueError):
            self.t.AddPatient("Name", 0)
        with self.assertRaises(ValueError):
            self.t.AddPatient("Name", 6)

if __name__ == "__main__":
    unittest.main()
