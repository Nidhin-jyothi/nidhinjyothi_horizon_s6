# Dynamic Circle Sketcher  

## Overview  
Dynamic Circle Sketcher is an interactive Pygame-based application that allows users to draw colorful circles dynamically. It tracks the total path length between circles and provides options to save sketches or reset the canvas.  

## Features  
- **Draw Circles**: Left-click to create expanding circles.  
- **Path Tracking**: Displays the total distance between connected circles.  
- **Erase Last Circle**: Right-click to remove the most recent circle.  
- **Save Sketch**: Press **'S'** to save the current drawing as an image.  
- **Clear Canvas**: Press **Spacebar** to reset everything.  

## Controls  
- **Left Click**: Start drawing a growing circle.  
- **Release Left Click**: Save the circle to the canvas.  
- **Right Click**: Undo the last drawn circle.  
- **'S' Key**: Save the sketch as `sketch.png`.  
- **Spacebar**: Clear all drawings.  

## Requirements   
- Pygame (`pip install pygame`)  

## How to Run  
1. Install dependencies:  
   ```sh
   pip install pygame
   ```  
2. Run the script:  
   ```sh
   python task1.py
   ```

