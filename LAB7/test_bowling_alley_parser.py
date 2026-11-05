from hypothesis import given, strategies as st
from bowling_alley_parser import format_player_name, parse_frame, parse_scoreboard

@given(st.text() | st.none())
def test_format_player_name_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_frame_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_scoreboard_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass
