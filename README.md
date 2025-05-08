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
   
