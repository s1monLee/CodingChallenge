class Solution:
    def interpret(self, command: str) -> str:
        return "".join(command.replace("(al)","al")).replace("()","o")
