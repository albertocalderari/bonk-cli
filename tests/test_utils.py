from bonkcli.actions.utils import build_and_sort_categories


def test_build_and_sort_categories(fake_meme_folder):
    category_score = {"Comunist": 5, "Cope": 7, "Demilitarize": 0}
    actual = build_and_sort_categories(category_score, fake_meme_folder)
    expected = ["Cope", "Comunist", "Demilitarize"]
    assert actual ==expected