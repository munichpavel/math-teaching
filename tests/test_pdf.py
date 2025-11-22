from pathlib import Path

from pypdf import PdfReader
import pytest

from teaching.pdf import (
    write_folder_ddmmyy_sorted_concatenated_pdf,
    order_parent_folders_ddmmyy,
    order_ddmmyy, #order_ddmmyy_w_extra,
    write_concatenated_pdf
)

TEST_DATA_DIR = Path(__file__).parent / 'data'


def test_write_folder_date_sorted_concatenated_pdf(tmp_path):

    target_dir = tmp_path / 'out'
    target_dir.mkdir()
    target_path = target_dir / 'concatenated.pdf'

    pdf_paths = [
        TEST_DATA_DIR / a_folder / 'content.pdf'
        for a_folder in [
            '030101', '010199', '020100', # have expected pdf file
            '040102'  # empty
        ]
    ]

    write_folder_ddmmyy_sorted_concatenated_pdf(sources=pdf_paths, target=target_path, folder_extra=None)

    expected = [
        'This is a story',
        'On the playground, is where I’d spend most of my days.'
    ]

    print(target_path, '\n\n')
    first_last_lines = get_first_last_pdf_lines(target_path=target_path)
    assert first_last_lines == expected


def get_first_last_pdf_lines(target_path: Path) -> list[str]:
    reader = PdfReader(target_path)

    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text()

    lines = [line.strip() for line in all_text.split('\n') if line.strip()]
    for a_line in lines:
        print(a_line)
    first_line = lines[0]
    last_line = lines[-1]

    return [first_line, last_line]


@pytest.mark.parametrize(
    'left, right, expected',
    [
        (Path('a/010100/0.pdf'), Path('b/010100/1.pdf'), 0),
        (Path('b/010100/0.pdf'), Path('b/010100/1.pdf'), 0),
        (Path('a/010100/1.pdf'), Path('b/010100/0.pdf'), 0),
        (Path('b/010100/1.pdf'), Path('a/010100/0.pdf'), 0),
        (Path('a/010100/file.pdf'), Path('b/010101/file.pdf'), 1),
        (Path('a/010101/file.pdf'), Path('b/010100/file.pdf'), -1),
        (Path('a/010199/file.pdf'), Path('b/101000/file.pdf'), 1),
        (Path('a/010100/file.pdf'), Path('b/101099/file.pdf'), -1),
    ]
)
def test_order_parent_folders_ddmmyy(left, right, expected):
    ordering = order_parent_folders_ddmmyy(left, right)

    assert ordering == expected


# @pytest.mark.parametrize(
#     'left, right, extra, expected',
#     [
#         ('010100a', '010100a', 'a', 0),
#         ('010100b', '010101b', 'b', 1),
#         ('010101c', '010100c', 'c', -1),
#         # ('010199', '101000', 1),
#         # ('010100', '101099', -1),
#     ]
# )
# def test_order_ddmmyy_w_extra(left, right, extra, expected):
#     ordering = order_ddmmyy_w_extra(left, right, extra=extra)

#     assert ordering == expected

@pytest.mark.parametrize(
    'left, right, expected',
    [
        ('010100', '010100', 0),
        ('010100', '010101', 1),
        ('010101', '010100', -1),
        ('010199', '101000', 1),
        ('010100', '101099', -1),
    ]
)
def test_order_ddmmyy(left, right, expected):
    ordering = order_ddmmyy(left, right)

    assert ordering == expected


def test_write_concatenated_pdf(tmp_path):
    target_dir = tmp_path / 'out'
    target_dir.mkdir()
    target_path = target_dir / 'concatenated.pdf'

    pdf_paths = [TEST_DATA_DIR / 'pdf-content-0.pdf', TEST_DATA_DIR / 'pdf-content-1.pdf']

    write_concatenated_pdf(sources=pdf_paths, target=target_path)


    n_source_pages = 0
    for a_path in pdf_paths:
        source_pdf = PdfReader(a_path)
        n_source_pages += len(source_pdf.pages)
    res = PdfReader(target_path)
    n_target_pages = len(res.pages)

    assert n_source_pages == n_target_pages
