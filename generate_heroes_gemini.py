#!/usr/bin/env python3
"""
Generate ModelIt! K12 Newsletter Hero Images with Google Gemini
Uses gemini-2.5-flash-image (Nano Banana) - FREE and VERIFIED WORKING
"""

import sys
import os
import base64
from dotenv import load_dotenv
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

load_dotenv('C:/Users/MarieLexisDad/.env')

# Check for google-generativeai library
try:
    import google.generativeai as genai
except ImportError:
    print("Installing google-generativeai...")
    import subprocess
    subprocess.check_call(['pip', 'install', '-q', 'google-generativeai'])
    import google.generativeai as genai

# Configure API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=api_key)

# Create output directory
output_dir = Path('C:/Users/MarieLexisDad/modelitk12-newsletter/assets/images')
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("GENERATING MODELIT! K12 NEWSLETTER HERO IMAGES")
print("=" * 80)
print("Using: Google Gemini 2.5 Flash Image (Nano Banana)")
print("Method: Official Google AI API - FREE")
print()

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash-image')

# Newsletter hero prompts
heroes = {
    "week1-hero": """Create a vibrant, photorealistic close-up image of a modern middle school science classroom:

COMPOSITION: Centered, tight framing on students and screens - NO black bars, NO letterboxing

SUBJECTS:
- 3-4 diverse students (ages 11-14: African American, Latino, Asian)
- Close-up view, students fill the frame
- Excited, engaged, collaborating around a laptop
- Pointing at screen, discussing animatedly

TECHNOLOGY (PROMINENT):
- Laptop in foreground showing colorful biological cell model
- Interactive molecular pathway diagram clearly visible on screen
- Bright, colorful scientific visualizations

SETTING:
- Bright modern classroom (background)
- Natural sunlight, professional educational environment
- Focus on students and technology (not empty space)

COLOR PALETTE:
- Navy blue (#030C3C) and bright blue (#0F6ACE) prominent in displays
- Colorful scientific visualizations (reds, blues, greens)
- Warm skin tones and natural classroom colors

MOOD: Inspiring, collaborative, exciting science education
STYLE: Professional educational photography, tight composition, NO EMPTY SPACE, NO BLACK BARS
FOCUS: Students actively engaged with computational biology - FILL THE ENTIRE FRAME""",

    "week2-hero": """Create a professional close-up image of Cell Collective platform:

COMPOSITION: Tight framing on screen content - NO black bars, NO letterboxing, FILL ENTIRE FRAME

MAIN ELEMENT:
- Close-up of monitor showing Cell Collective platform
- Screen FILLS THE ENTIRE IMAGE - no empty space
- Intricate biological network diagram prominently displayed
- Colorful interactive cellular models with nodes and connections

NETWORK VISUALIZATION (DETAILED):
- Interconnected pathways with navy blue (#030C3C) and bright blue (#0F6ACE) nodes
- Molecular interactions as connecting lines
- Light blue (#38aefd) accents throughout
- Complex, beautiful systems biology visualization
- Multiple biological components clearly visible

SETTING:
- Modern professional display
- Soft professional lighting on screen
- No black bars, no empty space - ZOOM IN ON THE VISUALIZATION

COLOR PALETTE:
- Navy blue (#030C3C) and bright blue (#0F6ACE) dominant
- Light blue (#38aefd) network connections
- Colorful biological components (greens, reds, purples)
- High contrast, visually striking

MOOD: Cutting-edge research, scientific innovation, beautiful complexity
STYLE: Professional screen capture, tight framing, NO EMPTY SPACE, NO BLACK BARS
FOCUS: Cell Collective network visualization - FILL ENTIRE IMAGE WITH COLORFUL BIOLOGY"""
}

results = []

for hero_id, prompt in heroes.items():
    print(f"\nGenerating: {hero_id}...")
    print(f"Prompt: {prompt[:100]}...")

    try:
        # Generate image
        response = model.generate_content(prompt)

        print(f"  Response received, checking for image data...")

        # Check if image was generated
        if not response.candidates or len(response.candidates) == 0:
            print(f"[FAILED] No candidates in response")
            print(f"  Response: {response}")
            continue

        candidate = response.candidates[0]
        print(f"  Got candidate, checking content...")

        # Extract image data
        if not hasattr(candidate, 'content') or not candidate.content.parts:
            print(f"[FAILED] No content.parts in response")
            print(f"  Candidate: {candidate}")
            continue

        print(f"  Found {len(candidate.content.parts)} parts")

        image_saved = False
        for i, part in enumerate(candidate.content.parts):
            print(f"  Part {i}: {type(part).__name__}")

            if hasattr(part, 'inline_data') and part.inline_data:
                print(f"    Found inline_data!")
                # Save image - get binary data
                image_data = part.inline_data.data

                if not image_data or len(image_data) == 0:
                    print(f"[FAILED] inline_data.data is empty!")
                    continue

                filepath = output_dir / f"{hero_id}.jpg"

                with open(filepath, 'wb') as f:
                    f.write(image_data)

                print(f"[SUCCESS] Saved {filepath} ({len(image_data)/1024:.1f} KB)")
                results.append(hero_id)
                image_saved = True
                break

        if not image_saved:
            print(f"[FAILED] No inline_data with content found in any part")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

print(f"\n\n{'=' * 80}")
print(f"GENERATION COMPLETE")
print(f"{'=' * 80}")
print(f"Generated: {len(results)}/2 images")
print(f"Output: {output_dir}")
print()

if len(results) == 2:
    print("[COMPLETE] Both newsletter hero images generated!")
    print(f"   - Week 1: {output_dir / 'week1-hero.jpg'}")
    print(f"   - Week 2: {output_dir / 'week2-hero.jpg'}")
else:
    print(f"[WARNING] Only {len(results)}/2 images generated successfully")

print("\nNext steps:")
print("1. Review images in assets/images/")
print("2. Commit changes to Git")
print("3. Push to GitHub to rebuild newsletter")
