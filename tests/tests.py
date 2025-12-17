import unittest

import misc_lib
import soundwarning


class WebwatcherTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_sound(self):
        soundwarning.ObvestiloZvok.predvajaj(self)
        self.assertTrue(True)

    def test_save(self):
        misc_lib.save("hudo")
        kraj = misc_lib.load()
        self.assertEqual(kraj, "hudo")
        misc_lib.save("radomlje")
        kraj = misc_lib.load()
        self.assertEqual(kraj, "radomlje")


if __name__ == '__main__':
    unittest.main()


