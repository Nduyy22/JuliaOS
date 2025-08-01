"""
Create a project banner integrated with JuliaOS framework
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon
import numpy as np

def create_juliaos_project_banner():
    """Create a comprehensive project banner with JuliaOS integration"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # JuliaOS inspired colors
    julia_purple = '#9558B2'  # Julia's signature purple
    julia_red = '#CB3C33'     # Julia's red
    julia_green = '#389826'   # Julia's green
    tech_cyan = '#00D4FF'     # Tech cyan
    tech_blue = '#0066FF'     # Tech blue
    dark_bg = '#0F0F23'       # Dark tech background
    gold = '#FFD700'          # Accent gold
    
    # Background with gradient effect
    background = FancyBboxPatch((0, 0), 16, 9,
                               boxstyle="round,pad=0",
                               facecolor=dark_bg, edgecolor='none')
    ax.add_patch(background)
    
    # Tech grid pattern
    for i in range(0, 17, 2):
        ax.axvline(i, color=julia_purple, alpha=0.08, linewidth=0.5)
    for i in range(0, 10, 2):
        ax.axhline(i, color=julia_purple, alpha=0.08, linewidth=0.5)
    
    # Left side - JuliaOS Framework Integration
    # JuliaOS logo area
    julia_center_x, julia_center_y = 3, 6
    
    # JuliaOS hexagonal framework
    radius = 1.5
    angles = np.linspace(0, 2*np.pi, 7)
    hex_x = julia_center_x + radius * np.cos(angles + np.pi/6)
    hex_y = julia_center_y + radius * np.sin(angles + np.pi/6)
    
    hexagon = Polygon(list(zip(hex_x, hex_y)), 
                     facecolor='none', edgecolor=julia_purple, linewidth=4)
    ax.add_patch(hexagon)
    
    # Julia's three dots
    julia_dots = [
        {'x': julia_center_x - 0.3, 'y': julia_center_y + 0.2, 'color': julia_red},
        {'x': julia_center_x + 0.3, 'y': julia_center_y + 0.2, 'color': julia_green},
        {'x': julia_center_x, 'y': julia_center_y - 0.3, 'color': julia_purple}
    ]
    
    for dot in julia_dots:
        julia_dot = Circle((dot['x'], dot['y']), 0.2, 
                          facecolor=dot['color'], edgecolor='white', linewidth=2)
        ax.add_patch(julia_dot)
    
    # JuliaOS text
    ax.text(julia_center_x, 4, 'JuliaOS', 
           ha='center', va='center', fontsize=20, fontweight='bold', 
           color=julia_purple, family='monospace')
    ax.text(julia_center_x, 3.5, 'Framework', 
           ha='center', va='center', fontsize=12, 
           color=tech_cyan, family='monospace')
    
    # Center - Main Project Title
    ax.text(8, 7.5, 'DeFi Guardian Swarm', 
           ha='center', va='center', fontsize=36, fontweight='bold', 
           color='white', family='monospace')
    
    ax.text(8, 6.8, 'AI-Powered Multi-Agent DeFi Protection System', 
           ha='center', va='center', fontsize=16, 
           color=tech_cyan, family='monospace')
    
    # Integration connection
    ax.plot([julia_center_x + 1.5, 5.5], [julia_center_y, 7], 
           color=julia_purple, linewidth=3, alpha=0.8, linestyle='--')
    ax.text(4.8, 6.5, 'Powered by', 
           ha='center', va='center', fontsize=10, 
           color=julia_purple, family='monospace', rotation=15)
    
    # Right side - Project Stats & Features
    stats_x = 13
    stats_y_start = 7.5
    
    stats = [
        {'label': '10 AI Agents', 'color': julia_green},
        {'label': '3 Swarms', 'color': julia_red},
        {'label': '98% Accuracy', 'color': gold},
        {'label': '<50ms Response', 'color': tech_cyan}
    ]
    
    for i, stat in enumerate(stats):
        y_pos = stats_y_start - i * 0.6
        
        # Stat box
        stat_box = FancyBboxPatch((stats_x - 1.2, y_pos - 0.2), 2.4, 0.4,
                                 boxstyle="round,pad=0.05",
                                 facecolor=stat['color'], edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(stat_box)
        
        ax.text(stats_x, y_pos, stat['label'], 
               ha='center', va='center', fontsize=12, fontweight='bold', 
               color='white', family='monospace')
    
    # Bottom - Three Swarms Visualization
    swarm_y = 3
    swarm_data = [
        {'name': 'RISK MANAGEMENT', 'x': 3, 'color': julia_red, 'agents': ['Portfolio', 'Liquidity', 'Volatility']},
        {'name': 'MEV PROTECTION', 'x': 8, 'color': julia_green, 'agents': ['Mempool', 'Sandwich', 'Optimizer']},
        {'name': 'GOVERNANCE', 'x': 13, 'color': julia_purple, 'agents': ['Proposal', 'Sentiment', 'Voting']}
    ]
    
    for swarm in swarm_data:
        # Swarm container
        swarm_box = FancyBboxPatch((swarm['x'] - 1.5, swarm_y - 1), 3, 2,
                                  boxstyle="round,pad=0.1",
                                  facecolor=swarm['color'], edgecolor=tech_cyan, linewidth=2, alpha=0.8)
        ax.add_patch(swarm_box)
        
        # Swarm title
        ax.text(swarm['x'], swarm_y + 0.5, swarm['name'], 
               ha='center', va='center', fontsize=10, fontweight='bold', 
               color='white', family='monospace')
        
        # Agent indicators
        for i, agent in enumerate(swarm['agents']):
            agent_y = swarm_y - 0.2 - i * 0.3
            agent_circle = Circle((swarm['x'], agent_y), 0.08, 
                                facecolor='white', edgecolor=swarm['color'], linewidth=1)
            ax.add_patch(agent_circle)
            ax.text(swarm['x'] + 0.3, agent_y, agent, 
                   ha='left', va='center', fontsize=8, 
                   color='white', family='monospace')
    
    # Connecting lines between swarms
    for i in range(len(swarm_data) - 1):
        start_x = swarm_data[i]['x'] + 1.5
        end_x = swarm_data[i + 1]['x'] - 1.5
        ax.plot([start_x, end_x], [swarm_y, swarm_y], 
               color=tech_cyan, linewidth=2, alpha=0.6)
    
    # Bottom banner - Competition info
    banner = FancyBboxPatch((1, 0.3), 14, 0.8,
                           boxstyle="round,pad=0.1",
                           facecolor=julia_purple, edgecolor=gold, linewidth=3)
    ax.add_patch(banner)
    
    ax.text(8, 0.7, '🏆 JuliaOS Bounty Competition Entry - $1,500 First Place Prize 🏆', 
           ha='center', va='center', fontsize=16, fontweight='bold', 
           color='white', family='monospace')
    
    # Corner decorations
    corner_decorations = [
        (0.5, 8.5), (15.5, 8.5), (0.5, 0.5), (15.5, 0.5)
    ]
    
    for corner in corner_decorations:
        decoration = Circle(corner, 0.15, facecolor=gold, alpha=0.8)
        ax.add_patch(decoration)
    
    # Tech accent lines
    accent_lines = [
        [(0, 8), (2, 8)], [(14, 8), (16, 8)],
        [(0, 1), (2, 1)], [(14, 1), (16, 1)]
    ]
    
    for line in accent_lines:
        ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 
               color=tech_cyan, linewidth=3, alpha=0.8)
    
    plt.tight_layout()
    plt.savefig('c:/Project/superearn/JuliaOS/juliaos_project_banner.png', 
                dpi=300, bbox_inches='tight', facecolor=dark_bg, transparent=False)
    plt.close()
    print("✅ JuliaOS project banner created!")

if __name__ == "__main__":
    print("🎨 Creating comprehensive project banner with JuliaOS integration...")
    create_juliaos_project_banner()
    print("\n🎉 Project banner created: juliaos_project_banner.png")
    print("🔥 Banner features:")
    print("   - JuliaOS framework integration with signature colors")
    print("   - Julia's three-dot logo prominently displayed")
    print("   - Complete project overview with stats")
    print("   - 3 DeFi swarms visualization")
    print("   - Competition entry branding")
    print("   - Perfect for social media headers! 🚀")
