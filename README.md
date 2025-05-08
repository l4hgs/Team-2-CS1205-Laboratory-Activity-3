# 🎵 Pythonic Orchestra: A Polymorphic Symphony in Python

## 👥 Team Members
- Cantos, Alodivinno Ricco  
- Canatuan, Tremonti  
- Ibon, Nash  
- Manalo, John Danver

---

## 📝 Description

**Pythonic Orchestra** is a Python-based simulation of a musical ensemble, built using **object-oriented programming (OOP)** principles.

This program features a class hierarchy that represents four main families of instruments:
- 🎻 **String Instruments** (e.g., Guitar, Violin)
- 🌬️ **Wind Instruments** (e.g., Flute, Trumpet)
- 🎶 **Plectrum Instruments** (e.g., Banduria, Octavina)
- 🥁 **Percussion Instruments** (e.g., Drum, Tambourine)

Each instrument class implements behaviors unique to its type (e.g., `pluck()`, `strum()`, `blow_air()`, `hit()`), 
while adhering to a shared interface via an abstract base class `MusicalInstrument`.

This design demonstrates:
- **Abstraction** through the use of abstract base classes  
- **Inheritance** for hierarchical and multi-level structure  
- **Polymorphism** to allow dynamic behavior via shared method calls  
- **Encapsulation** to group data and behaviors within each class  

---

## 🔍 Features

- Abstract base class for all instruments (`MusicalInstrument`)
- Intermediate classes (e.g., `StringInstrument`, `PlectrumInstrument`)
- Specific methods for each instrument (e.g., `strum()`, `blow_air()`)
- Demonstration of runtime polymorphism using a loop of mixed instrument types

---

## ▶️ How to Run the Program

1. Make sure you have **Python 3** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/l4hgs/Team-2-CS1205-Laboratory-Activity-3.git
   cd Team-2-CS1205-Laboratory-Activity-3
3. Run the main script:
   ```bash
   python musical_instrument.py

---

## 🙏 Acknowledgements
We would like to express our sincere gratitude to Ma'am Fatima, our CS1205 Laboratory instructor, for her guidance and support throughout this project. Her clear explanations and encouragement helped us understand the core concepts of object-oriented programming and inspired us to apply them creatively in this mini Python orchestra simulation.

This project was made more enjoyable and meaningful because of the collaborative learning environment she fostered.
   
