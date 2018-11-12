class TestLogin:

    def setup(self):
        print("setup")
        assert 1

    def teardown(self):
        print("teardown")
        assert 1

    def setup_class(self):
        print("setup_class")
        assert 0