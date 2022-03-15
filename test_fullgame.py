import pytest
from loto import Game
from user import UserType


@pytest.fixture()
def game(count_players):
    game = Game()
    for index in range(0, count_players):
        game.add_player(UserType.HUMAN, f"Игрок {index}")
    yield game
    game.clear_players()


class TestGame:
    @pytest.mark.parametrize("count_players", [
        1, 2, 5
    ])
    def test_add_player(self, game, count_players):
        assert game.count_players == count_players

    @pytest.mark.parametrize("count_players",  [2, 5])
    def test_clear_player(self, game, count_players):
        game.clear_players()
        assert game.count_players == 0
