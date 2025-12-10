class Highscore:
    def __init__(self, filename="high_score.txt"):
        self.filename = filename
        self.highscore = self.read_highscore()

    def read_highscore(self):
        try:
            with open(self.filename) as f:
                return int(f.read().strip())
        except:
            return 0

    def update_highscore(self, score):
        if score > self.highscore:
            self.highscore = score
            with open(self.filename, "w") as f:
                f.write(str(score))
      
