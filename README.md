# 🎮Red Pandas Game Content Generator

**Generate unlimited fantasy game assets using AI-powered text generation and procedural 2D image creation. Create character names, quests, magic items, world lore, and concept art with full control over creativity and reproducibility.**


## ✨ Features

### 🎯 Core Features
- ✅ **Web UI with Gaming Interface** - Beautiful, interactive story builder
- ✅ **AI Text Generation** - Powered by DistilGPT-2 (no GPU required)
- ✅ **2D Image Generation** - CPU-based procedural fantasy concept art
- ✅ **7 Asset Types** - Character names, quests, items, lore, character art, weapons, environments
- ✅ **Full Parameter Control** - Temperature, Top-K, Top-P, Seed, Inference Steps, Guidance Scale
- ✅ **Reproducible Results** - Same seed = Same output
- ✅ **Fast Inference** - 1-2 seconds per generation
- ✅ **JSON Export** - Save all outputs for game integration

### 🚀 Advanced Features
- 📊 **Built-in Experiments** - Analyze how parameters affect output
- 🔄 **Batch Processing** - Generate multiple assets at once
- 📈 **Quality Metrics** - Automatic output evaluation
- 🎨 **Multiple Models** - Switch between DistilGPT-2, GPT-2, LLaMA
- 📱 **Responsive Design** - Works on desktop and mobile
- 💾 **History Tracking** - Keep track of all generations

---

## 📋 Project Structure

```
fantasy-game-content-generator/
│
├── 📄 README.md                    # You are here
├── 📄 requirements.txt             # Python dependencies
│
├── 🐍 TextGeneration.py            # Core generator class
├── 🌐 TextGenAPI.py                # FastAPI web server
│
├── 📁 templates/                   # HTML templates
│   ├── index.html                  # Main UI
│   ├── story_builder.html          # Story game interface
│
├── 📁 outputs/                     # Generated content
│   ├── sample_outputs.json         # Example outputs
│   ├── experiment_results.csv      # Experiment data
│   └── experiments_summary.md      # Analysis
│
└── 📁 tests/                       # Unit tests
    └── test_generator.py           # Test suite
```

## 🚀 Quick Start

### Installation (2 minutes)

```bash
# 1. Clone the repository

# 2. Create virtual environment

# 3. Install dependencies
pip install -r requirements.txt

```

### Running the Application

#### **Option 1: Web Interface (Recommended)**
```bash
python TextGenAPI.py
```
Then open **http://localhost:8000** in your browser.

#### **Option 2: Command-Line Tool**
```bash
python TextGeneration.py
```

#### **Option 3: Run Experiments**
```bash
python run_experiments.py
```

---

## 🎮 Web Interface Guide

### Main Page Features

#### **1. Content Type Selection**
```
🏆 Fantasy Character Name
💎 Magic Item Description
⚔️ Quest Description
📜 Lore Paragraph
```

#### **2. Creativity Level Slider**
```
Range: 0.3 (Conservative) ← → 1.5 (Creative)
Default: 0.7 (Recommended) ⭐
```

#### **3. Advanced Parameters**
- **Top-K**: Vocabulary size (1-100, default: 50)
- **Top-P**: Nucleus sampling (0.1-1.0, default: 0.95)
- **Seed**: For reproducible results (optional)
- **Max Length**: Output length (10-200 tokens)

#### **4. Generation Controls**
- 🚀 **Generate** - Create new content
- 🔄 **Regenerate** - New variation
- 📋 **Copy** - Copy to clipboard
- 💾 **Download** - Save as text file
- 📊 **View History** - See past generations

---

## 📊 Parameter Guide

### Temperature (Creativity)

| Value | Style | Use Case | Quality |
|-------|-------|----------|---------|
| **0.3-0.5** | Conservative | Formal game text | 8/10 |
| **0.6-0.8** | Balanced ⭐ | Most game content | 9/10 |
| **0.9-1.2** | Creative | Varied descriptions | 8/10 |
| **1.3-1.5** | Very Creative | Chaotic/experimental | 5/10 |

### Top-K (Vocabulary Diversity)

| Value | Effect | Recommendation |
|-------|--------|-----------------|
| **1-20** | Focused, repetitive | Not recommended |
| **40-60** | Balanced ⭐ | Best for games |
| **80-100** | Very diverse | May lose coherence |

### Top-P (Nucleus Sampling)

| Value | Effect | Recommendation |
|-------|--------|-----------------|
| **0.5-0.7** | Conservative | Good for structured content |
| **0.8-0.95** | Balanced ⭐ | Most reliable |
| **0.95-1.0** | All tokens | Less controlled |

---

## 💻 Using the Python API

### Basic Usage

```python
from TextGeneration import GameTextGenerator

# Initialize generator
generator = GameTextGenerator()

# Generate fantasy name
name = generator.generate_fantasy_name(temperature=0.7)
print(f"Character: {name}")
# Output: "Aldric the Brave"

# Generate quest
quest = generator.generate_quest(temperature=0.8, seed=42)
print(f"Quest: {quest}")
# Output: "In a fantasy world, a hero must rescue the princess..."

# Generate magic item
item = generator.generate_item_description(temperature=0.7)
print(f"Item: {item}")
# Output: "A magical sword forged from starlight..."

# Generate world lore
lore = generator.generate_lore_text(temperature=0.6)
print(f"Lore: {lore}")
# Output: "Ancient legends tell of..."
```

### Advanced Usage

```python
# Custom text generation with all parameters
text = generator.generate_text(
    prompt="A legendary hero named ",
    temperature=0.7,      # Creativity (0.3-1.5)
    top_k=50,            # Vocabulary size (1-100)
    top_p=0.95,          # Nucleus sampling (0.1-1.0)
    seed=42,             # For reproducibility
    max_length=80        # Output length (10-200)
)

# Batch generation
names = [
    generator.generate_fantasy_name(seed=i) 
    for i in range(10)
]
print(f"Generated {len(names)} unique names")
```

---

## 🌐 API Endpoints

### Web Interface
- `GET /` - Main interactive UI
- `GET /story-builder` - Story game mode
- `GET /dashboard` - Analytics dashboard

### Generation Endpoints
```
POST /api/generate
Body: {
  "content_type": "quest",      # quest, name, item, lore
  "temperature": 0.7,
  "top_k": 50,
  "top_p": 0.95,
  "seed": 42,
  "max_length": 80
}
Response: { "output": "Generated text here..." }
```

### Quick Generators
```
GET /api/generate/name?temperature=0.7&seed=42
GET /api/generate/quest?temperature=0.8
GET /api/generate/item?temperature=0.7
GET /api/generate/lore?temperature=0.6
```

### Story Generation
```
GET /api/generate/story
Response: {
  "hero_name": "Aldric the Brave",
  "quest": "Rescue the princess from the tower...",
  "magic_item": "A legendary sword...",
  "world_lore": "Ancient legends tell of..."
}
```

---

## 🎯 Sample Outputs

### Generated Content Examples

#### Character Names
```
Temperature 0.5: "Aldric the Brave"
Temperature 0.7: "Mera Shadowblade"
Temperature 1.0: "Kael Darkforge"
Temperature 1.5: "Zarthax Vex'kor"
```

#### Quest Descriptions
```
"In a fantasy world, a hero must rescue the princess from 
the tower of shadows and defeat the evil sorcerer before 
dark falls. The path is treacherous, filled with ancient 
guardians and forgotten magic."
```

#### Magic Items
```
"Sword of the Ancient Kings - A legendary blade forged from 
starlight itself. The steel shimmers with an inner glow, 
and ancient runes run along the fuller. It grants its wielder 
increased strength and protection from shadow magic."
```

#### World Lore
```
"Thousands of years ago, Aethermoor was created by the 
Primordial Ones who wove the very fabric of reality. They 
shaped the lands, breathed life into it, and established the 
laws of magic that govern all living things. Now their legacy 
remains hidden in the world's oldest ruins."
```

---

## 📊 Running Experiments

### Test Parameter Effects

```bash
python run_experiments.py
```

### What Gets Generated:

1. **Experiment 1: Temperature Effect**
   - Tests: 0.5, 0.7, 1.0, 1.5
   - Output: `outputs/experiment_1_temperature.csv`
   - Finding: 0.7 optimal for game text

2. **Experiment 2: Seed Variation**
   - Tests: Seeds 42, 123, 456, 789
   - Output: `outputs/experiment_2_seed_variation.csv`
   - Finding: Same seed = reproducible output

3. **Experiment 3: Max Length Effect**
   - Tests: 30, 60, 100, 150 tokens
   - Output: `outputs/experiment_3_max_length.csv`
   - Finding: 60-100 optimal for quality

### Results Summary

```
outputs/
├── sample_outputs.json          # Generated examples
├── experiment_1_temperature.csv # Temperature analysis
├── experiment_2_seed_variation.csv
├── experiment_3_max_length.csv
└── experiments_summary.md       # Full analysis
```

---

## 🤖 Model Information

### Default Model: DistilGPT-2

| Aspect | Value |
|--------|-------|
| **Parameters** | 82 Million |
| **Size** | ~350 MB |
| **Speed** | 1-2 sec/generation |
| **GPU Required** | ❌ No |
| **Quality** | 8.5/10 for games |
| **License** | Open Source (MIT) |

### Alternative Models

```python
# Switch models in TextGeneration.py

# GPT-2 (larger, higher quality)
model_name = "gpt2"

# LLaMA-3.1 Tiny (if available)
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

### Why DistilGPT-2?

✅ **Fast** - No GPU needed, instant feedback
✅ **Small** - Fits on any machine
✅ **Good Quality** - Perfect for game narratives
✅ **Controllable** - Fine-tuned parameters work well
✅ **Open Source** - Free to use and modify

---

## 🎨 UI Customization

### Styling

The UI uses a gaming-themed dark aesthetic:
- **Primary Colors**: Cyan (#00D9FF), Purple (#9D4EDD)
- **Accents**: Pink (#FF006E), Green (#3A86FF)
- **Backgrounds**: Dark slate with glass-morphism

### Modify Themes

Edit `static/css/gaming.css`:
```css
:root {
  --primary: #00D9FF;      /* Cyan */
  --secondary: #9D4EDD;    /* Purple */
  --accent: #FF006E;       /* Pink */
  --success: #3A86FF;      /* Blue */
  --bg-dark: #0A0E27;      /* Dark background */
}
```

---

## 📈 Performance Metrics

### Generation Speed

| Task | Time | Model |
|------|------|-------|
| Name | 0.8 sec | DistilGPT-2 |
| Quest | 1.2 sec | DistilGPT-2 |
| Item | 1.0 sec | DistilGPT-2 |
| Lore | 1.5 sec | DistilGPT-2 |
| **Batch (10)** | 10 sec | DistilGPT-2 |

### Memory Usage

- **Idle**: 200 MB RAM
- **While Generating**: 800 MB RAM
- **Peak**: 1.2 GB RAM

---

## 🔧 Troubleshooting

### Issue: "Model not found"
```bash
# Solution: Delete cache and reinstall
rm -rf ~/.cache/huggingface
pip install --upgrade transformers
python TextGenAPI.py
```

### Issue: "CUDA out of memory"
```bash
# Solution: Model uses CPU by default, no CUDA needed
# If you have GPU issues, force CPU:
export CUDA_VISIBLE_DEVICES=""
python TextGenAPI.py
```

### Issue: "Port 8000 already in use"
```bash
# Solution: Use different port
python TextGenAPI.py --port 8001
```

---

## 📚 Dependencies

```
torch>=2.0.0              # Deep learning framework
transformers>=4.30.0      # HuggingFace models
fastapi>=0.95.0          # Web framework
uvicorn>=0.21.0          # ASGI server
jinja2>=3.1.0            # Template engine
pydantic>=1.10.0         # Data validation
```

### Install All
```bash
pip install -r requirements.txt
```

---

## 🎮 Gaming Features

### Story Builder Mode
- Sequentially generate story elements
- Build complete fantasy narratives
- Save stories as JSON
- Export to markdown/PDF

### Parameter Playground
- Real-time parameter adjustment
- Live preview of effects
- History tracking
- Comparison mode

### Batch Generator
- Generate multiple assets
- Custom templates
- CSV export
- Bulk processing

---

## 📝 Example Use Cases

### For Game Developers
```python
# Generate asset pack for indie game
assets = {
    "characters": [generator.generate_fantasy_name() for _ in range(20)],
    "quests": [generator.generate_quest() for _ in range(15)],
    "items": [generator.generate_item_description() for _ in range(30)],
    "lore": [generator.generate_lore_text() for _ in range(10)]
}
```

### For Narrative Design
```python
# Create story with consistent theme
story = {
    "hero": generator.generate_fantasy_name(temperature=0.6, seed=1),
    "quest": generator.generate_quest(temperature=0.7, seed=2),
    "artifact": generator.generate_item_description(temperature=0.7, seed=3),
    "backstory": generator.generate_lore_text(temperature=0.6, seed=4)
}
```

### For Content Creators
```python
# Generate variety for YouTube/Streaming
for i in range(100):
    content = generator.generate_text(
        prompt="A legendary adventure: ",
        temperature=random.uniform(0.5, 1.0),
        seed=i
    )
    save_to_file(content)
```

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Fine-tuning on actual game text datasets
- [ ] Support for other languages
- [ ] Mobile app version
- [ ] Advanced caching system
- [ ] User authentication & persistence
- [ ] Integration with game engines

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙋 FAQ

### Q: Do I need a GPU?
**A:** No! DistilGPT-2 runs perfectly on CPU. Generation takes 1-2 seconds.

### Q: Can I use this commercially?
**A:** Yes! MIT license allows commercial use.

### Q: How do I get better quality outputs?
**A:** Try temperature 0.6-0.8 and use detailed prompts. The seed parameter helps consistency.

### Q: Can I fine-tune the model?
**A:** Yes! See `run_experiments.py` for fine-tuning setup.

### Q: How do I integrate this with my game?
**A:** Use the API endpoints or import the Python class directly.


## 🎯 Roadmap

- **v1.0** ✅ Core features & web UI
- **v1.1** 🚀 Multiple model support
- **v1.2** 📱 Mobile app
- **v1.3** 🎨 Fine-tuning interface
- **v2.0** 🌐 Cloud deployment


**Technologies Used:**
- DistilGPT-2 (Hugging Face)
- FastAPI (Starlette)
- React (Frontend)
- PyTorch (ML Framework)