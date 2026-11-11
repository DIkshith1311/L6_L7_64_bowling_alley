"""Lab 6: decision outcomes and boundary tests for the bowling alley."""

import pytest

from bowling_alley import frame_score, lane_assignment, lane_cost


@pytest.mark.parametrize(
    "day,games,players,shoes,member,expected",
    [
        ("weekday", 1, 1, 0, False, 400),
        ("weekday", 2, 4, 2, False, 900),
        ("weekend", 2, 5, 2, True, 1200),
        ("weekend", 3, 6, 4, False, 2300),
        ("weekday", 1, 5, 1, True, 440),
    ],
)
def test_booking_decisions(day, games, players, shoes, member, expected):
    assert lane_cost(day, games, players, shoes, member) == expected


@pytest.mark.parametrize(
    "booking,message",
    [
        (("unknown", 1, 2, 0, False), "unknown day type"),
        (("weekday", 0, 2, 0, False), "invalid booking"),
        (("weekday", 1, 0, 0, False), "invalid booking"),
        (("weekday", 1, 7, 0, False), "invalid booking"),
        (("weekday", 1, 2, 3, False), "too many shoe rentals"),
    ],
)
def test_booking_validation_decisions(booking, message):
    with pytest.raises(ValueError, match=message):
        lane_cost(*booking)


@pytest.mark.parametrize(
    "first,second,bonus,expected",
    [
        (0, 0, [], 0),
        (3, 4, [], 7),
        (5, 5, [7], 17),
        (0, 10, [0], 10),
        (10, 0, [5, 6], 21),
        (10, 0, [10, 10], 30),
    ],
)
def test_frame_decisions(first, second, bonus, expected):
    assert frame_score(first, second, bonus) == expected


@pytest.mark.parametrize(
    "first,second,message",
    [
        (-1, 4, "invalid roll"),
        (11, 0, "invalid roll"),
        (7, -1, "invalid roll"),
        (7, 4, "invalid frame"),
    ],
)
def test_frame_validation_decisions(first, second, message):
    with pytest.raises(ValueError, match=message):
        frame_score(first, second, [])


@pytest.mark.parametrize(
    "players,kids,free,expected",
    [
        (4, False, 0, "wait"),
        (3, True, 0, "wait"),
        (3, True, 2, "bumper lane"),
        (7, False, 2, "two lanes"),
        (7, False, 1, "wait"),
        (6, False, 1, "standard lane"),
        (4, False, 2, "standard lane"),
    ],
)
def test_assignment_decisions(players, kids, free, expected):
    assert lane_assignment(players, kids, free) == expected
