import Code.Tetris as Tetris
import pytest


@pytest.fixture
def test_Piece__init__():
    piece1 = Tetris.Piece()
    assert piece1.x == 100
    assert piece1.y == 100
    assert piece1.shape == 'S'

def test_Create_Grid():
    test_Grid = Tetris.create_grid()
    print(test_Grid[0][0])
    assert test_Grid[0][0] == (0,0,0)
    assert len(test_Grid) == 20
    assert len(test_Grid[0]) == 10