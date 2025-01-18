from random import randint
import os


class DraftLetter:
    """
    This class drafts letters from a template and list of invited names
    """
    def __init__(self):
        self.template_path = self.random_letter_path()
        
    def random_letter_path(self):
        return os.path.join(os.path.dirname(__file__), f'./letter_templates/letter_{randint(1,3)}.txt')
    
    def draft_letter(self, name: str) -> str|None:
        try:
            with open(self.template_path) as template:
                self.template_lines = [line.strip() for line in template.readlines()]
                new_message = [line.replace('[NAME]', name) for line in self.template_lines]
        except FileNotFoundError:
            raise(f"Template file not found at {self.template_path}")
        
        return '\n'.join(new_message)

                        
                