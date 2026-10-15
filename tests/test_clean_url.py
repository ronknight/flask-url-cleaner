import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

BASE = "https://www.4sgm.com/search.jhtm"


def clean(url: str) -> str:
    return app.test_client().post("/clean_url", json={"url": url}).json["cleaned_url"]


def test_double_question_mark_is_not_kept() -> None:
    assert clean(BASE + "??keywords=toys&csrfToken=abc") == BASE + "?keywords=toys"


def test_question_mark_after_ampersand() -> None:
    assert clean(BASE + "?csrfToken=abc&?keywords=toys") == BASE + "?keywords=toys"


def test_param_glued_to_csrf_token_survives() -> None:
    assert clean(BASE + "?csrfToken=abc?keywords=toys&sort=") == BASE + "?keywords=toys&sort="


def test_blank_params_dropped_but_sort_kept() -> None:
    assert clean(BASE + "?csrfToken=abc&sort=&brand=") == BASE + "?sort="


def test_only_csrf_token_leaves_no_question_mark() -> None:
    assert clean(BASE + "?csrfToken=abc") == BASE


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
