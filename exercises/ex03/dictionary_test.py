"""Unit tests for function skeletons from dictionary.py"""

__author__: str = "730608493"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_1() -> None:
    """Tests a use case for the invert function"""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_use_2() -> None:
    """Tests a second use case for the invert function"""
    assert invert({"apple": "banana", "cherry": "tomato"}) == {
        "banana": "apple",
        "tomato": "cherry",
    }


def test_invert_edge() -> None:
    """Tests an edge case for the invert function"""
    assert invert({}) == {}


def test_count_use_1() -> None:
    """Tests a use case for the count function"""
    assert count(["Cadeau", "Davis", "Trimble", "Jackson", "Trimble"]) == {
        "Cadeau": 1,
        "Davis": 1,
        "Trimble": 2,
        "Jackson": 1,
    }


def test_count_use_2() -> None:
    """Tests a use case for the count function"""
    assert count(["apple", "banana", "peach"]) == {"apple": 1, "banana": 1, "peach": 1}


def test_count_edge() -> None:
    """Tests an edge case for the count function"""
    assert count([]) == {}


def test_favorite_color_use_1() -> None:
    """Tests a use case for the favorite_color function"""
    assert favorite_color({"Bob": "green", "Sue": "pink", "Dave": "pink"}) == "pink"


def test_favorite_color_use_2() -> None:
    """Tests a use case for the favorite_color function"""
    assert (
        favorite_color(
            {"sally": "gray", "sylvia": "orange", "rhiannon": "gray", "peeta": "orange"}
        )
        == "gray"
    )


def test_favorite_color_edge() -> None:
    """Tests an edge case for the favorite_color function"""
    assert favorite_color({}) == ""


def test_bin_len_use_1() -> None:
    """Tests a use case for the bin_len function"""
    assert bin_len(["March", "April", "May", "June"]) == {
        5: {"March", "April"},
        3: {"May"},
        4: {"June"},
    }


def test_bin_len_use_2() -> None:
    """Tests a use case for the bin_len function"""
    assert bin_len(["comp", "110", "unc"]) == {4: {"comp"}, 3: {"110", "unc"}}


def test_bin_len_edge() -> None:
    """Tests an edge case for the bin_len function"""
    assert bin_len([]) == {}
