from misc.am_i_free import Schedule


def test_am_i_free():
    sc = Schedule()
    assert sc.get_free_days() == []
