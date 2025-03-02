

class PhysicalObject:
    """
    Abstract class describing a physical object.

    Attributes:
        mass (float): Mass of the object in kilograms. Must be positive.
        volume (float): Volume of the object in cubic meters. Must be positive.
        name (str): Name of the object.
    """

    def __init__(self, mass: float, volume: float, name: str):
        """
        Constructor for the PhysicalObject class.

        Args:
            mass (float): Mass of the object in kilograms.
            volume (float): Volume of the object in cubic meters.
            name (str): Name of the object.

        Raises:
            ValueError: If mass or volume are not positive.
        """
        if mass <= 0:
            raise ValueError("Mass must be positive.")
        if volume <= 0:
            raise ValueError("Volume must be positive.")

        self.mass = mass
        self.volume = volume
        self.name = name

    def calculate_density(self) -> float:
        """
        Calculates the density of the object.

        Returns:
            float: Density of the object in kg/m^3.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.

        Examples:
            >>> obj = PhysicalObject(mass=10.0, volume=2.0, name="Test")
            ...
            NotImplementedError: calculate_density method must be implemented in a subclass.
        """
        raise NotImplementedError("calculate_density method must be implemented in a subclass.")

    def interact_with(self, other_object: "PhysicalObject") -> None:  # type: ignore
        """
        Describes the interaction of the object with another physical object.

        Args:
            other_object (PhysicalObject): The other physical object.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("interact_with method must be implemented in a subclass.")

    def describe(self) -> str:
        """
        Returns a text description of the object.

        Returns:
            str: Description of the object.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("describe method must be implemented in a subclass.")


class DataStructure:
    """
    Abstract class describing a data structure.

    Attributes:
        capacity (int): Maximum capacity of the data structure. Must be positive.
        name (str): Name of the data structure.
    """

    def __init__(self, capacity: int, name: str):
        """
        Constructor for the DataStructure class.

        Args:
            capacity (int): Maximum capacity of the data structure.
            name (str): Name of the data structure.

        Raises:
            ValueError: If capacity is not positive.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.name = name

    def insert(self, any) -> None:  # type: ignore
        """
        Inserts data into the data structure.

        Args:
            data (any): Data to insert.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("insert method must be implemented in a subclass.")

    def remove(self) -> any:  # type: ignore
        """
        Removes data from the data structure.

        Returns:
            any: The removed data.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.

        Examples:
            >>> ds = DataStructure(capacity=10, name="Test")
            ...
            NotImplementedError: remove method must be implemented in a subclass.
        """
        raise NotImplementedError("remove method must be implemented in a subclass.")

    def search(self, key: any) -> any:  # type: ignore
        """
        Searches for data in the data structure.

        Args:
            key (any): The search key.

        Returns:
            any: The found data, or None if nothing is found.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("search method must be implemented in a subclass.")

    def describe(self) -> str:
        """
        Returns a text description of the data structure.

        Returns:
            str: Description of the data structure.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("describe method must be implemented in a subclass.")


class SocialNetwork:
    """
    Abstract class describing a social network.

    Attributes:
        user_count (int): Number of users in the network. Must be non-negative.
        name (str): Name of the social network.
    """

    def __init__(self, user_count: int, name: str):
        """
        Constructor for the SocialNetwork class.

        Args:
            user_count (int): Number of users in the network.
            name (str): Name of the social network.

        Raises:
            ValueError: If user_count is negative.
        """
        if user_count < 0:
            raise ValueError("User count cannot be negative.")

        self.user_count = user_count
        self.name = name

    def add_user(self, user_name: str) -> None:
        """
        Adds a user to the social network.

        Args:
            user_name (str): The name of the user.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("add_user method must be implemented in a subclass.")

    def remove_user(self, user_name: str) -> None:
        """
        Removes a user from the social network.

        Args:
            user_name (str): The name of the user.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("remove_user method must be implemented in a subclass.")

    def create_connection(self, user1: str, user2: str) -> None:
        """
        Creates a connection between two users.

        Args:
            user1 (str): The name of the first user.
            user2 (str): The name of the second user.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("create_connection method must be implemented in a subclass.")

    def describe(self) -> str:
        """
        Returns a text description of the social network.

        Returns:
            str: Description of the social network.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("describe method must be implemented in a subclass.")