

from startup import parse_args
from paf import read_paf, summarise_paf
from reports import create_report, write_console


def main():
    context = parse_args()
    register = read_paf(context)

    for level in ['species', 'strain']:
        stats = summarise_paf(register, context, level)
        report = create_report(stats)
        write_console(report, level)


if __name__ == '__main__':
    main()