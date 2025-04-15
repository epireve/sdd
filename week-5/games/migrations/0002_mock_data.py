from django.db import migrations
from django.utils import timezone


def add_mock_data(apps, schema_editor):
    # Get the models
    Game = apps.get_model("games", "Game")
    Tags = apps.get_model("games", "Tags")
    Review = apps.get_model("games", "Review")

    # Create tags
    tags = {
        "Racing": Tags.objects.create(label="Racing"),
        "Adventure": Tags.objects.create(label="Adventure"),
        "Action": Tags.objects.create(label="Action"),
        "Sports": Tags.objects.create(label="Sports"),
        "Sandbox": Tags.objects.create(label="Sandbox"),
        "FPS": Tags.objects.create(label="FPS"),
        "Action-Adventure": Tags.objects.create(label="Action-Adventure"),
        "Platformer": Tags.objects.create(label="Platformer"),
    }

    # Create games with their tags
    games_data = [
        {
            "title": "Mario Kart 8 Deluxe",
            "developer": "Nintendo",
            "platform": "Nintendo Switch",
            "tags": ["Racing"],
            "review": "An excellent racing game with fantastic multiplayer features.",
        },
        {
            "title": "The Legend of Zelda: Breath of the Wild",
            "developer": "Nintendo",
            "platform": "Nintendo Switch",
            "tags": ["Adventure"],
            "review": "A masterpiece of open-world design with endless exploration.",
        },
        {
            "title": "Grand Theft Auto V",
            "developer": "Rockstar Games",
            "platform": "Multiple",
            "tags": ["Action"],
            "review": "A sprawling crime epic with incredible attention to detail.",
        },
        {
            "title": "FIFA 23",
            "developer": "EA Sports",
            "platform": "Multiple",
            "tags": ["Sports"],
            "review": "The most realistic football simulation to date.",
        },
        {
            "title": "Minecraft",
            "developer": "Mojang",
            "platform": "Multiple",
            "tags": ["Sandbox"],
            "review": "Endless creativity in a uniquely generated world.",
        },
        {
            "title": "Call of Duty: Modern Warfare",
            "developer": "Activision",
            "platform": "Multiple",
            "tags": ["FPS"],
            "review": "Fast-paced action with stunning graphics and tight controls.",
        },
        {
            "title": "Red Dead Redemption 2",
            "developer": "Rockstar Games",
            "platform": "Multiple",
            "tags": ["Action-Adventure"],
            "review": "A stunning western epic with an unforgettable story.",
        },
        {
            "title": "Super Mario Odyssey",
            "developer": "Nintendo",
            "platform": "Nintendo Switch",
            "tags": ["Platformer"],
            "review": "Creative and joyful platforming at its finest.",
        },
        {
            "title": "The Last of Us Part II",
            "developer": "Naughty Dog",
            "platform": "PlayStation",
            "tags": ["Action-Adventure"],
            "review": "A powerful narrative with intense gameplay moments.",
        },
        {
            "title": "Forza Horizon 5",
            "developer": "Playground Games",
            "platform": "Xbox/PC",
            "tags": ["Racing"],
            "review": "The ultimate racing playground with stunning visuals.",
        },
    ]

    # Add games and their reviews
    for game_data in games_data:
        game = Game.objects.create(
            title=game_data["title"],
            developer=game_data["developer"],
            platform=game_data["platform"],
        )

        # Add tags
        for tag_name in game_data["tags"]:
            game.label_tag.add(tags[tag_name])

        # Create review
        Review.objects.create(
            game=game, review=game_data["review"], date=timezone.now()
        )


def remove_mock_data(apps, schema_editor):
    # Remove all data
    Game = apps.get_model("games", "Game")
    Tags = apps.get_model("games", "Tags")
    Review = apps.get_model("games", "Review")

    Review.objects.all().delete()
    Game.objects.all().delete()
    Tags.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_mock_data, remove_mock_data),
    ]
