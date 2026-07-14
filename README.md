# Bowling Game Kata

Robert C. Martin이 고안한 **Bowling Game Kata**를 TDD(Red → Green)로 연습한 프로젝트입니다.
실제 볼링 게임(공 굴리기, UI)을 만드는 것이 아니라, 미국식 텐핀 볼링 한 게임의 투구
순서가 주어졌을 때 최종 총점을 계산하는 로직만 다룹니다.

## 무엇을 할 수 있나요

`Game` 클래스 하나로 구성되어 있고, 메서드는 두 개뿐입니다.

- `roll(pins)`: 투구 결과(쓰러뜨린 핀 수)를 기록합니다.
- `score()`: 게임이 끝난 뒤 총점을 계산해 반환합니다.

```python
from game import Game

game = Game()

# 퍼펙트 게임: 12번 모두 스트라이크
for _ in range(12):
    game.roll(10)

print(game.score())  # 300
```

다른 예시:

```python
game = Game()
game.roll(5)
game.roll(5)   # 1프레임: 스페어
game.roll(3)   # 2프레임 첫 투구 → 스페어 보너스로도 사용됨
for _ in range(17):
    game.roll(0)

print(game.score())  # 16  (= 5+5+3 보너스, + 3+0, + 0×8프레임)
```

## 시작하기

Python 3와 `pytest`만 있으면 됩니다.

```bash
python3 -m venv .venv
.venv/bin/pip install pytest

PYTHONPATH=. .venv/bin/python -m pytest -q
```

모두 통과하면 다음과 같은 결과가 나옵니다.

```
.......                                                                  [100%]
7 passed in 0.01s
```

## 점수 규칙 요약

- 한 게임은 10프레임, 각 프레임 최대 2투구(10번째 프레임은 최대 3투구)입니다.
- **스페어**(2투구로 10핀 모두): 다음 1투구가 보너스로 더해집니다.
- **스트라이크**(1투구로 10핀 모두): 다음 2투구가 보너스로 더해집니다.
- **10번째 프레임**: 스페어/스트라이크가 나오면 보너스용 추가 투구를 할 수 있지만, 그
  추가 투구 자체가 다시 스페어/스트라이크여도 별도의 추가 기회는 없습니다.

자세한 규칙과 예시는 [`CLAUDE.md`](CLAUDE.md)의 "Bowling 점수 규칙" 절을 참고하세요.

## 범위 밖 (Out of Scope)

핵심 로직 연습에 집중하기 위해 아래는 다루지 않습니다.

- 투구 값 검증(0~10 범위 확인 등), 투구/프레임 횟수 검증
- 프레임별 중간 점수 조회
- 실제 게임 진행 UI/CLI

## 더 읽어보기

- [`CLAUDE.md`](CLAUDE.md): 이 프로젝트의 TDD 진행 방식, 커밋 컨벤션, 문서 규칙
- [`docs/`](docs/): 각 phase(요구사항)별 구현 계획(`_plan.md`)과 결과(`_result.md`) 문서
