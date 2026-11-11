"""Lab 6: statement coverage tests for the bowling alley application."""

import pytest

from bowling_alley import frame_score, lane_assignment, lane_cost


def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900


def test_weekend_large_group_with_league_discount():
    assert lane_cost("weekend", 2, 5, 2, True) == 1200


@pytest.mark.parametrize(
    "booking,message",
    [
        (("unknown", 1, 2, 0, False), "unknown day type"),
        (("weekday", 0, 2, 0, False), "invalid booking"),
        (("weekday", 1, 2, 3, False), "too many shoe rentals"),
    ],
)
def test_booking_errors(booking, message):
    with pytest.raises(ValueError, match=message):
        lane_cost(*booking)


@pytest.mark.parametrize(
    "first,second,bonus,expected",
    [(3, 4, [], 7), (5, 5, [7], 17), (10, 0, [5, 6], 21)],
)
def test_frame_scores(first, second, bonus, expected):
    assert frame_score(first, second, bonus) == expected


@pytest.mark.parametrize(
    "first,second,message",
    [(-1, 4, "invalid roll"), (7, 4, "invalid frame")],
)
def test_frame_errors(first, second, message):
    with pytest.raises(ValueError, match=message):
        frame_score(first, second, [])


@pytest.mark.parametrize(
    "players,kids,free,expected",
    [
        (4, False, 0, "wait"),
        (3, True, 2, "bumper lane"),
        (7, False, 2, "two lanes"),
        (7, False, 1, "wait"),
        (4, False, 2, "standard lane"),
    ],
)
def test_lane_assignments(players, kids, free, expected):
    assert lane_assignment(players, kids, free) == expected
