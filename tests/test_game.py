from game import Game


def roll_many(game, times, pins):
    for _ in range(times):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()

    roll_many(game, 20, 0)

    assert game.score() == 0


def test_all_ones_scores_twenty():
    game = Game()

    roll_many(game, 20, 1)

    assert game.score() == 20


def test_one_spare_adds_next_roll_as_bonus():
    game = Game()

    game.roll(5)
    game.roll(5)  # frame 1: spare
    game.roll(3)
    roll_many(game, 17, 0)

    assert game.score() == 16


def test_one_strike_adds_next_two_rolls_as_bonus():
    game = Game()

    game.roll(10)  # frame 1: strike
    game.roll(3)
    game.roll(5)
    roll_many(game, 16, 0)

    assert game.score() == 26


def test_tenth_frame_strike_gets_two_bonus_rolls():
    game = Game()

    roll_many(game, 18, 0)  # frames 1-9: all gutter
    game.roll(10)  # frame 10: strike
    game.roll(5)
    game.roll(3)

    assert game.score() == 18


def test_tenth_frame_spare_gets_one_bonus_roll():
    game = Game()

    roll_many(game, 18, 0)  # frames 1-9: all gutter
    game.roll(5)
    game.roll(5)  # frame 10: spare
    game.roll(4)

    assert game.score() == 14
