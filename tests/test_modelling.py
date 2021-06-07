import psico.modelling
from pymol import cmd


def test_update_align():
    cmd.reinitialize()
    cmd.fab("CDEGGGGGGKRC", "m1")
    cmd.fab("CDEAAKRC", "m2")
    psico.modelling.update_align("m1", "m2")
    assert (cmd.get_coords("/m1///1-3") == cmd.get_coords("/m2///1-3")).all()
    assert (cmd.get_coords("/m1///10-") == cmd.get_coords("/m2///6-8")).all()
    assert 6 < cmd.get_distance("/m1///6/N", "/m1///5/C")


def test_sculpt_homolog():
    cmd.reinitialize()
    cmd.fab("CDEGGGGGGKRC", "m1")
    cmd.fab("CDEAAKRC", "m2")
    psico.modelling.sculpt_homolog("m1", "m2", cycles=10)
    assert (cmd.get_coords("/m1///1-3") == cmd.get_coords("/m2///1-3")).all()
    assert (cmd.get_coords("/m1///10-") == cmd.get_coords("/m2///6-8")).all()
    assert 6 > cmd.get_distance("/m1///6/N", "/m1///5/C")


# def mutate(selection, new_resn, inplace=0, sculpt=0, hydrogens='auto', mode=0, quiet=1):
# def mutate_all(selection, new_resn, inplace=1, sculpt=0, *args, **kwargs):
# def sculpt_relax(selection, backbone=1, neighbors=0, model=None, cycles=100,
# def add_missing_atoms(selection='all', cycles=200, quiet=1):
# def peptide_rebuild(name, selection='all', cycles=1000, state=1, quiet=1):
# def get_seq(selection, chainbreak='/', unknown='A'):
# def peptide_rebuild_modeller(name, selection='all', hetatm=0, sequence=None,
