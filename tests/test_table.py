import pytest

from teaching.table import sort_markdown_table

@pytest.mark.parametrize(
    'table, sort_column, expected',
    [
        (
            '''| English | Slovenšcina |
|---------|-------------|
| variable | spremenljivka |
| intersection | presek |
''',
            'English',
            '''| English | Slovenšcina |
|---------|-------------|
| intersection | presek |
| variable | spremenljivka |
'''
        ),
        (
            '''| English | Slovenšcina |
|---------|-------------|
| Variable | spremenljivka |
| intersection | presek |
''',
            'English',
            '''| English | Slovenšcina |
|---------|-------------|
| intersection | presek |
| Variable | spremenljivka |
'''
        )
    ]
)
def test_sort_markdown_table(table, sort_column, expected):
    res = sort_markdown_table(table, sort_column)

    assert res == expected
