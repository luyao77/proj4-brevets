from acp_times import open_time
from acp_times import close_time

import arrow

start = arrow.get("2017-01-01T00:00")


# invalid input

# def test_open_bad_time():
assert (open_time(0, 1200, start) is None)


# def test_close_bad_time():
assert (open_time(0, 1500, start) is None)


# def test_open_control_greater():
assert (open_time(500, 200, start) is None)


# def test_open_control_nagative():
assert (open_time(-100, 200, start) is None)


# def test_close_control_greater():
assert (open_time(250, 200, start) is None)


def test_close_nagative():
    assert (close_time(-100, 200, start) is None)


def check_200():
    assert (close_time(200, 200, start) == start.replace(hours=+ 13, minutes=+30))


def check_300():
    assert (close_time(300, 300, start) == start.replace(hours=+ 20, ))


def check_400():
    assert (close_time(400, 400, start) == start.replace(hours=+ 27))


def check_600():
    assert (close_time(600, 600, start) == start.replace(hours=+ 40))


def check_1000():
    assert (close_time(1000, 1000, start) == start.replace(hours=+ 75))


def check_0():
    assert (close_time(0, 400, start) == start.replace(hours=+ 1))


def test_open_ten():
    assert (open_time(220, 200, start) == open_time(200, 200, start))


def test_close_ten():
    assert (close_time(220, 200, start) == close_time(200, 200, start))
