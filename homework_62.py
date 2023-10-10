import pytest

from homework54 import Vector

def test_vector_init():
    v = Vector(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3

def test_vector_equality():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 2, 3)

    assert v1 == v3
    assert v1 != v2

def test_vector_call():
    v = Vector(1, 2, 3)
    result = v()
    assert result.x == 2
    assert result.y == 4
    assert result.z == 6


if __name__ == '__main__':
    pytest.main()