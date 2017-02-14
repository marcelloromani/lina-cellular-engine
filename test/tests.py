import unittest
from liblina import CellState, GOLEvolutionModel

class GOLModelTests(unittest.TestCase):

    def test_die_from_underpopulation(self):
        """
        Any live cell with fewer than two live neighbours dies
        """
        self.assertEqual(GOLEvolutionModel.evolve(CellState.ALIVE, 0), CellState.DEAD)
        self.assertEqual(GOLEvolutionModel.evolve(CellState.ALIVE, 1), CellState.DEAD)

    def test_remain_alive(self):
        """
        Any live cell with two or three live neighbours lives on to the next generation.
        """
        self.assertEqual(GOLEvolutionModel.evolve(CellState.ALIVE, 2), CellState.ALIVE)
        self.assertEqual(GOLEvolutionModel.evolve(CellState.ALIVE, 3), CellState.ALIVE)

    def test_die_from_overpopulation(self):
        """
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        """
        for neighbourCount in range(4, 10):
            self.assertEqual(GOLEvolutionModel.evolve(CellState.ALIVE, neighbourCount), CellState.DEAD)

    def test_birth(self):
        """
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        self.assertEqual(GOLEvolutionModel.evolve(CellState.DEAD, 3), CellState.ALIVE)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
