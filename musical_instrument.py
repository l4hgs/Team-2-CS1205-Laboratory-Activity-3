from abc import ABC, abstractmethod

# Abstract base class for all musical instruments
class MusicalInstrument(ABC):
    def __init__(self, instrument_type: str, brand: str, sound_range: str):
        self.instrument_type = instrument_type
        self.brand = brand
        self.sound_range = sound_range

    @abstractmethod
    def play_sound(self):
        pass

    def tune_instrument(self):
        print(f"Tuning the {self.instrument_type} ({self.brand})...")

# String Instruments
class StringInstrument(MusicalInstrument):
    def __init__(self, instrument_type: str, brand: str, sound_range: str,
                 string_material: str, string_count: int):
        super().__init__(instrument_type, brand, sound_range)
        self.string_material = string_material
        self.string_count = string_count

    def pluck(self):
        print(f"Plucking the {self.string_material} strings.")

class Guitar(StringInstrument):
    def __init__(self, brand: str, sound_range: str, string_material: str,
                 string_count: int, acoustic: bool):
        super().__init__("Guitar", brand, sound_range, string_material, string_count)
        self.acoustic = acoustic

    def play_sound(self):
        sound_type = "acoustic" if self.acoustic else "electric"
        print(f"{self.brand} Guitar produces a warm {sound_type} tone.")

    def strum(self):
        print("Strumming across all guitar strings.")

class Violin(StringInstrument):
    def __init__(self, brand: str, sound_range: str, string_material: str,
                 string_count: int, size: str, bow_material: str):
        super().__init__("Violin", brand, sound_range, string_material, string_count)
        self.size = size
        self.bow_material = bow_material

    def play_sound(self):
        print(f"{self.brand} Violin sings with a rich, expressive tone.")

    def bow(self):
        print(f"Using the {self.bow_material} bow to play the violin.")

# Wind Instruments
class WindInstrument(MusicalInstrument):
    def __init__(self, instrument_type: str, brand: str, sound_range: str):
        super().__init__(instrument_type, brand, sound_range)

class Flute(WindInstrument):
    def __init__(self, brand: str, sound_range: str, material: str, key_system: str):
        super().__init__("Flute", brand, sound_range)
        self.material = material
        self.key_system = key_system

    def play_sound(self):
        print(f"Playing a melodious sound on the {self.brand} flute.")

    def blow_air(self):
        print("Blowing air into the flute to produce sound.")

class Trumpet(WindInstrument):
    def __init__(self, brand: str, sound_range: str, num_valves: int, bore_size: float):
        super().__init__("Trumpet", brand, sound_range)
        self.num_valves = num_valves
        self.bore_size = bore_size

    def play_sound(self):
        print(f"Playing a bold sound on the {self.brand} trumpet.")

    def press_valves(self):
        print(f"Pressing {self.num_valves} valves to change pitch.")

# Plectrum Instruments
class PlectrumInstrument(MusicalInstrument):  # Dapat same parent class
    def __init__(self, instrument_type: str, brand: str, sound_range: str):
        super().__init__(instrument_type, brand, sound_range)  # Fixed: Proper init

class Banduria(PlectrumInstrument):
    def __init__(self, brand: str, sound_range: str, num_strings: int, body_shape: str):
        super().__init__("Banduria", brand, sound_range)
        self.num_strings = num_strings
        self.body_shape = body_shape

    def play_sound(self):
        print("Banduria is playing a bright and vibrant sound.")

    def pluck(self):
        print(f"Plucking the {self.num_strings} strings of the Banduria.")

class Octavina(PlectrumInstrument):
    def __init__(self, brand: str, sound_range: str, num_strings: int, material: str):
        super().__init__("Octavina", brand, sound_range)
        self.num_strings = num_strings
        self.material = material

    def play_sound(self):
        print("Octavina is producing a mellow and warm tone.")

    def strum(self):
        print(f"Strumming the {self.material} Octavina strings.")

# Percussion Instruments
class PercussionInstrument(MusicalInstrument):
    def __init__(self, instrument_type: str, brand: str, sound_range: str, strike_method: str):
        super().__init__(instrument_type, brand, sound_range)
        self.strike_method = strike_method
    
    def play_sound(self):
        print(f"Playing {self.instrument_type} sound with {self.strike_method}")
    
    def hit(self):
        print(f"Hitting the {self.instrument_type}")

class Drum(PercussionInstrument):
    def __init__(self, brand: str, sound_range: str, diameter: float, has_stand: bool):
        super().__init__("Drum", brand, sound_range, "stick")
        self.diameter = diameter
        self.has_stand = has_stand
    
    def play_sound(self):
        print("Boom! Boom! Drum sound playing")
    
    def adjust_tension(self):
        print("Adjusting drum head tension")

class Tambourine(PercussionInstrument):
    def __init__(self, brand: str, sound_range: str, has_jingles: bool):
        super().__init__("Tambourine", brand, sound_range, "hand")
        self.has_jingles = has_jingles
    
    def play_sound(self):
        sound = "Jingle!" if self.has_jingles else "Shake!"
        print(f"{sound} Tambourine sound playing")
    
    def shake(self):
        print("Shaking the tambourine")

# Demonstration of all instruments
if __name__ == "__main__":
    print("=== String Instruments ===")
    guitar = Guitar("Fender", "E2-E6", "Nylon", 6, True)
    guitar.tune_instrument()
    guitar.play_sound()
    guitar.strum()
    
    violin = Violin("Stradivarius", "G3-A7", "Steel", 4, "4/4", "Horsehair")
    violin.play_sound()
    violin.bow()
    
    print("\n=== Wind Instruments ===")
    flute = Flute("Yamaha", "C4-C7", "Silver", "Boehm")
    flute.play_sound()
    flute.blow_air()
    
    trumpet = Trumpet("Bach", "F#3-C6", 3, 0.46)
    trumpet.play_sound()
    trumpet.press_valves()
    
    print("\n=== Plectrum Instruments ===")
    banduria = Banduria("Reyes", "G3-G5", 14, "Pear-shaped")
    banduria.play_sound()
    banduria.pluck()
    
    octavina = Octavina("Reyes", "G2-G4", 14, "Mahogany")
    octavina.play_sound()
    octavina.strum()
    
    print("\n=== Percussion Instruments ===")
    drum = Drum("Pearl", "A1-A2", 14.0, True)
    drum.play_sound()
    drum.adjust_tension()
    
    tambourine = Tambourine("LP", "C5-C6", True)
    tambourine.play_sound()
    tambourine.shake()