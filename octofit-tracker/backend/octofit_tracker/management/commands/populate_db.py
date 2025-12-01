from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):

        # Drop collections using Djongo's database connection
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db['leaderboard'].drop()
        db['activities'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Medium')
        running = Workout.objects.create(name='Running', description='Run 5km', difficulty='Hard')

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=captain, type='Pushups', duration=20, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=120)
        Leaderboard.objects.create(user=batman, score=110)
        Leaderboard.objects.create(user=superman, score=130)
        Leaderboard.objects.create(user=captain, score=100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
