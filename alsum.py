

from startup import parse_args
from paf import read_paf, summarise_paf
from reports import create_report, write_console


def main():
    context = parse_args()
    register = read_paf(context)
    stats = summarise_paf(register, context)
    report = create_report(stats)
    write_console(report)


if __name__ == '__main__':
    main()