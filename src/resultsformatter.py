from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class ResultsFormatter:
    def format_group_results(self, results_source: Dict[str, List['Path']]) -> str:
        results_formatted = []

        for group_name, files in results_source.items():
            group_results = []
            num_files_in_group = len(files)

            self.__compose_header(group_name, num_files_in_group, group_results)

            self.__compose_file_list(files, group_results, num_files_in_group)

            results_formatted.append(
                "".join(group_results)
            )

        return "".join(results_formatted)

    def __compose_header(self, group_name: str, num_files_in_group: int, group_results: List[str]) -> None:
        group_header = "-----------\n" \
                       f"Group '{group_name}': {num_files_in_group} members.\n" \
                       "-----------\n"
        group_results.append(group_header)

    def __compose_file_list(self, files: List['Path'], group_results: List[str], num_files_in_group: int) -> None:
        if num_files_in_group == 1:
            group_results.append(f"File: {files[0]}\n")
            return

        group_results.append("Files:\n")

        for file in files:
            group_results.append(f"{str(file)}\n")
