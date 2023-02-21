import os


def draw_tree(dir_path, output_file):
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(dir_path):
            level = root.replace(dir_path, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(sub_indent, file))


# Example usage:
dir_path = '/users/fanmuchen/downloads/fmc-ai-project/'
output_file = 'file_tree.txt'
draw_tree(dir_path, output_file)
