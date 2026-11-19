class AIAssistant:
    """A simple description of Copilot in Python."""

    def __init__(self):
        self.name = "Copilot"
        self.type = "AI assistant"
        self.platform = "VS Code"
        self.purpose = "Helping users write, understand, and improve code"

    def introduce(self):
        return (
            f"I am {self.name}, an {self.type} using {self.platform}. "
            f"My purpose is {self.purpose.lower()}."
        )


copilot = AIAssistant()
print(copilot.introduce())