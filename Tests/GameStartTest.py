import pytest
from unittest.mock import patch, MagicMock
from main import main


@pytest.fixture
def mock_game():
    with patch('main.Game') as MockGame:
        instance = MockGame.return_value
        yield instance


def test_main_starts_game(mock_game):
    with patch('pygame.init') as mock_init, patch('pygame.quit') as mock_quit:
        main()

        mock_init.assert_called_once()

        mock_game.assert_called_once()

        mock_game.run.assert_called_once()

        mock_quit.assert_called_once()
