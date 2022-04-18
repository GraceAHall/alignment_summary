

from typing import Tuple
from paf.Alignment import Alignment
from startup.cli_args import Settings

from .AlignmentRegister import AlignmentRegister
from .Summary import Summary


def filter_alignments(alignments: list[Alignment], context: Settings) -> list[Alignment]:
    alignments = [al for al in alignments if al.get_read_len() >= context.min_read_len]
    alignments = [al for al in alignments if al.get_identity() >= context.min_identity]
    alignments = [al for al in alignments if al.get_align_block() >= context.min_span]
    return alignments

def select_best_alignment(alignments: list[Alignment]) -> Alignment:
    # retain alignments which are at least half as long as max block
    max_block = max([al.get_align_block() for al in alignments])
    alignments = [al for al in alignments if abs(max_block - al.get_align_block()) < 0.5] 

    # retain alignments with identity within 5% of max identity 
    max_ident = max([al.get_identity() for al in alignments])
    alignments = [al for al in alignments if abs(max_ident - al.get_identity()) < 0.03] 
    alignments.sort(key=lambda x: x.get_align_block(), reverse=True)
    return alignments[0]

def summarise_paf(register: AlignmentRegister, context: Settings, level: str) -> Summary:
    summary = Summary()
    for _, alignments in register.get_entries():
        qc_pass_alignments = filter_alignments(alignments, context)
        if qc_pass_alignments:
            best_alignment = select_best_alignment(qc_pass_alignments)
            organism_name = get_organism_name(best_alignment, level)
            summary.add_alignment_entry(organism_name, best_alignment)
    return summary

def get_organism_name(alignment: Alignment, level: str) -> str:
    if level == 'species':
        return alignment.get_species_name()
    elif level == 'strain':
        return alignment.get_strain_name()
    else:
        raise RuntimeError(f'cannot create summary for {level}')