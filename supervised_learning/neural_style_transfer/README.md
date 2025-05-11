# Neural Style Transfer

This directory contains implementations of Neural Style Transfer (NST), a deep learning technique that applies the artistic style of one image to the content of another image.

## Structure

The `neural_style_transfer` directory includes multiple versions of the `NST` class, each progressively implementing more features of the Neural Style Transfer process. Key files include:

- `0-neural_style.py`: Initial implementation of the `NST` class with basic functionality.
- `1-neural_style.py` to `5-neural_style.py`: Incremental improvements to the `NST` class, adding features such as style cost calculation, Gram matrix computation, and feature generation.

## Key Features

- **Style Layers**: Predefined layers used to extract style features from the style image.
- **Content Layer**: A specific layer used to extract content features from the content image.
- **Image Scaling**: Rescales images to ensure compatibility with the model.
- **Style and Content Cost**: Calculates the cost functions to blend style and content effectively.

## Usage

1. **Prepare Images**: Place your style and content images in the appropriate directory.
2. **Run the Script**: Use one of the provided Python scripts (e.g., `5-neural_style.py`) to perform style transfer.
3. **Output**: The generated image will be saved to the specified output path.

## Requirements

- Python 3.7 or higher
- TensorFlow
- NumPy
- Matplotlib

## Example

To run the style transfer using `5-neural_style.py`:

```bash
python [5-neural_style.py](http://_vscodecontentref_/0) --style_image path/to/style.jpg --content_image path/to/content.jpg --output_image path/to/output.jpg