import pytest

from sheetfu import TableSelector


class TestTableSelector:

    def test_or_clause(self, table):
        selector = TableSelector(table.items, [[{"name": "jane"}, {"name": "john"}]])
        values = selector.execute()
        assert len(values) == 2

    def test_and_clause_list_and_dict(self, table):
        selector = TableSelector(table.items, [{"age": 25}, [{"name": "john"}]])
        values = selector.execute()
        assert len(values) == 1

    def test_and_clause_list_of_dict(self, table):
        selector = TableSelector(table.items, [{"name": 'philippe'}, {"surname": 'oger'}])
        values = selector.execute()
        assert len(values) == 1

    def test_and_clause_dict(self, table):
        selector = TableSelector(table.items, {"name": 'jane', "age": 25})
        values = selector.execute()
        assert len(values) == 1

    def test_empty_select(self, table):
        selector = TableSelector(table.items, [{"age": 25}, [{"name": "phillipe"}]])
        values = selector.execute()
        assert len(values) == 0

    def test_value_error_exception(self, table):
        with pytest.raises(ValueError):
            TableSelector(table.items, [[25, 35]]).execute()
