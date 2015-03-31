from app.pattern import Pattern
from app.pattern import MPattern


def test_pattern():
    sequence = [5, 0]
    pattern = Pattern(sequence)

    assert pattern.sequence == sequence
    assert pattern.cursor == 0
    assert pattern.next_level() == 5
    assert pattern.cursor == 1
    assert pattern.next_level() == 0
    assert pattern.cursor == 0
    assert pattern.next_level() == 5

    pattern.sequence.append(10)
    pattern.next_level()
    assert pattern.next_level() == 10


def test_m_pattern():
    first_seq = [100, 10]
    second_seq = [5, 50]

    mpattern = MPattern([Pattern(first_seq), Pattern(second_seq)])

    assert mpattern.next_levels() == [100, 5]
    assert mpattern.next_levels() == [10, 50]
    assert mpattern.next_levels() == [100, 5]
