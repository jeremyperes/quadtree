from __future__ import annotations
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        """
        Créer un QuadTree avec quatre sous-arbres
        :param hg: Sous-arbre haut gauche
        :param hd: Sous-arbre haut droit
        :param bd: Sous-arbre bas droit
        :param bg: Sous-arbre bas gauche
        """
        self.hg = hg
        self.hd = hd
        self.bg = bg
        self.bd = bd

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree
            Liste les profondeurs des sous-arbres sans prendre les sous-arbres nuls
            Retourne la profondeur max des sous-arbres avec la valeur 1 par défaut
        """
        depths = [subtree.depth for subtree in (self.hg, self.hd, self.bd, self.bg) if isinstance(subtree, QuadTree)]
        return max(depths, default=1) + 1

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list
            Lit le fichier et convertit le contenu en une liste de nombres entiers
            Crée une instance de QuadTree avec la liste de nombre entiers
        """
        with open(filename, 'r') as f:
            data_list = f.read().strip().strip('[]')
            data = list(map(int, data_list.split(',')))
            return (data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation
            Divise la liste en quatre parties égales
            Crée les sous-arbres à partir des données
            Retourne le QuadTree avec les sous-arbres créés
        """
        mid = len(data) // 2
        hg_data, hd_data, bd_data, bg_data = data[:mid], data[mid:mid * 2], data[mid * 2:mid * 3], data[mid * 3:]

        hg_tree = QuadTree.fromList(hg_data)
        hd_tree = QuadTree.fromList(hd_data)
        bd_tree = QuadTree.fromList(bd_data)
        bg_tree = QuadTree.fromList(bg_data)

        return QuadTree(hg_tree, hd_tree, bd_tree, bg_tree)

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass