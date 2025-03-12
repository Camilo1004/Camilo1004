class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def set_width(self, width: float) -> None:
        self.__width = width

    def set_height(self, height: float) -> None:
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_area(self) -> float:
        return self.__width * self.__height

    def get_perimeter(self) -> float:
        return self.__width * 2 + self.__height * 2

    def get_diagonal(self) -> float:
        return (self.__width**2 + self.__height**2) ** 0.5

    def get_picture(self) -> str:
        if self.__width > 50 or self.__height > 50:
            return "Too big for picture."

        picture = ""
        for i in range(self.__height):
            picture += "*" * self.__width + "\n"

        return picture

    def get_amount_inside(self, figure: "Rectangle") -> float:
        fit_width = self.get_width() // figure.get_width()
        fit_height = self.get_height() // figure.get_height()
        return fit_width * fit_height


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_side(self, side: float) -> None:
        super().set_height(side)
        super().set_width(side)

    def __str__(self) -> str:
        return f"Square(side={self.get_width()})"

    def set_height(self, side) -> None:
        super().set_height(side)
        super().set_width(side)

    def set_width(self, side) -> None:
        super().set_height(side)
        super().set_width(side)
        