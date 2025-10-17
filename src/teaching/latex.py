from pathlib import Path
import subprocess

def pdflatex_paths(latex_paths: list[Path]) -> None:
    for a_latex_path in latex_paths:
        subprocess.run([
            'pdflatex', a_latex_path
        ], capture_output=True, cwd=a_latex_path.parent)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--latex-paths', type=str, required=True)
    args = parser.parse_args()

    latex_path_strs = ','.split(args.latex_paths)
    latex_paths = [Path(a_path_str) for a_path_str in latex_path_strs]
    pdflatex_paths(latex_paths)
