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
        members_word_form = self.__determine_word_form("member", num_files_in_group)

        group_header = f"Group '{group_name}': {num_files_in_group} {members_word_form}."
        group_header_with_frame = self.__frame_line(group_header)

        group_results.append(group_header_with_frame)

    def __determine_word_form(self, word: str, number: int) -> str:
        if number > 1:
            word = f"{word}s"

        return word

    def __frame_line(self, line: str) -> str:
        line_length = len(line)
        line_frame = f"{line_length * '-'}"
        line_with_frame = f"{line_frame}\n{line}\n{line_frame}\n"

        return line_with_frame

    def __compose_file_list(self, files: List['Path'], group_results: List[str], num_files_in_group: int) -> None:
        title = "Files:\n"

        if num_files_in_group == 1:
            title = "File:\n"

        group_results.append(title)

        for file in files:
            group_results.append(f"{str(file)}\n")

        group_results.append("\n")
