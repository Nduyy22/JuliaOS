"""
Create a tech-style logo integrated with JuliaOS framework
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon
import numpy as np

def create_juliaos_tech_logo():
    """Create a futuristic tech logo integrated with JuliaOS branding"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # JuliaOS inspired colors (Julia language colors + tech)
    julia_purple = '#9558B2'  # Julia's signature purple
    julia_red = '#CB3C33'     # Julia's red
    julia_green = '#389826'   # Julia's green
    tech_cyan = '#00D4FF'     # Tech cyan
    tech_blue = '#0066FF'     # Tech blue
    dark_bg = '#0F0F23'       # Dark tech background
    
    # Background with tech grid pattern
    background = FancyBboxPatch((0, 0), 12, 8,
                               boxstyle="round,pad=0",
                               facecolor=dark_bg, edgecolor='none')
    ax.add_patch(background)
    
    # Tech grid lines
    for i in range(0, 13, 2):
        ax.axvline(i, color=julia_purple, alpha=0.1, linewidth=0.5)
    for i in range(0, 9, 2):
        ax.axhline(i, color=julia_purple, alpha=0.1, linewidth=0.5)
    
    # Central JuliaOS integration symbol
    center_x, center_y = 6, 4
    
    # Main hexagonal frame (representing JuliaOS framework)
    radius = 2.2
    angles = np.linspace(0, 2*np.pi, 7)
    hex_x = center_x + radius * np.cos(angles + np.pi/6)
    hex_y = center_y + radius * np.sin(angles + np.pi/6)
    
    # Outer hexagon with JuliaOS colors
    hexagon = Polygon(list(zip(hex_x, hex_y)), 
                     facecolor='none', edgecolor=julia_purple, linewidth=4)
    ax.add_patch(hexagon)
    
    # Inner tech core
    inner_radius = radius * 0.7
    inner_hex_x = center_x + inner_radius * np.cos(angles + np.pi/6)
    inner_hex_y = center_y + inner_radius * np.sin(angles + np.pi/6)
    
    inner_hexagon = Polygon(list(zip(inner_hex_x, inner_hex_y)), 
                           facecolor=tech_blue, edgecolor=tech_cyan, linewidth=2, alpha=0.8)
    ax.add_patch(inner_hexagon)
    
    # JuliaOS "Julia" three dots symbol in center
    julia_dots = [
        {'x': center_x - 0.3, 'y': center_y + 0.2, 'color': julia_red},
        {'x': center_x + 0.3, 'y': center_y + 0.2, 'color': julia_green},
        {'x': center_x, 'y': center_y - 0.3, 'color': julia_purple}
    ]
    
    for dot in julia_dots:
        julia_dot = Circle((dot['x'], dot['y']), 0.25, 
                          facecolor=dot['color'], edgecolor='white', linewidth=2)
        ax.add_patch(julia_dot)
    
    # DeFi Guardian agents orbiting around JuliaOS core
    agent_radius = 0.15
    orbit_radius = 1.4
    num_agents = 10
    
    for i in range(num_agents):
        angle = (2 * np.pi * i) / num_agents
        agent_x = center_x + orbit_radius * np.cos(angle)
        agent_y = center_y + orbit_radius * np.sin(angle)
        
        # Cycle through colors
        colors = [tech_cyan, julia_green, julia_red, julia_purple, tech_blue]
        agent_color = colors[i % len(colors)]
        
        agent = Circle((agent_x, agent_y), agent_radius, 
                      facecolor=agent_color, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(agent)
        
        # Connection lines to center
        ax.plot([center_x, agent_x], [center_y, agent_y], 
               color=agent_color, linewidth=1, alpha=0.5)
    
    # Three swarm clusters
    swarm_positions = [
        (2.5, 6.5),  # Top left
        (9.5, 6.5),  # Top right  
        (6, 1.5)     # Bottom center
    ]
    
    swarm_names = ['RISK\nMANAGEMENT', 'MEV\nPROTECTION', 'GOVERNANCE\nADVISORY']
    swarm_colors = [julia_red, julia_green, julia_purple]
    
    for i, (pos, name, color) in enumerate(zip(swarm_positions, swarm_names, swarm_colors)):
        # Swarm container
        swarm_box = FancyBboxPatch((pos[0] - 1, pos[1] - 0.8), 2, 1.6,
                                  boxstyle="round,pad=0.1",
                                  facecolor=color, edgecolor=tech_cyan, linewidth=2, alpha=0.8)
        ax.add_patch(swarm_box)
        
        ax.text(pos[0], pos[1], name, 
               ha='center', va='center', fontsize=9, fontweight='bold', 
               color='white', family='monospace')
        
        # Connection to main framework
        ax.plot([center_x, pos[0]], [center_y, pos[1]], 
               color=color, linewidth=3, alpha=0.6, linestyle='--')
    
    # Tech circuit connections
    circuit_points = [
        (1, 2), (1, 6), (11, 6), (11, 2), (1, 2)  # Border circuit
    ]
    
    for i in range(len(circuit_points) - 1):
        ax.plot([circuit_points[i][0], circuit_points[i+1][0]], 
               [circuit_points[i][1], circuit_points[i+1][1]], 
               color=tech_cyan, linewidth=1, alpha=0.4)
    
    # Corner tech nodes
    corner_nodes = [(1, 2), (1, 6), (11, 6), (11, 2)]
    for node in corner_nodes:
        tech_node = Circle(node, 0.1, facecolor=tech_cyan, alpha=0.8)
        ax.add_patch(tech_node)
    
    # Title with JuliaOS integration
    ax.text(6, 0.8, 'DeFi Guardian Swarm', 
           ha='center', va='center', fontsize=28, fontweight='bold', 
           color='white', family='monospace')
    
    ax.text(6, 0.4, 'Powered by JuliaOS Framework', 
           ha='center', va='center', fontsize=14, 
           color=julia_purple, family='monospace')
    
    # JuliaOS branding
    ax.text(1, 7.5, 'JuliaOS', 
           ha='left', va='center', fontsize=16, fontweight='bold', 
           color=julia_purple, family='monospace')
    ax.text(1, 7.1, 'AI Agent Framework', 
           ha='left', va='center', fontsize=10, 
           color=tech_cyan, family='monospace')
    
    # Tech specs
    ax.text(11, 7.5, '10 AI Agents', 
           ha='right', va='center', fontsize=12, fontweight='bold', 
           color=julia_green, family='monospace')
    ax.text(11, 7.1, '3 Swarms', 
           ha='right', va='center', fontsize=12, fontweight='bold', 
           color=julia_red, family='monospace')
    ax.text(11, 6.7, '98% Accuracy', 
           ha='right', va='center', fontsize=12, fontweight='bold', 
           color=tech_cyan, family='monospace')
    
    plt.tight_layout()
    plt.savefig('c:/Project/superearn/JuliaOS/juliaos_tech_logo.png', 
                dpi=300, bbox_inches='tight', facecolor=dark_bg, transparent=False)
    plt.close()
    print("✅ JuliaOS integrated tech logo created!")

if __name__ == "__main__":
    print("🎨 Creating tech logo integrated with JuliaOS framework...")
    create_juliaos_tech_logo()
    print("\n🎉 Tech logo created: juliaos_tech_logo.png")
    print("🔥 Features:")
    print("   - JuliaOS signature purple/red/green colors")
    print("   - Julia's three-dot symbol in center")
    print("   - 10 AI agents orbiting around JuliaOS core")
    print("   - 3 DeFi swarms with framework integration")
    print("   - Futuristic tech grid design")
    print("   - Perfect for Twitter posting! 🚀")
