import mock

from dining_philosophers import main
# from dining_philosophers.main import main, init, Table


class TestMain:
    def test_main_should_start_dining(self):
        with mock.patch('dining_philosophers.main.Table') as mock_start_dining:
            main.main()

        mock_start_dining.assert_called_once()

    @mock.patch.object(main, "__name__", "__main__")
    def test_init(self):
        with mock.patch.object(main, 'main') as mock_main:
            main.init()

        mock_main.assert_called_once()
