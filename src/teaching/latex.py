from pathlib import Path
import subprocess

def pdflatex_paths(latex_paths: list[Path], timeout: int = 10) -> None:
    n_paths = len(latex_paths)
    failed_paths = []

    for idx, a_latex_path in enumerate(latex_paths):
        print(f"Processing {idx+1}/{n_paths}: {a_latex_path}")

        try:
            result = subprocess.run([
                'pdflatex',
                '-interaction=nonstopmode',
                a_latex_path
            ], capture_output=True, cwd=a_latex_path.parent, timeout=timeout)

            # Check if compilation failed
            if result.returncode != 0:
                stdout = result.stdout.decode()

                # Check for common signs of missing files
                if 'File' in stdout and 'not found' in stdout:
                    print(f"⚠️  Missing files detected: {a_latex_path}")
                    failed_paths.append((a_latex_path, "Missing files"))
                else:
                    print(f"⚠️  Compilation error: {a_latex_path}")
                    failed_paths.append((a_latex_path, "Compilation error"))

        except subprocess.TimeoutExpired:
            print(f"⏱️  TIMEOUT - pdflatex hung (likely waiting for input): {a_latex_path}")
            failed_paths.append((a_latex_path, "Timeout - waiting for input"))

        if (idx + 1) % 10 == 0:
            print(f'Finished {idx+1} of {n_paths} pdflatex jobs')

    # Print summary of failed paths
    if failed_paths:
        print("\n" + "="*60)
        print("SUMMARY OF FAILED COMPILATIONS:")
        print("="*60)
        for path, reason in failed_paths:
            print(f"  {reason}: {path}")
        print("="*60)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--latex-paths', type=str, required=True)
    args = parser.parse_args()

    latex_path_strs = ','.split(args.latex_paths)
    latex_paths = [Path(a_path_str) for a_path_str in latex_path_strs]
    pdflatex_paths(latex_paths)
