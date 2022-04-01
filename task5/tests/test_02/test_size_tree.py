import os.path
import pathlib
import tempfile


from tree_utils_02.size_tree import SizeTree, FileSizeNode


def test_tree_empty():
    with tempfile.TemporaryDirectory() as dirname:
        base = os.path.basename(dirname)
        assert (
            SizeTree().get(dirname, dirs_only=False) ==
            FileSizeNode(name=base, is_dir=True, children=[], size=4096)
        )


def test_filter_empty_nodes():
    with tempfile.TemporaryDirectory() as dirname:
        base = os.path.basename(dirname)

        pathlib.Path(f'{dirname}/x').touch()
        pathlib.Path(f'{dirname}/subdir').mkdir()

        tree = SizeTree()
        node_root = tree.get(dirname, dirs_only=False)    
        node_subdir, node_x = node_root.children
        assert node_subdir.name == 'subdir'
        assert node_x.name == 'x'

        assert tree.filter_empty_nodes(
            node_root, dirname
        ) is None