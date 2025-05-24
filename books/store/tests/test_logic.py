from store.logic import operations


class TestCaseLogic():
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_plus(self):
        result = operations(6, 13, '+')
        assert result == 19

    def test_minus(self):
        result = operations(6, 13, '-')
        assert result == -7

    def test_multiply(self):
        result = operations(6, 13, '*')
        assert result == 78

