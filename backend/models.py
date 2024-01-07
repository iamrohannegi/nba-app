import app 
from datetime import datetime

class Rating(app.db.Model):
    id = app.db.Column(app.db.String(50), primary_key=True)
    fta_rating = app.db.Column(app.db.Integer, nullable=False)
    fouls_rating = app.db.Column(app.db.Integer, nullable=False)
    competitive_rating = app.db.Column(app.db.Integer, nullable=False)
    highscoring_rating = app.db.Column(app.db.Integer, nullable=False)
    star_power_rating = app.db.Column(app.db.Integer, nullable=False)
    overall_rating = app.db.Column(app.db.Numeric(precision=3, scale=2), nullable=False)
    game_name = app.db.Column(app.db.String(100), nullable=False)
    game_date = app.db.Column(app.db.DateTime, nullable=False)
    created_at = app.db.Column(app.db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, game_id, game_data, ratings):
        self.id = game_id 
        self.game_date = game_data['game_date']
        self.game_name = game_data['game_name']
        self.fta_rating = ratings['fta_rating']
        self.fouls_rating = ratings['fouls_rating']
        self.competitive_rating = ratings['competitive_rating']
        self.highscoring_rating = ratings['highscoring_rating']
        self.star_power_rating = ratings['star_power_rating']
        self.overall_rating = ratings['overall_rating']
    
    
        
