import unittest

import soundwarning


class WebwatcherTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_sound(self):
        soundwarning.ObvestiloZvok.predvajaj(self)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()


