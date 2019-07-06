import pathlib


cwd = pathlib.Path.cwd()
phps = cwd.rglob("*.php")
groups = {}

for php in phps:
    php_content = php.read_text()
    php_content_lines = php_content.splitlines()
    for line in php_content_lines:
        group_annotation_pos = line.find("@group")
        if group_annotation_pos > -1:
            group_pos = group_annotation_pos + 7
            group = line[group_pos:]
            if group not in groups:
                groups[group] = [php]
            else:
                groups[group].append(php)

for group_name, phps in groups.items():
    group_num = len(phps)
    print(f"{group_name}: {group_num} in total, in the files: {phps}")
