


import argparse
from dataclasses import dataclass
import sys


mode_setting_map = {
    'relaxed': {
        'min-read-len': 1000,
        'min-identity': 0.8,
        'min-span': 0.7
    },
    'normal': {
        'min-read-len': 2000,
        'min-identity': 0.8,
        'min-span': 0.8
    },
    'strict': {
        'min-read-len': 5000,
        'min-identity': 0.9,
        'min-span': 0.9
    },
}

@dataclass
class Settings:
    paf_path: str
    min_read_len: int
    min_identity: float
    min_span: float


def namespace_to_settings(args: argparse.Namespace) -> Settings:
    if args.mode:
        preset = mode_setting_map[args.mode]
        return Settings(
            paf_path = args.paf,
            min_read_len = int(preset['min-read-len']),
            min_identity = preset['min-identity'],
            min_span = preset['min-span']
        )
    else:
        return Settings(
            paf_path = args.paf,
            min_read_len = args.min_read_len,
            min_identity = args.min_identity,
            min_span = args.min_span
        )

    
def parse_args() -> Settings:
    parser = argparse.ArgumentParser(
        description='Summarise read alignments per organism from PAF file'
    )
    parser.add_argument("-l",
                        "--min-read-len", 
                        default=2000,
                        help="[int] min length of reads to summarise. alignments of reads shorter than this value are ignored", 
                        type=int)
    parser.add_argument("-i",
                        "--min-identity", 
                        default=0.8,
                        help="[float] min percent similarity between aligned read and reference. alignments with lower alignment identity are ignored", 
                        type=float)
    parser.add_argument("-s",
                        "--min-span", 
                        default=0.8,
                        help="[float] min alignment span size, in terms of read length (percentage). reads with aligned portion less than --min-identity percent of the read length are ignored", 
                        type=float)
    parser.add_argument("-m",
                        "--mode", 
                        help="[str] preset mode - either relaxed, normal, or strict. governs -l, -i, and -s. \n\
                        relaxed: -l 1000 -i 0.8 -s 0.7\n\
                        normal: -l 2000 -i 0.8 -s 0.8\n\
                        strict: -l 5000 -i 0.9 -s 0.9\n", 
                        type=str)
    parser.add_argument("-p",
                        "--paf", 
                        help="Input paf file path", 
                        required=True,
                        type=str)
    args = parser.parse_args(sys.argv[1:])
    return namespace_to_settings(args)


