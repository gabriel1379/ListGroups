from typing import Generator, List

import pathlib

from filegatherer import FileGatherer


class GroupLister:
    def __init__(self):
        self.__fileGatherer: FileGatherer = FileGatherer()
        self.__groups: dict = {}

    def list_groups(self, from_here: pathlib.Path):
        files = self.__fileGatherer.gather_files(from_here, 'php')
        self.__gather_groups(files)
        self.__display_results()

    def __gather_groups(self, files: 'Generator'):
        for file in files:
            lines = self.__split_to_lines(file)
            self.__process_lines(lines, file)

    def __split_to_lines(self, file: pathlib.Path) -> List[str]:
        content = file.read_text()
        lines = content.splitlines()

        return lines

    def __process_lines(self, lines: List[str], file: pathlib.Path):
        for line in lines:
            annotation_at = line.find("@group")

            if annotation_at > -1:
                group_name = self.__extract_group_name(line, annotation_at)
                self.__record_group(group_name, file)

    def __extract_group_name(self, line: str, annotation_at: int) -> str:
        group_pos = annotation_at + 7
        group_name = line[group_pos:]

        return group_name

    def __record_group(self, group: str, file: pathlib.Path):
        if group not in self.__groups:
            self.__groups[group] = [file]
            return

        self.__groups[group].append(file)

    def __display_results(self):
        for group_name, files in self.__groups.items():
            group_num = len(files)
            print(f"{group_name}: {group_num} in total, in the files: {files}")


if __name__ == '__main__':
    cwd = pathlib.Path.cwd()
    groupLister = GroupLister()

    groupLister.list_groups(cwd)
