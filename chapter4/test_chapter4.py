from chapter4.to_str import to_str

def test_to_str():
    s = to_str(102, 2)
    assert s == '1100110'