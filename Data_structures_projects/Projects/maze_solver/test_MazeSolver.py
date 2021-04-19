"""
Test took from the CIS2001-Winter2021 github repo
"""


from unittest import TestCase
from maze_solver import Maze_solver


class TestMazeSolver(TestCase):

    def test_solve(self):
        # arrange
        maze = [
            ['S', 'W', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', ' ', 'E'],
        ]
        expected_shorted_path = 8

        # act
        mazeSolver = Maze_solver(maze)
        mazeSolver.solve()
        actual_shorted_path = mazeSolver.shortest_path()

        # assert
        self.assertEqual(expected_shorted_path, actual_shorted_path)

    def test_solve_other_maze(self):
        # arrange
        maze = [
            ['E', 'W', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', ' ', 'S'],
        ]
        expected_shorted_path = 8

        # act
        mazeSolver = Maze_solver(maze)
        mazeSolver.solve()
        actual_shorted_path = mazeSolver.shortest_path()

        # assert
        self.assertEqual(expected_shorted_path, actual_shorted_path)

    def test_solve_other_maze2(self):
        # arrange
        maze = [
            ['S', 'W', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', 'E'],
            [' ', 'W', ' ', ' ', ' '],
        ]
        expected_shorted_path = 7

        # act
        mazeSolver = Maze_solver(maze)
        mazeSolver.solve()
        actual_shorted_path = mazeSolver.shortest_path()

        # assert
        self.assertEqual(expected_shorted_path, actual_shorted_path)

    def test_solve_rectangle(self):
        # arrange
        maze = [
            ['S', 'W', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', 'E', ' '],
            [' ', 'W', ' ', ' ', ' ', ' '],
        ]
        expected_shorted_path = 7

        # act
        mazeSolver = Maze_solver(maze)
        mazeSolver.solve()
        actual_shorted_path = mazeSolver.shortest_path()

        # assert
        self.assertEqual(expected_shorted_path, actual_shorted_path)


    def test_solve_no_walls(self):
        # arrange
        maze = [
            ['S', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'E'],
        ]
        expected_shorted_path = 8

        # act
        mazeSolver = Maze_solver(maze)
        mazeSolver.solve()
        actual_shorted_path = mazeSolver.shortest_path()

        # assert
        self.assertEqual(expected_shorted_path, actual_shorted_path)
