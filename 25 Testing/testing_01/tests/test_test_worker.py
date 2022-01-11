from test_worker import Worker
import unittest


class TestWorker(unittest.TestCase):
    name = 'Test Worker'
    salary = 1000
    energy = 10

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init_correct_values(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_rest(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_work_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_work_raise_values(self):
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_work_energy_decreased(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f"{self.name} has saved 0 money.", self.worker.get_info())


if __name__ == '__main__':
    unittest.main()