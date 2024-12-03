#!/usr/bin/python3
import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    line_count = 0
    total_size = 0
    status_codes = defaultdict(int)
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    pattern = r'^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2}'
    r'\d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            try:
                line = line.strip()
                match = re.match(pattern, line)
                if match:
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))
                    if status_code in valid_codes:
                        status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)
            except ValueError:
                continue
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
