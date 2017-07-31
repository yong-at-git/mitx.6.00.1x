from unittest import TestCase
import ps7


class TestMITCampus(TestCase):
    """
    c.add_tent() should return True
c.add_tent(Location(1,2)) should return True
c.add_tent(Location(0,0)) should return False
c.add_tent(Location(2,3)) should return False
c.get_tents() should return ['<0,0>', '<1,2>', '<2,3>']
    """
    def test_add_tent_1(self):
        center_loc = ps7.Location(0,0)
        campus = ps7.MITCampus(center_loc)

        loc = ps7.Location(2, 3)

        self.assertTrue(campus.add_tent(loc))

    def test_add_tent_2(self):
        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        campus.add_tent(ps7.Location(2,3))

        loc = ps7.Location(1,2)

        self.assertTrue(campus.add_tent(loc))

    def test_add_tent_3(self):
        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        campus.add_tent(ps7.Location(2, 3))
        campus.add_tent(ps7.Location(1, 2))

        loc = ps7.Location(0,0)

        self.assertFalse(campus.add_tent(loc))

    def test_add_tent_4(self):
        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        campus.add_tent(ps7.Location(2, 3))
        campus.add_tent(ps7.Location(1, 2))
        campus.add_tent(ps7.Location(0, 0))

        loc = ps7.Location(2, 3)

        self.assertFalse(campus.add_tent(loc))

    def test_remove_tent_ok(self):
        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        new_tent = ps7.Location(2, 3)

        campus.add_tent(new_tent)

    def test_remove_tent_except(self):
        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        non_exist_tent = ps7.Location(2, 3)

        with self.assertRaises(ValueError):
            campus.remove_tent(non_exist_tent)

    def test_get_tents(self):

        center_loc = ps7.Location(0, 0)
        campus = ps7.MITCampus(center_loc)

        campus.add_tent(ps7.Location(2, 3))
        campus.add_tent(ps7.Location(1, 2))
        campus.add_tent(ps7.Location(0, 0))

        expected = ['<0,0>', '<1,2>', '<2,3>']
        actual = campus.get_tents()

        self.assertListEqual(expected, actual)

    def test_get_tests(self):
        c = ps7.MITCampus(ps7.Location(1, 2), ps7.Location(0, 1))
        c.add_tent(ps7.Location(-1, 2))
        c.add_tent(ps7.Location(1, -10))
        c.add_tent(ps7.Location(1, 10))
        c.add_tent(ps7.Location(1, 20))
        c.add_tent(ps7.Location(1, 40))

        expected = ['<-1,2>', '<0,1>', '<1,-10>', '<1,10>', '<1,20>', '<1,40>']

        self.assertListEqual(expected, c.get_tents())
