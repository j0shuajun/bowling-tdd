from game import Game


def roll_many(game, times, pins):
    for _ in range(times):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()

    roll_many(game, 20, 0)

    assert game.score() == 0
