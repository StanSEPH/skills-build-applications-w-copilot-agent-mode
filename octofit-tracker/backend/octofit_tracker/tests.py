from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user1 = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Medium')
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-12-01')
        Leaderboard.objects.create(user=user1, score=100)

    def test_user_team(self):
        user = User.objects.get(email='ironman@marvel.com')
        self.assertEqual(user.team.name, 'Marvel')

    def test_leaderboard(self):
        entry = Leaderboard.objects.first()
        self.assertTrue(entry.score > 0)
