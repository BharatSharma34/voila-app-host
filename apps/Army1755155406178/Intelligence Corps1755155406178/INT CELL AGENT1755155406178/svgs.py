SVGs = {
    # --- Land Forces with silhouettes ---
    "Friendly Infantry": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Crossed rifles style -->
      <g stroke="white" stroke-width="4" stroke-linecap="round">
        <line x1="25" y1="45" x2="55" y2="15"/>
        <line x1="55" y1="45" x2="25" y2="15"/>
      </g>
    </svg>""",
    "Hostile Infantry": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <polygon points="40,4 76,30 40,56 4,30" fill="red"/>
      <g stroke="white" stroke-width="4" stroke-linecap="round">
        <line x1="25" y1="45" x2="55" y2="15"/>
        <line x1="55" y1="45" x2="25" y2="15"/>
      </g>
    </svg>""",
    "Neutral Infantry": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="green"/>
      <g stroke="white" stroke-width="4" stroke-linecap="round">
        <line x1="25" y1="45" x2="55" y2="15"/>
        <line x1="55" y1="45" x2="25" y2="15"/>
      </g>
    </svg>""",
    "Unknown Infantry": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="38" ry="28" fill="yellow"/>
      <g stroke="black" stroke-width="4" stroke-linecap="round">
        <line x1="25" y1="45" x2="55" y2="15"/>
        <line x1="55" y1="45" x2="25" y2="15"/>
      </g>
    </svg>""",
    "Friendly Armor": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Stylized tank tread -->
      <rect x="22" y="32" width="36" height="10" fill="white"/>
      <circle cx="30" cy="37" r="4" fill="blue"/>
      <circle cx="50" cy="37" r="4" fill="blue"/>
      <rect x="32" y="22" width="16" height="10" fill="white"/>
    </svg>""",
    "Hostile Armor": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <polygon points="40,4 76,30 40,56 4,30" fill="red"/>
      <rect x="22" y="32" width="36" height="10" fill="white"/>
      <circle cx="30" cy="37" r="4" fill="red"/>
      <circle cx="50" cy="37" r="4" fill="red"/>
      <rect x="32" y="22" width="16" height="10" fill="white"/>
    </svg>""",

    "Friendly Artillery": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Artillery cannon (barrel and wheel) -->
      <circle cx="40" cy="38" r="8" fill="white"/>
      <rect x="37" y="18" width="6" height="20" fill="white"/>
      <rect x="34" y="14" width="12" height="6" fill="white"/>
    </svg>""",
    "Hostile Artillery": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <polygon points="40,4 76,30 40,56 4,30" fill="red"/>
      <circle cx="40" cy="38" r="8" fill="white"/>
      <rect x="37" y="18" width="6" height="20" fill="white"/>
      <rect x="34" y="14" width="12" height="6" fill="white"/>
    </svg>""",
    "Friendly Engineer": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Bridge shape (engineering) -->
      <rect x="26" y="34" width="28" height="8" fill="white"/>
      <polygon points="26,34 40,20 54,34" fill="white"/>
    </svg>""",
    "Friendly Signal": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Lightning bolt -->
      <polyline points="38,20 44,32 36,32 42,44" fill="none" stroke="white" stroke-width="4"/>
    </svg>""",
    "Friendly Medical": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Caduceus (medical): stylized cross -->
      <rect x="36" y="20" width="8" height="20" fill="white"/>
      <rect x="30" y="28" width="20" height="8" fill="white"/>
    </svg>""",
    "Friendly Recon": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Binoculars (recon) -->
      <ellipse cx="34" cy="32" rx="6" ry="10" fill="white"/>
      <ellipse cx="46" cy="32" rx="6" ry="10" fill="white"/>
      <rect x="34" y="24" width="12" height="8" fill="blue"/>
    </svg>""",
    "Friendly SF": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Stylized spearhead -->
      <polygon points="40,12 47,48 40,40 33,48" fill="white"/>
    </svg>""",
    "Friendly HQ": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- HQ staff (flag at top left) -->
      <rect x="12" y="6" width="16" height="8" fill="white"/>
      <polygon points="12,6 12,14 20,10" fill="white"/>
    </svg>""",
    "Friendly CBRN": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Trefoil symbol (CBRN) -->
      <g fill="yellow" stroke="black" stroke-width="1">
        <circle cx="40" cy="30" r="5"/>
        <circle cx="40" cy="20" r="6"/>
        <circle cx="32" cy="36" r="6"/>
        <circle cx="48" cy="36" r="6"/>
      </g>
    </svg>""",
    "Friendly UAV": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Stylized drone (UAV) -->
      <rect x="36" y="24" width="8" height="16" fill="white"/>
      <line x1="20" y1="32" x2="60" y2="32" stroke="white" stroke-width="4"/>
    </svg>""",
    "Friendly Radar": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <!-- Parabolic radar dish -->
      <ellipse cx="40" cy="40" rx="14" ry="8" fill="white"/>
      <line x1="40" y1="40" x2="40" y2="25" stroke="white" stroke-width="3"/>
      <circle cx="40" cy="25" r="3" fill="white"/>
    </svg>""",
    # --- Intelligence / Info (use text as before) ---
    "Friendly INT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <text x="40" y="35" font-size="28" fill="white" text-anchor="middle">INT</text>
    </svg>""",
    "Hostile INT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <polygon points="40,4 76,30 40,56 4,30" fill="red"/>
      <text x="40" y="35" font-size="28" fill="white" text-anchor="middle">INT</text>
    </svg>""",
    "Neutral INT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="green"/>
      <text x="40" y="35" font-size="28" fill="white" text-anchor="middle">INT</text>
    </svg>""",
    "Unknown INT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="38" ry="28" fill="yellow"/>
      <text x="40" y="35" font-size="28" fill="black" text-anchor="middle">INT</text>
    </svg>""",
    "Friendly SIGINT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <text x="40" y="28" font-size="18" fill="white" text-anchor="middle">SIG</text>
      <text x="40" y="45" font-size="18" fill="white" text-anchor="middle">INT</text>
    </svg>""",
    "Friendly ELINT": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <rect width="80" height="60" fill="blue"/>
      <text x="40" y="28" font-size="18" fill="white" text-anchor="middle">EL</text>
      <text x="40" y="45" font-size="18" fill="white" text-anchor="middle">INT</text>
    </svg>""",
    # --- Air / Naval ---
    "Friendly Air": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="38" ry="28" fill="blue"/>
      <!-- Chevron/triangle for air -->
      <polygon points="40,14 54,46 26,46" fill="white"/>
    </svg>""",
    "Hostile Air": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="38" ry="28" fill="red"/>
      <polygon points="40,14 54,46 26,46" fill="white"/>
    </svg>""",
    "Neutral Air": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="38" ry="28" fill="green"/>
      <polygon points="40,14 54,46 26,46" fill="white"/>
    </svg>""",
    "Friendly Naval": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <!-- Blue horizontal oval for naval -->
      <ellipse cx="40" cy="30" rx="30" ry="12" fill="blue"/>
      <!-- Superstructure -->
      <rect x="34" y="16" width="12" height="8" fill="white"/>
    </svg>""",
    "Hostile Naval": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="30" ry="12" fill="red"/>
      <rect x="34" y="16" width="12" height="8" fill="white"/>
    </svg>""",
    "Neutral Naval": """<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">
      <ellipse cx="40" cy="30" rx="30" ry="12" fill="green"/>
      <rect x="34" y="16" width="12" height="8" fill="white"/>
    </svg>""",
}

def wrap_with_red_ring(inner_svg: str) -> str:
    """Wrap an existing 80x60 SVG with a red ring for critical highlighting.
    Assumes the inner svg is sized 80x60; we expand to 90x70 and draw a circle.
    """
    return f"""
<svg xmlns='http://www.w3.org/2000/svg' width='90' height='70' viewBox='0 0 90 70'>
  <circle cx='45' cy='35' r='30' fill='none' stroke='#dc2626' stroke-width='4'/>
  <g transform='translate(5,5)'>
    {inner_svg}
  </g>
</svg>
"""