class C:
    def __init__(self, kg: float) -> None:
        self.mass_kg=kg
        
    @property
    def mass_g(self) -> float:
        """Dinamic property"""
        return self.mass_kg*1000
        
    @mass_g.setter
    def mass_g(self, mass_g: float) -> None:
        self.mass_kg = mass_g / 1000
        
c=C(2)
assert c.mass_g == 2000
c.mass_g == 4000
assert c.mass_kg == 4
assert c.mass_g == 4000
    