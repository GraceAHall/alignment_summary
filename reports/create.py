

from typing import Any
from paf.Summary import Summary

def create_report(summary: Summary) -> list[dict[str, Any]]:
    stats: dict[str, dict[str, Any]] = {}
    for organism, data in summary.organism_data.items():
        stats[organism] = {}
        stats[organism]['organism'] = organism
        stats[organism]['num_alignments'] = data.num_primary_alignments
        stats[organism]['avg_identity'] = data.get_avg_identity()
        stats[organism]['avg_block'] = data.get_avg_block()
    
    out: list[dict[str, Any]] = list(stats.values())
    out.sort(key=lambda x: x['num_alignments'], reverse=True)
    return out
