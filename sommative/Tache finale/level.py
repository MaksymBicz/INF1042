MAX_LEVEL = 5

LEVEL_THRESHOLDS = [0, 0, 10, 20, 35, 55]


class LevelSystem:

    def __init__(self):
        self.level     = 1
        self._prev_lvl = 1

    def update(self, score):
        for lvl in range(MAX_LEVEL, 0, -1):
            if score >= LEVEL_THRESHOLDS[lvl]:
                self.level = lvl
                break

    @property
    def level_changed(self):
        if self.level != self._prev_lvl:
            self._prev_lvl = self.level
            return True
        return False

    def fish_speed(self):
        return 2 + self.level * 0.8

    def obstacle_speed(self):
        return 3 + self.level * 0.8