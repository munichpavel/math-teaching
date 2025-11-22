from pathlib import Path
from datetime import datetime
import functools

from pypdf import PdfWriter


def write_folder_ddmmyy_sorted_concatenated_pdf(
    sources: list[Path], target: Path, folder_extra: str | None
) -> None:

    def order_parent_folders_ddmmyy_w_extra(left_path: Path, right_path: Path) -> int:
        left_parent_folder = left_path.parent.name
        right_parent_folder = right_path.parent.name

        return order_ddmmyy_w_extra(left_parent_folder, right_parent_folder)


    def order_ddmmyy_w_extra(left: str, right: str) -> int:
        """Most recent to oldest"""
        left_sans_extra = left.replace(folder_extra, '')
        right_sans_extra = right.replace(folder_extra, '')
        res = order_ddmmyy(left=left_sans_extra, right=right_sans_extra)
        return res


    if folder_extra:
        sorted_sources = sorted(sources, key=functools.cmp_to_key(order_parent_folders_ddmmyy_w_extra))
    else:
        sorted_sources = sorted(sources, key=functools.cmp_to_key(order_parent_folders_ddmmyy))

    write_concatenated_pdf(sources=sorted_sources, target=target)


def order_parent_folders_ddmmyy(left_path: Path, right_path: Path) -> int:
    left_parent_folder = left_path.parent.name
    right_parent_folder = right_path.parent.name

    return order_ddmmyy(left_parent_folder, right_parent_folder)


def order_ddmmyy(left: str, right: str) -> int:
    """Most recent to oldest"""
    date_format = '%d%m%y'
    date_left = datetime.strptime(left, date_format)
    date_right = datetime.strptime(right, date_format)

    if date_left < date_right:
        res = 1
    elif date_left > date_right:
        res = -1
    else:
        res = 0
    return res



def write_concatenated_pdf(sources: list[Path], target: Path) -> None:
    concatenator = PdfWriter()

    for a_source_path in sources:
        if a_source_path.exists():
            concatenator.append(a_source_path)

    concatenator.write(target)

