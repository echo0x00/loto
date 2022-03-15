import pytest
from user import User, UserStatus, UserType


class TestPlayer:
    @pytest.mark.parametrize("player_type",[
        UserType.HUMAN,
        UserType.COMPUTER,
    ])
    def test_player_type(self, player_type):
        player = User(player_type, "Тестовый")
        assert player.type == player_type

    def test_player_name(self):
        player_name = "Тестовый"
        player = User(UserType.HUMAN, player_name)
        assert player.name == player_name

    def test_player_status_input_wrong_keg(self):
        player = User(UserType.HUMAN, "TestPlayer")
        player.strike_out(100)
        assert player.status == UserStatus.LOST
