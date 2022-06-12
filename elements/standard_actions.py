from elements import Elements

from tools import Logger


class StandardActions:

    def __init__(self, browser, keyboard_actions=None, mouse_actions=None):
        self.browser = browser
        self.elements = Elements()
        self.keyboard_actions = keyboard_actions
        self.mouse_actions = mouse_actions

    def enter_value(self, locator: str, element: str, name) -> None:
        """Will be entered value in specified element."""
        Logger().info(f"Enter value(Element: {element}, name: {name}).")
        self.elements.click(self.browser, locator, element)
        self.keyboard_actions.enter_text(name)
