# AsphyxiaToKamaitachi

A converter for Asphyxia server databases to import scores to Kamaitachi.

## Requirements
- Python 3.10+

## Instructions

1. Place an `sdvx@asphyxia.db` and a `music_db.xml` file next to `convert.py`.
> The music_db.xml file must NOT have multi-byte encodings, or the importer will error. An easy way around this is to create a new XML file, then manually copy and paste the contents to the new one.

2. Launch the converter, then follow the instructions.
```
py convert.py
```

3. Import `batch-manual.json` into Kamaitachi.
