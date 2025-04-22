from hero import Hero

class Batman(Hero):
    def __init__(self, name, power_level, gadgets):
        super().__init__(name, power_level)
        self.__gadgets = gadgets  # private attribute

    def show_gadgets(self):
        return f"{self.name}'s gadgets: {', '.join(self.__gadgets)}"

    def add_gadget(self, gadget):
        self.__gadgets.append(gadget)


batman = Batman("Batman", 90, ["Batarang", "Grappling Hook"])
print(batman.introduce())
print(batman.show_gadgets())
batman.boost_power(10)
print("New Power Level:", batman.get_power_level())
