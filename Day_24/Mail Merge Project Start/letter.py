import os

template_letter_path = os.path.join(os.path.dirname(__file__),'./Input/Letters/starting_letter.txt')
invitation_names_path = os.path.join(os.path.dirname(__file__),'./Input/Names/invited_names.txt')
# draft_letter_path = os.path.join(os.path.dirname(__file__),'./Output/ReadyToSend/')

class Letter:
    '''
    Drafts letters from a template and list of invitated names
    '''
    def __init__(self):
        with open(template_letter_path) as template:
            self.lines = [line.rstrip() for line in template.readlines()]
        with open(invitation_names_path) as names:
            self.names = [name.removesuffix('\n') for name in names.readlines()]
            
        self.letters = {}
        


    def draft_letters_with_invitation(self):
        '''create draft letters by replacing name'''
        # replace template
        for name in self.names:
            self.lines[0] = f'Dear {name},'
            self.lines[6] = self.lines[6].replace('Angela', 'Dee')
            # draft letters and store in unique filename
            draft_letter_path = os.path.join(os.path.dirname(__file__),f'./Output/ReadyToSend/letter_for_{name}')
            with open(draft_letter_path, 'w') as draft_letter:
                for line in self.lines:
                    draft_letter.write(f'{line}\n')



            

        

        

        
        