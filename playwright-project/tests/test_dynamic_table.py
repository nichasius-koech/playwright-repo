import time


class TestLogin:
    """Dynamic Table TestSuite."""
    def test_headers(self, dyn_table):
        """Verify Table Headers are as expected."""
        assert (sorted(dyn_table.get_table_headers()) ==
                sorted(["Name","Memory","CPU","Disk","Network"]))

    def test_chrome_cpu_value(self, dyn_table):
        """Verify Chrome CPU Value is correct."""
        assert dyn_table.get_table_chrome_cpu_val() == dyn_table.get_actual_chrome_cpu_val()