from pathlib import Path

from teaching.latex import pdflatex_paths


LATEX_TEST_CONTENT = dict(
    latex_content_a=r"""\documentclass[a4paper,12pt]{article}
\begin{document}
Hello. It's me.
\end{document}
""",
    latex_content_b=r"""\documentclass[a4paper,12pt]{article}
\begin{document}
I've been wondering if after all this time you'd like to meet.
\end{document}
"""
)

def test_pdflatex_paths(tmp_path):
    # Create folder structure
    folder_a = tmp_path / 'folder-a'
    folder_b = tmp_path / 'folder-b'
    folder_a.mkdir()
    folder_b.mkdir()

    # Write content to folder-a/resitve.tex

    (folder_a / 'resitve.tex').write_text(LATEX_TEST_CONTENT['latex_content_a'])

    # Write content to folder-b/resitve.tex

    (folder_b / 'resitve.tex').write_text(LATEX_TEST_CONTENT['latex_content_b'])

    # Create list of latex paths
    latex_paths = [
        folder_a / 'resitve.tex',
        folder_b / 'resitve.tex'
    ]

    # Run the function being tested
    pdflatex_paths(latex_paths=latex_paths)

    # Check that PDFs were created
    pdf_exists_count = 0
    for a_latex_path in latex_paths:
        parent = a_latex_path.parent
        file_stem = a_latex_path.stem
        pdf_path = parent / (file_stem + '.pdf')
        if pdf_path.exists():
            pdf_exists_count += 1

    assert len(latex_paths) == pdf_exists_count
