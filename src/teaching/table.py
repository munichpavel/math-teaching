def sort_markdown_table(table, sort_column):
    lines = table.strip().split('\n')

    # Parse header
    header = lines[0]
    separator = lines[1]
    data_rows = lines[2:]

    # Extract column names
    columns = [col.strip() for col in header.split('|')[1:-1]]

    # Find the index of the sort column
    sort_index = columns.index(sort_column)

    # Parse data rows
    parsed_rows = []
    for row in data_rows:
        cells = [cell.strip() for cell in row.split('|')[1:-1]]
        parsed_rows.append(cells)

    # Sort rows by the specified column
    sorted_rows = sorted(parsed_rows, key=lambda x: (x[sort_index].lower(), x[sort_index]))

    # Rebuild the table
    result_lines = [header, separator]
    for row in sorted_rows:
        result_lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(result_lines) + '\n'


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('--sort-column', type=str, required=True)
    parser.add_argument('--table-text', type=str, default=None)
    parser.add_argument('--table-path', type=str, default="_markdown-table.md")
    parser.add_argument('--output-path', type=str, default=None, help='Output file (default: stdout)')
    args = parser.parse_args()

    if args.table_path:
        with open(args.table_path, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()

    sorted_table = sort_markdown_table(table=text, sort_column=args.sort_column)

    if args.output_path:
        with open(args.output_path, 'w') as f:
            f.write(sorted_table)
    else:
        print(sorted_table)
