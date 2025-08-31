# Earth-Moon-Mars Simulation Prototype 

This folder contains a **simple 3D prototype simulation** of the Earth, Moon, and Mars revolving around the Sun using **VPython**.  

---

## Purpose
The goal of this prototype is to **visualize basic orbital motion** using **parametric circular equations** in 3D space.  
It serves as the **first step** in a larger project of astronomical simulations.

---

## Features
- **Earth orbiting the Sun**  
- **Moon orbiting the Earth** with tilt  
- **Mars orbiting the Sun** with slight orbital tilt  
- **Trail visualization** to track orbital paths  
- **Adjustable speed** using a slider  
- **Date display** showing simulated days and years  
- **Sun glow** using emissive materials and light source  

---

## Technical Details
- Orbits modeled with **parametric circular motion**:  
  \[
     x = R * cos(theta)
  
     y = R * sin(theta) * cos(tilt)
  
     z = R * sin(theta) * sin(tilt)
  \]  
- Simulation speed can be scaled for faster or slower motion.  
- Moon trail is limited to improve performance and visualization clarity.  

---

## Future Work
- Replace circular approximation with **Kepler’s laws** for more realistic planetary motion  
- Add other celestial phenomena like **black holes, pulsars, supernovae** in this repo  

---


