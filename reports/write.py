
from typing import Any

"""
stats[organism]['num_alignments'] = data.num_primary_alignments
stats[organism]['avg_identity'] = data.get_avg_identity()
stats[organism]['avg_block'] = data.get_avg_block()
"""

def write_console(report: list[dict[str, Any]]):
    header = f'{"organism":40}{"alignments":>14}{"avg_identity":>14}{"avg_block":>11}'
    print('REPORT ---------------')
    print(header)
    for org in report:
        line = f'{org["organism"]:40}{org["num_alignments"]:>14}{org["avg_identity"]:>14.2f}{org["avg_block"]:>11.2f}'
        print(line)