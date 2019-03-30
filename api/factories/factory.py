import factory
import factory.django
from api.models import BoardGame, Expansion, Match
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username123_{}'.format(n))
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    is_superuser = False
    

class BoardGameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardGame
        
    name = factory.Faker('name')


class ExpansionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expansion

    name = factory.Faker('name')
    board_game = factory.Iterator(BoardGame.objects.all())
    

class MatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Match
    
    board_game = factory.Iterator(BoardGame.objects.all())
    expansion = factory.Iterator(Expansion.objects.all())
    players = factory.Iterator(User.objects.all())
    points = 12
    scenario = 'test'
    victory = False
    
    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for player in extracted:
                self.players.add(player)
    
