# Ray Tracer Python

A simple ray tracing renderer implemented in Python for computer graphics education.

## Description

This project implements a basic ray tracer that can render 3D scenes with geometric primitives like spheres and planes. It features refraction simulation for transparent objects and supports basic scene setup with colored walls and objects.

## Features

- Ray tracing algorithm implementation
- Support for spheres and planes
- Refraction effects for transparent materials
- Configurable camera with field of view
- Image output in PNG format
- Anti-aliasing support (configurable samples)

## Requirements

- Python 3.x
- NumPy
- PyGLM (OpenGL Mathematics for Python)
- Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sghaier9/ray-tracer-python.git
cd ray-tracer-python
```

2. Install dependencies:
```bash
pip install numpy pyglm pillow
```

## Usage

Run the main script to generate a rendered image:

```bash
python main.py
```

This will create `image_refraction.png` in the current directory, showing a scene with colored walls and a refractive sphere.

## Scene Description

The default scene includes:
- A room with colored walls (red, blue, magenta, yellow, green)
- A refractive sphere (simulating glass/water) positioned in the center
- A camera positioned at the origin looking down the negative Z-axis

## Project Structure

```
├── main.py                 # Main ray tracing script
├── image_utils.py          # Image saving utilities
├── classes/
│   ├── camera.py          # Camera and ray classes
│   └── objects/
│       ├── __init__.py
│       ├── object.py      # Base object class
│       ├── sphere.py      # Sphere implementation
│       └── plane.py       # Plane implementation
└── README.md              # This file
```

## Output Examples

The repository includes several rendered images demonstrating different features:
- `image1.png` - `image4.png`: Basic renders
- `image4_aa.png`: Anti-aliased version
- `image_lumiere.png`: Lighting effects
- `image_ombres.png`: Shadows
- `image_phong.png`: Phong shading
- `image_refraction.png`: Refraction effects

## Customization

You can modify the scene in `main.py` by:
- Changing camera parameters (position, FOV, target)
- Adding/removing objects
- Adjusting material properties (colors, refraction indices)
- Modifying rendering parameters (resolution, depth, anti-aliasing)

## License

MIT License - feel free to use for educational purposes.

## Author

[Sghaier9](https://github.com/Sghaier9)

*This project was created as part of a Computer Graphics course (TP Introduction Infographie).* 