from LS_toolbox import read_mesh as rm


# Read nodes coordinates from a .k file.
def read_nodes(file_path: str) -> dict:
    """
    Read a .k file and return the nodes coordinates.
    :param file_path: Path to the .k file.
    :return: Dictionary of nodes coordinates {node_id: [x, y, z]}.
    """
    nodes_list = rm.read_nodes(file_path)
    nodes = {}
    for node in nodes_list:
        nodes[node[0]] = node[1:]
    return nodes

def read_keyfile(file_path: str) -> list:
    """
    Read a .k file and return a list of lines.
    :param file_path: Path to the .k file.
    :return: List of lines in the key file.
    """
    with open(file_path, 'r') as f:
        # Read after the line "*KEYWORD"
        for line in f:
            if line.startswith('*KEYWORD'):
                break
        # Read until the line "*END"
        file = []
        for line in f:
            if line.startswith('*END'):
                break
            file.append(line)
    return file

def get_ids(key: str, list_lines) -> list:
    """
    Get the ids of the given key in the .k file.
    :param key: Key.
    :param list_lines: List of lines in the .k file.
    :return: List of ids.
    """
    var_len = 10
    if key in ["*NODE", "*ELEMENT_SOLID"]:
        var_len = 8
    ids = []
    i = 0
    while i < len(list_lines):
        if list_lines[i].startswith(key):
            i += 2
            while not (list_lines[i].startswith("*") or list_lines[i].startswith("$")):
                ids.append(int(list_lines[i][:var_len]))
                i += 1
                if i == len(list_lines):
                    break
        i += 1
    return ids

def read_elements(file_path: str, elements_keyword="ELEMENT_SOLID") -> list:
    """
    Read a .k file and return the elements.
    :param file_path: Path to the .k file.
    :return: List of elements [[element_id, node_id1, node_id2, ...]].
    """
    elements = rm.read_elements(file_path, keyword=elements_keyword)
    return elements
