class Member:
    
    def __init__(self, name, score, hole, add_score=0, center_skill=''):
        self.name = name
        self.score = score
        self.added = score
        self.hole = hole
        self.center_skill = center_skill
        self.add_score = add_score
        self.team = self.get_team()
        self.grade = self.get_grade()
        self.unit = self.get_unit()
        
    def __str__(self):
        return self.name + '_' + str(self.score)
    
    def __del__(self):
        pass
        #print('delete ' + self.__str__())
        
    def __dict__(self):
        return {}
    
    def get_team(self):
        name = self.name.split('_')[1].lower()
        if name in ('maki', 'rin', 'hanayo', 'honoka', 'kotori', 'umi', 'nico', 'eli', 'nozomi'):
            return "µ's"
        elif name in ('ruby', 'hanamaru', 'yoshiko', 'chika', 'you', 'riko', 'kanan', 'dia', 'mari'):
            return 'Aqours'
        else: raise Exception('member name error')

    def get_grade(self):
        name = self.name.split('_')[1].lower()
        if name in ('maki', 'rin', 'hanayo', 'ruby', 'hanamaru', 'yoshiko'):
            return 1
        elif name in ('honoka', 'kotori', 'umi', 'chika', 'you', 'riko'):
            return 2
        elif name in ('nico', 'eli', 'nozomi', 'kanan', 'dia', 'mari'):
            return 3
        else: raise Exception('member name error')

    def get_unit(self):
        name = self.name.split('_')[1].lower()
        if name in ('honoka', 'kotori', 'hanayo'):
            return 'Printemps'
        elif name in ('nico', 'eli', 'maki'):
            return 'BiBi'
        elif name in ('umi', 'rin', 'nozomi'):
            return 'lily while'
        elif name in ('chika', 'you', 'ruby'):
            return 'CYaRon!'
        elif name in ('kanan', 'dia', 'hanamaru'):
            return 'AZALEA'
        elif name in ('riko', 'yoshiko', 'mari'):
            return 'Guilty Kiss'
        else: raise Exception('member name error')