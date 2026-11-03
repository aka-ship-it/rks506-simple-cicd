import pytest


@pytest.mark.parametrize("path", [
    "/static/games/snake.html",
    "/static/games/minesweeper.html",
    "/static/games/2048.html",
])
def test_game_pages(path):
    client = app.test_client()
    response = client.get(path)
    assert response.status_code == 200
    response.close()
