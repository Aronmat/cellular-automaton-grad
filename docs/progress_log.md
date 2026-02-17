# Cellular Automaton – Progress Log

## Feb 10, 2026
- Built initial automaton engine
- Added grid update rules
- Created test_run.py
- Uploaded project to GitHub
## Feb 10, 2026 – Grid System
- Implemented Grid class
- Added random initialization
- Added alive cell counter
- Integrated with test script
## Feb 12, 2026 - Automaton & Testing Fixes
- Fixed grid.get_grid() and Grid.count_alive() methods
- Added CellularAutomaton.step() to advance one generation
- Updated test_run.py to correctly display inital and final grids
- Implemented CellularAutomaton.run() for multiple-step simulation
- Verified randomization and alive cell count functionality 
- updated imports and resolved module errors (from src.automaton import  CellularAutomaton)
## Feb 17, 2026 – Rule Customization & Visualization
- Added rules.json for customizable automaton rules
- Integrated JSON rule loading into automaton engine
- Implemented matplotlib live animation
- Added pause/resume via keyboard input