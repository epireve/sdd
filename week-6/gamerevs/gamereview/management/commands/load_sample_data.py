from django.core.management.base import BaseCommand
from gamerevs.gamereview.models import Game, Tags, Review
from django.utils import timezone


class Command(BaseCommand):
    help = "Loads sample game data into the database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating sample game data...")

        # Clear existing data
        Game.objects.all().delete()
        Tags.objects.all().delete()
        Review.objects.all().delete()

        # Create tags
        self.stdout.write("Creating tags...")
        rpg_tag = Tags.objects.create(label="RPG")
        action_tag = Tags.objects.create(label="Action")
        adventure_tag = Tags.objects.create(label="Adventure")
        strategy_tag = Tags.objects.create(label="Strategy")
        open_world_tag = Tags.objects.create(label="Open World")

        # Create games
        self.stdout.write("Creating games...")

        # Elden Ring
        elden_ring = Game.objects.create(
            title="Elden Ring",
            developer="FromSoftware",
            platform="PC, PlayStation, Xbox",
        )
        elden_ring.label_tag.add(rpg_tag, action_tag, open_world_tag)

        # Create reviews for Elden Ring
        Review.objects.create(
            game=elden_ring,
            review="An absolute masterpiece that combines the best elements of FromSoftware's previous titles with an open world design.",
            date=timezone.now(),
        )

        Review.objects.create(
            game=elden_ring,
            review="This game is absolutely incredible! The open world design is breathtaking, and the combat system is challenging but rewarding.",
            date=timezone.now(),
        )

        # Baldur's Gate 3
        baldurs_gate = Game.objects.create(
            title="Baldur's Gate 3",
            developer="Larian Studios",
            platform="PC, PlayStation",
        )
        baldurs_gate.label_tag.add(rpg_tag, strategy_tag)

        # Create reviews for Baldur's Gate 3
        Review.objects.create(
            game=baldurs_gate,
            review="Baldur's Gate 3 is an unprecedented achievement in the CRPG genre, offering unparalleled depth and player choice.",
            date=timezone.now(),
        )

        Review.objects.create(
            game=baldurs_gate,
            review="Baldur's Gate 3 successfully brings the depth of D&D to video games. The character customization is impressive, and the story branches significantly based on your choices.",
            date=timezone.now(),
        )

        # Hogwarts Legacy
        hogwarts = Game.objects.create(
            title="Hogwarts Legacy",
            developer="Avalanche Software",
            platform="PC, PlayStation, Xbox, Switch",
        )
        hogwarts.label_tag.add(action_tag, adventure_tag, rpg_tag)

        # Create reviews for Hogwarts Legacy
        Review.objects.create(
            game=hogwarts,
            review="Hogwarts Legacy delivers an immersive wizarding world experience with engaging gameplay and a rich story that fans of the franchise will appreciate.",
            date=timezone.now(),
        )

        self.stdout.write(self.style.SUCCESS("Successfully loaded sample game data!"))
