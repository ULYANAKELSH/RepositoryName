class Tree:
    def __init__(self, species: str, height: float, has_fruit: bool):
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self._species = species
        self.height = height
        self.has_fruit = has_fruit

    def __str__(self) -> str:
        return f"Дерево: вид - {self._species}, высота - {self.height} м, плодоносит - {self.has_fruit}"

    def __repr__(self) -> str:
        return f"Tree(species='{self._species}', height={self.height}, has_fruit={self.has_fruit})"

    def grow(self, years: int) -> None:
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным.")
        self.height += years * 0.5
        print(f"Дерево {self._species} выросло за {years} лет. Новая высота: {self.height} м")

    def get_species(self) -> str:
        return self._species

class ConiferousTree(Tree):
    def __init__(self, species: str, height: float, has_fruit: bool, needles_color: str):
        super().__init__(species, height, has_fruit)
        if not isinstance(needles_color, str):
            raise ValueError("Цвет хвои должен быть строкой.")
        self.needles_color = needles_color

    def __str__(self) -> str:
        return f"{super().__str__()} (цвет хвои: {self.needles_color})"

    def __repr__(self) -> str:
        return f"ConiferousTree(species='{self._species}', height={self.height}, has_fruit={self.has_fruit}, needles_color='{self.needles_color}')"

    def grow(self, years: int, sunlight: int) -> None:
        if not 1 <= sunlight <= 5:
            raise ValueError("Количество солнечного света должно быть от 1 до 5.")
        growth_rate = 0.5 + (sunlight - 3) * 0.1
        self.height += years * growth_rate
        print(f"Хвойное дерево {self._species} выросло за {years} лет при солнечном свете {sunlight}. Новая высота: {self.height} м")

    def shed_needles(self) -> None:
        if self.height > 5:
            needles_shed = self.height * 0.05
            print(f"С хвойного дерева {self._species} опало {needles_shed:.2f} м хвои.")
        else:
            print(f"Хвоя с дерева {self._species} не опадает, т.к. оно молодое")

