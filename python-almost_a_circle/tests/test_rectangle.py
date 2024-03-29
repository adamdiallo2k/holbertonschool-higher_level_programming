#!/usr/bin/python3
""" Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_rectangle_1(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.id, 1)
    
    def test_rectangle_2(self):
        obj = Rectangle(1, 2, 3)
        self.assertEqual(obj.id, 2)
    
    def test_rectangle_3(self):
        obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(obj.id, 3)
    
    def test_rectangle_4(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)


    def test_rectangle_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.area(), 12)

if __name__ == '__main__':
    unittest.main()
