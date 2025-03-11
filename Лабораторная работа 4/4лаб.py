class Tree:
    """Базовый класс для представления дерева с основными характеристиками."""
    
    def __init__(self, species: str, height: float, has_fruit: bool):
        """
        Инициализирует экземпляр дерева.
        
        Args:
            species (str): Вид/название дерева
            height (float): Высота дерева в метрах (должна быть > 0)
            has_fruit (bool): Плодоносит ли дерево
            
        Raises:
            ValueError: Если высота <= 0
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self._species = species
        self.height = height
        self.has_fruit = has_fruit

    def __str__(self) -> str:
        """Возвращает понятное строковое представление объекта для пользователя."""
        return f"Дерево: вид - {self._species}, высота - {self.height} м, плодоносит - {self.has_fruit}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление объекта для разработчика."""
        return f"Tree(species='{self._species}', height={self.height}, has_fruit={self.has_fruit})"

    def grow(self, years: int) -> None:
        """
        Симулирует рост дерева в течение заданного количества лет.
        
        Args:
            years (int): Количество лет роста (неотрицательное число)
            
        Raises:
            ValueError: Если years < 0
        """
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным.")
        self.height += years * 0.5
        print(f"Дерево {self._species} выросло за {years} лет. Новая высота: {self.height} м")

    def get_species(self) -> str:
        """Возвращает вид дерева (геттер для защищенного атрибута)."""
        return self._species


class ConiferousTree(Tree):
    """Класс для представления хвойных деревьев, наследуется от базового класса Tree."""
    
    def __init__(self, species: str, height: float, has_fruit: bool, needles_color: str):
        """
        Инициализирует экземпляр хвойного дерева.
        
        Args:
            needles_color (str): Цвет хвои
            Остальные параметры см. в документации Tree
            
        Raises:
            ValueError: Если цвет хвои не является строкой
        """
        super().__init__(species, height, has_fruit)
        if not isinstance(needles_color, str):
            raise ValueError("Цвет хвои должен быть строкой.")
        self.needles_color = needles_color

    def __str__(self) -> str:
        """Добавляет информацию о цвете хвои к базовому строковому представлению."""
        return f"{super().__str__()} (цвет хвои: {self.needles_color})"

    def __repr__(self) -> str:
        """Формальное представление с дополнительным параметром needles_color."""
        return f"ConiferousTree(species='{self._species}', height={self.height}, has_fruit={self.has_fruit}, needles_color='{self.needles_color}')"

    def grow(self, years: int, sunlight: int) -> None:
        """
        Переопределенный метод роста с учетом уровня солнечного света.
        
        Args:
            years (int): Количество лет роста
            sunlight (int): Уровень солнечного света (1-5 баллов)
            
        Raises:
            ValueError: Если sunlight вне диапазона 1-5
        """
        if not 1 <= sunlight <= 5:
            raise ValueError("Количество солнечного света должно быть от 1 до 5.")
        growth_rate = 0.5 + (sunlight - 3) * 0.1
        self.height += years * growth_rate
        print(f"Хвойное дерево {self._species} выросло за {years} лет при солнечном свете {sunlight}. Новая высота: {self.height} м")

    def shed_needles(self) -> None:
        """
        Симулирует процесс опадания хвои.
        Количество опавшей хвои зависит от высоты дерева.
        """
        if self.height > 5:
            needles_shed = self.height * 0.05
            print(f"С хвойного дерева {self._species} опало {needles_shed:.2f} м хвои.")
        else:
            print(f"Хвоя с дерева {self._species} не опадает, т.к. оно молодое")