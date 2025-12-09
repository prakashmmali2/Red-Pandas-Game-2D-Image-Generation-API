"""
Fantasy Image Generator
=======================
CPU-based procedural image generation for fantasy game concept art.
Creates detailed fantasy-themed images using PIL with procedural generation.
"""

import os
import random
import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

class GameImageGenerator:
    """
    CPU-based procedural image generator for fantasy game concept art.
    Generates detailed fantasy-themed images using PIL and procedural techniques.
    """

    def __init__(self, output_dir="outputs/images"):
        """Initialize the image generator."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # Try to load a font, fallback to default if not available
        try:
            self.font_large = ImageFont.truetype("arial.ttf", 24)
            self.font_small = ImageFont.truetype("arial.ttf", 16)
        except:
            self.font_large = ImageFont.load_default()
            self.font_small = ImageFont.load_default()

    def _get_fantasy_palette(self, theme="fantasy"):
        """Get color palettes for different fantasy themes."""
        palettes = {
            "warrior": {
                "primary": [(139, 69, 19), (255, 215, 0), (128, 128, 128), (0, 0, 0)],
                "secondary": [(178, 34, 34), (184, 134, 11), (105, 105, 105)],
                "accent": [(255, 0, 0), (0, 100, 0), (0, 0, 139)]
            },
            "wizard": {
                "primary": [(75, 0, 130), (255, 255, 255), (138, 43, 226), (25, 25, 112)],
                "secondary": [(148, 0, 211), (255, 20, 147), (0, 191, 255)],
                "accent": [(255, 215, 0), (50, 205, 50), (220, 20, 60)]
            },
            "elf": {
                "primary": [(34, 139, 34), (255, 255, 255), (139, 69, 19), (0, 100, 0)],
                "secondary": [(50, 205, 50), (107, 142, 35), (184, 134, 11)],
                "accent": [(255, 215, 0), (0, 191, 255), (255, 20, 147)]
            },
            "dwarf": {
                "primary": [(139, 69, 19), (255, 215, 0), (105, 105, 105), (47, 79, 79)],
                "secondary": [(160, 82, 45), (184, 134, 11), (112, 128, 144)],
                "accent": [(255, 0, 0), (0, 100, 0), (70, 130, 180)]
            },
            "rogue": {
                "primary": [(0, 0, 0), (128, 128, 128), (169, 169, 169), (105, 105, 105)],
                "secondary": [(47, 79, 79), (112, 128, 144), (119, 136, 153)],
                "accent": [(255, 215, 0), (255, 0, 0), (0, 191, 255)]
            }
        }
        return palettes.get(theme.lower(), palettes["warrior"])

    def _add_noise(self, img, intensity=0.1):
        """Add subtle noise to the image for texture."""
        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                if random.random() < intensity:
                    r, g, b = pixels[x, y]
                    noise = random.randint(-20, 20)
                    r = max(0, min(255, r + noise))
                    g = max(0, min(255, g + noise))
                    b = max(0, min(255, b + noise))
                    pixels[x, y] = (r, g, b)

        return img

    def _add_gradient_background(self, img, colors):
        """Add a gradient background."""
        width, height = img.size
        gradient = Image.new('RGB', (width, height), colors[0])

        for y in range(height):
            # Create a gradient from top to bottom
            factor = y / height
            r = int(colors[0][0] * (1 - factor) + colors[1][0] * factor)
            g = int(colors[0][1] * (1 - factor) + colors[1][1] * factor)
            b = int(colors[0][2] * (1 - factor) + colors[1][2] * factor)

            for x in range(width):
                gradient.putpixel((x, y), (r, g, b))

        # Composite with original image
        img = Image.alpha_composite(gradient.convert('RGBA'), img.convert('RGBA'))
        return img.convert('RGB')

    def _draw_fantasy_character(self, draw, palette, style, width, height):
        """Draw a detailed fantasy character."""
        center_x, center_y = width // 2, height // 2

        # Character silhouette/body
        body_color = random.choice(palette["primary"])
        draw.ellipse([center_x - 25, center_y - 40, center_x + 25, center_y + 40],
                    fill=body_color)

        # Head
        head_color = random.choice(palette["primary"])
        draw.ellipse([center_x - 20, center_y - 80, center_x + 20, center_y - 40],
                    fill=head_color)

        # Eyes
        eye_color = random.choice(palette["accent"])
        draw.ellipse([center_x - 8, center_y - 65, center_x - 2, center_y - 55],
                    fill=eye_color)
        draw.ellipse([center_x + 2, center_y - 65, center_x + 8, center_y - 55],
                    fill=eye_color)

        # Armor details
        armor_color = random.choice(palette["secondary"])
        # Shoulder pads
        draw.ellipse([center_x - 35, center_y - 30, center_x - 15, center_y - 10],
                    fill=armor_color)
        draw.ellipse([center_x + 15, center_y - 30, center_x + 35, center_y - 10],
                    fill=armor_color)

        # Belt
        draw.rectangle([center_x - 20, center_y + 10, center_x + 20, center_y + 20],
                      fill=armor_color)

        # Weapon (sword or staff based on style)
        weapon_color = random.choice(palette["secondary"])
        if "wizard" in style.lower() or "mage" in style.lower():
            # Staff
            draw.rectangle([center_x - 2, center_y - 100, center_x + 2, center_y + 50],
                          fill=weapon_color)
            # Crystal top
            crystal_color = random.choice(palette["accent"])
            draw.ellipse([center_x - 8, center_y - 110, center_x + 8, center_y - 90],
                        fill=crystal_color)
        else:
            # Sword
            draw.rectangle([center_x - 3, center_y - 90, center_x + 3, center_y + 30],
                          fill=weapon_color)
            # Crossguard
            draw.rectangle([center_x - 15, center_y + 25, center_x + 15, center_y + 35],
                          fill=weapon_color)

        # Add some decorative elements
        for _ in range(15):
            x = random.randint(0, width)
            y = random.randint(0, height)
            color = random.choice(palette["accent"])
            size = random.randint(2, 6)
            draw.ellipse([x, y, x + size, y + size], fill=color)

    def _draw_weapon(self, draw, palette, weapon_type, width, height):
        """Draw a detailed fantasy weapon."""
        center_x, center_y = width // 2, height // 2

        if weapon_type.lower() == "sword":
            # Blade
            blade_color = random.choice(palette["primary"])
            draw.rectangle([center_x - 4, center_y - 80, center_x + 4, center_y + 20],
                          fill=blade_color)

            # Guard
            guard_color = random.choice(palette["secondary"])
            draw.rectangle([center_x - 25, center_y + 15, center_x + 25, center_y + 25],
                          fill=guard_color)

            # Handle
            handle_color = random.choice(palette["primary"][2:])
            draw.rectangle([center_x - 3, center_y + 25, center_x + 3, center_y + 60],
                          fill=handle_color)

            # Pommel
            pommel_color = random.choice(palette["accent"])
            draw.ellipse([center_x - 6, center_y + 55, center_x + 6, center_y + 65],
                        fill=pommel_color)

        elif weapon_type.lower() == "axe":
            # Handle
            handle_color = random.choice(palette["primary"][2:])
            draw.rectangle([center_x - 3, center_y + 20, center_x + 3, center_y + 80],
                          fill=handle_color)

            # Blade
            blade_color = random.choice(palette["secondary"])
            # Draw axe head as polygon
            blade_points = [(center_x - 30, center_y - 20), (center_x + 30, center_y - 20),
                           (center_x + 20, center_y + 20), (center_x - 20, center_y + 20)]
            draw.polygon(blade_points, fill=blade_color)

            # Blade edge
            edge_color = random.choice(palette["accent"])
            draw.rectangle([center_x - 25, center_y - 15, center_x + 25, center_y - 5],
                          fill=edge_color)

        elif weapon_type.lower() == "bow":
            # Bow curve
            bow_color = random.choice(palette["primary"])
            # Draw curved bow using multiple lines
            for i in range(-20, 21, 2):
                y = center_y + (i * i) // 100
                draw.line([center_x - 40, center_y + i, center_x + 40, y],
                         fill=bow_color, width=3)

            # String
            string_color = random.choice(palette["secondary"])
            draw.line([center_x - 35, center_y, center_x + 35, center_y],
                     fill=string_color, width=2)

        elif weapon_type.lower() == "staff":
            # Staff shaft
            shaft_color = random.choice(palette["primary"][2:])
            draw.rectangle([center_x - 4, center_y - 100, center_x + 4, center_y + 80],
                          fill=shaft_color)

            # Crystal orb
            orb_color = random.choice(palette["accent"])
            draw.ellipse([center_x - 15, center_y - 110, center_x + 15, center_y - 80],
                        fill=orb_color)

            # Decorative rings
            ring_color = random.choice(palette["secondary"])
            for y in [center_y - 40, center_y - 10, center_y + 20]:
                draw.ellipse([center_x - 8, y - 3, center_x + 8, y + 3],
                           fill=ring_color)

        else:  # Default dagger
            # Blade
            blade_color = random.choice(palette["primary"])
            draw.rectangle([center_x - 2, center_y - 60, center_x + 2, center_y + 20],
                          fill=blade_color)

            # Guard
            guard_color = random.choice(palette["secondary"])
            draw.rectangle([center_x - 12, center_y + 15, center_x + 12, center_y + 25],
                          fill=guard_color)

            # Handle
            handle_color = random.choice(palette["primary"][2:])
            draw.rectangle([center_x - 2, center_y + 25, center_x + 2, center_y + 50],
                          fill=handle_color)

        # Add weapon glow effect
        glow_color = random.choice(palette["accent"])
        for _ in range(10):
            x = random.randint(center_x - 50, center_x + 50)
            y = random.randint(center_y - 50, center_y + 50)
            size = random.randint(1, 3)
            draw.ellipse([x, y, x + size, y + size], fill=glow_color)

    def _draw_environment(self, draw, palette, environment, width, height):
        """Draw a detailed fantasy environment."""
        if environment.lower() == "forest":
            # Sky gradient
            for y in range(height // 2):
                color = (
                    int(135 * (1 - y / (height // 2)) + 70 * (y / (height // 2))),
                    int(206 * (1 - y / (height // 2)) + 130 * (y / (height // 2))),
                    int(235 * (1 - y / (height // 2)) + 180 * (y / (height // 2)))
                )
                draw.line([0, y, width, y], fill=color)

            # Ground
            ground_color = random.choice(palette["primary"])
            draw.rectangle([0, height // 2, width, height], fill=ground_color)

            # Trees
            for _ in range(6):
                x = random.randint(50, width - 50)
                trunk_height = random.randint(60, 100)
                # Trunk
                trunk_color = random.choice(palette["secondary"])
                draw.rectangle([x - 8, height - trunk_height, x + 8, height],
                              fill=trunk_color)
                # Leaves
                leaves_color = random.choice(palette["primary"][:2])
                draw.ellipse([x - 25, height - trunk_height - 50, x + 25, height - trunk_height],
                            fill=leaves_color)

        elif environment.lower() == "mountain":
            # Sky
            sky_color = (135, 206, 235)
            draw.rectangle([0, 0, width, height // 2], fill=sky_color)

            # Mountains
            mountain_color = random.choice(palette["primary"])
            # Background mountain
            mountain1_points = [(-50, height // 2), (width // 3, height // 3),
                               (width // 2, height // 2)]
            draw.polygon(mountain1_points, fill=mountain_color)

            # Middle mountain
            mountain2_points = [(width // 2, height // 2), (2 * width // 3, height // 4),
                               (width + 50, height // 2)]
            draw.polygon(mountain2_points, fill=mountain_color)

            # Foreground mountain
            mountain3_points = [(2 * width // 3, height // 2), (width, height // 5),
                               (width + 50, height // 2)]
            draw.polygon(mountain3_points, fill=mountain_color)

            # Snow caps
            snow_color = (255, 255, 255)
            draw.ellipse([width // 3 - 40, height // 3 - 15, width // 3 + 40, height // 3 + 15],
                        fill=snow_color)
            draw.ellipse([2 * width // 3 - 35, height // 5 - 12, 2 * width // 3 + 35, height // 5 + 12],
                        fill=snow_color)

        elif environment.lower() == "castle":
            # Sky
            sky_color = (135, 206, 235)
            draw.rectangle([0, 0, width, height], fill=sky_color)

            # Castle base
            castle_color = random.choice(palette["primary"])
            draw.rectangle([width // 4, height // 2, 3 * width // 4, height],
                          fill=castle_color)

            # Towers
            tower_positions = [width // 4, width // 2, 3 * width // 4]
            for pos in tower_positions:
                # Tower body
                tower_color = random.choice(palette["secondary"])
                draw.rectangle([pos - 25, height // 3, pos + 25, height],
                              fill=tower_color)
                # Tower top
                top_color = random.choice(palette["accent"])
                draw.polygon([(pos - 30, height // 3), (pos + 30, height // 3),
                             (pos + 20, height // 4), (pos - 20, height // 4)],
                            fill=top_color)

            # Windows
            window_color = (255, 255, 0)  # Light from windows
            for pos in tower_positions:
                for y in range(height // 2, height - 40, 50):
                    draw.rectangle([pos - 10, y, pos + 10, y + 25], fill=window_color)

        elif environment.lower() == "desert":
            # Sky
            sky_color = (135, 206, 235)
            draw.rectangle([0, 0, width, height // 3], fill=sky_color)

            # Sand dunes
            sand_color = random.choice(palette["primary"])
            # Draw multiple dunes
            for i in range(4):
                y_base = height // 3 + i * 60
                points = []
                for x in range(0, width + 100, 80):
                    y = y_base + random.randint(-40, 40)
                    points.append((x, y))
                if len(points) > 2:
                    draw.polygon(points, fill=sand_color)

            # Cacti
            cactus_color = random.choice(palette["secondary"])
            for _ in range(4):
                x = random.randint(100, width - 100)
                # Cactus body
                draw.rectangle([x - 4, height - 80, x + 4, height - 30], fill=cactus_color)
                # Arms
                draw.rectangle([x - 12, height - 60, x - 4, height - 50], fill=cactus_color)
                draw.rectangle([x + 4, height - 65, x + 12, height - 55], fill=cactus_color)

        else:  # Default cave
            # Cave background
            cave_color = random.choice(palette["primary"])
            draw.rectangle([0, 0, width, height], fill=cave_color)

            # Stalactites and stalagmites
            rock_color = random.choice(palette["secondary"])
            for _ in range(8):
                x = random.randint(50, width - 50)
                height_var = random.randint(30, 80)
                # Stalactite (from ceiling)
                draw.polygon([(x - 5, 0), (x + 5, 0), (x, height_var)], fill=rock_color)
                # Stalagmite (from floor)
                draw.polygon([(x - 5, height), (x + 5, height), (x, height - height_var)],
                            fill=rock_color)

            # Crystals
            crystal_color = random.choice(palette["accent"])
            for _ in range(5):
                x = random.randint(100, width - 100)
                y = random.randint(100, height - 100)
                size = random.randint(10, 25)
                draw.polygon([(x, y - size), (x - size//2, y), (x + size//2, y)], fill=crystal_color)

    def _save_image(self, img, filename):
        """Save image and return the file path."""
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath)
        return filepath

    def generate_character_art(self, style="fantasy warrior", seed=None,
                              num_inference_steps=20, guidance_scale=7.5):
        """
        Generate fantasy character concept art.

        Args:
            style (str): Description of the character style
            seed (int, optional): Random seed for reproducibility
            num_inference_steps (int): Number of inference steps (placeholder)
            guidance_scale (float): Guidance scale (placeholder)

        Returns:
            str: Path to the generated image file
        """
        if seed is not None:
            random.seed(seed)

        width, height = 512, 512

        # Determine character theme
        if "wizard" in style.lower() or "mage" in style.lower():
            theme = "wizard"
        elif "elf" in style.lower():
            theme = "elf"
        elif "dwarf" in style.lower():
            theme = "dwarf"
        elif "rogue" in style.lower() or "thief" in style.lower():
            theme = "rogue"
        else:
            theme = "warrior"

        palette = self._get_fantasy_palette(theme)

        # Create base image with alpha channel for compositing
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw character
        self._draw_fantasy_character(draw, palette, style, width, height)

        # Add gradient background
        bg_colors = [(70, 90, 120), (30, 50, 80)]  # Dark fantasy sky
        img = self._add_gradient_background(img, bg_colors)

        # Add noise for texture
        img = self._add_noise(img.convert('RGB'), intensity=0.05)

        # Add subtle blur for artistic effect
        img = img.filter(ImageFilter.GaussianBlur(0.5))

        # Add title
        final_draw = ImageDraw.Draw(img)
        title = f"{style.title()}"
        bbox = final_draw.textbbox((0, 0), title, font=self.font_large)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        y = height - text_height - 30

        # Text shadow
        final_draw.text((x + 2, y + 2), title, font=self.font_large, fill=(0, 0, 0))
        final_draw.text((x, y), title, font=self.font_large, fill=(255, 255, 255))

        # Add subtitle
        subtitle = "Concept Art"
        bbox_sub = final_draw.textbbox((0, 0), subtitle, font=self.font_small)
        sub_width = bbox_sub[2] - bbox_sub[0]
        x_sub = (width - sub_width) // 2
        y_sub = y + text_height + 5
        final_draw.text((x_sub + 1, y_sub + 1), subtitle, font=self.font_small, fill=(0, 0, 0))
        final_draw.text((x_sub, y_sub), subtitle, font=self.font_small, fill=(200, 200, 200))

        # Generate unique filename
        params_str = f"{style}_{seed}_{num_inference_steps}_{guidance_scale}"
        filename = f"character_{hashlib.md5(params_str.encode()).hexdigest()[:8]}.png"

        return self._save_image(img, filename)

    def generate_weapon(self, weapon_type="sword", seed=None,
                       num_inference_steps=20, guidance_scale=7.5):
        """
        Generate weapon concept art.

        Args:
            weapon_type (str): Type of weapon to generate
            seed (int, optional): Random seed for reproducibility
            num_inference_steps (int): Number of inference steps (placeholder)
            guidance_scale (float): Guidance scale (placeholder)

        Returns:
            str: Path to the generated image file
        """
        if seed is not None:
            random.seed(seed)

        width, height = 512, 512

        # Use warrior palette for weapons
        palette = self._get_fantasy_palette("warrior")

        # Create base image
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw weapon
        self._draw_weapon(draw, palette, weapon_type, width, height)

        # Add gradient background
        bg_colors = [(40, 40, 60), (20, 20, 40)]  # Dark mystical background
        img = self._add_gradient_background(img, bg_colors)

        # Add noise and blur
        img = self._add_noise(img.convert('RGB'), intensity=0.03)
        img = img.filter(ImageFilter.GaussianBlur(0.3))

        # Add title
        final_draw = ImageDraw.Draw(img)
        title = f"{weapon_type.title()}"
        bbox = final_draw.textbbox((0, 0), title, font=self.font_large)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        y = height - text_height - 30

        final_draw.text((x + 2, y + 2), title, font=self.font_large, fill=(0, 0, 0))
        final_draw.text((x, y), title, font=self.font_large, fill=(255, 255, 255))

        # Generate unique filename
        params_str = f"{weapon_type}_{seed}_{num_inference_steps}_{guidance_scale}"
        filename = f"weapon_{hashlib.md5(params_str.encode()).hexdigest()[:8]}.png"

        return self._save_image(img, filename)

    def generate_environment_sketch(self, environment="forest", seed=None,
                                   num_inference_steps=20, guidance_scale=7.5):
        """
        Generate environment concept art.

        Args:
            environment (str): Type of environment to generate
            seed (int, optional): Random seed for reproducibility
            num_inference_steps (int): Number of inference steps (placeholder)
            guidance_scale (float): Guidance scale (placeholder)

        Returns:
            str: Path to the generated image file
        """
        if seed is not None:
            random.seed(seed)

        width, height = 512, 512

        # Use appropriate palette based on environment
        if environment.lower() in ["forest", "mountain"]:
            palette = self._get_fantasy_palette("elf")
        elif environment.lower() == "castle":
            palette = self._get_fantasy_palette("warrior")
        elif environment.lower() == "desert":
            palette = self._get_fantasy_palette("dwarf")
        else:
            palette = self._get_fantasy_palette("rogue")

        # Create base image
        img = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw environment
        self._draw_environment(draw, palette, environment, width, height)

        # Add atmospheric effects
        img = self._add_noise(img, intensity=0.02)
        img = img.filter(ImageFilter.GaussianBlur(0.5))

        # Add title
        final_draw = ImageDraw.Draw(img)
        title = f"{environment.title()}"
        bbox = final_draw.textbbox((0, 0), title, font=self.font_large)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        y = height - text_height - 30

        final_draw.text((x + 2, y + 2), title, font=self.font_large, fill=(0, 0, 0))
        final_draw.text((x, y), title, font=self.font_large, fill=(255, 255, 255))

        # Generate unique filename
        params_str = f"{environment}_{seed}_{num_inference_steps}_{guidance_scale}"
        filename = f"environment_{hashlib.md5(params_str.encode()).hexdigest()[:8]}.png"

        return self._save_image(img, filename)
