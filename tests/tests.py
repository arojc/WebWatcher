import unittest
import misc_lib
import soundwarning
from data_man import data_man


class WebwatcherTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_sound(self):
        soundwarning.ObvestiloZvok.predvajaj(self)
        self.assertTrue(True)

    def test_save(self):
        misc_lib.set_text_searched("hudo")
        kraj = misc_lib.get_text_searched()
        self.assertEqual(kraj, "hudo")
        misc_lib.set_text_searched("radomlje")
        kraj = misc_lib.get_text_searched()
        self.assertEqual(kraj, "radomlje")

    # def test_data_man(self):
    #     data = data_man()
    #     watch_list = {}
    #     watch_list["name"] = ["url", "kobcina"]
    #     data.set_data(watch_list)
    #     watch_list1 = data.get_data()
    #     self.assertEqual(len(watch_list1), 1)
    #     self.assertEqual(len(watch_list1["name"]), 2)


if __name__ == '__main__':
    unittest.main()


