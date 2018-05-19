from add_score_compute import add_score_compute
from Team import Team
from Member import Member

if __name__ == '__main__':
    us_smile = Team("µ's smile", [
                    Member('UR_Honoka', 5540, 4, 0, 'Grade'), 
                    Member('SSR_Honoka', 5860, 3, add_score_compute('note', 24, 0.31, 435), 'Grade'),
                    Member('UR_Rin', 6330, 4, add_score_compute('perfect', 25, 0.33, 700), 'Grade'),
                    Member('SSR_Rin', 5920, 3, 0, 'Unit'),
                    Member('UR_Maki', 5410, 4, add_score_compute('perfect', 28, 0.42, 1610), 'Team'),
                    Member('SR_Maki', 5450, 2, add_score_compute('note', 13, 0.24, 285)),
                    Member('UR_Eli', 6300, 4, 0, 'Team'),
                    Member('SSR_Nozomi', 5850, 3, add_score_compute('combo', 18, 0.28, 545), 'Unit'),
                    Member('SSR_Kotori', 5840, 3, add_score_compute('perfect', 24, 0.38, 515), 'Unit')
                ])
    us_pure = Team("µ's pure", [
                    Member('SSR_Umi', 5840, 5, add_score_compute('note', 23, 0.34, 455), 'Grade'),
                    Member('SSR_Eli', 5880, 5, 0, 'Grade'),
                    Member('UR_Eli', 5480, 4, add_score_compute('second', 13, 0.35, 600)),
                    Member('SSR_Nozomi', 5920, 3, 0, 'Grade'),
                    Member('UR_Nozomi', 5530, 4, 0, 'Grade'),
                    Member('UR_Maki', 6340, 4, 0),
                    Member('UR_Maki', 5510, 4, add_score_compute('perfect', 15, 0.4, 930), 'Team'),
                    Member('SSR_Maki', 5850, 4, add_score_compute('combo', 19, 0.33, 490), 'Unit'),
                    Member('SSR_Nico', 5860, 3, add_score_compute('note', 25, 0.35, 480), 'Grade')
                ])
    us_cool = Team("µ's cool", [
                    Member('SSR_Umi', 5920, 3, 0, 'Team'),
                    Member('UR_Umi', 5550, 4, 0, 'Unit'),
                    Member('UR_Hanayo', 6340, 5, 0, 'Unit'),
                    Member('SSR_Hanayo', 5890, 3, 0, 'Unit'),
                    Member('SSR_Nico', 5920, 6, 0, 'Grade'),
                    Member('UR_Nico', 6240, 5, add_score_compute('combo', 18, 0.39, 1170), 'Team'),
                    Member('SSR_Maki', 5890, 5, 0, 'Grade'),
                    Member('SSR_Rin', 5840, 3, add_score_compute('perfect', 26, 0.42, 505), 'Grade'),
                    Member('UR_Rin', 6280, 4, 0),
                ])
    aqours_smile = Team("Aqours smile", [
                    Member('SSR_Riko', 5850, 4, add_score_compute('perfect', 21, 0.39, 620), 'Grade'),
                    Member('SSR_Riko', 5890, 3, 0, 'Unit'),
                    Member('SSR_Ruby', 5840, 5, add_score_compute('perfect', 19, 0.4, 730), 'Unit'),
                    Member('UR_Mari', 6340, 4, 0, 'Team'),
                    Member('UR_Mari', 6370, 4, 0, 'Unit'),
                    Member('SSR_You', 5880, 3, 0, 'Unit'),
                    Member('SSR_You', 5840, 3, add_score_compute('combo', 26, 0.45, 670), 'Grade'),
                    Member('SSR_You', 5840, 3, add_score_compute('combo', 26, 0.45, 670), 'Grade'),
                    Member('SSR_Yoshiko', 5840, 5, add_score_compute('perfect', 25, 0.39, 745), 'Grade'),
                ])
    aqours_pure = Team("Aqours pure", [
                    Member('SSR_Mari', 5840, 3, add_score_compute('perfect', 21, 0.33, 520), 'Grade'),
                    Member('SSR_Ruby', 5890, 5, 0, 'Grade'),
                    Member('SSR_Ruby', 5850, 3, add_score_compute('combo', 22, 0.37, 505), 'Unit'),
                    Member('SSR_Ruby', 5850, 5, add_score_compute('combo', 22, 0.41, 630), 'Unit'),
                    Member('UR_Ruby', 6320, 4, add_score_compute('note', 26, 0.46, 1330), 'Team'), 
                    Member('SSR_You', 5850, 3, add_score_compute('note', 27, .36, 505), 'Unit'),
                    Member('SSR_You', 5920, 3, 0, 'Unit'),
                    Member('SSR_Riko', 5920, 3, 0, 'Grade'),
                    Member('SSR_Riko', 5920, 3, 0, 'Grade')
                ])
    aqours_cool = Team("Aqours cool", [
                    Member('UR_Mari', 5520, 4, add_score_compute('note', 25, 0.36, 640), 'Unit'), 
                    Member('SSR_Mari', 5850, 3, add_score_compute('combo', 25, 0.41, 520), 'Unit'), 
                    Member('SR_Dia', 5480, 3),
                    Member('SSR_Dia', 5890, 3, 0, 'Team'),
                    Member('UR_Hanamaru', 6350, 4, 0, 'Grade'),
                    Member('SSR_Hanamaru', 5840, 3, 0, 'Unit'),
                    Member('UR_Yoshiko', 6350, 4, add_score_compute('combo', 21, 0.4, 1225), 'Unit'),
                    Member('SSR_Yoshiko', 5920, 3, 0, 'Unit'),
                    Member('SSR_Riko', 5840, 3, add_score_compute('note', 22, 0.32, 410), 'Grade')
                ])
    
    print(us_smile)
    print(us_pure)
    print(us_cool)
    print(aqours_smile)
    print(aqours_pure)
    print(aqours_cool)