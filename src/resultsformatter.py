from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class ResultsFormatter:
    def display_results(self, results_source: Dict[str, List['Path']]):
        results_formatted = []

        for group_name, files in results_source.items():
            group_results = []

            group_num = len(files)
            group_header = "-----------\n" \
                           f"Group '{group_name}': {group_num} members.\n" \
                           "-----------\n"
            group_results.append(group_header)

            if group_num == 1:
                group_results.append(f"File: {files[0]}\n")
            else:
                group_results.append("Files:\n")
                for file in files:
                    group_results.append(f"{str(file)}\n")

            results_formatted.append("".join(group_results))

        return "".join(results_formatted)
