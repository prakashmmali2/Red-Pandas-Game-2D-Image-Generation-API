# 🎮 Fantasy Game Content Generator

Generate unlimited fantasy game assets using AI. Create character names, quests, magic items, and world lore with a beautiful web interface.

## ✨ Features

- 🎯 **4 Content Types** - Names, quests, items, lore
- 🌐 **Web UI** - Beautiful gaming-themed interface
- 🔌 **REST API** - 10+ endpoints for integration
- ⚙️ **Parameter Control** - Temperature, seed, top_k, top_p
- 💾 **Export** - Save as JSON or text
- ⚡ **Fast** - 1-2 seconds per generation
- 📱 **Responsive** - Mobile-friendly design

---

## 🚀 Quick Start

### Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
python TextGenAPI.py

# 3. Open browser
http://localhost:8000
```

## 📊 Sample Outputs

| Type | Example |
|------|---------|
| **Name** | "Mera Shadowblade" |
| **Quest** | "In a fantasy world, a hero must rescue the princess from the tower of shadows..." |
| **Item** | "Sword of the Ancient Kings - forged from starlight..." |
| **Lore** | "Ancient legends tell of a great wizard who lived in the mountains..." |

---

## 🎨 Web UI

**Controls:**
- 📚 Content Type dropdown (quest, name, item, lore)
- 🎨 Creativity slider (0.3 - 1.5)
- 🎲 Random seed (optional)
- 🚀 Generate button

**Features:**
- Copy to clipboard
- Download as .txt
- Regenerate variations
- View history

---

## 🔧 Parameters Guide

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| Temperature | 0.3-1.5 | 0.7 | Creativity level |
| Top-K | 1-100 | 50 | Vocabulary size |
| Top-P | 0.1-1.0 | 0.95 | Sampling diversity |
| Seed | Any int | Random | Reproducibility |
| Max Length | 10-200 | 80 | Output length |

**Recommended:** Temperature 0.7 (best balance for games)

---

## 📁 Project Structure

```
fantasy-game-content-generator/
├── TextGeneration.py         # Core generator
├── TextGenAPI.py             # Web server
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── outputs/                  # Generated files
│   ├── sample_outputs.json
│   └── generation_history.json
└── templates/
    └── index.html            # Web UI
```

---

## 🔌 API Endpoints

```
GET  /                          # Web interface
POST /api/generate              # Custom generation
GET  /api/generate/name         # Quick name
GET  /api/generate/quest        # Quick quest
GET  /api/generate/item         # Quick item
GET  /api/generate/lore         # Quick lore
GET  /api/generate/story        # Complete story
GET  /api/history               # View history
GET  /health                    # Status check
```

## 📊 Performance

| Metric | Value |
|--------|-------|
| Model | DistilGPT-2 (82M) |
| Speed | 1-2 sec/generation |
| GPU | Not required |
| Memory | 800MB-1.2GB |
| Model Size | 350MB |

---

## 📋 Requirements

```
torch>=2.0.0
transformers>=4.30.0
fastapi>=0.95.0
uvicorn>=0.21.0
pydantic>=1.10.0
numpy>=1.24.0
```

---

## 🎯 Usage Examples

### Generate 10 Names
```python
from TextGeneration import GameTextGenerator

gen = GameTextGenerator()
names = [gen.generate_fantasy_name() for _ in range(10)]
print(names)
```

### Generate Complete Story
```python
story = gen.generate_complete_story(temperature=0.7)
print(f"Hero: {story['hero_name']}")
print(f"Quest: {story['quest']}")
print(f"Item: {story['magic_item']}")
print(f"Lore: {story['world_lore']}")
```

### Batch Export
```python
batch = gen.export_batch(content_type="all", count=50)
gen.save_history_to_json("assets.json")
```

---

## 🐛 Troubleshooting

**Q: "ModuleNotFoundError: No module named 'torch'"**
```bash
pip install torch
```

**Q: "Port 8000 already in use"**
- Edit TextGenAPI.py, change port number
- Or kill process using port 8000

**Q: Model not found / No internet**
```bash
# Pre-download model
python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; AutoTokenizer.from_pretrained('distilgpt2')"
```

**Q: Generation is slow**
- First generation takes 30-60s (one-time model load)
- Subsequent: 1-2s per generation (normal)

---

## 🎓 Temperature Effects

```
0.5  → Conservative, repetitive
0.7  → Balanced, good quality  ⭐
1.0  → Creative, varied
1.5  → Very random, chaotic
```

---

## 📝 File Information

| File | Size | Purpose |
|------|------|---------|
| TextGeneration.py | 15KB | Core engine |
| TextGenAPI.py | 25KB | Web server |
| requirements.txt | 300B | Dependencies |
| README.md | 8KB | Documentation |

---

## 🎮 Use Cases

✅ Game asset generation
✅ Narrative design
✅ Content batching
✅ Story prototyping
✅ NPC dialogue creation
✅ Lore generation

---

## 🚀 Next Steps

1. ✅ Install dependencies
2. ✅ Run `python TextGenAPI.py`
3. ✅ Open http://localhost:8000
4. ✅ Generate your first asset!
5. ✅ Integrate with your game

