import math
class Team:
    
    def __init__(self, name, members):
        if len(members) != 9: raise Exception('Team error')
        self.name = name
        self.members = members
        self.score = sum([member.score for member in self.members])
        self.avg_score = 0
        self.score_string = ''
        self.perfect_fill()
        
    def __str__(self):
        return ('Team: ' + self.name + '\n' + 
                'Show Score:' + str(self.score) + '+' + str(self.best_center.center_score) + '\n' +
                self.score_string + 
                'Average Score:' + str(self.avg_score) + '\n')
    
    def __del__(self):
        pass
        #print('delete ' + self.__str__())

    def __dict__(self):
        return {}
    
    def personal(self, member, percent):
        return math.ceil(member.score * percent)
    
    def team(self, percent):
        return sum([math.ceil(member.score * percent) for member in self.members])
    
    def team_add(self, percent):
        for member in self.members:
            member.added += math.ceil(member.score * percent)
    
    def center_key(self, center, member):
        if center.name.split('_')[0] == 'UR':
            key1 = .09
            if center.center_skill == 'Team' and center.team == member.team: key2 = .03 
            elif center.center_skill == 'Grade' and center.grade == member.grade: key2 = .06
            elif center.center_skill == 'Unit' and center.unit == member.unit: key2 = .06
            else: key2 = .0
        elif center.name.split('_')[0] == 'SSR':
            key1 = .07
            if center.center_skill == 'Team' and center.team == member.team: key2 = .01
            elif center.center_skill == 'Grade' and center.grade == member.grade: key2 = .02
            elif center.center_skill == 'Unit' and center.unit == member.unit: key2 = .02
            else: key2 = .0
        else: key1, key2 = .0, .0
        return key1, key2
                
    def perfect_fill(self):
        self.perfect_rate = float(open('./perfect_rate', 'r').read())
        self.score_to_point = 1 / (.015972 + .002178 * self.perfect_rate)
        for member in self.members:
            if member.hole == 2:
                #2 personal 10%
                personal = self.personal(member, .1)
                member.added += personal
                self.score += personal
                self.avg_score += member.add_score * self.score_to_point
                self.score_string += member.__str__() + ' personal 10%\n'
            elif member.hole == 3:
                #3 personal 16%, team 1.8%
                personal = self.personal(member, .16)
                team = self.team(.018)
                self.avg_score += member.add_score * self.score_to_point
                if personal > team:
                    member.added += personal
                    self.score += personal
                    self.score_string += member.__str__() + ' personal 16%\n'
                else:
                    self.team_add(.018)
                    self.score += team
                    self.score_string += member.__str__() + ' team 1.8%\n'
            elif member.hole == 4:
                #4 personal 16% + 200, team 2.4%, add_score x2.5
                personal = self.personal(member, .16) + 200
                team = self.team(.024)
                add_score = member.add_score * 2.5 * self.score_to_point
                maximum = max(personal, team, add_score)
                if personal == maximum:
                    member.added += personal
                    self.score += personal
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' personal 16% + 200\n'
                elif team == maximum:
                    self.team_add(.024)
                    self.score += team
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 2.4%\n'
                else:
                    self.avg_score += member.add_score * 2.5 * self.score_to_point
                    self.score_string += member.__str__() + ' add score x2.5\n'
            elif member.hole == 5:
                #5 personal 26%, team 1.8% + personal 10%, team 2.4% + 200, add_score x2.5 + 200, personal 1400
                personal = self.personal(member, .26)
                team_personal = self.team(.018) + self.personal(member, .1)
                team = self.team(.024) + 200
                add_score = member.add_score * 2.5 * self.score_to_point + 200
                personal_add = 1400
                maximum = max(personal, team_personal, team, add_score, personal_add)
                if personal == maximum:
                    member.added += personal
                    self.score += personal
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' personal 16% + personal 10%\n'
                elif team_personal == maximum:
                    self.team_add(.018)
                    member.added += self.personal(member, .1)
                    self.score += team_personal
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 1.8% + personal 10%\n'
                elif team == maximum:
                    self.team_add(.024)
                    member.added += 200
                    self.score += team
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 2.4% + 200\n'
                elif add_score == maximum:
                    member.added += 200
                    self.score += 200
                    self.avg_score += member.add_score * 2.5 * self.score_to_point
                    self.score_string += member.__str__() + ' add score x2.5 + 200\n'
                else:
                    member.added += 1400
                    self.score += 1400
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' + 1400\n'
            elif member.hole == 6:
                #6 personal 16% + team 1.8%, team 2.4% + personal 10%, add_score x2.5 + personal 10%, team 4%
                personal_team = self.personal(member, .16) + self.team(.018)
                team_personal = self.team(.024) + self.personal(member, .1)
                add_score = member.add_score * 2.5 * self.score_to_point + self.personal(member, .1)
                team  = self.team(.04)
                maximum = max(personal_team, team_personal, add_score)
                if maximum == personal_team:
                    member.added += self.personal(member, .16)
                    self.team_add(.018)
                    self.score += personal_team
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 1.8% + personal 16%\n'
                elif maximum == team_personal:
                    member.added += self.personal(member, .1)
                    self.team_add(.024)
                    self.score += team_personal
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 2.4% + personal 10%\n'
                elif maximum == add_score :
                    member += self.personal(member, .1)
                    self.score += self.personal(member, .1)
                    self.avg_score += member.add_score * 2.5 * self.score_to_point
                    self.score_string += member.__str__() + ' add score x2.5 + personal 10%\n'
                else:
                    self.team_add(.04)
                    self.score += team
                    self.avg_score += member.add_score * self.score_to_point
                    self.score_string += member.__str__() + ' team 4%\n'
        self.best_center = self.members[0]
        for center in self.members:
            center.center_score = 0
            if center.center_skill == '': continue
            for member in self.members:
                key1, key2 = self.center_key(center, member)
                center.center_score += math.ceil(member.added * key1) + math.ceil(member.added * key2)
            if center.center_score > self.best_center.center_score: self.best_center = center
        self.score = self.score + self.best_center.center_score
        self.score_string = self.score_string.replace(self.best_center.__str__(), 'C: ' + self.best_center.__str__())
        self.avg_score = round(self.avg_score, 2) + self.score