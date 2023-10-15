# flac-tool

Tool to convert flac files to alac files

#### Requires:

`ffmpeg`:
- MacOS - `brew install ffmpeg`
- Linux - `sudo apt update && sudo apt install -y ffmpeg`

`poetry`:
- `pip install poetry`

### Installation:
- `poetry build`
- `pip install dist/tapers_io_flac_tools-0.1.0.tar.gz`



### Usage:

Convert Directory of `flac` files to `alac`:
```
flac-tool convert -id <input_dir> -od <output_dir> -t alac
```

Convert single `flac` file to `alac` file:
```
flac-tool convert -if <input_file> -of <output_file> -t alac
```
