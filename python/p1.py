class Player:
    total_players = 0
    def __init__(self,pname,team,role,credits,points_scored):
        self.pname = pname
        self.team = team
        self.role = role
        self.credits = credits
        self.points_scored = points_scored
        Player.total_players += 1
    
    def get_fantasy_points(self):
        return self.points_scored
    def __str__(self):
        return f"{self.pname} ({self.team}) - {self.role} - {self.credits} credits"
class Captain (Player):
    def __init__(self,pname,team,role,credits,points_scored):
        super().__init__(pname,team,role,credits,points_scored)
    def get_fantasy_points(self):
        return self.points_scored*2
    def __str__(self):
        return f"{self.pname}  ({self.team}) - {self.role} - {self.credits} credits"

p1 = Player("Virat Kohli", "RCB", "Batsman", 10.5, 80)
p2 = Player("Jasprit Bumrah", "MI", "Bowler", 9.0, 60)
c1 = Captain("Rohit Sharma", "MI", "Batsman", 9.5, 75)

print(p1)
print("Fantasy Points:", p1.get_fantasy_points())

print(p2)
print("Fantasy Points:", p2.get_fantasy_points())

print(c1)
print("Fantasy Points:", c1.get_fantasy_points())

print("Total Players:", Player.total_players)
