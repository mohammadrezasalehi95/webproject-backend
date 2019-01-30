import random
from random import randint
from .models import *
from .utils import rand_str
from faker import Faker
from faker.providers import address, date_time, profile, job, company

fake = Faker()
fake.add_provider(address)
fake.add_provider(date_time)
fake.add_provider(job)
fake.add_provider(company)
TEAM_NUM = 10
GAME_NUM = 10
LEAGUE_NUM = 10
LEAGUE_ROW_NUM = 10
PROFILE_NUM = 10
CUP_NUM = 10
NEWS_NUM = 10
GAME_REPORT_NUM = 10
GAME_EVENT_NUM = 10
BASKET_S_D_NUM = 10
FOOTBALL_S_D_NUM = 10
GAME_SPECIAL_DETAIL = 10

teams = [Team.objects.create(
    name=fake.city(),
    bio=fake.text(randint(40, 400)),
) for _ in range(TEAM_NUM)]

games = [Game.objects.create(
    team1=random.choice(randint(1, TEAM_NUM), None),
    team2=random.choice(randint(1, TEAM_NUM), None),
    date=fake.future_date(end_date="+30d", tzinfo=None),
    status=randint(0, 10),
    team1_score=randint(0, 20),
    team2_score=randint(0, 20),
    team1_point=randint(0, 5),
    team2_point=randint(0, 5),
    bestPlayer_id=randint(0, PROFILE_NUM),
    type=random.choice('F', 'B'),
) for _ in range(GAME_NUM)]

leagues = [League.objects.create(
    name=fake.company(),
    type=random.choice('F', 'B'),
) for _ in range(LEAGUE_NUM)]

league_rows = [LeagueRow.objects.create(
    team_id=randint(1, TEAM_NUM),
    league_id=randint(1, LEAGUE_NUM),
    win=randint(0, 9),
    lose=randint(0, 9),
    equal=randint(0, 9),
    gf=randint(0, 9),
    ga=randint(0, 9),
) for i in range(LEAGUE_ROW_NUM)]

profiles = [Profile.objects.create(
    name=fake.name(),
    type=random.choice('F', 'B'),
    gender=random.choice('Male', 'Female'),
    bio=fake.text(),
    height=randint(160, 210),
    weight=randint(55, 100),
    currentTeam_id=randint(1, TEAM_NUM),
    national=fake.country(),
    rule=fake.job(),
    born=fake.date_this_century(before_today=True, after_today=False),
) for _ in range(PROFILE_NUM)]

news = [New.objects.create(
    title=fake.text(40),
    subtitle=fake.text(40),
    content=fake.text(400),
) for _ in range(NEWS_NUM)]

game_reports = [Game_Report.objects.create(
    game_id=randint(1, GAME_NUM),
    last_report=fake.text(randint(20, 100)),
) for _ in range(GAME_REPORT_NUM)]

game_events = [Game_Event.objects.create(
    game_id=randint(1, GAME_NUM),
    time=fake.future_datetime(end_date="+30d", tzinfo=None),
    text=fake.text(randint(100, 400)),
) for _ in range(GAME_REPORT_NUM)]

basketSeasonDetails = [BasketSeasonDetail.objects.create(
    profile_id=randint(1,PROFILE_NUM),
    season=fake.year(),
    playTime=random.choice(da)
) for _ in range(BASKET_S_D_NUM)]

FootBallSeasonDetail = [FootBallSeasonDetail.objects.create() for i in range(FOOTBALL_S_D_NUM)]

gameSpecialDetail = [GameSpecialDetail.objects.create() for i in range(GAME_SPECIAL_DETAIL)]

# cupes = [Cup.objects.create() for _ in range(CUP_NUM)]
