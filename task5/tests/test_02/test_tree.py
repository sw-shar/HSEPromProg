import os.path
import pathlib
import tempfile

import pytest

from tree_utils_02.tree import Tree, FileNode


def test_tree_empty():
    with tempfile.TemporaryDirectory() as dirname:
        base = os.path.basename(dirname)
        assert (
            Tree().get(dirname, dirs_only=False) ==
            FileNode(name=base, is_dir=True, children=[])
        )

    #with open('file.txt') as file:  # context manager
    #    s = file.read()


def test_tree_subfile():
    with tempfile.TemporaryDirectory() as dirname:
        base = os.path.basename(dirname)
        pathlib.Path(f'{dirname}/x').touch()
        assert (
            Tree().get(dirname, dirs_only=False) ==
            FileNode(
                name=base, 
                is_dir=True, 
                children=[
                    FileNode(name='x', is_dir=False, children=[])
                ]
            )
        )


def test_tree_etc():
    with tempfile.TemporaryDirectory() as dirname:
        with pytest.raises(AttributeError):
            Tree().get(f'{dirname}/x', dirs_only=False)

    with tempfile.TemporaryDirectory() as dirname:
        pathlib.Path(f'{dirname}/x').touch()
        assert (
            Tree().get(
                f'{dirname}/x', dirs_only=True, recurse_call=True
            ) is None
        )

    with tempfile.TemporaryDirectory() as dirname:
        pathlib.Path(f'{dirname}/x').touch()
        with pytest.raises(AttributeError):
            Tree().get(
                f'{dirname}/x', dirs_only=True, recurse_call=False
            )


def test_filter_empty_nodes():
    with tempfile.TemporaryDirectory() as dirname:
        base = os.path.basename(dirname)

        pathlib.Path(f'{dirname}/x').touch()
        pathlib.Path(f'{dirname}/subdir').mkdir()

        tree = Tree()
        node_root = tree.get(dirname, dirs_only=False)    
        node_subdir, node_x = node_root.children
        assert node_subdir.name == 'subdir'
        assert node_x.name == 'x'

        assert tree.filter_empty_nodes(
            node_root, dirname
        ) is None

