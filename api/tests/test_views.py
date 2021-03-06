from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from api.models import BoardGame, Match, Expansion

User = get_user_model()


class ViewTestApi(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", is_superuser=False, is_active=True, password="test")
        self.player = User.objects.create(username="player", is_superuser=False, is_active=True)
        self.board_game = BoardGame.objects.create(name="testbg", edition=1)
        self.expansion = Expansion.objects.create(name="testexpansion", board_game=self.board_game)
        self.match = Match.objects.create(board_game=self.board_game, points=0, victory=False)
        self.match.save()
        self.match.players.add(self.user)
        self.client.force_authenticate(user=self.user)

    def test_get_boardgames(self):
        response = self.client.get('/api/boardgames/')
        self.assertEqual(response.status_code, 200)

    def test_post_boardgames(self):
        response = self.client.post('/api/boardgames/')
        self.assertEqual(response.status_code, 405)

    def test_get_expansions(self):
        response = self.client.get('/api/expansions/')
        self.assertEqual(response.status_code, 200)

    def test_post_expansions(self):
        response = self.client.post('/api/expansions/')
        self.assertEqual(response.status_code, 405)

    def test_get_matches(self):
        response = self.client.get('/api/matches/')
        self.assertEqual(response.status_code, 200)

    def test_get_match(self):
        response = self.client.get("/api/matches/{}/".format(self.match.id))
        self.assertEqual(response.status_code, 200)

    def test_post_matches(self):
        response = self.client.post('/api/matches/', {"victory": False,
                                                      "points": 100,
                                                      "scenario": "testscenario",
                                                      "board_game": self.board_game.id,
                                                      "expansion": self.expansion.id,
                                                      "players": [self.player.id]})
        self.assertEqual(response.status_code, 201)

    def test_get_top_three(self):
        response = self.client.get('/api/matches/top-three/')
        self.assertEqual(response.status_code, 200)

    def test_post_top_three(self):
        response = self.client.post('/api/matches/top-three/', {"victory": False,
                                                      "points": 100,
                                                      "scenario": "testscenario",
                                                      "board_game": self.board_game.id,
                                                      "expansion": self.expansion.id,
                                                      "players": [self.player.id]})
        self.assertEqual(response.status_code, 405)

    def test_create_user(self):
        self.client.logout()
        response = self.client.post('/api/users/register', {"username": "test",
                                                            "password": "test1234",
                                                            "confirm_password": "test1234",
                                                            "email": "test@test.com"})
        self.assertEqual(response.status_code, 301)

    def test_get_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_post_user_list(self):
        response = self.client.post('/api/users/')
        self.assertEqual(response.status_code, 405)

    def test_update_password(self):
        response = self.client.put('api/users/change-password/{}'.format(self.user.id), {
            'old_password': 'test',
            'new_password': 'test123',
            'confirm_password': 'test123'
        })
        self.assertEqual(response.status_code, 201)

