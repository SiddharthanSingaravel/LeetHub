class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()","o")
        command = command.replace("(","")
        command = command.replace(")","")
        
        return command