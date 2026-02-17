# Cellular Automaton – Progress Log

## Feb 10, 2026
- Built initial automaton engine
- Added grid update rules
- Created test_run.py
- Uploaded project to GitHub
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
- Implemented matplotlib animation
- Added pause/resume with spacebar
- Enabled cell editing via mouse clicks
- Integrated visualizer with automaton engine
- Added pause/resume via spacebar
- Fixed state loading size mismatch
- Added auto-centering for small patterns
- Enabled preset pattern demos (glider)
- Added menu for inital starts option random intial and custom