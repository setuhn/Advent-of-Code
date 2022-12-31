# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:30:44 2022

@author: Setuhn
"""

class Folder:
    def __init__(self, name, root=None):
        self.name = name
        self.root = root
        self.children = {} # dict containing the children indexed by name
        self.size = 0
    
    def update_size(self):
        [folder.update_size() for folder in self.children.values() if type(folder) is Folder]
        
        self.size = sum([c.size for c in self.children.values()])
    
    def get_folder_size_at_most(self, size):
        
        folder_list = [child for child in self.children.values() if isinstance(child, Folder)]
        
        if folder_list:
            output = []
            
            for folder in folder_list:
                
                if folder.size <= size:
                    output.extend(folder.get_folder_size_at_most(size))
                    
                output.extend([self.size] if self.size <= size else [])
                    
            return output
        
        else:

            return [self.size] if self.size <= size else [] 
        
    def get_folder_size_at_min(self, size):
        
        folder_list = [child for child in self.children.values() if isinstance(child, Folder)]
        
        if folder_list:
            output = []
            
            for folder in folder_list:
                
                if folder.size >= size:
                    output.extend(folder.get_folder_size_at_min(size))
                    
                output.extend([self.size] if self.size >= size else [])
                    
            return output
        
        else:

            return [self.size] if self.size >= size else [] 
        
        
class File:
    def __init__(self, name, root, size=0):
        self.name = name
        self.root = root
        self.size = size
        
def interpret_command(command, tree):
    
    if 'cd' in command:
        new_dir = command.split()[-1]
        
        if new_dir == '..' and tree != None:
            return tree.root
            
        elif tree != None:
            return tree.children[new_dir]
            
        else:
            return Folder(new_dir)
    
    else:
        return tree


def interpret_output(output, tree):
    size, name = output.split()
    
    if size == 'dir':
        tree.children[name] = Folder(name, tree)
        
    else:
        tree.children[name] = File(name, tree, int(size))
    


with open("input_7", 'r') as data:
    
    tree = None
    root = None

    for line in data.readlines():
        if '$' in line:
            
            if tree is None:
                root = tree = interpret_command(line, tree)
            else:
                tree = interpret_command(line, tree)
            
        else:
            interpret_output(line, tree)
                
    root.update_size()
    
    #part 1
    #print(sum(root.get_folder_size_at_most(100000)))
    
    #part 2
    total_space = 70000000
    needed_space = 30000000
    ununsed_space = total_space - root.size
    free_space = needed_space - ununsed_space
    
    list_folder_candidate = root.get_folder_size_at_min(free_space)
    
    print(min(list_folder_candidate))
